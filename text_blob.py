import mysql.connector
from textblob import *
import nltk
import json
import math
from collections import defaultdict

inverted_index = defaultdict(dict)
word_freq = {}
mydb = mysql.connector.connect(host="localhost", user="root", passwd="kritidb", database="new_praw_db")


def mysql_db():

    """
    mysql connection
    :return:
    """
    my_cursor = mydb.cursor()
    read_text(my_cursor)


def read_text(my_cursor):

    """
    Select query selects submission id and submission body from db.
    :param my_cursor:
    :return:
    """

    my_cursor.execute("select distinct `submission_id` as id, `submission_body` as body from `nmh_submissions_db`;")
    results = my_cursor.fetchall()
    total_submission = len(results)
    spell_check(results, my_cursor)

    idf_score(total_submission, my_cursor)


def spell_check(results, my_cursor):

    for i in range(0, len(results)):
        submission_id = results[i][0]
        print submission_id
        orig_data = results[i][1]
        b = TextBlob(orig_data)
        spell_checked = b.correct()
        print spell_checked
        topic_model(spell_checked, submission_id)
        analyze_sentiment(spell_checked, submission_id, my_cursor)


def analyze_sentiment(text, id, cursor):
    
    global mydb

    input_str = ""
    en_stop = set(nltk.corpus.stopwords.words('english'))

    for word in text.split(" "):
        if word not in en_stop:
            input_str += " " + word
        else:
            pass
    polarity = TextBlob(input_str).sentiment.polarity
    subjectivity = TextBlob(input_str).sentiment.subjectivity
    sql = "update nmh_submissions_db SET polarity = %s, subjectivity = %s where submission_id = %s"
    val = (polarity, subjectivity, id)
    print subjectivity
    print polarity
    cursor.execute(sql, val)
    mydb.commit()
    print subjectivity
    print val
    print polarity


def topic_model(results, submission_id):

    global inverted_index
    global word_freq
    input_str = ""
    en_stop = set(nltk.corpus.stopwords.words('english'))

    for word in results.split(" "):
        if word not in en_stop and word.isalnum():
            if word not in inverted_index:
                inverted_index[word] = {}
                inverted_index[word][submission_id] = 1
            elif word in inverted_index:
                child_dict = inverted_index[word]
                if submission_id in child_dict:
                    freq = child_dict[submission_id]
                    inverted_index[word][submission_id] = freq + 1
                else:
                    inverted_index[word][submission_id] = 1
            else:
                pass

            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    print inverted_index
    print word_freq

    output()


def idf_score(num_doc, cursor):

    global mydb
    submission_id = ""
    for word in word_freq:
        freq_of_word = word_freq[word]
        child_dict = inverted_index[word]
        word_in_doc = len(child_dict.keys())
        print word_in_doc
        idf = math.log((num_doc / word_in_doc), 10)
        print idf
        sql = "Insert into nmh_dictionary(word, total_freq, idf) values(%s, %s, %s)"
        val = (word, freq_of_word, idf)
        cursor.execute(sql, val)
        mydb.commit()

    for word in inverted_index:
        child_dict = inverted_index[word]
        submission = child_dict.keys()
        for id in submission:
            submission_id += id + ", "
            print submission_id
        sql = "UPDATE nmh_dictionary SET submission_id = % s where word = % s"
        val = (submission_id, word)
        cursor.execute(sql, val)
        mydb.commit()


def output():
    with open('inverted_index_nmh.json', 'w') as fp:
        json.dump(inverted_index, fp)
    with open('word_freq_nmh.json', 'w') as fp:
        json.dump(word_freq, fp)


if __name__ == "__main__":
    mysql_db()

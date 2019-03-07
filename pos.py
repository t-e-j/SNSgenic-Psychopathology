import nltk
import mysql.connector
from collections import Counter
import time


def mysql_db():

    mydb = mysql.connector.connect(host= "localhost", user= "root", passwd= "kritidb", database= "new_praw_db")
    my_cursor = mydb.cursor()
    read_text(my_cursor)
    my_cursor.close()
    mydb.close()


def read_text(my_cursor):

    my_cursor.execute("select distinct `submission_id` as id, `submission_body` as body from `support_submissions_db`;")
    results = my_cursor.fetchall()
    part_of_speech(results)
    readability_index(results)


def part_of_speech(results):

    support_pos_dict = {}

    for i in range(0, len(results)):
        submission_id = results[i][0]
        print submission_id
        support_pos_dict[submission_id] = {}
        pos_data = results[i][1]
        pos_token =nltk.word_tokenize(pos_data.lower())
        pos_text = nltk.Text(pos_token)
        pos_tags = nltk.pos_tag(pos_text)
        counts = Counter(tag for word, tag in pos_tags)
        total_pos = sum(counts.values())
        support_pos_dict[submission_id] = dict((word, float(count)/total_pos) for word, count in counts.items())
        print support_pos_dict


def readability_index(results):

    char_count = 0
    word_count = 0
    sent_count = 0
    read_index = {}

    for i in range(0, len(results)):
        submission_id = results[i][0]
        read_index[submission_id] = {}
        data = results[i][1]
        print data
        for word in data.split(" "):
            if word.isalnum():
                word_count += 1
        for character in data:
            if character.isalnum():
                char_count += 1
        for sentence in data.split("."):
            sent_count += 1
        print word_count, char_count, sent_count
        readability = 5.89*(char_count / word_count) - 29.5*(sent_count / word_count) - 15.8
        print readability
        read_index[submission_id] = readability
        print read_index


def correct_date(date):

    fmt = "%Y-%m-%d %H:%M:%S"
    t = time.strftime(fmt, time.localtime(date))
    return t


if __name__ == "__main__":
    mysql_db()

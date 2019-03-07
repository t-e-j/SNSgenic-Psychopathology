import mysql.connector
import json


bigram_dict = {}


def mysql_db():

    """
    mysql connection
    :return:
    """
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="kritidb", database="new_praw_db")

    my_cursor = mydb.cursor()
    read_text(my_cursor)
    write_db(mydb, my_cursor)


def read_text(my_cursor):

    """
    Select query selects submission id and submission body from db.
    :param my_cursor:
    :return:
    """
    my_cursor.execute("select distinct `submission_id` as id, `submission_body` as body from `mh_submissions_db` "
                      "where `sm_senti` > '0.01'")
    results = my_cursor.fetchall()
    ngrams(results)


def ngrams(data):

    global bigram_dict
    for i in range(0, len(data)):
        submission_id = data[i][0]
        text = data[i][1]

        word_stream = text.split(' ')

        for i in range(0, len(word_stream)-1):
            if word_stream[i].isalnum() and word_stream[i+1].isalnum():
                bigram = word_stream[i] + " " + word_stream[i+1]

                if bigram in bigram_dict:
                    bigram_dict[bigram] += 1
                else:
                    bigram_dict[bigram] = 1
                    print bigram_dict

    output()


def write_db(mydb, cursor):

    global bigram_dict
    for word in bigram_dict:
        bigram = word
        freq = bigram_dict[word]
        sql = "insert into mh_bigram(bigram, freq) values(%s, %s)"
        val = (bigram, freq)
        cursor.execute(sql, val)
    mydb.commit()


def output():

    global bigram_dict
    with open('bigram_mh.json', 'w') as fp:
        json.dump(bigram_dict, fp)


if __name__ == "__main__":
    mysql_db()

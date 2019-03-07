import mysql.connector
import json


trigram_dict_mh = {}


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

    global trigram_dict_mh
    for i in range(0, len(data)):
        submission_id = data[i][0]
        text = data[i][1]

        word_stream = text.split(' ')

        for i in range(0, len(word_stream)-2):
            if word_stream[i].isalnum() and word_stream[i+1].isalnum() and word_stream[i+2].isalnum():
                trigram = word_stream[i] + " " + word_stream[i+1] + " " + word_stream[i+2]

                if trigram in trigram_dict_mh:
                    trigram_dict_mh[trigram] += 1
                else:
                    trigram_dict_mh[trigram] = 1
                    print trigram_dict_mh
    output()


def write_db(mydb, cursor):

    global trigram_dict_mh
    for word in trigram_dict_mh:
        trigram = word
        freq = trigram_dict_mh[word]
        sql = "insert into mh_trigram(trigram, freq) values(%s, %s)"
        val = (trigram, freq)
        cursor.execute(sql, val)
    mydb.commit()


def output():

    global trigram_dict_mh
    with open('trigram_mh.json', 'w') as fp:
        json.dump(trigram_dict_mh, fp)


if __name__ == "__main__":
    mysql_db()

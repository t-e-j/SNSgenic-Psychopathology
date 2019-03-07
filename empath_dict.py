from empath import Empath
import nltk
import mysql.connector
import json


def mysql_db():

    mydb = mysql.connector.connect(host= "localhost", user= "root", passwd= "kritidb", database= "new_praw_db")
    my_cursor = mydb.cursor()
    em_trial(my_cursor, mydb)
    mydb.close()


def em_trial(my_cursor, mydb):

    lexica = Empath()
    support_empath_dict = {}
    input_str = ""
    my_cursor.execute("select distinct `submission_id` as id, `submission_body` as body from `support_submissions_db`;")
    results = my_cursor.fetchall()
    en_stop = set(nltk.corpus.stopwords.words('english'))

    for i in range(0, len(results)):
        submission_id = results[i][0]
        print submission_id
        support_empath_dict[submission_id] = {}
        string_lexica = results[i][1]
        for word in string_lexica.split(" "):
            if word not in en_stop:
                input_str += " " + word
        support_empath_dict[submission_id] = lexica.analyze(string_lexica, normalize=True)
        if support_empath_dict[submission_id] is not None:
            sm = support_empath_dict[submission_id]["social_media"]

            print sm

            if sm == 0:
                status = "n"
            elif sm is None:
                status = "n"
            else:
                status = "y"
            print status
            sql = """UPDATE support_submissions_db SET sm_senti = %s, sm_status = %s where submission_id = %s"""
            val = (sm, status, submission_id)
            my_cursor.execute(sql, val)

        else:
            pass
    mydb.commit()
    my_cursor.close()
    output(support_empath_dict)


def output(empath_dict):
    with open('support_empath_file.json', 'w') as fp:
        json.dump(empath_dict, fp)


if __name__ == "__main__":
    mysql_db()

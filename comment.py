import praw
import mysql.connector
import time


def db_connect():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="kritidb", database="new_praw_db")
    my_cursor = mydb.cursor()
    user_class(my_cursor, mydb)


def user_class(my_cursor, mydb):

    sql = "select distinct `author` from `support_submissions_db` where `sm_status` = 'y'"
    my_cursor.execute(sql)
    results = my_cursor.fetchall()
    extract_comment(results, my_cursor, mydb)


def extract_comment(users, cursor, db):

    reddit_Object = praw.Reddit(client_id='YPcscwriPcF4eQ', client_secret='w8lEbc7DBkaILK1CRk45uYGAAKI',
                                user_agent='confusedengg')
    for entry in users:
        author = entry[0]
        for comment in reddit_Object.redditor(name=author).comments.new(limit=None):
            body = comment.body
            date = correct_date(comment.created_utc)

            id = comment.id
            submission_link = comment.link_id
            subreddit = comment.subreddit.display_name
            parent = comment.parent_id
            score = comment.score
            print date, id, submission_link, subreddit, parent
            sql = "Insert into comments_db(comment_id, author, body, creation_dt, link_id, parent, subreddit, score) " \
                  "values(%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (id, author, body, date, id, parent, subreddit, score)
            cursor.execute(sql, val)
        db.commit()


def correct_date(date):
    fmt = "%Y-%m-%d %H:%M:%S"
    t = time.strftime(fmt, time.localtime(date))
    return t


if __name__ == "__main__":
    db_connect()

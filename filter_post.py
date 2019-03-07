
import praw
import time
import mysql.connector


def praw_trial():

    submission_list = []
    datasource = "https://www.reddit.com"

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="kritidb", database="new_praw_db")
    my_cursor = mydb.cursor()

    reddit_Object = praw.Reddit(client_id='YPcscwriPcF4eQ', client_secret='w8lEbc7DBkaILK1CRk45uYGAAKI',
                                user_agent='confusedengg')

    search_keyword = ['social media', 'instagram', 'facebook', 'twitter', 'snapchat']

    mh_subreddit = ['mentalhealth', 'traumatoolbox', 'bipolarreddit', 'BPD', 'ptsd', 'psychoticreddit',
                    'EatingDisorders', 'StopSelfHarm', 'survivorsofabuse', 'panicparty', 'socialanxiety',
                    'hardshipmates']

    support_subreddit = ['SuicideWatch', 'depression', 'Anxiety', 'foreveralone', 'socialanxiety']

    nmh_subreddit = ['simpleliving', 'self', 'confession', 'confessions', 'AskReddit', 'TooAfraidToAsk', 'nosleep',
                     'nosurf', 'productivity', 'selfimprovement','Advice', 'antisocialmedia']

    subreddit_list = [mh_subreddit, support_subreddit, nmh_subreddit]
    for sub in subreddit_list:
        print sub
        for red in sub:
            for keyword in search_keyword:
                print(keyword)
                print("*******************************")

                for submissions in reddit_Object.subreddit(red).search(keyword):
                    if datasource in submissions.url and submissions.id not in submission_list:

                        author = submissions.author.name
                        title = submissions.title
                        score = submissions.score
                        id = submissions.id
                        url = submissions.url
                        no_of_Comments = submissions.num_comments
                        created_dt = correct_date(submissions.created)
                        body = submissions.selftext
                        subreddit = submissions.subreddit.display_name
                        submission_list.append(id)
                        if (sub == nmh_subreddit):

                            sql = "INSERT INTO nmh_submissions_db(submission_id, subreddit_name, " \
                                  "submission_url, submission_title, submission_body, submission_date, " \
                                  "No_of_comment, score, author) values" \
                                  " (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

                        elif (sub == mh_subreddit):

                            sql = "INSERT INTO mh_submissions_db(submission_id, subreddit_name, " \
                                "submission_url, submission_title, submission_body, submission_date, " \
                                "No_of_comment, score, author) values" \
                                " (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

                        elif (sub == support_subreddit):

                            sql = "INSERT INTO support_submissions_db(submission_id, subreddit_name, " \
                                    "submission_url, " \
                                    "submission_title, submission_body, submission_date, No_of_comment, score, author)" \
                                    " values" \
                                    " (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

                        else:
                            pass

                        val = (id, subreddit, url, title, body.lower(), created_dt, no_of_Comments, score,
                               author)
                        my_cursor.execute(sql, val)
                        mydb.commit()

                    else:
                        pass


def correct_date(date):

    fmt = "%Y-%m-%d %H:%M:%S"
    t = time.strftime(fmt, time.localtime(date))
    return t


if __name__ == "__main__":
    praw_trial()

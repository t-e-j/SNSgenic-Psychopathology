import praw
from requests import Session

session = Session()

reddit = praw.Reddit(client_id='Q8LE3MaZpp4gKQ',
                     client_secret='qSiKA2PVIR-BEkEY8ikbbcMKLL4',
                     username = 'btejasvi',
                     password = 'btejasvisfsu',
                     user_agent='myuseragent')

#print(reddit.read_only)


subreddits = { 'mentalhealth', 'psychology','ptsd','depression','anxiety','ocd','stress','mentalhealth','suicidewatch','addiction','getdisciplined','selfhelp','selfimprovement','self','bipolarreddit','bpd','socialanxiety'}

#for submission in reddit.subreddit(subreddits).hot(limit=10):
#    print(submission.title)

subreddit = reddit.subreddit('ocd')

hot_python = subreddit.hot(limit = 5)

for submission in hot_python:
    #print (dir(submission))
    print (submission.title)
    print (submission.score)
    print (submission.author)

    #comments = submission.comments.list()
    submission.comments.replace_more(limit=0)

    #for comment in comments:
    for comment in submission.comments.list():

        print (20*'#')
        print ('Parent ID:', comment.parent())
        print ('Comment ID:', comment.id)
        print (comment.body)

        #if len(comment.replies) > 0:
         #   for reply in comment.replies:
          #      print ('REPLY:',reply.body)

# secret	qSiKA2PVIR-BEkEY8ikbbcMKLL4

#reddit SNSgenic
#personal use script
#Q8LE3MaZpp4gKQ

#url - https://pages.github.com/
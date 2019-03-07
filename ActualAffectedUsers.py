
#  path - /home/ubuntu/database/SNSgenicPsychopathology/tejasvi_annotations
import pickle

# annotations = {}
# name = raw_input("Please enter your name:")
# name = name.lower()

# with open(name+".pickle") as f : data = pickle.load(f)

with open("tejasvi100_annotations.pickle") as f : data = pickle.load(f)
for i,entry in enumerate(data):
    print "\n\n\n"
    # id = entry["submission_id"]
    print i
    print entry[0]
    print entry[1]
   # print entry["submission_id"]
   # print entry["submission_body"]

print "done!"





# {u'submission_date': u'2018-10-24 23:23:08', u'submission_id': u'9r4doz', u'subreddit_name': u'SuicideWatch',
# u'submission_body': u" i'm stuck on the bottom being homeless and unemployed
# and i just want to find something safe before i take my own life.", u'sm_status': u'y', u'adverb': 123.52976480193678,
#  u'author': u'some_pop_punk_kid', u'sm_senti': 0.00396825, u'subjectivity': 0.39382086167800456, u'possesive_pr': 0.028368794326241134,
#  u'submission_title': u'Need some/any support', u'personal_pr': 0.0070921985815602835, u'verb': 330.7408953375414, u'related': u'',
# u'polarity': 0.03138012811541557, u'No_of_comment': 3, u'submission_url': u'https://www.reddit.com/r/SuicideWatch/comments/9r4doz/need_someany_support/',
#  u'noun': 0.1453900709219858, u'score': 1, u'readability': 7.759999999999998, u'category': u'support'}

submission_date
submission_id
subreddit_name
submission_body
sm_status
adverb
author
sm_senti
subjectivity
possessive_pr
submission_title
personal_pr
verb
related
polarity
No_of_comment
submission_url
noun
score
readability
category



# path - /home/ubuntu/database/SNSgenicPsychopathology

import pickle

# annotations = {}
name = raw_input("Please enter your name:")
name = name.lower()
with open(name+".pickle") as f : data = pickle.load(f)
for i,entry in enumerate(data["separate"]):
    print "\n\n\n"
    # id = entry["submission_id"]
    print entry
   # print entry["submission_id"]
   # print entry["submission_body"]

print "done!"
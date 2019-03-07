import operator
import sqlite3
from collections import defaultdict, Counter
import cPickle as pickle
from scipy.stats.stats import pearsonr

def make_parallel_async(aFunc):

def make_author_table(dbpath):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    columns = ["freq_by_sr",
               "SWfreq",
               "overall_freq",
               "mh_freq",
               "daily_sentiment",
               "daily_subj",
               "length"]
    columns = reduce(operator.add, [[c,
                                     "7_day_mov_avg_"+c,
                                     "14_day_mov_avg_"+c,
                                     "30_dav_mov_avg_"+c] for c in columns])
    columns = [c + " TEXT" for c in columns]
    correlatable = ["SWfreq","overall_freq","mh_freq","daily_sentiment","daily_subj","length"]
    for i, field1 in enumerate(correlatable[:-1]):
        for field2 in correlatable[i+1:]:
            name = "%s_by_%s" % (field1, field2)
            name7 = "7_day_mov_avg_%s" % (name,)
            name14 = "14_day_mov_avg_%s" % (name,)
            name30 = "14_day_mov_avg_%s" % (name,)
            new_cols = [name, name7, name14, name30]
            new_cols = ["%s FLOAT" % (col,) for col in new_cols]
    columns = ["author TEXT"] + columns + new_cols
    columns = ",".join(columns)
    query = "CREATE TABLE authors(%s)" % (columns,)
    c.execute(query)
    conn.commit()
    conn.close()

def get_author_entries(dbpath, author):
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    fields = ("author", "subreddit", "textblob_sentiment", "subjectivity", "length", "julian_day")
    query = ("SELECT %s,%s,%s,%s,%s,%s " % fields+
            ("FROM comments WHERE author=%s" % (author,)))
    results = []
    for result in c.execute(query):
        results.append(dict(zip(fields,result)))
    return results

def get_corr_coefficient(field1, field2):
    days = sorted(field1.keys())
    data1 = [field1[key] for key in days]
    data2 = [field2[key] for key in days]

def get_active_days(comments):
    return set([comment["julian_day"] for comment in comments])

def get_active_subreddits(comments):
    return set([comment["subreddit"] for comment in comments])

def get_freq_by_day(comments):
    post_days = [comment["julian_day"] for comment in comments]
    return Counter(post_days)

def group_by_subreddit(comments):
    returnDict = defaultdict(list)
    for comment in comments:
        returnDict[comment["subreddit"]].append(comment)

def average(lst):
    return sum(lst)/float(len(lst))

def daily_average(comments, fieldName):
    returnDict = defaultdict(lambda : [0,0])
    for comment in comments:
        returnDict[comment["julian_day"]][0] += comment[fieldName]
        returnDict[comment["julian_day"]][1] += 1
    for key,value in returnDict.items():
        returnDict[key] = value[0]/float(value[1])

def getMovingAverage(data, span):
    minDay = min(data.keys())
    maxDay = max(data.keys())
    returnDict = {}
    if maxDay-minDay < span:
        return {}
    for jday in range(minDay,1+maxDay-span):
        returnDict[jday+span-1] = average([data[day] for day in range(jday,jday+span)])

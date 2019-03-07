# coding=utf-8
import json
import datetime
from datetime import datetime
import sqlite3
from sqlite3 import Error
import pandas as pd


startDate = "01/01/18"


def getNextWindow(startDate, periodInDays):
    windowStartDate = datetime.datetime.strptime(startDate, "%m/%d/%y")
    # date = datetime.strftime(startDate,"%m/%d/%y")
    print windowStartDate

    windowEndDate = windowStartDate + datetime.timedelta(days=periodInDays)

    print windowEndDate
    return windowEndDate


#data1 = {'data':[1,2,3,4,5,9,6,8]}
#df = pd.DataFrame(data1)
#df = [df.the_date_column.dt.date > datetime.datetime.now() - pd.to_timedelta("30day")]
#print df


#=====================

#db_filename = '/Users/tejasvibelsare/Documents/SFSU/sqlite/first.db'
#with sqlite3.connect(db_filename) as conn:
#    cursor = conn.cursor()
#    cursor.execute("""
#        create table first
#        select * from first.db
 #   """)

#conn.commit()
#conn.close()

# def calculateRecords(result):
#     dict = {}
#     for entry in result:
#         print entry
#         print "entry"
#         print "entry[0]"
#         print entry[0]
#         print entry[1]
#         #entry[1]= datetime.datetime.utcfromtimestamp(entry[1]).strftime('%Y-%m-%d')
#         print entry[1]
#         if entry[1] not in dict:
#             #print {entry[1]:0}
#             dict[entry[0]]={entry[1]:0}
#         print "before"
#         print dict[entry[0]][entry[1]]
#         dict[entry[0]][entry[1]]+=1
#         print "after"
#         print dict[entry[0]][entry[1]]
#
#     print "This is dictionary"
#     print dict



def countPerDay(conn):
    conn.text_factory = str
    cur = conn.cursor()
    # cur.execute("select * from comments;")
    # cur.execute("SHOW TABLES IN SEProject")
    #users = cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()

    #everything = cur.execute("select * from comments;").fetchall()
    #allUsers = cur.execute("select author,subreddit, post_date from comments").fetchall()
    # users = cur.execute("select distinct author from comments").fetchall()
    #
    # print "Printing tables!"
    # print users
    # print "Printing data"
    # #print everything
    # allUsers =[]
    # u = 0
    # while u < len(users):
    #     print "users[u][0]"
    #     print users[u][0]
    #     allUsers.append(users[u][0])
    #     u+=1
    # print "allUsers"
    # print allUsers
    # #cur.execute("select author, subreddit, post_date from comments")
    #
    # print type(allUsers)
    # i = 0
    # #for user in allUsers:
    # while i < len(allUsers):
    #     #dict = {}
    #     #print type(user)
    #     command = "select subreddit, post_date from comments where author ='" + str(allUsers[i] + "';")
    #     print command
    #     result = cur.execute(command).fetchall()
    #     print type(result)
    #     calculateRecords(result)
    #     print result
    #     print ("This is record for user " + allUsers[i])
    #     #print allUsers[i]
    #     i +=1
    #
    # # datelist = pd.date_range(pd.datetime.today(), periods=2).tolist()
    # # datelist = pd.date_range()
    # # print datelist
    #
    # print "Converting epoch to day "
    # convert_time(conn)
    #
    # print "command executed"

    #rows = cur.fetchall()

    #for row in rows:
     #   print row

    # users = cur.execute("SELECT COUNT(*) FROM comments GROUP BY date(post_date, 'unixepoch')")
    # print "Printing tables!"
    # print users

    count = cur.execute("select author, subreddit, date(post_date, 'unixepoch'), count(*) from comments group by author, subreddit, date(post_date, 'unixepoch')").fetchall()
    print "Printing count!"
    print count

#      saving it in a table

    cur.execute("create table if not exists dayAverageComments (author, subreddit, day, count )").fetchall()

    for eachCount in count:
        cur.execute("insert into dayAverageComments values (?,?,?,?)",eachCount)

    conn.commit()




# def convert_time(conn):
#     conn.text_factory = str
#     cur = conn.cursor()
#
#      # = cur.execute("select distinct author from comments").fetchall()
#
#     cur.execute('select post_date from comments')
#     print "Printing every date"
#     # cur.execute('alter table comments add convertedDate TEXT')
#     for row in cur:
#         # do_stuff_with_row
#         print row
#         dateToConvert = row[0]
#         print dateToConvert
#         convertedDate = datetime.datetime.fromtimestamp(dateToConvert).strftime('%Y-%m-%d')
#         print convertedDate
#         #cur.execute('insert into comments (convertedDate) values (convertedDay)')
#
#         command = "insert into comments (convertedDate) values (" + convertedDate + ") where post_date = dateToConvert"
#         print command
#         cur.execute(command)
#         #result = cur.execute(command).fetchall()


def countPerWindow(conn,periodInDays):
    conn.text_factory = str
    cur = conn.cursor()

    startDate = datetime.strptime('2014-01-01','%Y-%m-%d')
    print startDate
    #endDate = datetime.strptime('2014-01-01','%Y-%d-%m')
    #print endDate

    endDate = getNextWindow(startDate, 3)

    allAuthors = cur.execute("select distinct author from dayAverageComments").fetchall()
    allSubreddits = cur.execute('select distinct subreddit from dayAverageComments').fetchall()

    for everyAuthor in allAuthors :
        command = "select subreddit, day, count from dayAverageComments where author ='" + str(everyAuthor[0] + "';")
        print command
        result = cur.execute(command).fetchall()
        # cur.execute("select subreddit, day,count where author")
        print result

        for subreddit in allSubreddits:
            command = 'select day,count from dayAverageComments where subreddit = "'+ subreddit[0] + '" '


    # countPerDay(conn)



def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print "Connected!"
        conn.text_factory = str
        print(sqlite3.version)
        with conn:
            print "Executing commands!"
            countPerDay(conn)

    except Error as e:
        print "error!"
        print(e)
    finally:
        conn.close()


#datetime.datetime.utcfromtimestamp(1540362130).strftime('%Y-%m-%d')


if __name__ == '__main__':
    #create_connection("/Users/tejasvibelsare/Documents/SFSU/sqlite/Trial.db")
    create_connection("/Users/tejasvibelsare/Documents/SFSU/sqlite/SEProject")
    # create_connection("/Users/tejasvibelsare/Library/Mobile Documents/com~apple~CloudDocs/Fall 2018/Search Engines/Project/myCode/SEProject.db")

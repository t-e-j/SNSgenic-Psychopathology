import json
from datetime import datetime
import datetime
import sqlite3
from sqlite3 import Error
import pandas as pd
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plot
import matplotlib.dates as mdates
from matplotlib import style
# style.use('fivethirtyeight')
import numpy as np


def executeCommands(conn):
    conn.text_factory = str
    cur = conn.cursor()

    # users = cur.execute("select distinct author from comments").fetchall()

    # users = cur.execute("select * from comments").fetchall()

    # users = cur.execute("select * from dayAverageComments").fetchall()
    # #users = cur.execute("SELECT COUNT(*) FROM comments GROUP BY date(post_date, 'unixepoch')")
    # print "Printing tables!"
    # print users

    startDate = datetime.strptime('2014-01-01', '%Y-%m-%d')
    print startDate

    allAuthors = cur.execute("select distinct author from dayAverageComments").fetchall()

    for everyAuthor in allAuthors:
        command = "select subreddit, day, count from dayAverageComments where author ='" + str(everyAuthor[0] + "';")
        print command
        result = cur.execute(command).fetchall()
        # cur.execute("select subreddit, day,count where author")
        print result


    # command = "select subreddit, post_date from comments where author ='" + str(allUsers[i] + "';")
    # print command
    # result = cur.execute(command).fetchall()


    # command = "insert into comments (convertedDate) values (" + convertedDate + ");"
    # print command
    # cur.execute(command)


def graph_data(conn):
    conn.text_factory = str
    cur = conn.cursor()

    # dates = []
    # values = []
    #allData = cur.execute('select * from dayAverageComments').fetchall()
    #print allData
    allSubreddits = cur.execute('select distinct subreddit from dayAverageComments').fetchall()
    for subreddit in allSubreddits:
        dates = []
        values = []
        print subreddit[0]
        command = 'select day,count from dayAverageComments where subreddit = "'+ subreddit[0] + '" '
        allData = cur.execute(command).fetchall()
        # allData = cur.execute('select day,count from dayAverageComments group by subreddit').fetchall()
        print allData
        for row in allData:
            print (row[0])
            # print (datetime.datetime.fromtimestamp(row[0]))
            # dates.append(datetime.datetime.fromtimestamp(row[0]))
            dates.append(datetime.datetime.strptime(row[0], "%Y-%m-%d"))
            values.append(row[1])

        converted_date = mpl.dates.date2num(dates)
        # npValues = np.
        print "printing dates"
        print type(dates)
        print dates
        print "printing vakues!!!"
        print values

        # t = np.arange(values)
        plot.plot_date(dates, values, '-')
        plot.xlabel('Date')
        plot.ylabel('Number of comments')

        # plot.plot(t, t, 'bs')
        # plot.show()

        # plot.axis([XStart, XEnd, YStart, YEnd])

    plot.show()

    # for row in allData :
    #     print (row[0])
    #     #print (datetime.datetime.fromtimestamp(row[0]))
    #     #dates.append(datetime.datetime.fromtimestamp(row[0]))
    #     dates.append(datetime.datetime.strptime(row[0], "%Y-%m-%d"))
    #     values.append(row[1])

    # print dates
    # print values
    # plot.plot_date(dates,values, '-')
    # plot.show()






def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        print "Connected!"
        conn.text_factory = str
        print(sqlite3.version)
        with conn:
            print "Executing commands!"
            #executeCommands(conn)
            graph_data(conn)
    except Error as e:
        print "error!"
        print(e)
    finally:
        conn.close()




if __name__ == '__main__':
    #create_connection("/Users/tejasvibelsare/Documents/SFSU/sqlite/Trial.db")
    create_connection("/Users/tejasvibelsare/Documents/SFSU/sqlite/SEProject")
    # create_connection("/Users/tejasvibelsare/Library/Mobile Documents/com~apple~CloudDocs/Fall 2018/Search Engines/Project/myCode/SEProject.db")

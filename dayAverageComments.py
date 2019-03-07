import sqlite3

def dayAverageComments(c, connection):
    allUsers = []
    for entry in c.execute("select distinct author from comments"):
        allUsers.append(entry[0])

    print len(allUsers)

    for everyUser in allUsers:
        command = "select author, created_utc, count(*) from comments where author ='" + str(
            everyUser + "' group by post_date;")
        result = c.execute(command).fetchall()
        print result
        break;

    count = c.execute(
        "select author, subreddit, date(created_utc, 'unixepoch'), count(*) from comments group by author, subreddit, date(created_utc, 'unixepoch')").fetchall()
    print "Printing count!"
    print count

    #      saving it in a table
    print ("Creating table if do not exist")
    c.execute("create table if not exists dayAverageComments (author, subreddit, day, count )").fetchall()

    # print ("Inserting values in table")
    # for eachCount in count:
    #     c.execute("insert into dayAverageComments values (?,?,?,?)", eachCount)
    # connection.commit()

    #Inserting values
    print ("Inserting values in table")
    c.execute("insert into dayAverageComments (author, subreddit, day, count) select author,subreddit, date(created_utc,'unixepoch'), "
              "count(*) from comments group by author, subreddit, date(created_utc, 'unixepoch')")
    connection.commit()


def main():
    conn = sqlite3.connect("comments.db")
    c = conn.cursor()
    dayAverageComments(c, conn)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # calling main function
    main()



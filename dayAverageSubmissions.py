import sqlite3

def dayAverageSubmissions(c, connection):
    allUsers = []
    for entry in c.execute("select distinct author from submissions"):
        allUsers.append(entry[0])

    print len(allUsers)

    for everyUser in allUsers:
        command = "select author, post_date, count(*) from submissions where author ='" + str(
            everyUser + "' group by post_date;")
        result = c.execute(command).fetchall()
        print result
        break;

    count = c.execute(
        "select author, subreddit, date(post_date, 'unixepoch'), count(*) from submissions group by author, subreddit, date(post_date, 'unixepoch')").fetchall()
    print "Printing count!"
    print count

    #      saving it in a table
    print ("Creating table if do not exist")
    c.execute("create table if not exists dayAverageComments (author, subreddit, day, count )").fetchall()

    print ("Inserting values in table")
    for eachCount in count:
        c.execute("insert into dayAverageComments values (?,?,?,?)", eachCount)
    connection.commit()

    # Inserting values
    # c.execute(
    #     "insert into dayAverageComments values (select author, subreddit, date(post_date, 'unixepoch'), count(*) from submissions group by author, subreddit, date(post_date, 'unixepoch')")



def main():
    conn = sqlite3.connect("submissions.db")
    c = conn.cursor()
    dayAverageSubmissions(c, conn)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # calling main function
    main()



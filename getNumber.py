
import sqlite3
conn = sqlite3.connect("submissions.db")
c = conn.cursor()
allUsers = []
for entry in c.execute("select distinct author from submissions"):
    allUsers.append(entry[0])

print len(allUsers)

for everyUser in allUsers:
    command = "select author, post_date, count(*) from submissions where author ='" + str(everyUser + "' group by post_date;")
    result = c.execute(command).fetchall()
    print result
    break;

count = c.execute("select author, subreddit, date(post_date, 'unixepoch'), count(*) from submissions group by author, subreddit, date(post_date, 'unixepoch')").fetchall()
print "Printing count!"
print count

#      saving it in a table

c.execute("create table if not exists dayAverageComments (author, subreddit, day, count )").fetchall()

for eachCount in count:
    c.execute("insert into dayAverageComments values (?,?,?,?)",eachCount)




c.execute("insert into dayAverageComments values (select author, subreddit, date(post_date, 'unixepoch'), count(*) from submissions group by author, subreddit, date(post_date, 'unixepoch')")
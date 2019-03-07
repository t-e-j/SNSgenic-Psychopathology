'''

 printing xs values
[u'2017-04', u'2017-30', u'2017-33', u'2017-32', u'2017-39', u'2017-51', u'2017-22', u'2017-23', u'2017-24', u'2017-28', u'2018-28', u'2017-44', u'2017-47', u'2017-41', u'2018-29', u'2017-43', u'2018-27', u'2018-25', u'2018-24', u'2017-48', u'2018-06', u'2016-23', u'2018-23', u'2016-43', u'2016-47', u'2016-46']

 printing ys values
[2, 2, 2, 6, 4, 2, 6, 2, 4, 2, 6, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2]

  printing xs values
[u'2018-09', u'2018-08', u'2018-01', u'2018-02', u'2018-12', u'2018-11']





 printing ys values
[2, 2, 2, 2, 4, 4]

'''



import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
from datetime import datetime
import datetime
import time

# style.use('fivethirtyeight')
fig = plt.figure()

# def create_plots():
#     xs = [u'2017-04', u'2017-30', u'2017-33', u'2017-32', u'2017-39', u'2017-51', u'2017-22', u'2017-23', u'2017-24', u'2017-28', u'2018-28', u'2017-44', u'2017-47', u'2017-41', u'2018-29', u'2017-43', u'2018-27', u'2018-25', u'2018-24', u'2017-48', u'2018-06', u'2016-23', u'2018-23', u'2016-43', u'2016-47', u'2016-46']
#
#     ys = [2, 2, 2, 6, 4, 2, 6, 2, 4, 2, 6, 4, 4, 4, 2, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2]
#
#     x = [u'2018-09', u'2018-08', u'2018-01', u'2018-02', u'2018-12', u'2018-11']
#
#     y = [2, 2, 2, 2, 4, 4]
#
#     return xs, ys, x, y




def main():


    # ax1 = fig.add_subplot(211)
    # ax2 = fig.add_subplot(212)
    '''
    xs = [u'2018 27', u'2018 23', u'2018 30', u'2018 22', u'2018 35']

    ys = [2, 2, 2, 2, 2]

    x = [u'2018 08', u'2017 47', u'2017 40', u'2017 43', u'2018 34', u'2018 05', u'2018 25',
     u'2018 30', u'2017 49', u'2018 21', u'2018 17', u'2018 14', u'2018 10', u'2018 35']
    y = [2, 4, 2, 2, 2, 2, 4, 2, 2, 2, 4, 2, 4, 4]


    ax = ['2018 08', '2018 17', '2018 05', '2018 14', '2018 35', '2018 34', '2018 30',
     '2018 10', '2017 49', '2018 27', '2018 25', '2018 22', '2018 23', '2018 21',
     '2017 40', '2017 43', '2017 47']

    ay = [4.0, 25.0, 5.0, 9.0, 4.0, 6.0, 4.5, 1.5, 0.0, 1.0, 9.0, 2.0, 1.0, 133.0, 7.0, 2.0, 9.0]
    '''

    xs = [u'2017 45', u'2017 40', u'2018 04', u'2017 42', u'2017 43']
    ys = [2,2,6,2,2]

    x = [u'2017 44', u'2017 45', u'2017 40', u'2017 41', u'2017 42', u'2017 43', u'2018 02', u'2017 37', u'2017 31', u'2017 33', u'2017 39']
    y = [4,2, 2, 2, 2, 4, 2, 2, 2, 6, 6]


    ax = ['2017 31', '2017 33', '2017 37', '2018 04',
     '2017 39', '2018 02', '2017 41', '2017 40', '2017 43',
     '2017 42', '2017 45', '2017 44']

    ay = [2.5, 7.33, 11.0, 13.33, 2.66, 6.0, 9.0, 9.0, 3.66, 16.0, 26.0, 10.5]

    dates = []
    date = []
    date1 = []
    #
    for i in xs:
        i = str(i)
        dates.append(datetime.datetime.strptime(i + ' 0', "%Y %W %w"))
        # datetime.strptime(myDate + ' 0', "%Y %W %w")

    # dates.sort(key=lambda x: time.mktime(time.strptime(x, "%Y-%W")))
    # sorted(dates, key=lambda x: datetime.datetime.strptime(str(dates), "%Y-%W").strftime("%Y-W"))

    # sorted(dates, key = lambda x: datetime.strptime(x,"%Y%W "))

    dates.sort()
    print dates

    for j in x :
        j = str(j)
        date.append(datetime.datetime.strptime(j + ' 0', "%Y %W %w"))

    date.sort()
    print date

    for k in ax :
        k = str(k)
        date1.append(datetime.datetime.strptime(k + ' 0', "%Y %W %w"))

    date1.sort()
    print date1

    # ax1.plot(xs, ys)
    # ax2.plot(x, y)
    #
    # plt.plot(xs, ys, label = "Relevant subreddits count" )
    # plt.plot(x,y, label = "Non-relevant subreddits count")

    plt.plot_date(dates, ys, label = "Relevant subreddits", linestyle = ':')

    plt.plot_date(date, y, label ='Non-relevant subreddits', linestyle = ':')

    plt.plot_date(date1, ay, label='Average score', linestyle=':')

    # ax1.title = "Relevant subreddits count"
    # ax2.title = "Non-relevant subreddits count"

    me = "NJ_Yankees_Fan"
    plt.xlabel("Year-Week")
    plt.ylabel("Count")
    myTitle = "Author = "+ me
    plt.title(myTitle)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # calling main function
    main()

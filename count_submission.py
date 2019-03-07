# actual relevant authors

'''
4dolfin
7_Pixel_7
9754213680632
AVZ_Gone
AbstrakThought
AdvancedFish
AnonymousButterfly01
BAJJAB001
BestOldExFriendRay
Bronzehawkattack
CanNotLiveLikeThis
Cri1654
Damn_Madame
Eric2517
Ge0rgeBr0ughton
Gtj_2036
IsAFailure
Ivoriy
KnowThat205
Kookie_212
KriegRipper
Lily1018
LivelyWallflower
Mazzy1978
Messedupmesss
Millennial_Ennui
Mohankumar12345
MrRebornX
MyLifelines
No1stupid
Nocturnalonerr
OldManoftheNorth
Onikouzou
PRS501
PanTostadoo
ProfessorTurtlez
RnLraep
Runechi
SadiMasta
ShittyNoodle
SilentHuman
Snedwardowden
Tettrabyte
Throwaway124522
TimorousCharles
Violetsuger
VioletteRose29
VolgaSvetlana
WinterWitch89
Zedevile
Zephandrypus
Zorkats1
adannytoremember
albundy12345
an_on_ym_ou_s
andrewerdna100
ashleyoglesby
ayesmyownaccount
bellavita1577
bikramxo
blenda_mae
bluegrassinthebreeze
bookloverphile
cobo3388
corvith
dVNsp
danielmann862
dannythfc
dkjones05
elton_johns_glasses
fifimcg
grossko19
haymansafc
herolance
idontknowanymore3500
imthepotatoqueen
is_reddit_useful
isolatedesolate
jakey3209
jamlesstoast
jdawg7780
jefflucas
jibberjabbery
jockcel
jxseyrae_
keepit-ethereal
klotzonater420
kumadoki
large255
liam_a1
meiniemoon
mertensmen14
minusman652
miriamurphy
mitsukiowl
moldybritches
moomooboo
mostdietwater
myusernamebeatsyours
nehway
neurosthetic
notoriousOLG
paynexkiller
peeblicity
piyopyoko
playingtricksonme
rayj33
riot-nerf-red-buff
robuttnikinin
satuza
scryptx
seeingwishes
selfdxaries
thegamerrr
throwaway19941984
tristdog27
turbochickenkiev
velociraptor94
waitingdaisy
warners919

'''


import sqlite3
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
from datetime import datetime
import datetime

# style.use('fivethirtyeight')
# fig = plt.figure()


def relevantUsersSubredditSubmissionCount(c, connection):

    print ("Getting relevant author's subredditwise submissions count")


    query = """select author, subreddit, count(*) from dayAverageSubmissions where 
    author in ('Wred27', 'jllxxp', 'expressivewords', 'miriamurphy', 'MyLifelines',
               'PRS501', 'bikramxo', 'idontknowanymore3500', 'wh3reismym1nd',
               'Lazentro', 'TheRealTayler', 'Zorkats1', 'stereotypicalbritish',
               'Runechi', 'Onikouzou', '9754213680632', 'CanNotLiveLikeThis',
               'Snedwardowden', 'jxseyrae_', 'SadiMasta', 'Shadowing234', 'Violetsuger',
               'dragonwarrior09', '4dolfin', 'Jaybo78', 'jakey3209', 'ruckanoise88',
               'mertensmen14', 'myusernamebeatsyours', 'Joesuds', 'albundy12345',
               'spooky-mermaid', 'dkjones05', 'velociraptor94', 'likeroscoe',
               'Radoslaw76', 'AVZ_Gone', 'No1stupid', 'ProfessorTurtlez', 'large255',
               'jhmillard', 'Flowersformybutt', 'campycynic', 'kisyy',
               'spagootinurpoot', 'MrRebornX', 'turbochickenkiev',
               'bluegrassinthebreeze', 'blenda_mae', 'VroomBrapBrap',
               'liam_a1', 'imthepotatoqueen', 'Tettrabyte', 'turbochickenkiev',
               'SPD87', 'isolatedesolate', 'JillyBoel69', 'pakelis_vafliuku',
               'KastMigVaek', 'MinimalSass', 'warners919', 'DoSexTheConspiracy',
               'VioletteRose29', 'bookloverphile', 'undercover_intern',
               'hellohereiamok', 'Anxmess', 'LolaIsLoud', 'Ds3y', 'meiniemoon',
               'throwaway0817161616', 'paynexkiller', 'fifimcg', 'agoldfish378',
               'jockcel', 'burritos4me', 'waitingdaisy', 'quirilon', 'LivelyWallflower',
               'klotzonater420', 'TheSaltySeaDog22', 'riot-nerf-red-buff', 'Webimpulse',
               'ayesmyownaccount', 'KnowThat205', 'thatshawtyp', 'OldManoftheNorth',
               'VolgaSvetlana', 'oIndiex', '69SaggyButtCheeks69', 'andrewerdna100',
               'corvith', 'IsAFailure', 'YoIGotASoulVoice', 'neurosthetic',
               'wheresmyadventure', 'AhoyThereFancypants', 'ashleyoglesby',
               'Mazzy1978', 'tristdog27', 'AnonymousButterfly01', 'DeadHands26',
               'caillou_getsgrounded', 'mitsukiowl', 'anyc84_m', 'Damn_Madame',
               'cuernodechivos2', 'BotFarm_drone1134', 'X_Dragonkill', 'glowigoo88',
               'OldManoftheNorth', 'TeacherJuana', 'lonesomesoul95', 'an_on_ym_ou_s',
               'adannytoremember', 'BAJJAB001', 'Throwaway124522', 'dVNsp', 'honey2190',
               'WinterWitch89', 'Zephandrypus', 'equilibrium21', 'fasttradeboyman',
               'moomooboo', 'Lily1018', 'Eric2517', 'hauntedhillswhore', 'Ganxious',
               'MelonyHope', 'pinkgirlystuffjody', 'Bronzehawkattack', 'cobo3388',
               'piyopyoko', 'sicaspeak', 'PorSiempreSolo', 'Cri1654', 'CinnamonThePig',
               'AdvancedFish', 'peeblicity', 'Ivoriy', 'PanTostadoo',
               'BestOldExFriendRay', 'bulldozer9999999999', 'jefflucas', 'SilentHuman',
               'rayj33', 'macproafro', 'Carpbeat24', 'RnLraep', 'redfern962',
               '7_Pixel_7', 'throwaway19941984', 'minusman652', 'HandMeMyThinkingPipe',
               'AbstrakThought', 'Kookie_212', 'bellavita1577', 'LogiCparty',
               'SPD87', 'ShittyNoodle', 'jdawg7780', 'seeingwishes', 'ekek26',
               'reallyloudcrier', 'playingtricksonme', 'Zedevile', 'undercovur',
               'scryptx', 'Jellolmao124', 'ratcatching', 'KriegRipper', 'Faithlee26',
               'IAmTheScarBrother', 'mostdietwater', 'herolance', 'TimorousCharles',
               'danielmann862', 'furmthewurm', 'studentstudylife', 'Gtj_2036',
               'JohnV318', 'anonymous4226', 'dannythfc', 'kwassa7', 'Millennial_Ennui',
               'Nocturnalonerr', 'satuza', 'thegamerrr', 'kumadoki', 'HerThoughts88',
               'keepit-ethereal', 'Messedupmesss', 'Soopa_dude', 'grossko19',
               'RedishZipper', 'notoriousOLG', 'jamlesstoast', 'Damn_Madame',
               'cuernodechivos2', 'BotFarm_drone1134', 'glowigoo88', 'OldManoftheNorth',
               'khaledur01', 'an_on_ym_ou_s', 'subcuta', 'tar4ntula', 'BAJJAB001',
               'EDPostRequests', 'jibberjabbery', 'nehway', 'Throwaway124522',
               'haymansafc', 'Encoraskrc', 'Zephandrypus', 'Mohankumar12345',
               'robuttnikinin', 'moldybritches', 'Ge0rgeBr0ughton', 'moomooboo',
               'selfdxaries', 'Lily1018', 'Eric2517', 'hauntedhillswhore', 'Ganxious',
               'MelonyHope', 'FeelThePower999', 'elton_johns_glasses', 'piyopyoko',
               'PorSiempreSolo', 'Cri1654', 'AdvancedFish', 'Cheesycreature',
               'kenndot', 'Ivoriy', 'PanTostadoo', 'speak721', 'hesback_inpogform',
               'BestOldExFriendRay', 'jefflucas', 'SilentHuman', 'Angle-of-depression',
               'macproafro', 'Shanbae', 'AgitatedAdvantage', 'is_reddit_useful',
               'Carpbeat24', 'RnLraep', 'redfern962', '7_Pixel_7', 'felipe5083',
               'WellDeserved101', 'minusman652', 'HandMeMyThinkingPipe',
               'AbstrakThought', 'Kookie_212')
    group by author, subreddit;"""

    count = c.execute(query).fetchall()
    # print (count)


    print ("Considering 20 authors at a time to recognise pattern if any and getting every relevant author's subreddit wise weekly count of submissions")

    query1 = """ select author, subreddit, strftime('%Y-%W', day), count(*) from dayAverageSubmissions where author in ( "4dolfin", "7_Pixel_7", "9754213680632", "AVZ_Gone", "AbstrakThought", "AdvancedFish", "AnonymousButterfly01", "BAJJAB001",
               "BestOldExFriendRay","Bronzehawkattack", "CanNotLiveLikeThis","Cri1654", "Damn_Madame","Eric2517","Ge0rgeBr0ughton", "Gtj_2036",
                "IsAFailure","Ivoriy", "KnowThat205", "Kookie_212",  "KriegRipper")
                group by author,subreddit, strftime('%Y %W', day);"""

    short20Count = c.execute(query1).fetchall()
    # print (short20Count)
    comparisonPerAuthor(short20Count,c)
    type(short20Count)

'''
short20Count format :

KriegRipper|trucksim|2017-23|4
KriegRipper|trucksim|2017-24|4
KriegRipper|watercooling|2017-17|2

'''

def comparisonPerAuthor(resultList,c):

    authors = ["4dolfin", "7_Pixel_7", "9754213680632", "AVZ_Gone", "AbstrakThought", "AdvancedFish", "AnonymousButterfly01", "BAJJAB001",
               "BestOldExFriendRay","Bronzehawkattack", "CanNotLiveLikeThis","Cri1654", "Damn_Madame","Eric2517","Ge0rgeBr0ughton", "Gtj_2036",
                "IsAFailure","Ivoriy", "KnowThat205", "Kookie_212",  "KriegRipper"]

    listOfSubreddits = ["simpleliving","productivity", "AskReddit", "selfimprovement", "nosurf", "TooAfraidToAsk", "Advice", "antisocialmedia",
                        "confessions", "xxfitness", "DecidingToBeBetter","hardshipmates", "psychology", "ptsd", "depression", "anxiety","ocd",
                        "stress", "mentalhealth", "suicidewatch", "addiction", "getdisciplined", "selfhelp", "selfimprovement", "self",
                        "bipolarreddit", "bpd", "socialanxiety","SuicideWatch","traumatoolbox","psychoticreddit","StopSelfHarm",
                        "survivorsofabuse","bipolar","foreveralone","panicparty"]




    for everyAuthor in authors:
        relevantSubreddit = {}
        nonRelevantSubreddit = {}

        #Getting distinct subreddits
        query1 = "select distinct subreddit from dayAverageSubmissions where author = '" + str(everyAuthor) + "';"
        distinctSubredditsPerAuthor = c.execute(query1).fetchall()
        print distinctSubredditsPerAuthor


        for i in range(len(resultList)):

            singleTuple = resultList[i]

            if singleTuple[0] == everyAuthor :

                if singleTuple[1] in listOfSubreddits:

                    if singleTuple[2] in relevantSubreddit:

                        relevantSubreddit[singleTuple[2]] = relevantSubreddit[singleTuple[2]] + singleTuple[3]

                    else :
                        relevantSubreddit[singleTuple[2]] = singleTuple[3]

                else :

                    if singleTuple[2] in nonRelevantSubreddit:

                        nonRelevantSubreddit[singleTuple[2]] = nonRelevantSubreddit[singleTuple[2]] + singleTuple[3]

                    else :

                        nonRelevantSubreddit[singleTuple[2]] = singleTuple[3]

        print ("\n\n *************************************************************************")
        print ("\nThis is for author :" + everyAuthor)
        print ("\n\n Relevant subreddit with day and count list")
        print (relevantSubreddit)

        query1 = """ select author, strftime('%Y %W', date(post_date, 'unixepoch') ), avg(score) from submissions where author in ( "4dolfin", "7_Pixel_7", 
                           "9754213680632", "AVZ_Gone", "AbstrakThought", "AdvancedFish", "AnonymousButterfly01", "BAJJAB001",
                           "BestOldExFriendRay","Bronzehawkattack", "CanNotLiveLikeThis","Cri1654", "Damn_Madame","Eric2517","Ge0rgeBr0ughton", "Gtj_2036",
                           "IsAFailure","Ivoriy", "KnowThat205", "Kookie_212",  "KriegRipper")
                             group by author, strftime('%Y %W', date(post_date, 'unixepoch'));"""

        c.execute(query1)

        fetchedData = c.fetchall()

        for everyAuthor1 in authors:

            average_score = {}

            for i in range(len(fetchedData)):

                singleTuple = fetchedData[i]

                if singleTuple[0] == everyAuthor1:
                    average_score[singleTuple[1]] = singleTuple[2]

            print ("\n\n This is for author :")
            print everyAuthor1

            print ("\n")
            print average_score



########  graph plotting

        # xs = []
        # ys = []

        dater = []
        daten = []
        dates = []

        xr = relevantSubreddit.keys()
        yr = relevantSubreddit.values()
        # ax1 = fig.add_subplot(211)
        # ax2 = fig.add_subplot(212)

        for p in xr:
            p = str(p)
            dater.append(datetime.datetime.strptime(p + ' 0', "%Y %W %w"))

        dater.sort()

        # ax1.plot(xs,ys)
        # ax2.plot(xs,ys)
        # plt.show()


        print ("\n This is non-relevant subreddit with day and count list")
        print (nonRelevantSubreddit)

        xn = nonRelevantSubreddit.keys()
        yn = nonRelevantSubreddit.values()

        for q in xn:
            q = str(q)
            daten.append(datetime.datetime.strptime(q + ' 0', "%Y %W %w"))

        daten.sort()

        ax = average_score.keys()
        ay = average_score.values()

        for k in ax:
            k = str(k)
            dates.append(datetime.datetime.strptime(k + ' 0', "%Y %W %w"))

        dates.sort()
        print dates

        plt.plot_date(dater, yr, label="Relevant subreddits", linestyle=':')

        plt.plot_date(daten, yn, label='Non-relevant subreddits', linestyle=':')

        plt.plot_date(date1, ay, label='Average score', linestyle=':')

        # ax1.title = "Relevant subreddits count"
        # ax2.title = "Non-relevant subreddits count"

        plt.xlabel("year-week")
        plt.ylabel("number of posts")
        plt.legend()
        myTitle = "Author = " + everyAuthor
        plt.title(myTitle)
        plt.show()



def main():
    conn = sqlite3.connect("submissions.db")
    c = conn.cursor()
    relevantUsersSubredditSubmissionCount(c, conn)
    # comparisonPerAuthor(c,conn)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # calling main function
    main()



#####################################################################



'''
results :

Getting relevant author's subredditwise submissions count
Considering 20 authors at a time to recognise pattern if any and getting every relevant author's subreddit wise weekly count of submissions


 *************************************************************************

This is for author :4dolfin


 Relevant subreddit with day and count list
{u'2017-47': 2, u'2017-51': 2, u'2018-02': 2, u'2017-48': 4, u'2017-49': 4, u'2018-16': 2, u'2018-12': 2}

 This is non-relevant subreddit with day and count list
{u'2015-08': 2, u'2017-48': 10, u'2015-51': 4, u'2015-50': 4, u'2015-27': 2, u'2015-52': 2, u'2018-16': 2, u'2017-34': 2, u'2017-37': 2, u'2018-12': 6, u'2018-13': 6, u'2018-11': 6, u'2015-10': 2, u'2015-34': 2, u'2015-15': 2, u'2018-14': 10, u'2015-30': 2, u'2015-12': 2, u'2017-52': 2, u'2017-51': 2, u'2017-50': 6, u'2015-33': 4, u'2017-17': 2, u'2016-48': 2, u'2015-17': 4, u'2016-38': 4, u'2016-36': 2, u'2016-34': 4, u'2016-32': 2, u'2016-33': 2, u'2015-05': 4, u'2016-12': 2, u'2014-51': 2, u'2015-42': 10, u'2015-43': 12, u'2015-46': 4, u'2015-47': 2, u'2015-44': 4, u'2015-45': 4, u'2017-22': 2, u'2016-50': 4, u'2015-28': 2, u'2015-29': 2, u'2017-25': 2, u'2015-24': 2, u'2015-26': 2, u'2017-29': 4, u'2015-20': 4, u'2015-22': 2, u'2015-23': 6, u'2017-08': 2, u'2015-19': 2, u'2017-46': 8, u'2017-47': 2, u'2018-17': 2, u'2018-01': 6, u'2017-04': 4, u'2017-05': 4, u'2016-49': 4, u'2016-04': 4, u'2016-03': 2, u'2016-01': 4, u'2016-29': 6, u'2016-42': 2, u'2016-47': 4, u'2016-46': 4, u'2016-44': 2}


 *************************************************************************

This is for author :7_Pixel_7


 Relevant subreddit with day and count list
{u'2017-04': 2, u'2017-30': 2, u'2017-33': 2, u'2017-32': 6, u'2017-39': 4, u'2017-51': 2, u'2017-22': 6, u'2017-23': 2, u'2017-24': 4, u'2017-28': 2, u'2018-28': 6, u'2017-44': 4, u'2017-47': 4, u'2017-41': 4, u'2018-29': 2, u'2017-43': 2, u'2018-27': 2, u'2018-25': 2, u'2018-24': 2, u'2017-48': 2, u'2018-06': 4, u'2016-23': 2, u'2018-23': 2, u'2016-43': 2, u'2016-47': 2, u'2016-46': 2}

 This is non-relevant subreddit with day and count list
{u'2017-07': 2, u'2017-40': 2, u'2017-24': 2, u'2016-22': 2, u'2018-24': 4, u'2018-06': 2, u'2017-22': 8, u'2017-21': 2, u'2017-31': 2, u'2017-27': 2, u'2017-33': 4, u'2017-32': 2, u'2017-29': 2, u'2016-45': 2}


 *************************************************************************

This is for author :9754213680632


 Relevant subreddit with day and count list
{u'2018-25': 2, u'2018-23': 2, u'2018-29': 2, u'2018-28': 2}

 This is non-relevant subreddit with day and count list
{u'2017-45': 4, u'2017-47': 2, u'2017-51': 2, u'2018-28': 2, u'2018-34': 4, u'2018-26': 4, u'2018-24': 6, u'2018-30': 4, u'2018-31': 4, u'2018-21': 4, u'2018-33': 2, u'2018-22': 2, u'2018-13': 6, u'2018-10': 2, u'2018-11': 2, u'2018-19': 2}


 *************************************************************************

This is for author :AVZ_Gone


 Relevant subreddit with day and count list
{u'2018-34': 2, u'2017-46': 2, u'2017-48': 2, u'2018-32': 2, u'2018-33': 4}

 This is non-relevant subreddit with day and count list
{u'2018-02': 4, u'2017-34': 2, u'2017-33': 4, u'2018-22': 30, u'2017-35': 2, u'2018-17': 6, u'2017-37': 6, u'2018-10': 2, u'2017-39': 2, u'2017-38': 4, u'2018-18': 10, u'2017-52': 10, u'2018-34': 40, u'2018-35': 16, u'2018-30': 26, u'2018-31': 16, u'2018-32': 12, u'2018-33': 24, u'2017-46': 6, u'2017-47': 4, u'2018-29': 30, u'2018-28': 22, u'2018-01': 2, u'2018-26': 24, u'2018-25': 8, u'2018-24': 14, u'2018-23': 10, u'2018-04': 2, u'2018-21': 4, u'2018-27': 24, u'2017-49': 6}


 *************************************************************************

This is for author :AbstrakThought


 Relevant subreddit with day and count list
{u'2018-09': 2, u'2018-08': 2, u'2018-01': 2, u'2018-02': 2, u'2018-12': 4, u'2018-11': 4}

 This is non-relevant subreddit with day and count list
{u'2017-17': 2, u'2017-49': 2, u'2018-16': 2, u'2018-14': 2, u'2018-15': 2, u'2017-30': 2, u'2018-10': 4, u'2018-06': 2, u'2017-39': 2, u'2017-38': 2, u'2018-18': 2, u'2018-19': 2, u'2017-04': 2, u'2017-19': 2, u'2017-18': 2, u'2017-52': 6, u'2017-50': 2, u'2017-12': 2, u'2017-10': 4, u'2018-30': 2, u'2017-16': 2, u'2018-32': 2, u'2017-09': 4, u'2018-08': 2, u'2017-44': 4, u'2017-45': 2, u'2018-20': 2, u'2017-22': 2, u'2017-23': 2, u'2017-21': 2, u'2017-26': 2, u'2017-27': 6, u'2017-24': 6, u'2017-06': 2, u'2017-29': 2, u'2018-28': 2, u'2017-08': 8, u'2017-35': 2, u'2017-46': 2, u'2017-40': 2, u'2017-41': 2, u'2017-42': 4, u'2017-43': 2, u'2018-27': 2, u'2018-26': 2, u'2018-25': 2, u'2018-24': 6, u'2017-48': 4, u'2018-04': 2, u'2018-21': 2, u'2017-07': 4, u'2017-01': 2, u'2018-07': 2, u'2018-03': 2}


 *************************************************************************

This is for author :AdvancedFish


 Relevant subreddit with day and count list
{u'2018-32': 2, u'2018-33': 2}

 This is non-relevant subreddit with day and count list
{u'2018-23': 2, u'2018-32': 4, u'2018-18': 4}


 *************************************************************************

This is for author :AnonymousButterfly01


 Relevant subreddit with day and count list
{u'2018-27': 2, u'2018-23': 2, u'2018-30': 2, u'2018-22': 2, u'2018-35': 2}

 This is non-relevant subreddit with day and count list
{u'2018-08': 2, u'2017-47': 4, u'2017-40': 2, u'2017-43': 2, u'2018-34': 2, u'2018-05': 2, u'2018-25': 4, u'2018-30': 2, u'2017-49': 2, u'2018-21': 2, u'2018-17': 4, u'2018-14': 2, u'2018-10': 4, u'2018-35': 4}


 *************************************************************************

This is for author :BAJJAB001


 Relevant subreddit with day and count list
{u'2017-52': 2, u'2017-51': 2, u'2017-50': 2, u'2018-01': 2, u'2018-03': 2, u'2018-02': 2, u'2018-05': 4, u'2018-22': 2, u'2018-20': 2, u'2018-14': 2, u'2018-11': 4}

 This is non-relevant subreddit with day and count list
{u'2018-02': 2, u'2018-05': 2, u'2018-11': 2, u'2018-22': 2, u'2017-49': 6, u'2017-35': 4, u'2017-34': 6, u'2017-37': 8, u'2018-15': 2, u'2017-31': 2, u'2018-21': 8, u'2017-33': 4, u'2017-32': 8, u'2017-39': 2, u'2017-38': 2, u'2018-14': 2, u'2018-19': 2, u'2017-52': 4, u'2017-51': 8, u'2017-50': 4, u'2018-34': 4, u'2018-35': 2, u'2018-30': 2, u'2018-31': 8, u'2018-32': 6, u'2018-33': 2, u'2018-18': 4, u'2017-26': 2, u'2017-25': 2, u'2017-28': 6, u'2017-29': 2, u'2018-09': 2, u'2017-47': 4, u'2018-29': 2, u'2017-43': 2, u'2018-01': 2, u'2018-26': 4, u'2018-03': 4, u'2018-24': 4, u'2017-48': 2, u'2018-04': 2, u'2018-07': 4, u'2018-27': 2, u'2017-36': 2, u'2018-23': 2, u'2018-12': 2, u'2018-13': 4}


 *************************************************************************

This is for author :BestOldExFriendRay


 Relevant subreddit with day and count list
{u'2018-09': 2, u'2018-24': 8, u'2017-52': 2, u'2017-51': 2, u'2018-34': 8, u'2018-26': 2, u'2018-02': 4, u'2018-05': 2, u'2018-31': 6, u'2018-07': 4, u'2018-06': 2, u'2018-01': 2, u'2018-12': 4, u'2018-11': 4, u'2018-18': 2}

 This is non-relevant subreddit with day and count list
{u'2018-24': 2, u'2018-29': 2}


 *************************************************************************

This is for author :Bronzehawkattack


 Relevant subreddit with day and count list
{u'2015-10': 2, u'2017-33': 2, u'2015-01': 2}

 This is non-relevant subreddit with day and count list
{u'2017-32': 2, u'2015-51': 2, u'2015-52': 2, u'2018-16': 2, u'2015-18': 2, u'2017-30': 2, u'2018-10': 4, u'2018-11': 2, u'2018-06': 2, u'2014-45': 2, u'2015-17': 2, u'2015-15': 2, u'2016-25': 6, u'2015-06': 2, u'2016-46': 4, u'2015-42': 2, u'2014-39': 2, u'2015-09': 2, u'2015-21': 2, u'2018-09': 2, u'2018-08': 2, u'2018-27': 2, u'2018-03': 2, u'2018-05': 2, u'2018-04': 4, u'2018-07': 4, u'2018-20': 4, u'2016-20': 2, u'2016-48': 2, u'2016-03': 2, u'2018-25': 2, u'2016-09': 2}


 *************************************************************************

This is for author :CanNotLiveLikeThis


 Relevant subreddit with day and count list
{u'2018-24': 2}

 This is non-relevant subreddit with day and count list
{}


 *************************************************************************

This is for author :Cri1654


 Relevant subreddit with day and count list
{u'2018-06': 2}

 This is non-relevant subreddit with day and count list
{u'2017-32': 2, u'2017-34': 2, u'2018-11': 2, u'2015-37': 2, u'2015-36': 2, u'2015-32': 2, u'2015-30': 2, u'2017-18': 2, u'2017-51': 2, u'2017-10': 2, u'2018-30': 4, u'2017-16': 4, u'2017-15': 2, u'2016-17': 2, u'2016-11': 2, u'2016-37': 2, u'2016-34': 2, u'2016-35': 2, u'2016-33': 2, u'2016-30': 4, u'2016-31': 2, u'2015-43': 2, u'2018-25': 2, u'2015-47': 2, u'2015-44': 2, u'2017-23': 2, u'2016-51': 2, u'2016-23': 2, u'2015-26': 2, u'2017-02': 2, u'2018-24': 2, u'2017-04': 2, u'2017-49': 2, u'2017-06': 2, u'2018-06': 2, u'2016-05': 2, u'2016-22': 2, u'2016-03': 2, u'2016-27': 6, u'2016-43': 2, u'2016-42': 2, u'2016-40': 2, u'2016-49': 2, u'2016-44': 2}


 *************************************************************************

This is for author :Damn_Madame


 Relevant subreddit with day and count list
{u'2018-34': 2, u'2018-28': 4}

 This is non-relevant subreddit with day and count list
{u'2018-28': 2, u'2018-34': 4, u'2018-26': 2, u'2018-30': 8, u'2018-31': 4, u'2018-32': 2}


 *************************************************************************

This is for author :Eric2517


 Relevant subreddit with day and count list
{u'2018-01': 2, u'2017-34': 2, u'2017-47': 2, u'2017-39': 2, u'2018-07': 2}

 This is non-relevant subreddit with day and count list
{u'2018-09': 2, u'2018-08': 2, u'2018-29': 4, u'2018-28': 2, u'2018-34': 4, u'2018-03': 4, u'2018-02': 2, u'2018-30': 2, u'2018-07': 4, u'2018-33': 2, u'2018-17': 2, u'2018-14': 2, u'2017-26': 4, u'2018-13': 2, u'2018-10': 4, u'2017-32': 2, u'2018-20': 2, u'2017-11': 2, u'2018-18': 2, u'2018-19': 2}


 *************************************************************************

This is for author :Ge0rgeBr0ughton


 Relevant subreddit with day and count list
{u'2017-46': 2, u'2017-52': 2, u'2018-01': 2, u'2018-32': 2, u'2018-16': 2, u'2017-24': 2, u'2017-32': 2, u'2018-19': 2}

 This is non-relevant subreddit with day and count list
{u'2018-02': 4, u'2017-33': 2, u'2017-04': 2, u'2018-22': 2, u'2017-35': 4, u'2017-34': 2, u'2017-37': 2, u'2018-15': 2, u'2018-12': 4, u'2018-13': 4, u'2018-10': 4, u'2018-11': 6, u'2018-05': 2, u'2018-06': 6, u'2018-18': 14, u'2018-19': 4, u'2017-52': 4, u'2018-34': 2, u'2018-35': 4, u'2018-30': 2, u'2018-32': 2, u'2018-33': 6, u'2017-05': 2, u'2017-08': 4, u'2017-45': 2, u'2017-09': 2, u'2017-27': 4, u'2017-24': 4, u'2018-09': 8, u'2018-08': 10, u'2017-47': 4, u'2018-28': 4, u'2018-01': 6, u'2018-03': 14, u'2017-03': 4, u'2017-48': 10, u'2018-04': 10, u'2018-20': 4, u'2017-02': 4}


 *************************************************************************

This is for author :Gtj_2036


 Relevant subreddit with day and count list
{u'2017-44': 2, u'2018-09': 2, u'2017-46': 4, u'2018-02': 2, u'2017-33': 2, u'2017-51': 4, u'2017-50': 4, u'2018-03': 2, u'2017-43': 2, u'2017-48': 2, u'2018-04': 4, u'2017-34': 4, u'2018-14': 2, u'2018-15': 2, u'2017-31': 2, u'2018-10': 4, u'2017-25': 2, u'2017-28': 2, u'2017-39': 6, u'2017-38': 2}

 This is non-relevant subreddit with day and count list
{u'2018-02': 4, u'2017-34': 16, u'2017-33': 10, u'2017-48': 16, u'2017-32': 14, u'2018-22': 10, u'2018-16': 12, u'2018-17': 10, u'2017-37': 4, u'2018-15': 4, u'2017-31': 8, u'2017-30': 16, u'2018-10': 8, u'2018-11': 10, u'2018-20': 14, u'2017-39': 10, u'2017-38': 8, u'2018-18': 8, u'2018-19': 10, u'2017-19': 2, u'2017-52': 6, u'2017-51': 22, u'2017-50': 8, u'2018-30': 4, u'2018-21': 6, u'2018-14': 6, u'2017-44': 14, u'2017-35': 4, u'2018-08': 12, u'2017-27': 6, u'2017-24': 2, u'2017-25': 6, u'2017-28': 4, u'2017-29': 2, u'2018-28': 6, u'2018-09': 8, u'2017-45': 18, u'2017-46': 10, u'2017-47': 6, u'2017-40': 6, u'2017-41': 10, u'2017-42': 6, u'2017-43': 6, u'2018-27': 2, u'2018-26': 4, u'2018-25': 4, u'2018-24': 8, u'2018-05': 16, u'2018-04': 18, u'2018-07': 6, u'2018-06': 22, u'2017-49': 4, u'2018-29': 4, u'2018-23': 4, u'2018-12': 24, u'2018-03': 4, u'2018-13': 24}


 *************************************************************************

This is for author :IsAFailure


 Relevant subreddit with day and count list
{u'2017-46': 2, u'2017-41': 2, u'2017-42': 2, u'2017-35': 2, u'2017-34': 6, u'2017-31': 2, u'2017-38': 2}

 This is non-relevant subreddit with day and count list
{u'2017-44': 2, u'2017-35': 2, u'2017-37': 2, u'2017-40': 2, u'2018-29': 2, u'2017-51': 2, u'2017-50': 2, u'2018-35': 2, u'2017-45': 2, u'2017-48': 4, u'2017-49': 4, u'2018-32': 2, u'2018-22': 2, u'2018-16': 2, u'2017-34': 2, u'2018-14': 2, u'2017-36': 2, u'2018-33': 2, u'2017-39': 4, u'2017-38': 2}


 *************************************************************************

This is for author :Ivoriy


 Relevant subreddit with day and count list
{u'2017-45': 6, u'2017-40': 4, u'2017-41': 4, u'2017-42': 4, u'2017-43': 4, u'2018-03': 2, u'2018-30': 2, u'2017-35': 4, u'2017-34': 2, u'2017-37': 2, u'2017-36': 2, u'2017-33': 4, u'2017-32': 4, u'2017-39': 4, u'2017-38': 2}

 This is non-relevant subreddit with day and count list
{u'2018-05': 2, u'2017-32': 2, u'2017-35': 4, u'2017-34': 8, u'2017-36': 4, u'2017-31': 2, u'2017-30': 2, u'2018-11': 4, u'2017-39': 2, u'2017-38': 4, u'2017-52': 2, u'2017-51': 2, u'2017-50': 2, u'2018-34': 2, u'2018-35': 2, u'2018-33': 2, u'2017-45': 2, u'2017-23': 2, u'2017-24': 2, u'2017-28': 2, u'2018-09': 4, u'2018-08': 8, u'2017-40': 6, u'2017-41': 2, u'2018-27': 2, u'2018-23': 2}


 *************************************************************************

This is for author :KnowThat205


 Relevant subreddit with day and count list
{u'2018-27': 2, u'2018-26': 2, u'2018-05': 2, u'2018-04': 2, u'2018-11': 2}

 This is non-relevant subreddit with day and count list
{u'2018-09': 2, u'2018-30': 2, u'2017-48': 2, u'2018-05': 2, u'2018-04': 2, u'2018-21': 2, u'2018-15': 2, u'2018-12': 2}


 *************************************************************************

This is for author :Kookie_212


 Relevant subreddit with day and count list
{u'2017-45': 2, u'2017-40': 2, u'2018-04': 6, u'2017-42': 2, u'2017-43': 2}

 This is non-relevant subreddit with day and count list
{u'2017-44': 4, u'2017-45': 2, u'2017-40': 2, u'2017-41': 2, u'2017-42': 2, u'2017-43': 4, u'2018-02': 2, u'2017-37': 2, u'2017-31': 4, u'2017-33': 6, u'2017-39': 6}


 *************************************************************************

This is for author :KriegRipper


 Relevant subreddit with day and count list
{u'2018-10': 2}

 This is non-relevant subreddit with day and count list
{u'2018-17': 4, u'2018-02': 2, u'2018-10': 4, u'2017-17': 4, u'2017-16': 6, u'2015-50': 2, u'2018-04': 4, u'2014-49': 2, u'2017-34': 6, u'2018-22': 4, u'2018-12': 4, u'2017-06': 2, u'2017-33': 8, u'2017-32': 8, u'2015-11': 2, u'2015-10': 6, u'2015-13': 2, u'2018-06': 10, u'2015-15': 4, u'2015-14': 2, u'2017-13': 4, u'2014-46': 2, u'2017-42': 2, u'2017-19': 10, u'2017-18': 10, u'2017-52': 2, u'2017-50': 4, u'2018-34': 2, u'2017-12': 2, u'2015-33': 2, u'2018-30': 2, u'2018-31': 4, u'2018-32': 2, u'2018-33': 2, u'2017-09': 2, u'2018-18': 2, u'2017-14': 6, u'2016-51': 2, u'2016-52': 2, u'2016-31': 2, u'2015-06': 4, u'2015-07': 4, u'2014-35': 2, u'2014-50': 2, u'2017-45': 2, u'2015-43': 2, u'2015-08': 2, u'2018-20': 2, u'2017-22': 4, u'2017-23': 8, u'2017-20': 6, u'2017-21': 2, u'2017-26': 4, u'2017-27': 4, u'2017-24': 6, u'2017-25': 2, u'2018-09': 2, u'2018-08': 8, u'2017-46': 4, u'2017-41': 4, u'2018-29': 8, u'2018-28': 8, u'2018-01': 6, u'2017-01': 4, u'2018-03': 4, u'2018-24': 4, u'2018-23': 10, u'2017-49': 2, u'2018-21': 8, u'2017-07': 2, u'2018-27': 8, u'2016-49': 4, u'2018-15': 2, u'2016-25': 6, u'2017-02': 2, u'2018-26': 6, u'2017-44': 2, u'2018-25': 2, u'2017-15': 6}
'''
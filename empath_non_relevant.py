import sqlite3
from sqlite3 import Error
from empath import Empath
import pickle


def empath_values(conn):
    conn.text_factory = str
    cur = conn.cursor()

    lexicon = Empath()

    # body = cur.execute("select title from submissions").fetchone()
    # while True:

    authors = ["4dolfin", "7_Pixel_7", "9754213680632", "AVZ_Gone", "AbstrakThought", "AdvancedFish", "AnonymousButterfly01", "BAJJAB001",
               "BestOldExFriendRay", "Bronzehawkattack", "CanNotLiveLikeThis", "Cri1654", "Damn_Madame", "Eric2517","Ge0rgeBr0ughton",
               "Gtj_2036", "IsAFailure", "Ivoriy", "KnowThat205", "Kookie_212", "KriegRipper"]

    listOfSubreddits = ["simpleliving", "productivity", "AskReddit", "selfimprovement", "nosurf", "TooAfraidToAsk","Advice", "antisocialmedia",
                        "confessions", "xxfitness", "DecidingToBeBetter", "hardshipmates", "psychology", "ptsd", "depression", "anxiety", "ocd",
                        "stress", "mentalhealth", "suicidewatch", "addiction", "getdisciplined", "selfhelp", "selfimprovement", "self",
                        "bipolarreddit", "bpd", "socialanxiety", "SuicideWatch", "traumatoolbox", "psychoticreddit", "StopSelfHarm",
                        "survivorsofabuse", "bipolar", "foreveralone", "panicparty"]

    score_pickle = []

    for everyAuthor in authors:

        # score_pickle = []
        query = "select title,selftext from submissions where author = '" + str(everyAuthor) + "';"
        cur.execute(query)

        # row = cur.fetchone()
        # if row == None:
        #    break
        # print(row)

        # fetchedData = cur.fetchmany(5)
        fetchedData = cur.fetchall()

        for row in fetchedData:

            # print row
            row = str(row)
            title_score = lexicon.analyze(row,
            categories=["social_media", "positive_emotion", "negative_emotion", "fear", "sleep", "hate", "cheerfulness", "aggression",
                        "attractive", "health", "nervousness", "irritability", "healing", "celebration", "anonymity", "disgust",
                        "sadness", "fun", "emotional", "joy", "affection", "lust", "ugliness", "pain", "friends","disappointment",
                        "breaking", "shame", "anger", "love"], normalize=True)

            if (title_score["social_media"] == 0.0):
                print ("\n\n*************************** \n\n")
                # print "\n\n Printing score!"
                # print title_score
                score_pickle.append(title_score)

    print ("printing final score pickle")
    print score_pickle
    print ("\n\nLength of score_pickle")
    print (len(score_pickle))
    with open("empath_non_relevant.pickle", "w") as f:
        pickle.dump(score_pickle, f)
    # lexicon = Empath()
    # title_score =lexicon.analyze(body, normalize = True)


####### for reading pickle values for each entry:
    with open("empath_non_relevant.pickle", "r") as f:
        data = pickle.load(f)

    for everyData in data:
        print ("\n\n")
        print everyData


def main():
    """ create a database connection to a SQLite database """
    conn = sqlite3.connect("submissions.db")

    empath_values(conn)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # calling main function
    main()


##################################

''' 
Result :

{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.011764705882352941, 'lust': 0.0, 'shame': 0.011764705882352941, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.011764705882352941, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.011764705882352941, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.011764705882352941, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011764705882352941, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.012244897959183673, 'lust': 0.0, 'shame': 0.0163265306122449, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.004081632653061225, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.012244897959183673, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.012244897959183673, 'pain': 0.012244897959183673, 'joy': 0.0, 'healing': 0.0, 'friends': 0.004081632653061225, 'celebration': 0.0, 'negative_emotion': 0.00816326530612245, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012244897959183673, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.012345679012345678, 'lust': 0.0, 'shame': 0.01646090534979424, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00411522633744856, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.012345679012345678, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.012345679012345678, 'pain': 0.012345679012345678, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00411522633744856, 'celebration': 0.0, 'negative_emotion': 0.00823045267489712, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012345679012345678, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.021052631578947368, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.010526315789473684, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.010638297872340425, 'lust': 0.0, 'shame': 0.010638297872340425, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.02127659574468085, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.010638297872340425, 'pain': 0.010638297872340425, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.010638297872340425, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.010638297872340425, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.008849557522123894, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.2, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.022727272727272728, 'cheerfulness': 0.0, 'aggression': 0.022727272727272728, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.022727272727272728, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.022727272727272728, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.045454545454545456, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.02531645569620253, 'hate': 0.0, 'cheerfulness': 0.012658227848101266, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.02531645569620253, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.02531645569620253, 'pain': 0.0, 'joy': 0.0, 'healing': 0.012658227848101266, 'friends': 0.0, 'celebration': 0.012658227848101266, 'negative_emotion': 0.02531645569620253, 'sadness': 0.02531645569620253, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02531645569620253, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.008333333333333333, 'lust': 0.008333333333333333, 'shame': 0.020833333333333332, 'sleep': 0.004166666666666667, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.020833333333333332, 'hate': 0.016666666666666666, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0125, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.03333333333333333, 'pain': 0.020833333333333332, 'joy': 0.008333333333333333, 'healing': 0.004166666666666667, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0125, 'sadness': 0.020833333333333332, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004166666666666667, 'positive_emotion': 0.008333333333333333, 'affection': 0.008333333333333333}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.006896551724137931, 'friends': 0.006896551724137931, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.006896551724137931, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013793103448275862, 'affection': 0.0}



{'love': 0.011049723756906077, 'lust': 0.0, 'shame': 0.022099447513812154, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0055248618784530384, 'hate': 0.022099447513812154, 'cheerfulness': 0.0, 'aggression': 0.011049723756906077, 'irritability': 0.0, 'breaking': 0.0055248618784530384, 'health': 0.011049723756906077, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.016574585635359115, 'pain': 0.027624309392265192, 'joy': 0.0, 'healing': 0.0055248618784530384, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.022099447513812154, 'sadness': 0.011049723756906077, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.022099447513812154, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.013888888888888888, 'lust': 0.0, 'shame': 0.027777777777777776, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.013888888888888888, 'pain': 0.013888888888888888, 'joy': 0.0, 'healing': 0.013888888888888888, 'friends': 0.0, 'celebration': 0.013888888888888888, 'negative_emotion': 0.013888888888888888, 'sadness': 0.013888888888888888, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.027777777777777776, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.01694915254237288, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03389830508474576, 'affection': 0.01694915254237288}



{'love': 0.0, 'lust': 0.0, 'shame': 0.013888888888888888, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.013888888888888888, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.013888888888888888, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.013888888888888888, 'negative_emotion': 0.013888888888888888, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.013888888888888888, 'positive_emotion': 0.013888888888888888, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.017543859649122806, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.1, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.013157894736842105, 'lust': 0.0, 'shame': 0.019736842105263157, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.013157894736842105, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.006578947368421052, 'health': 0.0, 'attractive': 0.006578947368421052, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.013157894736842105, 'pain': 0.013157894736842105, 'joy': 0.0, 'healing': 0.006578947368421052, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.019736842105263157, 'sadness': 0.006578947368421052, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.006578947368421052, 'positive_emotion': 0.02631578947368421, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00641025641025641, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.00641025641025641, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.03225806451612903, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.16666666666666666, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.1, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.007518796992481203, 'sleep': 0.0037593984962406013, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0037593984962406013, 'hate': 0.007518796992481203, 'cheerfulness': 0.0, 'aggression': 0.0037593984962406013, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.022556390977443608, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0037593984962406013, 'pain': 0.015037593984962405, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.011278195488721804, 'sadness': 0.007518796992481203, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.007518796992481203, 'positive_emotion': 0.0037593984962406013, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.010638297872340425, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.008928571428571428, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.026785714285714284, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.029411764705882353, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.1111111111111111, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.025, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0125, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.005128205128205128, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.010256410256410256, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.005128205128205128, 'pain': 0.005128205128205128, 'joy': 0.0, 'healing': 0.005128205128205128, 'friends': 0.010256410256410256, 'celebration': 0.0, 'negative_emotion': 0.015384615384615385, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.005128205128205128, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.05555555555555555, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.07692307692307693, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.07692307692307693, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.07692307692307693, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.07692307692307693, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.07692307692307693, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.011494252873563218, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.019230769230769232, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.023255813953488372, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.125, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.024691358024691357, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012345679012345678, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.010869565217391304, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.02, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.02, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.011904761904761904, 'celebration': 0.011904761904761904, 'negative_emotion': 0.011904761904761904, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011904761904761904, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0625, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0125, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0038314176245210726, 'sleep': 0.0038314176245210726, 'anger': 0.0038314176245210726, 'anonymity': 0.0, 'fear': 0.0038314176245210726, 'hate': 0.0038314176245210726, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.007662835249042145, 'health': 0.007662835249042145, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0038314176245210726, 'nervousness': 0.0, 'pain': 0.0038314176245210726, 'joy': 0.0, 'healing': 0.0038314176245210726, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.007662835249042145, 'sadness': 0.0038314176245210726, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0038314176245210726, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.1111111111111111, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.07692307692307693, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.047619047619047616, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.047619047619047616, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.02631578947368421, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02631578947368421, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02631578947368421, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.06666666666666667, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.25, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.125, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.06666666666666667, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.06666666666666667, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.09090909090909091, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.07692307692307693, 'sleep': 0.0, 'anger': 0.07692307692307693, 'anonymity': 0.0, 'fear': 0.07692307692307693, 'hate': 0.07692307692307693, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.15384615384615385, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.15384615384615385, 'sadness': 0.07692307692307693, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.07692307692307693, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.09090909090909091, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.1, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.1, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.07692307692307693, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.1, 'lust': 0.0, 'shame': 0.1, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.1, 'pain': 0.1, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02857142857142857, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.014285714285714285, 'emotional': 0.0, 'positive_emotion': 0.02857142857142857, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.08333333333333333, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.10526315789473684, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.10526315789473684, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.10526315789473684, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.10526315789473684, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.07142857142857142, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.012195121951219513, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012195121951219513, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0016638935108153079, 'sleep': 0.0016638935108153079, 'anger': 0.0033277870216306157, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0066555740432612314, 'cheerfulness': 0.0, 'aggression': 0.0016638935108153079, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.018302828618968387, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0016638935108153079, 'nervousness': 0.0, 'pain': 0.004991680532445923, 'joy': 0.0, 'healing': 0.004991680532445923, 'friends': 0.0066555740432612314, 'celebration': 0.011647254575707155, 'negative_emotion': 0.014975041597337771, 'sadness': 0.0033277870216306157, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004991680532445923, 'positive_emotion': 0.016638935108153077, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0022026431718061676, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0022026431718061676, 'hate': 0.0022026431718061676, 'cheerfulness': 0.0, 'aggression': 0.004405286343612335, 'irritability': 0.004405286343612335, 'breaking': 0.0, 'health': 0.004405286343612335, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.004405286343612335, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00881057268722467, 'celebration': 0.011013215859030838, 'negative_emotion': 0.019823788546255508, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.015418502202643172, 'positive_emotion': 0.019823788546255508, 'affection': 0.0}



{'love': 0.0, 'lust': 0.004545454545454545, 'shame': 0.004545454545454545, 'sleep': 0.004545454545454545, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.004545454545454545, 'hate': 0.004545454545454545, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.013636363636363636, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004545454545454545, 'pain': 0.004545454545454545, 'joy': 0.004545454545454545, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.004545454545454545, 'negative_emotion': 0.0, 'sadness': 0.004545454545454545, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.00909090909090909, 'affection': 0.004545454545454545}



{'love': 0.010416666666666666, 'lust': 0.0, 'shame': 0.020833333333333332, 'sleep': 0.010416666666666666, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.010416666666666666, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.020833333333333332, 'pain': 0.020833333333333332, 'joy': 0.0, 'healing': 0.010416666666666666, 'friends': 0.010416666666666666, 'celebration': 0.0, 'negative_emotion': 0.010416666666666666, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.010416666666666666, 'positive_emotion': 0.020833333333333332, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.013574660633484163, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00904977375565611, 'cheerfulness': 0.0, 'aggression': 0.004524886877828055, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.004524886877828055, 'attractive': 0.004524886877828055, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.00904977375565611, 'pain': 0.00904977375565611, 'joy': 0.0, 'healing': 0.004524886877828055, 'friends': 0.0, 'celebration': 0.013574660633484163, 'negative_emotion': 0.013574660633484163, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004524886877828055, 'positive_emotion': 0.004524886877828055, 'affection': 0.0}



{'love': 0.003215434083601286, 'lust': 0.006430868167202572, 'shame': 0.003215434083601286, 'sleep': 0.003215434083601286, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.003215434083601286, 'hate': 0.003215434083601286, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.003215434083601286, 'breaking': 0.003215434083601286, 'health': 0.003215434083601286, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.003215434083601286, 'pain': 0.006430868167202572, 'joy': 0.003215434083601286, 'healing': 0.0, 'friends': 0.006430868167202572, 'celebration': 0.00964630225080386, 'negative_emotion': 0.012861736334405145, 'sadness': 0.003215434083601286, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.003215434083601286, 'positive_emotion': 0.006430868167202572, 'affection': 0.00964630225080386}



{'love': 0.0, 'lust': 0.006024096385542169, 'shame': 0.0, 'sleep': 0.006024096385542169, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.012048192771084338, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.012048192771084338, 'negative_emotion': 0.018072289156626505, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.012048192771084338, 'affection': 0.0}



{'love': 0.009345794392523364, 'lust': 0.001557632398753894, 'shame': 0.012461059190031152, 'sleep': 0.001557632398753894, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.006230529595015576, 'hate': 0.003115264797507788, 'cheerfulness': 0.0, 'aggression': 0.001557632398753894, 'irritability': 0.0, 'breaking': 0.001557632398753894, 'health': 0.006230529595015576, 'attractive': 0.001557632398753894, 'disgust': 0.0, 'ugliness': 0.001557632398753894, 'nervousness': 0.012461059190031152, 'pain': 0.014018691588785047, 'joy': 0.003115264797507788, 'healing': 0.004672897196261682, 'friends': 0.001557632398753894, 'celebration': 0.0, 'negative_emotion': 0.017133956386292833, 'sadness': 0.006230529595015576, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004672897196261682, 'positive_emotion': 0.004672897196261682, 'affection': 0.001557632398753894}



{'love': 0.006968641114982578, 'lust': 0.0, 'shame': 0.010452961672473868, 'sleep': 0.003484320557491289, 'anger': 0.0, 'anonymity': 0.006968641114982578, 'fear': 0.003484320557491289, 'hate': 0.003484320557491289, 'cheerfulness': 0.003484320557491289, 'aggression': 0.0, 'irritability': 0.003484320557491289, 'breaking': 0.0, 'health': 0.003484320557491289, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.013937282229965157, 'pain': 0.013937282229965157, 'joy': 0.0, 'healing': 0.003484320557491289, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.024390243902439025, 'sadness': 0.006968641114982578, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.013937282229965157, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.004310344827586207, 'fear': 0.004310344827586207, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.004310344827586207, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.008620689655172414, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008620689655172414, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.004310344827586207, 'celebration': 0.0, 'negative_emotion': 0.004310344827586207, 'sadness': 0.004310344827586207, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.004310344827586207, 'affection': 0.0}



{'love': 0.012853470437017995, 'lust': 0.0, 'shame': 0.012853470437017995, 'sleep': 0.002570694087403599, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.002570694087403599, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.002570694087403599, 'breaking': 0.0, 'health': 0.005141388174807198, 'attractive': 0.002570694087403599, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015424164524421594, 'pain': 0.012853470437017995, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.002570694087403599, 'negative_emotion': 0.010282776349614395, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.002570694087403599, 'positive_emotion': 0.002570694087403599, 'affection': 0.0}



{'love': 0.0058997050147492625, 'lust': 0.0029498525073746312, 'shame': 0.0029498525073746312, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.011799410029498525, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0058997050147492625, 'health': 0.008849557522123894, 'attractive': 0.0029498525073746312, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.014749262536873156, 'pain': 0.0058997050147492625, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0029498525073746312, 'celebration': 0.0029498525073746312, 'negative_emotion': 0.02359882005899705, 'sadness': 0.0029498525073746312, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0058997050147492625, 'positive_emotion': 0.0029498525073746312, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.017857142857142856, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.008928571428571428, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.00631578947368421, 'lust': 0.0, 'shame': 0.00631578947368421, 'sleep': 0.002105263157894737, 'anger': 0.002105263157894737, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.004210526315789474, 'cheerfulness': 0.0, 'aggression': 0.00631578947368421, 'irritability': 0.0, 'breaking': 0.002105263157894737, 'health': 0.008421052631578947, 'attractive': 0.0, 'disgust': 0.002105263157894737, 'ugliness': 0.008421052631578947, 'nervousness': 0.00631578947368421, 'pain': 0.010526315789473684, 'joy': 0.0, 'healing': 0.002105263157894737, 'friends': 0.004210526315789474, 'celebration': 0.004210526315789474, 'negative_emotion': 0.021052631578947368, 'sadness': 0.002105263157894737, 'social_media': 0.0, 'disappointment': 0.002105263157894737, 'fun': 0.002105263157894737, 'emotional': 0.004210526315789474, 'positive_emotion': 0.002105263157894737, 'affection': 0.0}



{'love': 0.009478672985781991, 'lust': 0.0, 'shame': 0.023696682464454975, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.014218009478672985, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.009478672985781991, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009478672985781991, 'pain': 0.02843601895734597, 'joy': 0.0, 'healing': 0.004739336492890996, 'friends': 0.004739336492890996, 'celebration': 0.0, 'negative_emotion': 0.018957345971563982, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.014218009478672985, 'positive_emotion': 0.004739336492890996, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.004484304932735426, 'sleep': 0.004484304932735426, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.004484304932735426, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.004484304932735426, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017937219730941704, 'celebration': 0.004484304932735426, 'negative_emotion': 0.008968609865470852, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004484304932735426, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.005076142131979695, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.005076142131979695, 'breaking': 0.0, 'health': 0.005076142131979695, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.005076142131979695, 'pain': 0.005076142131979695, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.015228426395939087, 'negative_emotion': 0.01015228426395939, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.01015228426395939, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.002688172043010753, 'anger': 0.002688172043010753, 'anonymity': 0.0, 'fear': 0.005376344086021506, 'hate': 0.008064516129032258, 'cheerfulness': 0.0, 'aggression': 0.016129032258064516, 'irritability': 0.002688172043010753, 'breaking': 0.0, 'health': 0.002688172043010753, 'attractive': 0.005376344086021506, 'disgust': 0.002688172043010753, 'ugliness': 0.0, 'nervousness': 0.005376344086021506, 'pain': 0.010752688172043012, 'joy': 0.0, 'healing': 0.002688172043010753, 'friends': 0.01881720430107527, 'celebration': 0.0, 'negative_emotion': 0.024193548387096774, 'sadness': 0.002688172043010753, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.002688172043010753, 'emotional': 0.010752688172043012, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.009345794392523364, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.009345794392523364, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.004405286343612335, 'lust': 0.0, 'shame': 0.00881057268722467, 'sleep': 0.0, 'anger': 0.0022026431718061676, 'anonymity': 0.0, 'fear': 0.004405286343612335, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0022026431718061676, 'breaking': 0.0022026431718061676, 'health': 0.015418502202643172, 'attractive': 0.0, 'disgust': 0.0022026431718061676, 'ugliness': 0.0, 'nervousness': 0.00881057268722467, 'pain': 0.006607929515418502, 'joy': 0.0, 'healing': 0.004405286343612335, 'friends': 0.004405286343612335, 'celebration': 0.0022026431718061676, 'negative_emotion': 0.00881057268722467, 'sadness': 0.0022026431718061676, 'social_media': 0.0, 'disappointment': 0.0022026431718061676, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0022026431718061676, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.022727272727272728, 'lust': 0.0, 'shame': 0.022727272727272728, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.022727272727272728, 'pain': 0.022727272727272728, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.045454545454545456, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.034482758620689655, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.034482758620689655, 'lust': 0.0, 'shame': 0.034482758620689655, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.034482758620689655, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.034482758620689655, 'pain': 0.06896551724137931, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.06896551724137931, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02702702702702703, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02702702702702703, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0625, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.02040816326530612, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.07692307692307693, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.07692307692307693, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.125, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.125, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.125, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.125, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.25, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.125, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.015151515151515152, 'lust': 0.0, 'shame': 0.015151515151515152, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.015151515151515152, 'attractive': 0.015151515151515152, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015151515151515152, 'pain': 0.015151515151515152, 'joy': 0.0, 'healing': 0.0, 'friends': 0.015151515151515152, 'celebration': 0.015151515151515152, 'negative_emotion': 0.0, 'sadness': 0.015151515151515152, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.015151515151515152, 'positive_emotion': 0.015151515151515152, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.14285714285714285, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.14285714285714285, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.2857142857142857, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.07692307692307693, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.07692307692307693, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.027777777777777776, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.027777777777777776, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.05555555555555555, 'negative_emotion': 0.027777777777777776, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.09090909090909091, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.09090909090909091, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.1, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.05263157894736842, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.05263157894736842, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.07142857142857142, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.125, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.047619047619047616, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.047619047619047616, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.08333333333333333, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.02857142857142857, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.058823529411764705, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.058823529411764705, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.058823529411764705, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.058823529411764705, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.058823529411764705, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.058823529411764705, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.08333333333333333, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03636363636363636, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.01818181818181818, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0038022813688212928, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0038022813688212928, 'hate': 0.0076045627376425855, 'cheerfulness': 0.0, 'aggression': 0.0038022813688212928, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.011406844106463879, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0038022813688212928, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0038022813688212928, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.019230769230769232, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.005, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.005, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.01, 'fun': 0.0, 'emotional': 0.005, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.005747126436781609, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.005747126436781609, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.011494252873563218, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011494252873563218, 'positive_emotion': 0.005747126436781609, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.023809523809523808, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.023809523809523808, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.023809523809523808, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.023809523809523808, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.1111111111111111, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015384615384615385, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.015384615384615385, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.03125, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03125, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03125, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.011363636363636364, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.014925373134328358, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0625, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0392156862745098, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.034482758620689655, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.038461538461538464, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.1, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02631578947368421, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03125, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03125, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.03571428571428571, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03571428571428571, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03571428571428571, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.03225806451612903, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03225806451612903, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.05263157894736842, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.05263157894736842, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.05263157894736842, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05263157894736842, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.05263157894736842, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.045454545454545456, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.045454545454545456, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.058823529411764705, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0625, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.016666666666666666, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.058823529411764705, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.1, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.045454545454545456, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.045454545454545456, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.045454545454545456, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.045454545454545456, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.07692307692307693, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.07692307692307693, 'joy': 0.0, 'healing': 0.0, 'friends': 0.07692307692307693, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.1, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.047619047619047616, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02702702702702703, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.01818181818181818, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03636363636363636, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.020833333333333332, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.009900990099009901, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.019801980198019802, 'cheerfulness': 0.0, 'aggression': 0.009900990099009901, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.009900990099009901, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.019801980198019802, 'joy': 0.0, 'healing': 0.0, 'friends': 0.009900990099009901, 'celebration': 0.0, 'negative_emotion': 0.019801980198019802, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.009900990099009901, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0234375, 'lust': 0.0078125, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0078125, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0390625, 'celebration': 0.0078125, 'negative_emotion': 0.0078125, 'sadness': 0.0078125, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0078125, 'positive_emotion': 0.03125, 'affection': 0.015625}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017857142857142856, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.01, 'lust': 0.0, 'shame': 0.02, 'sleep': 0.01, 'anger': 0.01, 'anonymity': 0.0, 'fear': 0.01, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.02, 'attractive': 0.0, 'disgust': 0.01, 'ugliness': 0.0, 'nervousness': 0.02, 'pain': 0.02, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.01, 'sadness': 0.02, 'social_media': 0.0, 'disappointment': 0.01, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.017241379310344827, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.017241379310344827, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.017241379310344827, 'joy': 0.0, 'healing': 0.008620689655172414, 'friends': 0.008620689655172414, 'celebration': 0.0, 'negative_emotion': 0.017241379310344827, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.017241379310344827, 'positive_emotion': 0.008620689655172414, 'affection': 0.0}



{'love': 0.02564102564102564, 'lust': 0.0, 'shame': 0.01282051282051282, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01282051282051282, 'pain': 0.01282051282051282, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02564102564102564, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02564102564102564, 'affection': 0.01282051282051282}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.009523809523809525, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.009523809523809525, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.009523809523809525, 'emotional': 0.0, 'positive_emotion': 0.01904761904761905, 'affection': 0.0}



{'love': 0.019230769230769232, 'lust': 0.019230769230769232, 'shame': 0.0, 'sleep': 0.019230769230769232, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.019230769230769232, 'celebration': 0.019230769230769232, 'negative_emotion': 0.019230769230769232, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.025, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.025, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.025, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.00980392156862745, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.014705882352941176, 'celebration': 0.0, 'negative_emotion': 0.0196078431372549, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.014705882352941176, 'emotional': 0.0, 'positive_emotion': 0.024509803921568627, 'affection': 0.00980392156862745}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.02702702702702703, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01818181818181818, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.027777777777777776, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.010309278350515464, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.038461538461538464, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.029411764705882353, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.04, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.04, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02564102564102564, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.023809523809523808, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.015384615384615385, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02564102564102564, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.02702702702702703, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.1, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.1, 'negative_emotion': 0.1, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.1, 'affection': 0.0}



{'love': 0.017543859649122806, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017543859649122806, 'celebration': 0.017543859649122806, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03508771929824561, 'affection': 0.017543859649122806}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.014285714285714285, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.014285714285714285, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.03571428571428571, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.03571428571428571, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.03571428571428571, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03571428571428571, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.03571428571428571, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.03389830508474576, 'disgust': 0.0, 'ugliness': 0.01694915254237288, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.16666666666666666, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.012345679012345678, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012345679012345678, 'celebration': 0.0, 'negative_emotion': 0.024691358024691357, 'sadness': 0.012345679012345678, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012345679012345678, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.011111111111111112, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.011111111111111112, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.011111111111111112, 'pain': 0.011111111111111112, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.022222222222222223, 'negative_emotion': 0.011111111111111112, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.004878048780487805, 'lust': 0.004878048780487805, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.004878048780487805, 'cheerfulness': 0.0, 'aggression': 0.004878048780487805, 'irritability': 0.004878048780487805, 'breaking': 0.0, 'health': 0.004878048780487805, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004878048780487805, 'pain': 0.004878048780487805, 'joy': 0.0, 'healing': 0.004878048780487805, 'friends': 0.0, 'celebration': 0.004878048780487805, 'negative_emotion': 0.00975609756097561, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004878048780487805, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.012987012987012988, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.025974025974025976, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.010101010101010102, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.00823045267489712, 'lust': 0.0, 'shame': 0.01646090534979424, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00823045267489712, 'cheerfulness': 0.0, 'aggression': 0.00411522633744856, 'irritability': 0.0, 'breaking': 0.00823045267489712, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.00411522633744856, 'pain': 0.012345679012345678, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00823045267489712, 'celebration': 0.0, 'negative_emotion': 0.012345679012345678, 'sadness': 0.012345679012345678, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.00823045267489712, 'positive_emotion': 0.00411522633744856, 'affection': 0.00411522633744856}



{'love': 0.009708737864077669, 'lust': 0.0048543689320388345, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.009708737864077669, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.009708737864077669, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009708737864077669, 'pain': 0.0048543689320388345, 'joy': 0.0, 'healing': 0.0, 'friends': 0.009708737864077669, 'celebration': 0.0048543689320388345, 'negative_emotion': 0.009708737864077669, 'sadness': 0.009708737864077669, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0048543689320388345, 'emotional': 0.0, 'positive_emotion': 0.0048543689320388345, 'affection': 0.0048543689320388345}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.018867924528301886, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.018867924528301886, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03773584905660377, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.018867924528301886, 'affection': 0.0}



{'love': 0.017241379310344827, 'lust': 0.0, 'shame': 0.017241379310344827, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.008620689655172414, 'hate': 0.02586206896551724, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.017241379310344827, 'nervousness': 0.017241379310344827, 'pain': 0.008620689655172414, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04310344827586207, 'sadness': 0.008620689655172414, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.017241379310344827, 'affection': 0.008620689655172414}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02702702702702703, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02702702702702703, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.022727272727272728, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.022727272727272728, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.017543859649122806, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.006289308176100629, 'hate': 0.006289308176100629, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.006289308176100629, 'pain': 0.006289308176100629, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.025157232704402517, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.023255813953488372, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.023255813953488372, 'pain': 0.023255813953488372, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.09302325581395349, 'sadness': 0.023255813953488372, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.023255813953488372, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0028653295128939827, 'lust': 0.0, 'shame': 0.0028653295128939827, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0028653295128939827, 'hate': 0.008595988538681949, 'cheerfulness': 0.0, 'aggression': 0.0028653295128939827, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0028653295128939827, 'pain': 0.008595988538681949, 'joy': 0.0, 'healing': 0.0, 'friends': 0.008595988538681949, 'celebration': 0.0, 'negative_emotion': 0.008595988538681949, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0028653295128939827, 'emotional': 0.008595988538681949, 'positive_emotion': 0.0028653295128939827, 'affection': 0.0028653295128939827}



{'love': 0.009523809523809525, 'lust': 0.0038095238095238095, 'shame': 0.0019047619047619048, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0019047619047619048, 'hate': 0.0038095238095238095, 'cheerfulness': 0.0038095238095238095, 'aggression': 0.0, 'irritability': 0.0019047619047619048, 'breaking': 0.0038095238095238095, 'health': 0.005714285714285714, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0019047619047619048, 'nervousness': 0.0038095238095238095, 'pain': 0.0038095238095238095, 'joy': 0.0, 'healing': 0.0, 'friends': 0.007619047619047619, 'celebration': 0.0019047619047619048, 'negative_emotion': 0.011428571428571429, 'sadness': 0.0038095238095238095, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0019047619047619048, 'emotional': 0.0038095238095238095, 'positive_emotion': 0.009523809523809525, 'affection': 0.0019047619047619048}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.024390243902439025, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.05555555555555555, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.05555555555555555, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.05555555555555555, 'affection': 0.05555555555555555}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.09090909090909091, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.09090909090909091, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.017094017094017096, 'lust': 0.0, 'shame': 0.008547008547008548, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.008547008547008548, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.017094017094017096, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008547008547008548, 'pain': 0.008547008547008548, 'joy': 0.0, 'healing': 0.008547008547008548, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.014705882352941176, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.1, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.011764705882352941, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03529411764705882, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011764705882352941, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.007194244604316547, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.07142857142857142, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.07142857142857142, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.03488372093023256, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.011627906976744186, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.023255813953488372, 'emotional': 0.0, 'positive_emotion': 0.023255813953488372, 'affection': 0.0}



{'love': 0.014285714285714285, 'lust': 0.0, 'shame': 0.007142857142857143, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.014285714285714285, 'health': 0.007142857142857143, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.007142857142857143, 'pain': 0.007142857142857143, 'joy': 0.0, 'healing': 0.007142857142857143, 'friends': 0.02142857142857143, 'celebration': 0.0, 'negative_emotion': 0.02142857142857143, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02142857142857143, 'affection': 0.007142857142857143}



{'love': 0.010416666666666666, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.03125, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.00819672131147541, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.00819672131147541, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.00819672131147541, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.08333333333333333, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.08333333333333333, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0076045627376425855, 'lust': 0.0038022813688212928, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0076045627376425855, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0076045627376425855, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0038022813688212928, 'healing': 0.0038022813688212928, 'friends': 0.011406844106463879, 'celebration': 0.011406844106463879, 'negative_emotion': 0.0038022813688212928, 'sadness': 0.0038022813688212928, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.022813688212927757, 'affection': 0.0038022813688212928}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.07142857142857142, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0044444444444444444, 'lust': 0.0, 'shame': 0.0044444444444444444, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0044444444444444444, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0044444444444444444, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0044444444444444444, 'pain': 0.0044444444444444444, 'joy': 0.0, 'healing': 0.0044444444444444444, 'friends': 0.008888888888888889, 'celebration': 0.013333333333333334, 'negative_emotion': 0.0, 'sadness': 0.0044444444444444444, 'social_media': 0.0, 'disappointment': 0.008888888888888889, 'fun': 0.013333333333333334, 'emotional': 0.0, 'positive_emotion': 0.008888888888888889, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.01282051282051282, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.013157894736842105, 'lust': 0.0, 'shame': 0.02631578947368421, 'sleep': 0.0, 'anger': 0.019736842105263157, 'anonymity': 0.0, 'fear': 0.02631578947368421, 'hate': 0.006578947368421052, 'cheerfulness': 0.006578947368421052, 'aggression': 0.013157894736842105, 'irritability': 0.006578947368421052, 'breaking': 0.0, 'health': 0.013157894736842105, 'attractive': 0.0, 'disgust': 0.006578947368421052, 'ugliness': 0.0, 'nervousness': 0.02631578947368421, 'pain': 0.03289473684210526, 'joy': 0.0, 'healing': 0.0, 'friends': 0.006578947368421052, 'celebration': 0.006578947368421052, 'negative_emotion': 0.013157894736842105, 'sadness': 0.019736842105263157, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.006578947368421052, 'positive_emotion': 0.006578947368421052, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.025423728813559324, 'lust': 0.00847457627118644, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00847457627118644, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00847457627118644, 'celebration': 0.0, 'negative_emotion': 0.01694915254237288, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.025423728813559324, 'affection': 0.01694915254237288}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.010869565217391304, 'lust': 0.0, 'shame': 0.021739130434782608, 'sleep': 0.0, 'anger': 0.010869565217391304, 'anonymity': 0.0, 'fear': 0.010869565217391304, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.021739130434782608, 'pain': 0.021739130434782608, 'joy': 0.0, 'healing': 0.0, 'friends': 0.010869565217391304, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.010869565217391304, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.010869565217391304, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.013333333333333334, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.013333333333333334, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.013333333333333334, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.02666666666666667, 'emotional': 0.0, 'positive_emotion': 0.013333333333333334, 'affection': 0.013333333333333334}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.008130081300813009, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.020833333333333332, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.005405405405405406, 'lust': 0.005405405405405406, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.010810810810810811, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.005405405405405406, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.010309278350515464, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.010309278350515464, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.011764705882352941, 'affection': 0.011764705882352941}



{'love': 0.05555555555555555, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.05555555555555555, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.05555555555555555, 'affection': 0.05555555555555555}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.023809523809523808, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.015873015873015872, 'sadness': 0.007936507936507936, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.007936507936507936, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.013793103448275862, 'lust': 0.0, 'shame': 0.006896551724137931, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.006896551724137931, 'irritability': 0.0, 'breaking': 0.006896551724137931, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.013793103448275862, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.006896551724137931, 'celebration': 0.0, 'negative_emotion': 0.027586206896551724, 'sadness': 0.006896551724137931, 'social_media': 0.0, 'disappointment': 0.006896551724137931, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.027586206896551724, 'affection': 0.006896551724137931}



{'love': 0.01818181818181818, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.00909090909090909, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01818181818181818, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.01020408163265306, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0056179775280898875, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.016853932584269662, 'cheerfulness': 0.0056179775280898875, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0056179775280898875, 'healing': 0.0, 'friends': 0.0056179775280898875, 'celebration': 0.0, 'negative_emotion': 0.011235955056179775, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.016853932584269662, 'affection': 0.0}



{'love': 0.019230769230769232, 'lust': 0.0, 'shame': 0.009615384615384616, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009615384615384616, 'pain': 0.009615384615384616, 'joy': 0.0, 'healing': 0.0, 'friends': 0.019230769230769232, 'celebration': 0.019230769230769232, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.028846153846153848, 'emotional': 0.0, 'positive_emotion': 0.009615384615384616, 'affection': 0.009615384615384616}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.004149377593360996, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.004149377593360996, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.004149377593360996, 'ugliness': 0.004149377593360996, 'nervousness': 0.0, 'pain': 0.004149377593360996, 'joy': 0.0, 'healing': 0.0, 'friends': 0.004149377593360996, 'celebration': 0.0, 'negative_emotion': 0.024896265560165973, 'sadness': 0.004149377593360996, 'social_media': 0.0, 'disappointment': 0.004149377593360996, 'fun': 0.004149377593360996, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.031578947368421054, 'lust': 0.0, 'shame': 0.010526315789473684, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.010526315789473684, 'pain': 0.010526315789473684, 'joy': 0.0, 'healing': 0.0, 'friends': 0.005263157894736842, 'celebration': 0.005263157894736842, 'negative_emotion': 0.005263157894736842, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03684210526315789, 'affection': 0.005263157894736842}



{'love': 0.0072992700729927005, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0072992700729927005, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.018518518518518517, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.018518518518518517, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.09090909090909091, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.019230769230769232, 'lust': 0.0, 'shame': 0.019230769230769232, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.019230769230769232, 'pain': 0.019230769230769232, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.019230769230769232, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.030303030303030304, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.030303030303030304, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.009345794392523364, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.009345794392523364, 'irritability': 0.0, 'breaking': 0.009345794392523364, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.009345794392523364, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.018691588785046728, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.009345794392523364, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.011235955056179775, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.011235955056179775, 'hate': 0.0449438202247191, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.011235955056179775, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.011235955056179775, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.011235955056179775, 'negative_emotion': 0.056179775280898875, 'sadness': 0.02247191011235955, 'social_media': 0.0, 'disappointment': 0.011235955056179775, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0047169811320754715, 'lust': 0.0, 'shame': 0.0047169811320754715, 'sleep': 0.0047169811320754715, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0047169811320754715, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0047169811320754715, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0047169811320754715, 'pain': 0.0047169811320754715, 'joy': 0.0, 'healing': 0.014150943396226415, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.018867924528301886, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0047169811320754715, 'positive_emotion': 0.009433962264150943, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.007692307692307693, 'friends': 0.015384615384615385, 'celebration': 0.015384615384615385, 'negative_emotion': 0.007692307692307693, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.007692307692307693, 'emotional': 0.007692307692307693, 'positive_emotion': 0.023076923076923078, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.007662835249042145, 'sleep': 0.007662835249042145, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.007662835249042145, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.007662835249042145, 'health': 0.0, 'attractive': 0.0038314176245210726, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.01532567049808429, 'joy': 0.0, 'healing': 0.0, 'friends': 0.011494252873563218, 'celebration': 0.0038314176245210726, 'negative_emotion': 0.007662835249042145, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0038314176245210726, 'emotional': 0.007662835249042145, 'positive_emotion': 0.0038314176245210726, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.1111111111111111, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.00641025641025641, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.00641025641025641, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00641025641025641, 'celebration': 0.0, 'negative_emotion': 0.01282051282051282, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01282051282051282, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.014492753623188406, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.028985507246376812, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.01, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.01, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.01, 'joy': 0.0, 'healing': 0.0, 'friends': 0.01, 'celebration': 0.0, 'negative_emotion': 0.03, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.01, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.004016064257028112, 'lust': 0.0, 'shame': 0.004016064257028112, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.004016064257028112, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.004016064257028112, 'health': 0.004016064257028112, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.004016064257028112, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.004016064257028112, 'negative_emotion': 0.0321285140562249, 'sadness': 0.004016064257028112, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004016064257028112, 'positive_emotion': 0.004016064257028112, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.010752688172043012, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.010752688172043012, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.010752688172043012, 'negative_emotion': 0.043010752688172046, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.01020408163265306, 'shame': 0.01020408163265306, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.01020408163265306, 'hate': 0.02040816326530612, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01020408163265306, 'pain': 0.01020408163265306, 'joy': 0.01020408163265306, 'healing': 0.01020408163265306, 'friends': 0.01020408163265306, 'celebration': 0.0, 'negative_emotion': 0.02040816326530612, 'sadness': 0.02040816326530612, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.01020408163265306, 'positive_emotion': 0.02040816326530612, 'affection': 0.01020408163265306}



{'love': 0.005952380952380952, 'lust': 0.005952380952380952, 'shame': 0.005952380952380952, 'sleep': 0.0, 'anger': 0.005952380952380952, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02976190476190476, 'cheerfulness': 0.005952380952380952, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.005952380952380952, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.011904761904761904, 'joy': 0.005952380952380952, 'healing': 0.0, 'friends': 0.011904761904761904, 'celebration': 0.0, 'negative_emotion': 0.03571428571428571, 'sadness': 0.011904761904761904, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.005952380952380952, 'positive_emotion': 0.017857142857142856, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03571428571428571, 'sadness': 0.07142857142857142, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.07142857142857142, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.041666666666666664, 'lust': 0.0, 'shame': 0.041666666666666664, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.041666666666666664, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.041666666666666664, 'pain': 0.041666666666666664, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0425531914893617, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02127659574468085, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.009708737864077669, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.038834951456310676, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.009708737864077669, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.009708737864077669, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.009708737864077669, 'positive_emotion': 0.009708737864077669, 'affection': 0.0}



{'love': 0.009900990099009901, 'lust': 0.0, 'shame': 0.009900990099009901, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.009900990099009901, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.019801980198019802, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009900990099009901, 'pain': 0.009900990099009901, 'joy': 0.0, 'healing': 0.009900990099009901, 'friends': 0.009900990099009901, 'celebration': 0.009900990099009901, 'negative_emotion': 0.019801980198019802, 'sadness': 0.009900990099009901, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.009900990099009901, 'positive_emotion': 0.019801980198019802, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.018633540372670808, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.006211180124223602, 'health': 0.0, 'attractive': 0.006211180124223602, 'disgust': 0.0, 'ugliness': 0.006211180124223602, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.006211180124223602, 'friends': 0.006211180124223602, 'celebration': 0.0, 'negative_emotion': 0.031055900621118012, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.006211180124223602, 'affection': 0.0}



{'love': 0.015873015873015872, 'lust': 0.0, 'shame': 0.031746031746031744, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.015873015873015872, 'hate': 0.015873015873015872, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.015873015873015872, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.031746031746031744, 'pain': 0.015873015873015872, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.015873015873015872, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.015873015873015872, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.012422360248447204, 'lust': 0.006211180124223602, 'shame': 0.0, 'sleep': 0.003105590062111801, 'anger': 0.003105590062111801, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.012422360248447204, 'aggression': 0.003105590062111801, 'irritability': 0.0, 'breaking': 0.009316770186335404, 'health': 0.006211180124223602, 'attractive': 0.0, 'disgust': 0.003105590062111801, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.006211180124223602, 'joy': 0.003105590062111801, 'healing': 0.006211180124223602, 'friends': 0.0, 'celebration': 0.006211180124223602, 'negative_emotion': 0.006211180124223602, 'sadness': 0.006211180124223602, 'social_media': 0.0, 'disappointment': 0.003105590062111801, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.021739130434782608, 'affection': 0.0}



{'love': 0.011799410029498525, 'lust': 0.0058997050147492625, 'shame': 0.0, 'sleep': 0.0029498525073746312, 'anger': 0.0029498525073746312, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.011799410029498525, 'aggression': 0.0029498525073746312, 'irritability': 0.0, 'breaking': 0.008849557522123894, 'health': 0.0058997050147492625, 'attractive': 0.0, 'disgust': 0.0029498525073746312, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0058997050147492625, 'joy': 0.0029498525073746312, 'healing': 0.008849557522123894, 'friends': 0.0, 'celebration': 0.0058997050147492625, 'negative_emotion': 0.014749262536873156, 'sadness': 0.0058997050147492625, 'social_media': 0.0, 'disappointment': 0.0029498525073746312, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02359882005899705, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.029411764705882353, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.01, 'lust': 0.0, 'shame': 0.03, 'sleep': 0.0, 'anger': 0.01, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.06, 'cheerfulness': 0.01, 'aggression': 0.01, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.01, 'attractive': 0.0, 'disgust': 0.01, 'ugliness': 0.01, 'nervousness': 0.01, 'pain': 0.02, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.01, 'negative_emotion': 0.05, 'sadness': 0.01, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.00558659217877095, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0111731843575419, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.00558659217877095, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.00558659217877095, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0111731843575419, 'celebration': 0.0, 'negative_emotion': 0.0111731843575419, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.00558659217877095, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.00558659217877095, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0111731843575419, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.00558659217877095, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.00558659217877095, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0111731843575419, 'celebration': 0.0, 'negative_emotion': 0.0111731843575419, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.00558659217877095, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.07142857142857142, 'cheerfulness': 0.0, 'aggression': 0.07142857142857142, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.07142857142857142, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.07142857142857142, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.012048192771084338, 'lust': 0.0, 'shame': 0.008032128514056224, 'sleep': 0.0, 'anger': 0.004016064257028112, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.01606425702811245, 'cheerfulness': 0.0, 'aggression': 0.008032128514056224, 'irritability': 0.004016064257028112, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.004016064257028112, 'ugliness': 0.012048192771084338, 'nervousness': 0.008032128514056224, 'pain': 0.012048192771084338, 'joy': 0.0, 'healing': 0.0, 'friends': 0.004016064257028112, 'celebration': 0.0, 'negative_emotion': 0.01606425702811245, 'sadness': 0.004016064257028112, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.004016064257028112, 'emotional': 0.008032128514056224, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.013157894736842105, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.013157894736842105, 'attractive': 0.02631578947368421, 'disgust': 0.0, 'ugliness': 0.013157894736842105, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.05263157894736842, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013157894736842105, 'affection': 0.013157894736842105}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.009345794392523364, 'joy': 0.0, 'healing': 0.0, 'friends': 0.018691588785046728, 'celebration': 0.0, 'negative_emotion': 0.009345794392523364, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.014084507042253521, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.007042253521126761, 'nervousness': 0.0, 'pain': 0.007042253521126761, 'joy': 0.0, 'healing': 0.0, 'friends': 0.028169014084507043, 'celebration': 0.0, 'negative_emotion': 0.014084507042253521, 'sadness': 0.014084507042253521, 'social_media': 0.0, 'disappointment': 0.007042253521126761, 'fun': 0.0, 'emotional': 0.02112676056338028, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.012658227848101266, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.012658227848101266, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.012658227848101266, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.013986013986013986, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.006993006993006993, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.013986013986013986, 'disgust': 0.02097902097902098, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.013986013986013986, 'celebration': 0.006993006993006993, 'negative_emotion': 0.013986013986013986, 'sadness': 0.013986013986013986, 'social_media': 0.0, 'disappointment': 0.006993006993006993, 'fun': 0.006993006993006993, 'emotional': 0.006993006993006993, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.00684931506849315, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.00684931506849315, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0273972602739726, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.010101010101010102, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.010101010101010102, 'negative_emotion': 0.020202020202020204, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.014598540145985401, 'lust': 0.014598540145985401, 'shame': 0.0, 'sleep': 0.0072992700729927005, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0072992700729927005, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0072992700729927005, 'joy': 0.0072992700729927005, 'healing': 0.0, 'friends': 0.0072992700729927005, 'celebration': 0.0, 'negative_emotion': 0.014598540145985401, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0072992700729927005, 'affection': 0.0072992700729927005}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.014925373134328358, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.018867924528301886, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.018867924528301886, 'attractive': 0.018867924528301886, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.018867924528301886, 'pain': 0.0, 'joy': 0.0, 'healing': 0.018867924528301886, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.018867924528301886, 'sadness': 0.018867924528301886, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.018867924528301886, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.013157894736842105, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02631578947368421, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.009523809523809525, 'lust': 0.0008658008658008658, 'shame': 0.012121212121212121, 'sleep': 0.0017316017316017316, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.003463203463203463, 'hate': 0.009523809523809525, 'cheerfulness': 0.0017316017316017316, 'aggression': 0.0017316017316017316, 'irritability': 0.0, 'breaking': 0.0008658008658008658, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0008658008658008658, 'ugliness': 0.005194805194805195, 'nervousness': 0.008658008658008658, 'pain': 0.012121212121212121, 'joy': 0.0017316017316017316, 'healing': 0.003463203463203463, 'friends': 0.004329004329004329, 'celebration': 0.0025974025974025974, 'negative_emotion': 0.02943722943722944, 'sadness': 0.0017316017316017316, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0017316017316017316, 'emotional': 0.006060606060606061, 'positive_emotion': 0.011255411255411256, 'affection': 0.0008658008658008658}



{'love': 0.03333333333333333, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.03333333333333333, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03333333333333333, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03333333333333333, 'affection': 0.03333333333333333}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.1, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.029411764705882353, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.058823529411764705, 'pain': 0.029411764705882353, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.058823529411764705, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.05, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.022727272727272728, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.011363636363636364, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0625, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0625, 'pain': 0.0625, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0625, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0625, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.045454545454545456, 'lust': 0.0, 'shame': 0.045454545454545456, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.045454545454545456, 'pain': 0.045454545454545456, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.045454545454545456, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.02654867256637168, 'lust': 0.008849557522123894, 'shame': 0.05309734513274336, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.02654867256637168, 'hate': 0.017699115044247787, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.008849557522123894, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.035398230088495575, 'pain': 0.035398230088495575, 'joy': 0.008849557522123894, 'healing': 0.0, 'friends': 0.008849557522123894, 'celebration': 0.017699115044247787, 'negative_emotion': 0.02654867256637168, 'sadness': 0.02654867256637168, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.017699115044247787, 'positive_emotion': 0.02654867256637168, 'affection': 0.008849557522123894}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.02127659574468085, 'hate': 0.010638297872340425, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.031914893617021274, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.02127659574468085, 'pain': 0.010638297872340425, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.010638297872340425, 'sadness': 0.02127659574468085, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.010638297872340425, 'positive_emotion': 0.010638297872340425, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.021739130434782608, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.021739130434782608, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.021739130434782608, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.021739130434782608, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.021739130434782608, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.010416666666666666, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.012048192771084338, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.012048192771084338, 'hate': 0.024096385542168676, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.012048192771084338, 'pain': 0.024096385542168676, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03614457831325301, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012048192771084338, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.013888888888888888, 'negative_emotion': 0.013888888888888888, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013888888888888888, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.013888888888888888, 'negative_emotion': 0.013888888888888888, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013888888888888888, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.025974025974025976, 'sleep': 0.0, 'anger': 0.025974025974025976, 'anonymity': 0.0, 'fear': 0.06493506493506493, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.012987012987012988, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.03896103896103896, 'pain': 0.05194805194805195, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.06493506493506493, 'sadness': 0.03896103896103896, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.04, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.02, 'hate': 0.02, 'cheerfulness': 0.02, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.02, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.02, 'pain': 0.02, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.02, 'negative_emotion': 0.04, 'sadness': 0.04, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.06, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.02, 'lust': 0.0, 'shame': 0.04, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.04, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.02, 'pain': 0.06, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02, 'celebration': 0.0, 'negative_emotion': 0.06, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.02, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.011235955056179775, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.028985507246376812, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.028985507246376812, 'negative_emotion': 0.014492753623188406, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.028985507246376812, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.023809523809523808, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.047619047619047616, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.04225352112676056, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.014084507042253521, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.04225352112676056, 'pain': 0.028169014084507043, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.028169014084507043, 'sadness': 0.014084507042253521, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03225806451612903, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03225806451612903, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.03225806451612903, 'emotional': 0.0, 'positive_emotion': 0.03225806451612903, 'affection': 0.03225806451612903}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.05263157894736842, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.06818181818181818, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.058823529411764705, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.058823529411764705, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.022222222222222223, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.044444444444444446, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.016129032258064516, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.016129032258064516, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.002898550724637681, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.002898550724637681, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.005797101449275362, 'friends': 0.0, 'celebration': 0.002898550724637681, 'negative_emotion': 0.002898550724637681, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.002898550724637681, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.09090909090909091, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.02702702702702703, 'lust': 0.02702702702702703, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.018867924528301886, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02702702702702703, 'celebration': 0.0, 'negative_emotion': 0.04054054054054054, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02702702702702703, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.015151515151515152, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.010416666666666666, 'anonymity': 0.0, 'fear': 0.020833333333333332, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.010416666666666666, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.010416666666666666, 'ugliness': 0.0, 'nervousness': 0.020833333333333332, 'pain': 0.010416666666666666, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.020833333333333332, 'sadness': 0.010416666666666666, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.010416666666666666, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.02857142857142857, 'lust': 0.0, 'shame': 0.014285714285714285, 'sleep': 0.02857142857142857, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.014285714285714285, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.04285714285714286, 'pain': 0.014285714285714285, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.014285714285714285, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.014084507042253521, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.008695652173913044, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.017391304347826087, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017391304347826087, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.008695652173913044, 'affection': 0.008695652173913044}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.028169014084507043, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.018518518518518517, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.037037037037037035, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.037037037037037035, 'celebration': 0.0, 'negative_emotion': 0.018518518518518517, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.018518518518518517, 'positive_emotion': 0.018518518518518517, 'affection': 0.018518518518518517}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.013333333333333334, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02666666666666667, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.022222222222222223, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.022222222222222223, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.044444444444444446, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.022222222222222223, 'celebration': 0.0, 'negative_emotion': 0.022222222222222223, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.044444444444444446, 'affection': 0.022222222222222223}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.004310344827586207, 'shame': 0.004310344827586207, 'sleep': 0.02586206896551724, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.008620689655172414, 'hate': 0.004310344827586207, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.004310344827586207, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004310344827586207, 'pain': 0.004310344827586207, 'joy': 0.004310344827586207, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.008620689655172414, 'sadness': 0.008620689655172414, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.004310344827586207, 'affection': 0.004310344827586207}



{'love': 0.008130081300813009, 'lust': 0.0, 'shame': 0.016260162601626018, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.008130081300813009, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.008130081300813009, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.016260162601626018, 'pain': 0.016260162601626018, 'joy': 0.0, 'healing': 0.0, 'friends': 0.024390243902439025, 'celebration': 0.024390243902439025, 'negative_emotion': 0.016260162601626018, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.016260162601626018, 'emotional': 0.008130081300813009, 'positive_emotion': 0.016260162601626018, 'affection': 0.0}



{'love': 0.008130081300813009, 'lust': 0.0, 'shame': 0.008130081300813009, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.016260162601626018, 'cheerfulness': 0.0, 'aggression': 0.016260162601626018, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008130081300813009, 'pain': 0.008130081300813009, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.008130081300813009, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.008130081300813009, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.006493506493506494, 'lust': 0.012987012987012988, 'shame': 0.006493506493506494, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.012987012987012988, 'hate': 0.006493506493506494, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.025974025974025976, 'pain': 0.012987012987012988, 'joy': 0.006493506493506494, 'healing': 0.006493506493506494, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.025974025974025976, 'sadness': 0.006493506493506494, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.012987012987012988, 'affection': 0.006493506493506494}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.047619047619047616, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.023809523809523808, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.05555555555555555, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.05555555555555555, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05555555555555555, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.05555555555555555}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.1111111111111111, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.1111111111111111, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.015384615384615385, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.015384615384615385, 'friends': 0.015384615384615385, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02631578947368421, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.08333333333333333, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.08333333333333333, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.009433962264150943, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009433962264150943, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.008771929824561403, 'negative_emotion': 0.008771929824561403, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.05555555555555555, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.008403361344537815, 'lust': 0.0, 'shame': 0.008403361344537815, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.008403361344537815, 'irritability': 0.0, 'breaking': 0.008403361344537815, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008403361344537815, 'pain': 0.01680672268907563, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.01680672268907563, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.01680672268907563, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03333333333333333, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.03333333333333333, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.008064516129032258, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.008064516129032258, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.008064516129032258, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.008, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.008, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.016, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.023809523809523808, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.125, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.16666666666666666, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.16666666666666666, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0022123893805309734, 'lust': 0.0022123893805309734, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.00663716814159292, 'irritability': 0.0, 'breaking': 0.0022123893805309734, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.004424778761061947, 'friends': 0.0022123893805309734, 'celebration': 0.0, 'negative_emotion': 0.008849557522123894, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0022123893805309734, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.006369426751592357, 'anonymity': 0.0, 'fear': 0.006369426751592357, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.006369426751592357, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.006369426751592357, 'ugliness': 0.0, 'nervousness': 0.006369426751592357, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.006369426751592357, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0056179775280898875, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.011235955056179775, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017543859649122806, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.01, 'celebration': 0.0, 'negative_emotion': 0.01, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.024390243902439025, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.024390243902439025, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.014285714285714285, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.125, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.02127659574468085, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.014705882352941176, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.014705882352941176, 'positive_emotion': 0.014705882352941176, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.02, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.011363636363636364, 'lust': 0.0, 'shame': 0.011363636363636364, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.011363636363636364, 'pain': 0.011363636363636364, 'joy': 0.0, 'healing': 0.0, 'friends': 0.022727272727272728, 'celebration': 0.0, 'negative_emotion': 0.011363636363636364, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.011363636363636364, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.09090909090909091, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.05063291139240506, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012658227848101266, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0125, 'lust': 0.0125, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.025, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0125, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0125}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.04, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.006666666666666667, 'friends': 0.0, 'celebration': 0.006666666666666667, 'negative_emotion': 0.02, 'sadness': 0.006666666666666667, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.013333333333333334, 'emotional': 0.0, 'positive_emotion': 0.006666666666666667, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.017094017094017096, 'lust': 0.0, 'shame': 0.008547008547008548, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.008547008547008548, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.008547008547008548, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008547008547008548, 'pain': 0.008547008547008548, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.008547008547008548, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02564102564102564, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.012345679012345678, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.14285714285714285, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.038461538461538464, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.08571428571428572, 'negative_emotion': 0.02857142857142857, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.05714285714285714, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03125, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.03125, 'disgust': 0.0, 'ugliness': 0.03125, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03125, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.03125}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.07692307692307693, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.017467248908296942, 'lust': 0.0, 'shame': 0.004366812227074236, 'sleep': 0.004366812227074236, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.017467248908296942, 'disgust': 0.0, 'ugliness': 0.004366812227074236, 'nervousness': 0.004366812227074236, 'pain': 0.004366812227074236, 'joy': 0.0, 'healing': 0.0, 'friends': 0.008733624454148471, 'celebration': 0.013100436681222707, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013100436681222707, 'affection': 0.008733624454148471}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.03225806451612903, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.03225806451612903, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.03225806451612903, 'negative_emotion': 0.06451612903225806, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.03225806451612903, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.14285714285714285, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.013333333333333334, 'shame': 0.013333333333333334, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.013333333333333334, 'hate': 0.013333333333333334, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.013333333333333334, 'pain': 0.013333333333333334, 'joy': 0.013333333333333334, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.013333333333333334, 'negative_emotion': 0.0, 'sadness': 0.013333333333333334, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013333333333333334, 'affection': 0.013333333333333334}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.058823529411764705, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.015151515151515152, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03571428571428571, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.03571428571428571, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.03571428571428571}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.021739130434782608, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.043478260869565216, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0625, 'lust': 0.0, 'shame': 0.0625, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0625, 'pain': 0.0625, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.007518796992481203, 'lust': 0.0, 'shame': 0.007518796992481203, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.022556390977443608, 'nervousness': 0.007518796992481203, 'pain': 0.007518796992481203, 'joy': 0.0, 'healing': 0.007518796992481203, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.007518796992481203, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.021739130434782608, 'lust': 0.0, 'shame': 0.043478260869565216, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.043478260869565216, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.021739130434782608, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.021739130434782608, 'nervousness': 0.021739130434782608, 'pain': 0.06521739130434782, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.021739130434782608, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.021739130434782608, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.04, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0064516129032258064, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.008547008547008548, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.008547008547008548, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.02564102564102564, 'friends': 0.008547008547008548, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.008547008547008548, 'affection': 0.0}



{'love': 0.041666666666666664, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0196078431372549, 'lust': 0.0, 'shame': 0.0196078431372549, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0196078431372549, 'pain': 0.0196078431372549, 'joy': 0.0, 'healing': 0.0, 'friends': 0.058823529411764705, 'celebration': 0.0196078431372549, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0196078431372549, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.14285714285714285, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.14285714285714285, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.04, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.04, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.047619047619047616, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.047619047619047616, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.047619047619047616, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.047619047619047616, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.047619047619047616, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.045454545454545456, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.029411764705882353, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.029411764705882353, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.038461538461538464, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.07142857142857142, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.07142857142857142, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.047619047619047616, 'lust': 0.0, 'shame': 0.023809523809523808, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.023809523809523808, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.023809523809523808, 'affection': 0.023809523809523808}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.038461538461538464, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.038461538461538464, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.038461538461538464, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.010526315789473684, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.021052631578947368, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.010526315789473684, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.010526315789473684, 'joy': 0.0, 'healing': 0.0, 'friends': 0.010526315789473684, 'celebration': 0.0, 'negative_emotion': 0.031578947368421054, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.010526315789473684, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.029850746268656716, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.07142857142857142, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.07142857142857142, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.08108108108108109, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02702702702702703, 'affection': 0.0}



{'love': 0.014388489208633094, 'lust': 0.0, 'shame': 0.007194244604316547, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.014388489208633094, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.007194244604316547, 'attractive': 0.007194244604316547, 'disgust': 0.0, 'ugliness': 0.007194244604316547, 'nervousness': 0.0, 'pain': 0.014388489208633094, 'joy': 0.0, 'healing': 0.0, 'friends': 0.007194244604316547, 'celebration': 0.0, 'negative_emotion': 0.02158273381294964, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.007194244604316547, 'emotional': 0.007194244604316547, 'positive_emotion': 0.007194244604316547, 'affection': 0.014388489208633094}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.024390243902439025, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.024390243902439025, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.024390243902439025, 'negative_emotion': 0.024390243902439025, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.019230769230769232, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.019230769230769232, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.023809523809523808, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.023809523809523808, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.023809523809523808, 'affection': 0.0}



{'love': 0.015151515151515152, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.015151515151515152, 'celebration': 0.0, 'negative_emotion': 0.06060606060606061, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.015151515151515152, 'affection': 0.015151515151515152}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.03333333333333333, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.037037037037037035, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.06666666666666667, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.13333333333333333, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.05263157894736842, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.125, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.14285714285714285, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.020134228187919462, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.006711409395973154, 'health': 0.0, 'attractive': 0.020134228187919462, 'disgust': 0.0, 'ugliness': 0.006711409395973154, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.006711409395973154, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.006711409395973154, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.006711409395973154, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.09090909090909091, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.09090909090909091, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.08333333333333333, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.08333333333333333, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.08333333333333333, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.08333333333333333, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.08333333333333333, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.10526315789473684, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.05263157894736842, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.05263157894736842, 'negative_emotion': 0.05263157894736842, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.018518518518518517, 'pain': 0.0, 'joy': 0.0, 'healing': 0.018518518518518517, 'friends': 0.0, 'celebration': 0.018518518518518517, 'negative_emotion': 0.037037037037037035, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.018518518518518517, 'emotional': 0.037037037037037035, 'positive_emotion': 0.018518518518518517, 'affection': 0.0}



{'love': 0.023076923076923078, 'lust': 0.0, 'shame': 0.046153846153846156, 'sleep': 0.007692307692307693, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.007692307692307693, 'hate': 0.007692307692307693, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.03076923076923077, 'pain': 0.023076923076923078, 'joy': 0.0, 'healing': 0.007692307692307693, 'friends': 0.0, 'celebration': 0.007692307692307693, 'negative_emotion': 0.015384615384615385, 'sadness': 0.007692307692307693, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.007692307692307693, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.005813953488372093, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.005813953488372093, 'celebration': 0.0, 'negative_emotion': 0.005813953488372093, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.005813953488372093, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.047619047619047616, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03333333333333333, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.03333333333333333, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.012345679012345678, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.012345679012345678, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012345679012345678, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012345679012345678, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.010362694300518135, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0051813471502590676, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.031088082901554404, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.020833333333333332, 'anonymity': 0.0, 'fear': 0.020833333333333332, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.020833333333333332, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.020833333333333332, 'ugliness': 0.0, 'nervousness': 0.020833333333333332, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.020833333333333332, 'negative_emotion': 0.041666666666666664, 'sadness': 0.020833333333333332, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.020833333333333332, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.07142857142857142, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.07142857142857142, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.006666666666666667, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.013333333333333334, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.006666666666666667, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.006666666666666667, 'joy': 0.0, 'healing': 0.0, 'friends': 0.04, 'celebration': 0.0, 'negative_emotion': 0.006666666666666667, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.013333333333333334, 'positive_emotion': 0.006666666666666667, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.023809523809523808, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.023809523809523808, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.023809523809523808, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.02631578947368421, 'lust': 0.0, 'shame': 0.02631578947368421, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.02631578947368421, 'pain': 0.02631578947368421, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.030303030303030304, 'emotional': 0.0, 'positive_emotion': 0.030303030303030304, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.09090909090909091, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.18181818181818182, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.09090909090909091, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.18181818181818182, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.09090909090909091, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.06666666666666667, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.030303030303030304, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.030303030303030304, 'celebration': 0.0, 'negative_emotion': 0.030303030303030304, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.015151515151515152, 'positive_emotion': 0.030303030303030304, 'affection': 0.030303030303030304}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.034482758620689655, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.06896551724137931, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.034482758620689655, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.011627906976744186, 'breaking': 0.0, 'health': 0.023255813953488372, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.011627906976744186, 'pain': 0.011627906976744186, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.023255813953488372, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.125, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.125, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.03125, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.029411764705882353, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.029411764705882353, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.029411764705882353, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.015625, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.015625, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.015625, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.05, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03773584905660377, 'celebration': 0.0, 'negative_emotion': 0.018867924528301886, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03125, 'affection': 0.0}



{'love': 0.004901960784313725, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00980392156862745, 'cheerfulness': 0.0, 'aggression': 0.004901960784313725, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.004901960784313725, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00980392156862745, 'celebration': 0.0, 'negative_emotion': 0.014705882352941176, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.004901960784313725, 'affection': 0.004901960784313725}



{'love': 0.0044444444444444444, 'lust': 0.0, 'shame': 0.008888888888888889, 'sleep': 0.0, 'anger': 0.0044444444444444444, 'anonymity': 0.0, 'fear': 0.0044444444444444444, 'hate': 0.0044444444444444444, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0044444444444444444, 'attractive': 0.0, 'disgust': 0.0044444444444444444, 'ugliness': 0.0, 'nervousness': 0.0044444444444444444, 'pain': 0.0044444444444444444, 'joy': 0.0, 'healing': 0.0, 'friends': 0.008888888888888889, 'celebration': 0.0044444444444444444, 'negative_emotion': 0.0, 'sadness': 0.0044444444444444444, 'social_media': 0.0, 'disappointment': 0.0044444444444444444, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0392156862745098, 'lust': 0.0, 'shame': 0.058823529411764705, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0392156862745098, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0196078431372549, 'nervousness': 0.0392156862745098, 'pain': 0.058823529411764705, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.058823529411764705, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0392156862745098, 'positive_emotion': 0.0196078431372549, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.011764705882352941, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.011764705882352941, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.011764705882352941, 'breaking': 0.011764705882352941, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.023529411764705882, 'nervousness': 0.0, 'pain': 0.011764705882352941, 'joy': 0.0, 'healing': 0.0, 'friends': 0.011764705882352941, 'celebration': 0.0, 'negative_emotion': 0.023529411764705882, 'sadness': 0.011764705882352941, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011764705882352941, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.058823529411764705, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.029411764705882353, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.029411764705882353, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.016666666666666666, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.016666666666666666, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.016666666666666666, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.08695652173913043, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.029411764705882353, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.029411764705882353, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.029411764705882353, 'nervousness': 0.058823529411764705, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.029411764705882353, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.00980392156862745, 'health': 0.0, 'attractive': 0.00980392156862745, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00980392156862745, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.02, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.04, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.01282051282051282, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.01282051282051282, 'friends': 0.01282051282051282, 'celebration': 0.0, 'negative_emotion': 0.01282051282051282, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.041666666666666664, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.041666666666666664, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.041666666666666664, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.05263157894736842, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05263157894736842, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.018518518518518517, 'lust': 0.0, 'shame': 0.018518518518518517, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.018518518518518517, 'nervousness': 0.018518518518518517, 'pain': 0.018518518518518517, 'joy': 0.0, 'healing': 0.0, 'friends': 0.037037037037037035, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.023255813953488372, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.023255813953488372, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.023255813953488372, 'friends': 0.023255813953488372, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.06976744186046512, 'affection': 0.023255813953488372}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.058823529411764705, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.058823529411764705, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.058823529411764705, 'positive_emotion': 0.058823529411764705, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.06666666666666667, 'cheerfulness': 0.0, 'aggression': 0.06666666666666667, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.06666666666666667, 'celebration': 0.0, 'negative_emotion': 0.06666666666666667, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.06666666666666667, 'positive_emotion': 0.06666666666666667, 'affection': 0.0}



{'love': 0.03125, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0625, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.05, 'cheerfulness': 0.0, 'aggression': 0.05, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.05, 'nervousness': 0.0, 'pain': 0.05, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.05, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.058823529411764705, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01098901098901099, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.011111111111111112, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.012658227848101266, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.012658227848101266, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02531645569620253, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.012658227848101266, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.018867924528301886, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.018867924528301886, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.018867924528301886, 'pain': 0.03773584905660377, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05660377358490566, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.25, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.045454545454545456, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.022727272727272728, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.047619047619047616, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03125, 'lust': 0.0, 'shame': 0.0625, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.03125, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.03125, 'nervousness': 0.03125, 'pain': 0.0625, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03125, 'celebration': 0.0, 'negative_emotion': 0.03125, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.03125, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.013888888888888888, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.027777777777777776, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.027777777777777776, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.013888888888888888, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.037037037037037035, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.018518518518518517, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.030303030303030304, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02857142857142857, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.024390243902439025, 'disgust': 0.0, 'ugliness': 0.012195121951219513, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012195121951219513, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.01098901098901099, 'cheerfulness': 0.0, 'aggression': 0.01098901098901099, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.02197802197802198, 'disgust': 0.0, 'ugliness': 0.02197802197802198, 'nervousness': 0.0, 'pain': 0.01098901098901099, 'joy': 0.0, 'healing': 0.0, 'friends': 0.01098901098901099, 'celebration': 0.0, 'negative_emotion': 0.01098901098901099, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.045454545454545456, 'lust': 0.0, 'shame': 0.09090909090909091, 'sleep': 0.0, 'anger': 0.045454545454545456, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.045454545454545456, 'cheerfulness': 0.0, 'aggression': 0.045454545454545456, 'irritability': 0.045454545454545456, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.045454545454545456, 'pain': 0.09090909090909091, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.045454545454545456, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.045454545454545456, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.1111111111111111, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.16666666666666666, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.1111111111111111, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.06666666666666667, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.13333333333333333, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.06666666666666667, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0625, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0625, 'celebration': 0.0, 'negative_emotion': 0.0625, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.041666666666666664, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.022222222222222223, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.044444444444444446, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.022222222222222223, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.022222222222222223, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.009259259259259259, 'health': 0.0, 'attractive': 0.027777777777777776, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.05555555555555555, 'celebration': 0.0, 'negative_emotion': 0.009259259259259259, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.015625, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.015625, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.010309278350515464, 'lust': 0.010309278350515464, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.010309278350515464, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.010309278350515464, 'celebration': 0.0, 'negative_emotion': 0.030927835051546393, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.022727272727272728, 'lust': 0.0, 'shame': 0.045454545454545456, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.045454545454545456, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.022727272727272728, 'ugliness': 0.0, 'nervousness': 0.022727272727272728, 'pain': 0.045454545454545456, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.022727272727272728, 'sadness': 0.022727272727272728, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.06818181818181818, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.02127659574468085, 'lust': 0.010638297872340425, 'shame': 0.02127659574468085, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.010638297872340425, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.010638297872340425, 'pain': 0.02127659574468085, 'joy': 0.0, 'healing': 0.0, 'friends': 0.010638297872340425, 'celebration': 0.0, 'negative_emotion': 0.031914893617021274, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.010638297872340425, 'positive_emotion': 0.010638297872340425, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.02040816326530612, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.01020408163265306, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01020408163265306, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.01020408163265306, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.02040816326530612}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.14285714285714285, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.14285714285714285, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.05555555555555555, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.027777777777777776, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.03571428571428571, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.07142857142857142, 'affection': 0.0}



{'love': 0.0, 'lust': 0.058823529411764705, 'shame': 0.058823529411764705, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.058823529411764705, 'hate': 0.058823529411764705, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.058823529411764705, 'pain': 0.058823529411764705, 'joy': 0.058823529411764705, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.058823529411764705, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.058823529411764705, 'emotional': 0.0, 'positive_emotion': 0.058823529411764705, 'affection': 0.058823529411764705}



{'love': 0.0, 'lust': 0.0, 'shame': 0.037037037037037035, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.037037037037037035, 'ugliness': 0.07407407407407407, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.037037037037037035, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.012195121951219513, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.012195121951219513, 'disgust': 0.0, 'ugliness': 0.012195121951219513, 'nervousness': 0.024390243902439025, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04878048780487805, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.01694915254237288, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.01694915254237288, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.01694915254237288, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.05084745762711865, 'affection': 0.01694915254237288}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03333333333333333, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.06666666666666667, 'celebration': 0.0, 'negative_emotion': 0.016666666666666666, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03333333333333333, 'affection': 0.03333333333333333}



{'love': 0.0, 'lust': 0.0, 'shame': 0.005, 'sleep': 0.005, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.01, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.005, 'health': 0.0, 'attractive': 0.02, 'disgust': 0.0, 'ugliness': 0.005, 'nervousness': 0.0, 'pain': 0.005, 'joy': 0.0, 'healing': 0.0, 'friends': 0.01, 'celebration': 0.0, 'negative_emotion': 0.02, 'sadness': 0.005, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.01, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.012658227848101266, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012658227848101266, 'celebration': 0.012658227848101266, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.012658227848101266, 'affection': 0.0}



{'love': 0.002364066193853428, 'lust': 0.0, 'shame': 0.004728132387706856, 'sleep': 0.002364066193853428, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.004728132387706856, 'hate': 0.004728132387706856, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0070921985815602835, 'attractive': 0.002364066193853428, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0070921985815602835, 'pain': 0.004728132387706856, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.002364066193853428, 'negative_emotion': 0.004728132387706856, 'sadness': 0.009456264775413711, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.002364066193853428, 'positive_emotion': 0.004728132387706856, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.14285714285714285, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.01, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.04, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02, 'celebration': 0.0, 'negative_emotion': 0.01, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.018518518518518517, 'disgust': 0.0, 'ugliness': 0.018518518518518517, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.018518518518518517, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.018518518518518517, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.02040816326530612, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02040816326530612, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.02040816326530612, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.02040816326530612, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02040816326530612, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.02040816326530612, 'positive_emotion': 0.02040816326530612, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.02040816326530612, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02040816326530612, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.02040816326530612, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.02040816326530612, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02040816326530612, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.02040816326530612, 'positive_emotion': 0.02040816326530612, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.02040816326530612, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02040816326530612, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.02040816326530612, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.02040816326530612, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02040816326530612, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.02040816326530612, 'positive_emotion': 0.02040816326530612, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.05263157894736842, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02631578947368421, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.05128205128205128, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.018867924528301886, 'cheerfulness': 0.0, 'aggression': 0.018867924528301886, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.03773584905660377, 'nervousness': 0.0, 'pain': 0.018867924528301886, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03773584905660377, 'celebration': 0.0, 'negative_emotion': 0.018867924528301886, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.058823529411764705, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.058823529411764705, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.058823529411764705, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0625, 'anonymity': 0.0, 'fear': 0.0625, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0625, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0625, 'ugliness': 0.0625, 'nervousness': 0.0625, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0625, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.1, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.05, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.05, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.05, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.05, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.05, 'social_media': 0.0, 'disappointment': 0.05, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.05, 'affection': 0.1}



{'love': 0.012903225806451613, 'lust': 0.0, 'shame': 0.012903225806451613, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0064516129032258064, 'nervousness': 0.012903225806451613, 'pain': 0.012903225806451613, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012903225806451613, 'celebration': 0.012903225806451613, 'negative_emotion': 0.01935483870967742, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0064516129032258064, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.024390243902439025, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.024390243902439025, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.024390243902439025, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.07317073170731707, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.024390243902439025, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0625, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.1111111111111111, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.020833333333333332, 'lust': 0.0, 'shame': 0.020833333333333332, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.020833333333333332, 'pain': 0.020833333333333332, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.041666666666666664, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.041666666666666664, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.030303030303030304, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.06060606060606061, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.030303030303030304, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.030303030303030304, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02040816326530612, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.02040816326530612, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.05, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.05, 'disgust': 0.0, 'ugliness': 0.05, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.04, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.08, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.018518518518518517, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.03225806451612903, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.03225806451612903, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03225806451612903, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.003484320557491289, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.003484320557491289, 'hate': 0.003484320557491289, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.003484320557491289, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.006968641114982578, 'nervousness': 0.003484320557491289, 'pain': 0.003484320557491289, 'joy': 0.0, 'healing': 0.0, 'friends': 0.006968641114982578, 'celebration': 0.0, 'negative_emotion': 0.010452961672473868, 'sadness': 0.003484320557491289, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.003484320557491289, 'positive_emotion': 0.003484320557491289, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.09090909090909091, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.037037037037037035, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0055248618784530384, 'lust': 0.0055248618784530384, 'shame': 0.0, 'sleep': 0.0055248618784530384, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0055248618784530384, 'friends': 0.011049723756906077, 'celebration': 0.0, 'negative_emotion': 0.0055248618784530384, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.011049723756906077, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.014925373134328358, 'lust': 0.014925373134328358, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.014925373134328358, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.014925373134328358, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.014925373134328358, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03225806451612903, 'celebration': 0.03225806451612903, 'negative_emotion': 0.06451612903225806, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.03225806451612903, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.038461538461538464, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.038461538461538464, 'celebration': 0.038461538461538464, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.038461538461538464, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.018867924528301886, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.018867924528301886, 'friends': 0.07547169811320754, 'celebration': 0.0, 'negative_emotion': 0.018867924528301886, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.018867924528301886, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.016666666666666666, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.016666666666666666, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.016666666666666666, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.029411764705882353, 'lust': 0.014705882352941176, 'shame': 0.014705882352941176, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.007352941176470588, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.007352941176470588, 'disgust': 0.0, 'ugliness': 0.022058823529411766, 'nervousness': 0.014705882352941176, 'pain': 0.014705882352941176, 'joy': 0.0, 'healing': 0.007352941176470588, 'friends': 0.014705882352941176, 'celebration': 0.0, 'negative_emotion': 0.007352941176470588, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.04, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.029850746268656716, 'disgust': 0.0, 'ugliness': 0.014925373134328358, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.014925373134328358, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.1, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.038461538461538464, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.04, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.04, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.043478260869565216, 'celebration': 0.0, 'negative_emotion': 0.043478260869565216, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.1, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.14285714285714285, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.14285714285714285, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.14285714285714285, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.02127659574468085, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.06382978723404255, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.02127659574468085}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.01282051282051282, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.01282051282051282, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.05128205128205128, 'celebration': 0.01282051282051282, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.01282051282051282, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.05128205128205128, 'hate': 0.05128205128205128, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.07692307692307693, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.05128205128205128, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.10256410256410256, 'sadness': 0.07692307692307693, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.06060606060606061, 'lust': 0.0, 'shame': 0.06060606060606061, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.06060606060606061, 'pain': 0.06060606060606061, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.008547008547008548, 'anonymity': 0.0, 'fear': 0.02564102564102564, 'hate': 0.008547008547008548, 'cheerfulness': 0.0, 'aggression': 0.008547008547008548, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.017094017094017096, 'attractive': 0.0, 'disgust': 0.008547008547008548, 'ugliness': 0.0, 'nervousness': 0.02564102564102564, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.008547008547008548, 'sadness': 0.02564102564102564, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.015384615384615385, 'lust': 0.0, 'shame': 0.015384615384615385, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.015384615384615385, 'nervousness': 0.015384615384615385, 'pain': 0.015384615384615385, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.015384615384615385, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.045454545454545456, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.045454545454545456, 'celebration': 0.0, 'negative_emotion': 0.045454545454545456, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.05555555555555555, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.05555555555555555, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.006369426751592357, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.01910828025477707, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.006369426751592357, 'nervousness': 0.006369426751592357, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012738853503184714, 'celebration': 0.025477707006369428, 'negative_emotion': 0.01910828025477707, 'sadness': 0.006369426751592357, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012738853503184714, 'positive_emotion': 0.01910828025477707, 'affection': 0.0}



{'love': 0.04878048780487805, 'lust': 0.0, 'shame': 0.07317073170731707, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.024390243902439025, 'hate': 0.07317073170731707, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.04878048780487805, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.024390243902439025, 'nervousness': 0.04878048780487805, 'pain': 0.0975609756097561, 'joy': 0.0, 'healing': 0.0, 'friends': 0.024390243902439025, 'celebration': 0.0, 'negative_emotion': 0.12195121951219512, 'sadness': 0.04878048780487805, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.04878048780487805, 'positive_emotion': 0.04878048780487805, 'affection': 0.024390243902439025}



{'love': 0.013333333333333334, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.013333333333333334, 'disgust': 0.0, 'ugliness': 0.02666666666666667, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.013333333333333334, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.013333333333333334, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.06666666666666667, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0136986301369863, 'sleep': 0.0, 'anger': 0.0136986301369863, 'anonymity': 0.0, 'fear': 0.0136986301369863, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0136986301369863, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0136986301369863, 'ugliness': 0.0136986301369863, 'nervousness': 0.0136986301369863, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0136986301369863, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0273972602739726, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.00819672131147541, 'lust': 0.0, 'shame': 0.00819672131147541, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.00819672131147541, 'ugliness': 0.00819672131147541, 'nervousness': 0.00819672131147541, 'pain': 0.00819672131147541, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00819672131147541, 'celebration': 0.02459016393442623, 'negative_emotion': 0.0, 'sadness': 0.00819672131147541, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.00819672131147541, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.01639344262295082, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.01639344262295082, 'disgust': 0.0, 'ugliness': 0.01639344262295082, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03278688524590164, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.04918032786885246, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.021739130434782608, 'cheerfulness': 0.0, 'aggression': 0.010869565217391304, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.010869565217391304, 'disgust': 0.0, 'ugliness': 0.03260869565217391, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.010869565217391304, 'celebration': 0.010869565217391304, 'negative_emotion': 0.03260869565217391, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.010869565217391304, 'emotional': 0.0, 'positive_emotion': 0.010869565217391304, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.010101010101010102, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.020202020202020204, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.010101010101010102, 'friends': 0.020202020202020204, 'celebration': 0.0, 'negative_emotion': 0.010101010101010102, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.010101010101010102, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.022727272727272728, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.022727272727272728, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.022727272727272728, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.022727272727272728, 'positive_emotion': 0.022727272727272728, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.18181818181818182, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.004484304932735426, 'lust': 0.004484304932735426, 'shame': 0.004484304932735426, 'sleep': 0.0, 'anger': 0.004484304932735426, 'anonymity': 0.0, 'fear': 0.008968609865470852, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.004484304932735426, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008968609865470852, 'pain': 0.008968609865470852, 'joy': 0.0, 'healing': 0.004484304932735426, 'friends': 0.004484304932735426, 'celebration': 0.0, 'negative_emotion': 0.013452914798206279, 'sadness': 0.008968609865470852, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013452914798206279, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.012658227848101266, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02531645569620253, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.012658227848101266, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.012658227848101266, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02531645569620253, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012658227848101266, 'positive_emotion': 0.012658227848101266, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0196078431372549, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0196078431372549, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0196078431372549, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.00980392156862745, 'sadness': 0.0196078431372549, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.125, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.012048192771084338, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.012048192771084338, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.012048192771084338, 'ugliness': 0.012048192771084338, 'nervousness': 0.012048192771084338, 'pain': 0.012048192771084338, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012048192771084338, 'celebration': 0.0, 'negative_emotion': 0.012048192771084338, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.02040816326530612, 'lust': 0.0, 'shame': 0.02040816326530612, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.02040816326530612, 'pain': 0.02040816326530612, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.04081632653061224, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.04081632653061224, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.006711409395973154, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.020134228187919462, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.006711409395973154, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.020134228187919462, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.006944444444444444, 'lust': 0.0, 'shame': 0.006944444444444444, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.020833333333333332, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.013888888888888888, 'attractive': 0.013888888888888888, 'disgust': 0.0, 'ugliness': 0.013888888888888888, 'nervousness': 0.020833333333333332, 'pain': 0.006944444444444444, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.027777777777777776, 'sadness': 0.013888888888888888, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.020833333333333332, 'affection': 0.0}



{'love': 0.00819672131147541, 'lust': 0.0, 'shame': 0.00819672131147541, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.00819672131147541, 'pain': 0.00819672131147541, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.00819672131147541, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.00819672131147541, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.004081632653061225, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.012244897959183673, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.00816326530612245, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.004081632653061225, 'health': 0.00816326530612245, 'attractive': 0.004081632653061225, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.00816326530612245, 'pain': 0.004081632653061225, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00816326530612245, 'celebration': 0.0, 'negative_emotion': 0.00816326530612245, 'sadness': 0.00816326530612245, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02040816326530612, 'affection': 0.004081632653061225}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.009009009009009009, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.009009009009009009, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.009009009009009009, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02127659574468085, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.02127659574468085, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02127659574468085, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.025974025974025976, 'cheerfulness': 0.0, 'aggression': 0.012987012987012988, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.012987012987012988, 'nervousness': 0.0, 'pain': 0.012987012987012988, 'joy': 0.0, 'healing': 0.012987012987012988, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05194805194805195, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.06666666666666667, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.021739130434782608, 'lust': 0.0, 'shame': 0.021739130434782608, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.021739130434782608, 'pain': 0.021739130434782608, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.021739130434782608, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.021739130434782608, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.012345679012345678, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.012345679012345678, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.012987012987012988, 'shame': 0.012987012987012988, 'sleep': 0.012987012987012988, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.012987012987012988, 'hate': 0.012987012987012988, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.012987012987012988, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.012987012987012988, 'pain': 0.012987012987012988, 'joy': 0.012987012987012988, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03896103896103896, 'sadness': 0.012987012987012988, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.012987012987012988, 'affection': 0.012987012987012988}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.01, 'celebration': 0.0, 'negative_emotion': 0.01, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.006134969325153374, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.006134969325153374, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.006134969325153374, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.006134969325153374, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.006134969325153374, 'negative_emotion': 0.012269938650306749, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.006134969325153374, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.03125, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03125, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.012345679012345678, 'sleep': 0.0, 'anger': 0.012345679012345678, 'anonymity': 0.0, 'fear': 0.012345679012345678, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.024691358024691357, 'attractive': 0.0, 'disgust': 0.012345679012345678, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.012345679012345678, 'negative_emotion': 0.0, 'sadness': 0.012345679012345678, 'social_media': 0.0, 'disappointment': 0.012345679012345678, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.009771986970684038, 'sleep': 0.003257328990228013, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.009771986970684038, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.009771986970684038, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.003257328990228013, 'pain': 0.013029315960912053, 'joy': 0.0, 'healing': 0.0, 'friends': 0.003257328990228013, 'celebration': 0.003257328990228013, 'negative_emotion': 0.03908794788273615, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.009771986970684038, 'positive_emotion': 0.003257328990228013, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.012658227848101266, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.023622047244094488, 'lust': 0.007874015748031496, 'shame': 0.015748031496062992, 'sleep': 0.023622047244094488, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.007874015748031496, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.015748031496062992, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015748031496062992, 'pain': 0.015748031496062992, 'joy': 0.007874015748031496, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.007874015748031496, 'negative_emotion': 0.007874015748031496, 'sadness': 0.007874015748031496, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.015748031496062992, 'affection': 0.007874015748031496}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.015151515151515152, 'sleep': 0.015151515151515152, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015151515151515152, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.030303030303030304, 'negative_emotion': 0.030303030303030304, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.006666666666666667, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.006666666666666667, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.013333333333333334, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.02, 'negative_emotion': 0.006666666666666667, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.006666666666666667, 'emotional': 0.0, 'positive_emotion': 0.013333333333333334, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.00909090909090909, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00909090909090909, 'celebration': 0.0, 'negative_emotion': 0.00909090909090909, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01818181818181818, 'affection': 0.00909090909090909}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.05263157894736842, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.04, 'celebration': 0.04, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.03333333333333333, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03333333333333333, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.05263157894736842, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0035842293906810036, 'sleep': 0.007168458781362007, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0035842293906810036, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.007168458781362007, 'health': 0.010752688172043012, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0035842293906810036, 'friends': 0.0, 'celebration': 0.007168458781362007, 'negative_emotion': 0.010752688172043012, 'sadness': 0.007168458781362007, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0035842293906810036, 'positive_emotion': 0.0035842293906810036, 'affection': 0.0}



{'love': 0.005780346820809248, 'lust': 0.005780346820809248, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.005780346820809248, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.005780346820809248, 'healing': 0.0, 'friends': 0.011560693641618497, 'celebration': 0.005780346820809248, 'negative_emotion': 0.005780346820809248, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.011560693641618497, 'emotional': 0.0, 'positive_emotion': 0.005780346820809248, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.012345679012345678, 'lust': 0.00411522633744856, 'shame': 0.01646090534979424, 'sleep': 0.01646090534979424, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.00411522633744856, 'hate': 0.012345679012345678, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.01646090534979424, 'health': 0.00823045267489712, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01646090534979424, 'pain': 0.0205761316872428, 'joy': 0.00411522633744856, 'healing': 0.00411522633744856, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.00823045267489712, 'sadness': 0.00411522633744856, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.00823045267489712, 'affection': 0.00411522633744856}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.007352941176470588, 'lust': 0.007352941176470588, 'shame': 0.01838235294117647, 'sleep': 0.04779411764705882, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.007352941176470588, 'hate': 0.011029411764705883, 'cheerfulness': 0.0, 'aggression': 0.003676470588235294, 'irritability': 0.0, 'breaking': 0.003676470588235294, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.014705882352941176, 'pain': 0.01838235294117647, 'joy': 0.007352941176470588, 'healing': 0.003676470588235294, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.003676470588235294, 'sadness': 0.011029411764705883, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.003676470588235294, 'positive_emotion': 0.011029411764705883, 'affection': 0.007352941176470588}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0196078431372549, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0196078431372549, 'health': 0.0, 'attractive': 0.0196078431372549, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0196078431372549, 'pain': 0.0392156862745098, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0196078431372549, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.008928571428571428, 'lust': 0.002976190476190476, 'shame': 0.011904761904761904, 'sleep': 0.0, 'anger': 0.002976190476190476, 'anonymity': 0.0, 'fear': 0.020833333333333332, 'hate': 0.005952380952380952, 'cheerfulness': 0.0, 'aggression': 0.002976190476190476, 'irritability': 0.002976190476190476, 'breaking': 0.008928571428571428, 'health': 0.017857142857142856, 'attractive': 0.0, 'disgust': 0.005952380952380952, 'ugliness': 0.0, 'nervousness': 0.026785714285714284, 'pain': 0.01488095238095238, 'joy': 0.002976190476190476, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.002976190476190476, 'negative_emotion': 0.01488095238095238, 'sadness': 0.011904761904761904, 'social_media': 0.0, 'disappointment': 0.002976190476190476, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.002976190476190476, 'affection': 0.002976190476190476}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.07692307692307693, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.07692307692307693, 'affection': 0.0}



{'love': 0.009174311926605505, 'lust': 0.0, 'shame': 0.009174311926605505, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.01834862385321101, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009174311926605505, 'pain': 0.009174311926605505, 'joy': 0.0, 'healing': 0.027522935779816515, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.01834862385321101, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.009174311926605505, 'positive_emotion': 0.01834862385321101, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.013513513513513514, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.02702702702702703, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04054054054054054, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.005988023952095809, 'lust': 0.0, 'shame': 0.005988023952095809, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.011976047904191617, 'pain': 0.005988023952095809, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017964071856287425, 'celebration': 0.0, 'negative_emotion': 0.005988023952095809, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.017964071856287425, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.013333333333333334, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.013333333333333334, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.013333333333333334, 'pain': 0.013333333333333334, 'joy': 0.0, 'healing': 0.013333333333333334, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.013333333333333334, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.013333333333333334, 'positive_emotion': 0.013333333333333334, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.058823529411764705, 'celebration': 0.058823529411764705, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.058823529411764705, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.012658227848101266, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.012658227848101266, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02531645569620253, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012658227848101266, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.012121212121212121, 'lust': 0.0030303030303030303, 'shame': 0.00909090909090909, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.006060606060606061, 'hate': 0.0030303030303030303, 'cheerfulness': 0.012121212121212121, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.00909090909090909, 'attractive': 0.0030303030303030303, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015151515151515152, 'pain': 0.00909090909090909, 'joy': 0.0030303030303030303, 'healing': 0.0030303030303030303, 'friends': 0.006060606060606061, 'celebration': 0.00909090909090909, 'negative_emotion': 0.021212121212121213, 'sadness': 0.00909090909090909, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.015151515151515152, 'affection': 0.0030303030303030303}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.006211180124223602, 'lust': 0.006211180124223602, 'shame': 0.006211180124223602, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.018633540372670808, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.006211180124223602, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.012422360248447204, 'pain': 0.024844720496894408, 'joy': 0.006211180124223602, 'healing': 0.0, 'friends': 0.012422360248447204, 'celebration': 0.0, 'negative_emotion': 0.043478260869565216, 'sadness': 0.006211180124223602, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.006211180124223602, 'positive_emotion': 0.012422360248447204, 'affection': 0.006211180124223602}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03571428571428571, 'celebration': 0.0, 'negative_emotion': 0.03571428571428571, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03571428571428571, 'affection': 0.0}



{'love': 0.02564102564102564, 'lust': 0.0, 'shame': 0.02564102564102564, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.02564102564102564, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.02564102564102564, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.05128205128205128, 'pain': 0.02564102564102564, 'joy': 0.0, 'healing': 0.01282051282051282, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.02564102564102564, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.015384615384615385, 'lust': 0.0, 'shame': 0.046153846153846156, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015384615384615385, 'pain': 0.015384615384615385, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.046153846153846156, 'sadness': 0.038461538461538464, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.03076923076923077, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.020618556701030927, 'lust': 0.010309278350515464, 'shame': 0.030927835051546393, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.030927835051546393, 'hate': 0.010309278350515464, 'cheerfulness': 0.0, 'aggression': 0.010309278350515464, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.020618556701030927, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.08247422680412371, 'pain': 0.030927835051546393, 'joy': 0.010309278350515464, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.010309278350515464, 'sadness': 0.030927835051546393, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.020618556701030927, 'affection': 0.010309278350515464}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.021052631578947368, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.010526315789473684, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.021052631578947368, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.010526315789473684, 'sadness': 0.010526315789473684, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.005263157894736842, 'affection': 0.0}



{'love': 0.014492753623188406, 'lust': 0.0, 'shame': 0.014492753623188406, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.028985507246376812, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.014492753623188406, 'pain': 0.014492753623188406, 'joy': 0.0, 'healing': 0.0, 'friends': 0.014492753623188406, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.010309278350515464, 'lust': 0.0, 'shame': 0.010309278350515464, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.010309278350515464, 'health': 0.010309278350515464, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.010309278350515464, 'pain': 0.010309278350515464, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.010309278350515464, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.020618556701030927, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.03571428571428571, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.03571428571428571, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03571428571428571, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.015384615384615385, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.012345679012345678, 'anonymity': 0.0, 'fear': 0.024691358024691357, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.012345679012345678, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.012345679012345678, 'attractive': 0.0, 'disgust': 0.012345679012345678, 'ugliness': 0.0, 'nervousness': 0.024691358024691357, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.012345679012345678, 'sadness': 0.024691358024691357, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.012345679012345678, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.05172413793103448, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.004329004329004329, 'lust': 0.0, 'shame': 0.004329004329004329, 'sleep': 0.0, 'anger': 0.004329004329004329, 'anonymity': 0.0, 'fear': 0.008658008658008658, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.004329004329004329, 'irritability': 0.004329004329004329, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.008658008658008658, 'ugliness': 0.0, 'nervousness': 0.012987012987012988, 'pain': 0.004329004329004329, 'joy': 0.0, 'healing': 0.0, 'friends': 0.004329004329004329, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.008658008658008658, 'social_media': 0.0, 'disappointment': 0.004329004329004329, 'fun': 0.004329004329004329, 'emotional': 0.004329004329004329, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.03125, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.017937219730941704, 'lust': 0.004484304932735426, 'shame': 0.017937219730941704, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.013452914798206279, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.008968609865470852, 'attractive': 0.008968609865470852, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.017937219730941704, 'pain': 0.017937219730941704, 'joy': 0.004484304932735426, 'healing': 0.0, 'friends': 0.004484304932735426, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.013452914798206279, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.004484304932735426, 'affection': 0.0}



{'love': 0.004166666666666667, 'lust': 0.0, 'shame': 0.004166666666666667, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004166666666666667, 'pain': 0.004166666666666667, 'joy': 0.0, 'healing': 0.004166666666666667, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.008333333333333333, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004166666666666667, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.016129032258064516, 'lust': 0.008064516129032258, 'shame': 0.024193548387096774, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.008064516129032258, 'hate': 0.008064516129032258, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.008064516129032258, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.024193548387096774, 'pain': 0.03225806451612903, 'joy': 0.008064516129032258, 'healing': 0.008064516129032258, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.024193548387096774, 'sadness': 0.008064516129032258, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.016129032258064516, 'affection': 0.008064516129032258}



{'love': 0.009259259259259259, 'lust': 0.0030864197530864196, 'shame': 0.009259259259259259, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.009259259259259259, 'hate': 0.006172839506172839, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0030864197530864196, 'health': 0.009259259259259259, 'attractive': 0.0030864197530864196, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015432098765432098, 'pain': 0.012345679012345678, 'joy': 0.0030864197530864196, 'healing': 0.009259259259259259, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.012345679012345678, 'sadness': 0.006172839506172839, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.012345679012345678, 'affection': 0.0030864197530864196}



{'love': 0.045871559633027525, 'lust': 0.0, 'shame': 0.027522935779816515, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.009174311926605505, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.027522935779816515, 'pain': 0.027522935779816515, 'joy': 0.0, 'healing': 0.009174311926605505, 'friends': 0.009174311926605505, 'celebration': 0.0, 'negative_emotion': 0.009174311926605505, 'sadness': 0.03669724770642202, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.05504587155963303, 'affection': 0.05504587155963303}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.008695652173913044, 'hate': 0.008695652173913044, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.008695652173913044, 'health': 0.017391304347826087, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008695652173913044, 'pain': 0.008695652173913044, 'joy': 0.0, 'healing': 0.008695652173913044, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.017391304347826087, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.012987012987012988, 'shame': 0.012987012987012988, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.012987012987012988, 'hate': 0.012987012987012988, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.012987012987012988, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.012987012987012988, 'pain': 0.012987012987012988, 'joy': 0.012987012987012988, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.012987012987012988, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.012987012987012988, 'affection': 0.012987012987012988}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.02, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.02, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.02, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02, 'celebration': 0.0, 'negative_emotion': 0.02, 'sadness': 0.02, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.013157894736842105, 'hate': 0.013157894736842105, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.013157894736842105, 'health': 0.0, 'attractive': 0.013157894736842105, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.013157894736842105, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.013157894736842105, 'celebration': 0.0, 'negative_emotion': 0.02631578947368421, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03333333333333333, 'lust': 0.03333333333333333, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.03333333333333333}



{'love': 0.0, 'lust': 0.005571030640668524, 'shame': 0.011142061281337047, 'sleep': 0.0, 'anger': 0.002785515320334262, 'anonymity': 0.0, 'fear': 0.011142061281337047, 'hate': 0.011142061281337047, 'cheerfulness': 0.0, 'aggression': 0.002785515320334262, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.002785515320334262, 'disgust': 0.002785515320334262, 'ugliness': 0.0, 'nervousness': 0.013927576601671309, 'pain': 0.008356545961002786, 'joy': 0.005571030640668524, 'healing': 0.002785515320334262, 'friends': 0.008356545961002786, 'celebration': 0.016713091922005572, 'negative_emotion': 0.013927576601671309, 'sadness': 0.008356545961002786, 'social_media': 0.0, 'disappointment': 0.002785515320334262, 'fun': 0.011142061281337047, 'emotional': 0.002785515320334262, 'positive_emotion': 0.008356545961002786, 'affection': 0.005571030640668524}



{'love': 0.007936507936507936, 'lust': 0.003968253968253968, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.003968253968253968, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.003968253968253968, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.003968253968253968, 'pain': 0.003968253968253968, 'joy': 0.0, 'healing': 0.0, 'friends': 0.011904761904761904, 'celebration': 0.0, 'negative_emotion': 0.01984126984126984, 'sadness': 0.003968253968253968, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.003968253968253968, 'positive_emotion': 0.003968253968253968, 'affection': 0.003968253968253968}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.03225806451612903, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.007462686567164179, 'lust': 0.0, 'shame': 0.014925373134328358, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.007462686567164179, 'hate': 0.007462686567164179, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.022388059701492536, 'pain': 0.014925373134328358, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.022388059701492536, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.014925373134328358, 'affection': 0.0}



{'love': 0.013333333333333334, 'lust': 0.0, 'shame': 0.017777777777777778, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0044444444444444444, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.008888888888888889, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.013333333333333334, 'pain': 0.017777777777777778, 'joy': 0.0, 'healing': 0.0, 'friends': 0.008888888888888889, 'celebration': 0.0044444444444444444, 'negative_emotion': 0.035555555555555556, 'sadness': 0.0044444444444444444, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.017777777777777778, 'positive_emotion': 0.013333333333333334, 'affection': 0.0}



{'love': 0.003937007874015748, 'lust': 0.003937007874015748, 'shame': 0.007874015748031496, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.003937007874015748, 'hate': 0.011811023622047244, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.003937007874015748, 'attractive': 0.011811023622047244, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.007874015748031496, 'pain': 0.007874015748031496, 'joy': 0.003937007874015748, 'healing': 0.0, 'friends': 0.007874015748031496, 'celebration': 0.0, 'negative_emotion': 0.011811023622047244, 'sadness': 0.007874015748031496, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.007874015748031496, 'affection': 0.003937007874015748}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.023255813953488372, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.023255813953488372, 'celebration': 0.0, 'negative_emotion': 0.023255813953488372, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.046511627906976744, 'affection': 0.0}



{'love': 0.010362694300518135, 'lust': 0.0, 'shame': 0.015544041450777202, 'sleep': 0.010362694300518135, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0051813471502590676, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0051813471502590676, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.010362694300518135, 'pain': 0.015544041450777202, 'joy': 0.0, 'healing': 0.010362694300518135, 'friends': 0.010362694300518135, 'celebration': 0.010362694300518135, 'negative_emotion': 0.010362694300518135, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0051813471502590676, 'emotional': 0.0051813471502590676, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00847457627118644, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.00847457627118644, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00847457627118644, 'celebration': 0.00847457627118644, 'negative_emotion': 0.00847457627118644, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.00847457627118644, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.010752688172043012, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.010752688172043012, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.021505376344086023, 'sadness': 0.010752688172043012, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03278688524590164, 'lust': 0.0, 'shame': 0.03278688524590164, 'sleep': 0.0, 'anger': 0.01639344262295082, 'anonymity': 0.0, 'fear': 0.01639344262295082, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.01639344262295082, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.03278688524590164, 'ugliness': 0.0, 'nervousness': 0.04918032786885246, 'pain': 0.03278688524590164, 'joy': 0.0, 'healing': 0.01639344262295082, 'friends': 0.01639344262295082, 'celebration': 0.0, 'negative_emotion': 0.01639344262295082, 'sadness': 0.03278688524590164, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.01639344262295082, 'positive_emotion': 0.01639344262295082, 'affection': 0.0}



{'love': 0.0, 'lust': 0.005988023952095809, 'shame': 0.011976047904191617, 'sleep': 0.005988023952095809, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.005988023952095809, 'hate': 0.005988023952095809, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.005988023952095809, 'breaking': 0.005988023952095809, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.005988023952095809, 'pain': 0.011976047904191617, 'joy': 0.005988023952095809, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.023952095808383235, 'sadness': 0.005988023952095809, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011976047904191617, 'positive_emotion': 0.005988023952095809, 'affection': 0.005988023952095809}



{'love': 0.022727272727272728, 'lust': 0.003787878787878788, 'shame': 0.01893939393939394, 'sleep': 0.003787878787878788, 'anger': 0.003787878787878788, 'anonymity': 0.0, 'fear': 0.01893939393939394, 'hate': 0.022727272727272728, 'cheerfulness': 0.003787878787878788, 'aggression': 0.007575757575757576, 'irritability': 0.003787878787878788, 'breaking': 0.003787878787878788, 'health': 0.011363636363636364, 'attractive': 0.003787878787878788, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.041666666666666664, 'pain': 0.022727272727272728, 'joy': 0.003787878787878788, 'healing': 0.003787878787878788, 'friends': 0.003787878787878788, 'celebration': 0.003787878787878788, 'negative_emotion': 0.015151515151515152, 'sadness': 0.015151515151515152, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011363636363636364, 'positive_emotion': 0.026515151515151516, 'affection': 0.003787878787878788}



{'love': 0.031007751937984496, 'lust': 0.0, 'shame': 0.015503875968992248, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.007751937984496124, 'hate': 0.015503875968992248, 'cheerfulness': 0.0, 'aggression': 0.023255813953488372, 'irritability': 0.0, 'breaking': 0.007751937984496124, 'health': 0.0, 'attractive': 0.015503875968992248, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.007751937984496124, 'pain': 0.023255813953488372, 'joy': 0.0, 'healing': 0.0, 'friends': 0.031007751937984496, 'celebration': 0.0, 'negative_emotion': 0.03875968992248062, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.015503875968992248, 'positive_emotion': 0.015503875968992248, 'affection': 0.015503875968992248}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0091324200913242, 'anger': 0.0045662100456621, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0091324200913242, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0045662100456621, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0045662100456621, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0045662100456621, 'friends': 0.0136986301369863, 'celebration': 0.0, 'negative_emotion': 0.0091324200913242, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0136986301369863, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.07142857142857142, 'lust': 0.0, 'shame': 0.07142857142857142, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.03571428571428571, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.07142857142857142, 'pain': 0.07142857142857142, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0038314176245210726, 'lust': 0.0, 'shame': 0.007662835249042145, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0038314176245210726, 'hate': 0.007662835249042145, 'cheerfulness': 0.0, 'aggression': 0.007662835249042145, 'irritability': 0.0038314176245210726, 'breaking': 0.0, 'health': 0.0038314176245210726, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.007662835249042145, 'pain': 0.01532567049808429, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.022988505747126436, 'sadness': 0.0038314176245210726, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011494252873563218, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.01834862385321101, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.009174311926605505, 'hate': 0.009174311926605505, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.009174311926605505, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01834862385321101, 'pain': 0.009174311926605505, 'joy': 0.0, 'healing': 0.009174311926605505, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.009174311926605505, 'sadness': 0.009174311926605505, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.009174311926605505, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.005555555555555556, 'lust': 0.0, 'shame': 0.011111111111111112, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.016666666666666666, 'hate': 0.011111111111111112, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.005555555555555556, 'health': 0.005555555555555556, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.03333333333333333, 'pain': 0.027777777777777776, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.005555555555555556, 'negative_emotion': 0.03333333333333333, 'sadness': 0.005555555555555556, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.005555555555555556, 'positive_emotion': 0.005555555555555556, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.002702702702702703, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.002702702702702703, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.002702702702702703, 'irritability': 0.0, 'breaking': 0.005405405405405406, 'health': 0.0, 'attractive': 0.005405405405405406, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.013513513513513514, 'celebration': 0.002702702702702703, 'negative_emotion': 0.005405405405405406, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.002702702702702703, 'emotional': 0.0, 'positive_emotion': 0.005405405405405406, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.014705882352941176, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.007352941176470588, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.022058823529411766, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.014705882352941176, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.1111111111111111, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.017543859649122806, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.08333333333333333, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.01818181818181818, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.02857142857142857, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.02702702702702703, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02702702702702703, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.02702702702702703, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.058823529411764705, 'lust': 0.0, 'shame': 0.058823529411764705, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.058823529411764705, 'pain': 0.058823529411764705, 'joy': 0.0, 'healing': 0.058823529411764705, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.058823529411764705, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03225806451612903, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.1111111111111111, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02127659574468085, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03225806451612903, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.023255813953488372, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.011904761904761904, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.011904761904761904, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.011904761904761904, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011904761904761904, 'positive_emotion': 0.011904761904761904, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.014705882352941176, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02040816326530612, 'celebration': 0.0, 'negative_emotion': 0.02040816326530612, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.08333333333333333, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.08333333333333333, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.024390243902439025, 'celebration': 0.0, 'negative_emotion': 0.04878048780487805, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.024390243902439025}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.021739130434782608, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.027777777777777776, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.027777777777777776, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0196078431372549, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009615384615384616, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.00980392156862745, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009615384615384616, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009615384615384616, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009523809523809525, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.045454545454545456, 'lust': 0.09090909090909091, 'shame': 0.045454545454545456, 'sleep': 0.045454545454545456, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.045454545454545456, 'hate': 0.13636363636363635, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.045454545454545456, 'pain': 0.045454545454545456, 'joy': 0.045454545454545456, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.09090909090909091, 'sadness': 0.045454545454545456, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.045454545454545456, 'affection': 0.045454545454545456}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009523809523809525, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.014492753623188406, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.020833333333333332, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.00980392156862745, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009523809523809525, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009708737864077669, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.010101010101010102, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009523809523809525, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.00980392156862745, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009900990099009901, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009433962264150943, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009523809523809525, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009523809523809525, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.022727272727272728, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.022727272727272728, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.02702702702702703, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.038461538461538464, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.034482758620689655, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.03225806451612903, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.03125, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.027777777777777776, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.058823529411764705, 'celebration': 0.0, 'negative_emotion': 0.058823529411764705, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.058823529411764705, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.004878048780487805, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.01694915254237288, 'celebration': 0.01694915254237288, 'negative_emotion': 0.01694915254237288, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.05, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.030303030303030304, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.030303030303030304, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.022727272727272728, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.022727272727272728, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.045454545454545456, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.038461538461538464, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.038461538461538464}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}


'''
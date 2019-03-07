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

            if (title_score["social_media"] != 0.0):
                print ("\n\n*************************** \n\n")
                # print "\n\n Printing score!"
                # print title_score
                score_pickle.append(title_score)



    print ("printing final score pickle")
    print score_pickle
    print ("\n\nLength of score_pickle")
    print (len(score_pickle))


    with open("empath.pickle", "w") as f:
        pickle.dump(score_pickle, f)
    # lexicon = Empath()
    # title_score =lexicon.analyze(body, normalize = True)


####### for reading pickle values for each entry:
    with open("empath.pickle", "r") as f:
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




#####################

'''
result:


{'love': 0.006134969325153374, 'lust': 0.0, 'shame': 0.002044989775051125, 'sleep': 0.0, 'anger': 0.002044989775051125, 'anonymity': 0.002044989775051125, 'fear': 0.002044989775051125, 'hate': 0.0, 'cheerfulness': 0.002044989775051125, 'aggression': 0.002044989775051125, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.002044989775051125, 'attractive': 0.006134969325153374, 'disgust': 0.002044989775051125, 'ugliness': 0.0, 'nervousness': 0.002044989775051125, 'pain': 0.0, 'joy': 0.0, 'healing': 0.002044989775051125, 'friends': 0.010224948875255624, 'celebration': 0.00408997955010225, 'negative_emotion': 0.002044989775051125, 'sadness': 0.00408997955010225, 'social_media': 0.00408997955010225, 'disappointment': 0.002044989775051125, 'fun': 0.016359918200409, 'emotional': 0.0, 'positive_emotion': 0.010224948875255624, 'affection': 0.006134969325153374}



{'love': 0.0047169811320754715, 'lust': 0.0047169811320754715, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0047169811320754715, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009433962264150943, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.13636363636363635, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.003484320557491289, 'sleep': 0.0, 'anger': 0.003484320557491289, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.003484320557491289, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.006968641114982578, 'celebration': 0.010452961672473868, 'negative_emotion': 0.006968641114982578, 'sadness': 0.003484320557491289, 'social_media': 0.003484320557491289, 'disappointment': 0.003484320557491289, 'fun': 0.003484320557491289, 'emotional': 0.003484320557491289, 'positive_emotion': 0.010452961672473868, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.011627906976744186, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.011627906976744186, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.011627906976744186, 'affection': 0.0}



{'love': 0.008456659619450317, 'lust': 0.0, 'shame': 0.010570824524312896, 'sleep': 0.0021141649048625794, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0021141649048625794, 'cheerfulness': 0.0, 'aggression': 0.004228329809725159, 'irritability': 0.0, 'breaking': 0.004228329809725159, 'health': 0.008456659619450317, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008456659619450317, 'pain': 0.008456659619450317, 'joy': 0.0, 'healing': 0.0021141649048625794, 'friends': 0.006342494714587738, 'celebration': 0.0, 'negative_emotion': 0.010570824524312896, 'sadness': 0.004228329809725159, 'social_media': 0.0021141649048625794, 'disappointment': 0.0, 'fun': 0.0021141649048625794, 'emotional': 0.0021141649048625794, 'positive_emotion': 0.004228329809725159, 'affection': 0.0}



{'love': 0.002152852529601722, 'lust': 0.001076426264800861, 'shame': 0.010764262648008612, 'sleep': 0.0032292787944025836, 'anger': 0.0032292787944025836, 'anonymity': 0.0, 'fear': 0.005382131324004306, 'hate': 0.005382131324004306, 'cheerfulness': 0.0, 'aggression': 0.0032292787944025836, 'irritability': 0.0, 'breaking': 0.002152852529601722, 'health': 0.008611410118406888, 'attractive': 0.0032292787944025836, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004305705059203444, 'pain': 0.013993541442411194, 'joy': 0.001076426264800861, 'healing': 0.002152852529601722, 'friends': 0.005382131324004306, 'celebration': 0.0, 'negative_emotion': 0.015069967707212056, 'sadness': 0.005382131324004306, 'social_media': 0.002152852529601722, 'disappointment': 0.001076426264800861, 'fun': 0.0, 'emotional': 0.004305705059203444, 'positive_emotion': 0.0032292787944025836, 'affection': 0.001076426264800861}



{'love': 0.0125, 'lust': 0.0, 'shame': 0.0375, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0125, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0125, 'pain': 0.0125, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0125, 'celebration': 0.0, 'negative_emotion': 0.025, 'sadness': 0.025, 'social_media': 0.025, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.025, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.012658227848101266, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.008438818565400843, 'sadness': 0.0, 'social_media': 0.004219409282700422, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.005917159763313609, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.005917159763313609, 'celebration': 0.005917159763313609, 'negative_emotion': 0.011834319526627219, 'sadness': 0.0, 'social_media': 0.005917159763313609, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.011764705882352941, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.03529411764705882, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.011764705882352941, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.011764705882352941, 'celebration': 0.011764705882352941, 'negative_emotion': 0.047058823529411764, 'sadness': 0.0, 'social_media': 0.011764705882352941, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.010067114093959731, 'lust': 0.003355704697986577, 'shame': 0.013422818791946308, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.02348993288590604, 'hate': 0.010067114093959731, 'cheerfulness': 0.0, 'aggression': 0.003355704697986577, 'irritability': 0.003355704697986577, 'breaking': 0.003355704697986577, 'health': 0.026845637583892617, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.03355704697986577, 'pain': 0.02348993288590604, 'joy': 0.003355704697986577, 'healing': 0.003355704697986577, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.016778523489932886, 'sadness': 0.013422818791946308, 'social_media': 0.006711409395973154, 'disappointment': 0.0, 'fun': 0.003355704697986577, 'emotional': 0.0, 'positive_emotion': 0.006711409395973154, 'affection': 0.003355704697986577}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.011363636363636364, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.011363636363636364, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.011363636363636364, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.002398081534772182, 'fear': 0.0, 'hate': 0.002398081534772182, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.002398081534772182, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.002398081534772182, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.009592326139088728, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009592326139088728, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.012048192771084338, 'sadness': 0.0, 'social_media': 0.024096385542168676, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.01020408163265306, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.01020408163265306, 'celebration': 0.0, 'negative_emotion': 0.01020408163265306, 'sadness': 0.0, 'social_media': 0.01020408163265306, 'disappointment': 0.0, 'fun': 0.01020408163265306, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.038461538461538464, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0008257638315441783, 'lust': 0.0, 'shame': 0.0008257638315441783, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0008257638315441783, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0016515276630883566, 'pain': 0.0008257638315441783, 'joy': 0.0, 'healing': 0.002477291494632535, 'friends': 0.0008257638315441783, 'celebration': 0.0008257638315441783, 'negative_emotion': 0.00495458298926507, 'sadness': 0.0, 'social_media': 0.004128819157720892, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.010101010101010102, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.014705882352941176, 'sadness': 0.0, 'social_media': 0.014705882352941176, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.09090909090909091, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.09090909090909091, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.08333333333333333, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.012345679012345678, 'sleep': 0.0, 'anger': 0.012345679012345678, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.012345679012345678, 'cheerfulness': 0.0, 'aggression': 0.012345679012345678, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.012345679012345678, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.024691358024691357, 'sadness': 0.0, 'social_media': 0.012345679012345678, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.012345679012345678, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.08333333333333333, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0029154518950437317, 'lust': 0.0029154518950437317, 'shame': 0.0029154518950437317, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0029154518950437317, 'fear': 0.0029154518950437317, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0029154518950437317, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.014577259475218658, 'attractive': 0.0029154518950437317, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0029154518950437317, 'pain': 0.008746355685131196, 'joy': 0.0, 'healing': 0.0029154518950437317, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.01749271137026239, 'sadness': 0.0058309037900874635, 'social_media': 0.0029154518950437317, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0058309037900874635, 'positive_emotion': 0.008746355685131196, 'affection': 0.0}



{'love': 0.008086253369272238, 'lust': 0.01078167115902965, 'shame': 0.01078167115902965, 'sleep': 0.0, 'anger': 0.008086253369272238, 'anonymity': 0.0, 'fear': 0.008086253369272238, 'hate': 0.01078167115902965, 'cheerfulness': 0.0, 'aggression': 0.01078167115902965, 'irritability': 0.0026954177897574125, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.008086253369272238, 'ugliness': 0.0, 'nervousness': 0.016172506738544475, 'pain': 0.016172506738544475, 'joy': 0.0026954177897574125, 'healing': 0.0, 'friends': 0.005390835579514825, 'celebration': 0.0, 'negative_emotion': 0.013477088948787063, 'sadness': 0.01078167115902965, 'social_media': 0.01078167115902965, 'disappointment': 0.0026954177897574125, 'fun': 0.0, 'emotional': 0.0026954177897574125, 'positive_emotion': 0.0026954177897574125, 'affection': 0.005390835579514825}



{'love': 0.015337423312883436, 'lust': 0.009202453987730062, 'shame': 0.024539877300613498, 'sleep': 0.006134969325153374, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.012269938650306749, 'hate': 0.015337423312883436, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.003067484662576687, 'health': 0.02147239263803681, 'attractive': 0.003067484662576687, 'disgust': 0.0, 'ugliness': 0.003067484662576687, 'nervousness': 0.02147239263803681, 'pain': 0.027607361963190184, 'joy': 0.009202453987730062, 'healing': 0.018404907975460124, 'friends': 0.0, 'celebration': 0.003067484662576687, 'negative_emotion': 0.02147239263803681, 'sadness': 0.015337423312883436, 'social_media': 0.003067484662576687, 'disappointment': 0.003067484662576687, 'fun': 0.006134969325153374, 'emotional': 0.012269938650306749, 'positive_emotion': 0.027607361963190184, 'affection': 0.009202453987730062}



{'love': 0.0037593984962406013, 'lust': 0.0, 'shame': 0.007518796992481203, 'sleep': 0.0037593984962406013, 'anger': 0.0, 'anonymity': 0.0037593984962406013, 'fear': 0.0, 'hate': 0.007518796992481203, 'cheerfulness': 0.0, 'aggression': 0.0037593984962406013, 'irritability': 0.0, 'breaking': 0.0037593984962406013, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0037593984962406013, 'pain': 0.011278195488721804, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.007518796992481203, 'negative_emotion': 0.022556390977443608, 'sadness': 0.0, 'social_media': 0.007518796992481203, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.011278195488721804, 'positive_emotion': 0.0037593984962406013, 'affection': 0.0}



{'love': 0.0, 'lust': 0.00516795865633075, 'shame': 0.00516795865633075, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.00516795865633075, 'hate': 0.007751937984496124, 'cheerfulness': 0.002583979328165375, 'aggression': 0.002583979328165375, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.041343669250646, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.00516795865633075, 'pain': 0.0103359173126615, 'joy': 0.00516795865633075, 'healing': 0.00516795865633075, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.031007751937984496, 'sadness': 0.007751937984496124, 'social_media': 0.002583979328165375, 'disappointment': 0.002583979328165375, 'fun': 0.0, 'emotional': 0.002583979328165375, 'positive_emotion': 0.0103359173126615, 'affection': 0.00516795865633075}



{'love': 0.001834862385321101, 'lust': 0.0, 'shame': 0.007339449541284404, 'sleep': 0.003669724770642202, 'anger': 0.001834862385321101, 'anonymity': 0.0, 'fear': 0.009174311926605505, 'hate': 0.005504587155963303, 'cheerfulness': 0.001834862385321101, 'aggression': 0.003669724770642202, 'irritability': 0.0, 'breaking': 0.005504587155963303, 'health': 0.0, 'attractive': 0.001834862385321101, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.001834862385321101, 'pain': 0.009174311926605505, 'joy': 0.0, 'healing': 0.0, 'friends': 0.001834862385321101, 'celebration': 0.005504587155963303, 'negative_emotion': 0.02018348623853211, 'sadness': 0.003669724770642202, 'social_media': 0.001834862385321101, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.003669724770642202, 'positive_emotion': 0.003669724770642202, 'affection': 0.0}



{'love': 0.0, 'lust': 0.012048192771084338, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.012048192771084338, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.006024096385542169, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.006024096385542169, 'nervousness': 0.0, 'pain': 0.006024096385542169, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012048192771084338, 'celebration': 0.0, 'negative_emotion': 0.012048192771084338, 'sadness': 0.0, 'social_media': 0.012048192771084338, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.012539184952978056, 'lust': 0.0, 'shame': 0.012539184952978056, 'sleep': 0.0, 'anger': 0.003134796238244514, 'anonymity': 0.0, 'fear': 0.006269592476489028, 'hate': 0.003134796238244514, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.003134796238244514, 'breaking': 0.0, 'health': 0.003134796238244514, 'attractive': 0.0, 'disgust': 0.003134796238244514, 'ugliness': 0.0, 'nervousness': 0.009404388714733543, 'pain': 0.009404388714733543, 'joy': 0.0, 'healing': 0.003134796238244514, 'friends': 0.012539184952978056, 'celebration': 0.006269592476489028, 'negative_emotion': 0.018808777429467086, 'sadness': 0.0, 'social_media': 0.003134796238244514, 'disappointment': 0.003134796238244514, 'fun': 0.0, 'emotional': 0.003134796238244514, 'positive_emotion': 0.009404388714733543, 'affection': 0.003134796238244514}



{'love': 0.0034522439585730723, 'lust': 0.0011507479861910242, 'shame': 0.009205983889528193, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0011507479861910242, 'hate': 0.0034522439585730723, 'cheerfulness': 0.0, 'aggression': 0.0011507479861910242, 'irritability': 0.0, 'breaking': 0.0011507479861910242, 'health': 0.014959723820483314, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.006904487917146145, 'pain': 0.006904487917146145, 'joy': 0.0011507479861910242, 'healing': 0.004602991944764097, 'friends': 0.012658227848101266, 'celebration': 0.0034522439585730723, 'negative_emotion': 0.012658227848101266, 'sadness': 0.0023014959723820483, 'social_media': 0.0011507479861910242, 'disappointment': 0.0, 'fun': 0.0023014959723820483, 'emotional': 0.0011507479861910242, 'positive_emotion': 0.0023014959723820483, 'affection': 0.0011507479861910242}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.05263157894736842, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.05263157894736842, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0043859649122807015, 'shame': 0.0043859649122807015, 'sleep': 0.0043859649122807015, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.008771929824561403, 'hate': 0.0043859649122807015, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0043859649122807015, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008771929824561403, 'pain': 0.008771929824561403, 'joy': 0.0043859649122807015, 'healing': 0.0, 'friends': 0.0043859649122807015, 'celebration': 0.0, 'negative_emotion': 0.021929824561403508, 'sadness': 0.0043859649122807015, 'social_media': 0.013157894736842105, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0043859649122807015, 'affection': 0.0043859649122807015}



{'love': 0.0, 'lust': 0.004761904761904762, 'shame': 0.004761904761904762, 'sleep': 0.004761904761904762, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.009523809523809525, 'hate': 0.004761904761904762, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.004761904761904762, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009523809523809525, 'pain': 0.009523809523809525, 'joy': 0.004761904761904762, 'healing': 0.0, 'friends': 0.004761904761904762, 'celebration': 0.0, 'negative_emotion': 0.023809523809523808, 'sadness': 0.004761904761904762, 'social_media': 0.014285714285714285, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.004761904761904762, 'affection': 0.004761904761904762}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.023255813953488372, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.023255813953488372, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.023255813953488372, 'friends': 0.023255813953488372, 'celebration': 0.0, 'negative_emotion': 0.023255813953488372, 'sadness': 0.0, 'social_media': 0.023255813953488372, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.023255813953488372, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.012345679012345678, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.012345679012345678, 'sadness': 0.0, 'social_media': 0.012345679012345678, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.025, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.025, 'disappointment': 0.0, 'fun': 0.025, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.02127659574468085, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.015625, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.015625, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.015625, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.005319148936170213, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.010638297872340425, 'sadness': 0.0, 'social_media': 0.005319148936170213, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.005319148936170213, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.05, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.1, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.018867924528301886, 'sadness': 0.0, 'social_media': 0.05660377358490566, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.046511627906976744, 'lust': 0.046511627906976744, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.023255813953488372, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.1, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.024390243902439025, 'lust': 0.00975609756097561, 'shame': 0.004878048780487805, 'sleep': 0.004878048780487805, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.004878048780487805, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004878048780487805, 'pain': 0.004878048780487805, 'joy': 0.0, 'healing': 0.004878048780487805, 'friends': 0.004878048780487805, 'celebration': 0.004878048780487805, 'negative_emotion': 0.014634146341463415, 'sadness': 0.0, 'social_media': 0.00975609756097561, 'disappointment': 0.0, 'fun': 0.004878048780487805, 'emotional': 0.004878048780487805, 'positive_emotion': 0.024390243902439025, 'affection': 0.00975609756097561}



{'love': 0.026490066225165563, 'lust': 0.006622516556291391, 'shame': 0.019867549668874173, 'sleep': 0.0033112582781456954, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.013245033112582781, 'hate': 0.006622516556291391, 'cheerfulness': 0.006622516556291391, 'aggression': 0.0033112582781456954, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.019867549668874173, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.026490066225165563, 'pain': 0.026490066225165563, 'joy': 0.006622516556291391, 'healing': 0.0, 'friends': 0.016556291390728478, 'celebration': 0.0033112582781456954, 'negative_emotion': 0.023178807947019868, 'sadness': 0.026490066225165563, 'social_media': 0.009933774834437087, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0033112582781456954, 'positive_emotion': 0.019867549668874173, 'affection': 0.009933774834437087}



{'love': 0.012295081967213115, 'lust': 0.0, 'shame': 0.01092896174863388, 'sleep': 0.006830601092896175, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.001366120218579235, 'hate': 0.004098360655737705, 'cheerfulness': 0.001366120218579235, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.006830601092896175, 'attractive': 0.001366120218579235, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.00819672131147541, 'pain': 0.012295081967213115, 'joy': 0.001366120218579235, 'healing': 0.0, 'friends': 0.004098360655737705, 'celebration': 0.0, 'negative_emotion': 0.017759562841530054, 'sadness': 0.00273224043715847, 'social_media': 0.009562841530054645, 'disappointment': 0.0, 'fun': 0.001366120218579235, 'emotional': 0.01366120218579235, 'positive_emotion': 0.00546448087431694, 'affection': 0.001366120218579235}



{'love': 0.0, 'lust': 0.0, 'shame': 0.01834862385321101, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.009174311926605505, 'hate': 0.03669724770642202, 'cheerfulness': 0.0, 'aggression': 0.009174311926605505, 'irritability': 0.0, 'breaking': 0.009174311926605505, 'health': 0.009174311926605505, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.027522935779816515, 'pain': 0.01834862385321101, 'joy': 0.0, 'healing': 0.0, 'friends': 0.009174311926605505, 'celebration': 0.0, 'negative_emotion': 0.06422018348623854, 'sadness': 0.01834862385321101, 'social_media': 0.009174311926605505, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.01834862385321101, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.017857142857142856, 'cheerfulness': 0.0, 'aggression': 0.017857142857142856, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.017857142857142856, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05357142857142857, 'sadness': 0.017857142857142856, 'social_media': 0.03571428571428571, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.017857142857142856, 'positive_emotion': 0.017857142857142856, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.046153846153846156, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.015384615384615385, 'celebration': 0.0, 'negative_emotion': 0.06153846153846154, 'sadness': 0.0, 'social_media': 0.015384615384615385, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.010416666666666666, 'health': 0.010416666666666666, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.052083333333333336, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.010416666666666666, 'social_media': 0.020833333333333332, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.010416666666666666, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.007194244604316547, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.005128205128205128, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.005128205128205128, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.005128205128205128, 'celebration': 0.0, 'negative_emotion': 0.005128205128205128, 'sadness': 0.0, 'social_media': 0.005128205128205128, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.009852216748768473, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0049261083743842365, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0049261083743842365, 'celebration': 0.0, 'negative_emotion': 0.0049261083743842365, 'sadness': 0.0, 'social_media': 0.0049261083743842365, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00966183574879227, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.004830917874396135, 'disgust': 0.0, 'ugliness': 0.004830917874396135, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.004830917874396135, 'celebration': 0.0, 'negative_emotion': 0.004830917874396135, 'sadness': 0.0, 'social_media': 0.004830917874396135, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004830917874396135, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.010869565217391304, 'cheerfulness': 0.0, 'aggression': 0.0036231884057971015, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.014492753623188406, 'disgust': 0.0, 'ugliness': 0.0036231884057971015, 'nervousness': 0.0, 'pain': 0.007246376811594203, 'joy': 0.0, 'healing': 0.0036231884057971015, 'friends': 0.0036231884057971015, 'celebration': 0.0, 'negative_emotion': 0.025362318840579712, 'sadness': 0.007246376811594203, 'social_media': 0.0036231884057971015, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.014492753623188406, 'positive_emotion': 0.0036231884057971015, 'affection': 0.0}



{'love': 0.012711864406779662, 'lust': 0.00423728813559322, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00423728813559322, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.00423728813559322, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.00423728813559322, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012711864406779662, 'celebration': 0.012711864406779662, 'negative_emotion': 0.00423728813559322, 'sadness': 0.0, 'social_media': 0.00847457627118644, 'disappointment': 0.0, 'fun': 0.00423728813559322, 'emotional': 0.0, 'positive_emotion': 0.012711864406779662, 'affection': 0.012711864406779662}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.013157894736842105, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.01639344262295082, 'lust': 0.00819672131147541, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.00819672131147541, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.00819672131147541, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00819672131147541, 'celebration': 0.0, 'negative_emotion': 0.00819672131147541, 'sadness': 0.0, 'social_media': 0.00819672131147541, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01639344262295082, 'affection': 0.01639344262295082}



{'love': 0.0035587188612099642, 'lust': 0.0, 'shame': 0.0071174377224199285, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.010676156583629894, 'cheerfulness': 0.0, 'aggression': 0.0035587188612099642, 'irritability': 0.0, 'breaking': 0.0035587188612099642, 'health': 0.0035587188612099642, 'attractive': 0.0035587188612099642, 'disgust': 0.0, 'ugliness': 0.0035587188612099642, 'nervousness': 0.0035587188612099642, 'pain': 0.010676156583629894, 'joy': 0.0, 'healing': 0.0035587188612099642, 'friends': 0.010676156583629894, 'celebration': 0.0, 'negative_emotion': 0.017793594306049824, 'sadness': 0.0, 'social_media': 0.0035587188612099642, 'disappointment': 0.0, 'fun': 0.0035587188612099642, 'emotional': 0.0035587188612099642, 'positive_emotion': 0.017793594306049824, 'affection': 0.0}



{'love': 0.008695652173913044, 'lust': 0.008695652173913044, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.017391304347826087, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.008695652173913044}



{'love': 0.001639344262295082, 'lust': 0.0, 'shame': 0.001639344262295082, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.001639344262295082, 'hate': 0.004918032786885246, 'cheerfulness': 0.0, 'aggression': 0.003278688524590164, 'irritability': 0.001639344262295082, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.001639344262295082, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.001639344262295082, 'pain': 0.006557377049180328, 'joy': 0.0, 'healing': 0.0, 'friends': 0.004918032786885246, 'celebration': 0.0, 'negative_emotion': 0.006557377049180328, 'sadness': 0.0, 'social_media': 0.004918032786885246, 'disappointment': 0.0, 'fun': 0.004918032786885246, 'emotional': 0.004918032786885246, 'positive_emotion': 0.001639344262295082, 'affection': 0.001639344262295082}



{'love': 0.008344923504867872, 'lust': 0.0013908205841446453, 'shame': 0.004172461752433936, 'sleep': 0.0013908205841446453, 'anger': 0.0013908205841446453, 'anonymity': 0.0, 'fear': 0.0013908205841446453, 'hate': 0.005563282336578581, 'cheerfulness': 0.0027816411682892906, 'aggression': 0.0013908205841446453, 'irritability': 0.0013908205841446453, 'breaking': 0.0013908205841446453, 'health': 0.005563282336578581, 'attractive': 0.0027816411682892906, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0013908205841446453, 'pain': 0.0027816411682892906, 'joy': 0.0013908205841446453, 'healing': 0.0013908205841446453, 'friends': 0.009735744089012517, 'celebration': 0.0013908205841446453, 'negative_emotion': 0.011126564673157162, 'sadness': 0.004172461752433936, 'social_media': 0.005563282336578581, 'disappointment': 0.0, 'fun': 0.0027816411682892906, 'emotional': 0.005563282336578581, 'positive_emotion': 0.009735744089012517, 'affection': 0.004172461752433936}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.07692307692307693, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.07692307692307693, 'affection': 0.0}



{'love': 0.014598540145985401, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.014598540145985401, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0072992700729927005, 'healing': 0.0, 'friends': 0.0072992700729927005, 'celebration': 0.0072992700729927005, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0072992700729927005, 'disappointment': 0.0, 'fun': 0.029197080291970802, 'emotional': 0.0, 'positive_emotion': 0.021897810218978103, 'affection': 0.0}



{'love': 0.006369426751592357, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.006369426751592357, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.006369426751592357, 'sadness': 0.0, 'social_media': 0.012738853503184714, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0196078431372549, 'lust': 0.0196078431372549, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0196078431372549, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.030303030303030304, 'lust': 0.010101010101010102, 'shame': 0.010101010101010102, 'sleep': 0.005050505050505051, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.010101010101010102, 'cheerfulness': 0.010101010101010102, 'aggression': 0.010101010101010102, 'irritability': 0.005050505050505051, 'breaking': 0.005050505050505051, 'health': 0.0, 'attractive': 0.005050505050505051, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.010101010101010102, 'pain': 0.025252525252525252, 'joy': 0.005050505050505051, 'healing': 0.005050505050505051, 'friends': 0.005050505050505051, 'celebration': 0.005050505050505051, 'negative_emotion': 0.025252525252525252, 'sadness': 0.005050505050505051, 'social_media': 0.005050505050505051, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.005050505050505051, 'positive_emotion': 0.025252525252525252, 'affection': 0.005050505050505051}



{'love': 0.0057306590257879654, 'lust': 0.0, 'shame': 0.017191977077363897, 'sleep': 0.0, 'anger': 0.0028653295128939827, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.011461318051575931, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0028653295128939827, 'attractive': 0.0057306590257879654, 'disgust': 0.0028653295128939827, 'ugliness': 0.0, 'nervousness': 0.0057306590257879654, 'pain': 0.014326647564469915, 'joy': 0.0, 'healing': 0.0028653295128939827, 'friends': 0.011461318051575931, 'celebration': 0.0, 'negative_emotion': 0.02865329512893983, 'sadness': 0.0028653295128939827, 'social_media': 0.0057306590257879654, 'disappointment': 0.0028653295128939827, 'fun': 0.008595988538681949, 'emotional': 0.008595988538681949, 'positive_emotion': 0.017191977077363897, 'affection': 0.0}



{'love': 0.02195121951219512, 'lust': 0.0024390243902439024, 'shame': 0.03170731707317073, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.004878048780487805, 'hate': 0.00975609756097561, 'cheerfulness': 0.004878048780487805, 'aggression': 0.004878048780487805, 'irritability': 0.0, 'breaking': 0.004878048780487805, 'health': 0.0024390243902439024, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01951219512195122, 'pain': 0.02926829268292683, 'joy': 0.0024390243902439024, 'healing': 0.0024390243902439024, 'friends': 0.007317073170731708, 'celebration': 0.007317073170731708, 'negative_emotion': 0.01951219512195122, 'sadness': 0.007317073170731708, 'social_media': 0.012195121951219513, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.00975609756097561, 'positive_emotion': 0.01707317073170732, 'affection': 0.0024390243902439024}



{'love': 0.0136986301369863, 'lust': 0.0045662100456621, 'shame': 0.0091324200913242, 'sleep': 0.0, 'anger': 0.0091324200913242, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0045662100456621, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0045662100456621, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0091324200913242, 'pain': 0.0091324200913242, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0091324200913242, 'celebration': 0.0045662100456621, 'negative_emotion': 0.0091324200913242, 'sadness': 0.0091324200913242, 'social_media': 0.0136986301369863, 'disappointment': 0.0091324200913242, 'fun': 0.0, 'emotional': 0.0045662100456621, 'positive_emotion': 0.0091324200913242, 'affection': 0.0}



{'love': 0.01276595744680851, 'lust': 0.00425531914893617, 'shame': 0.00851063829787234, 'sleep': 0.0, 'anger': 0.00851063829787234, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.00425531914893617, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.00425531914893617, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.00851063829787234, 'pain': 0.00851063829787234, 'joy': 0.0, 'healing': 0.0, 'friends': 0.00851063829787234, 'celebration': 0.00425531914893617, 'negative_emotion': 0.00851063829787234, 'sadness': 0.00851063829787234, 'social_media': 0.01276595744680851, 'disappointment': 0.00851063829787234, 'fun': 0.0, 'emotional': 0.00425531914893617, 'positive_emotion': 0.00851063829787234, 'affection': 0.0}



{'love': 0.009852216748768473, 'lust': 0.0, 'shame': 0.014778325123152709, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0049261083743842365, 'hate': 0.0, 'cheerfulness': 0.009852216748768473, 'aggression': 0.0049261083743842365, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0049261083743842365, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009852216748768473, 'pain': 0.014778325123152709, 'joy': 0.0, 'healing': 0.0, 'friends': 0.019704433497536946, 'celebration': 0.014778325123152709, 'negative_emotion': 0.0049261083743842365, 'sadness': 0.009852216748768473, 'social_media': 0.0049261083743842365, 'disappointment': 0.0049261083743842365, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009852216748768473, 'affection': 0.0}



{'love': 0.0033112582781456954, 'lust': 0.006622516556291391, 'shame': 0.013245033112582781, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.006622516556291391, 'hate': 0.013245033112582781, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.009933774834437087, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009933774834437087, 'pain': 0.026490066225165563, 'joy': 0.0033112582781456954, 'healing': 0.0033112582781456954, 'friends': 0.026490066225165563, 'celebration': 0.023178807947019868, 'negative_emotion': 0.033112582781456956, 'sadness': 0.013245033112582781, 'social_media': 0.009933774834437087, 'disappointment': 0.0, 'fun': 0.009933774834437087, 'emotional': 0.019867549668874173, 'positive_emotion': 0.013245033112582781, 'affection': 0.0033112582781456954}



{'love': 0.014218009478672985, 'lust': 0.004739336492890996, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.004739336492890996, 'hate': 0.0, 'cheerfulness': 0.004739336492890996, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.004739336492890996, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.004739336492890996, 'sadness': 0.0, 'social_media': 0.004739336492890996, 'disappointment': 0.0, 'fun': 0.018957345971563982, 'emotional': 0.009478672985781991, 'positive_emotion': 0.014218009478672985, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.017543859649122806, 'hate': 0.03508771929824561, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.02631578947368421, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.017543859649122806, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017543859649122806, 'celebration': 0.008771929824561403, 'negative_emotion': 0.03508771929824561, 'sadness': 0.02631578947368421, 'social_media': 0.017543859649122806, 'disappointment': 0.0, 'fun': 0.008771929824561403, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.005714285714285714, 'lust': 0.0, 'shame': 0.005714285714285714, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.005714285714285714, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.005714285714285714, 'pain': 0.005714285714285714, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.005714285714285714, 'sadness': 0.0, 'social_media': 0.005714285714285714, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.005714285714285714, 'affection': 0.0}



{'love': 0.0029585798816568047, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0029585798816568047, 'cheerfulness': 0.0029585798816568047, 'aggression': 0.0029585798816568047, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.005917159763313609, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.005917159763313609, 'friends': 0.014792899408284023, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0029585798816568047, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.005917159763313609, 'affection': 0.0}



{'love': 0.009615384615384616, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.004807692307692308, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.004807692307692308, 'celebration': 0.004807692307692308, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.004807692307692308, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004807692307692308, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.005291005291005291, 'sleep': 0.005291005291005291, 'anger': 0.005291005291005291, 'anonymity': 0.0, 'fear': 0.005291005291005291, 'hate': 0.005291005291005291, 'cheerfulness': 0.0, 'aggression': 0.005291005291005291, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.015873015873015872, 'attractive': 0.0, 'disgust': 0.005291005291005291, 'ugliness': 0.0, 'nervousness': 0.005291005291005291, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.010582010582010581, 'celebration': 0.0, 'negative_emotion': 0.005291005291005291, 'sadness': 0.010582010582010581, 'social_media': 0.005291005291005291, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.005291005291005291, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0027247956403269754, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.01907356948228883, 'anger': 0.0, 'anonymity': 0.0027247956403269754, 'fear': 0.0, 'hate': 0.005449591280653951, 'cheerfulness': 0.0, 'aggression': 0.005449591280653951, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.005449591280653951, 'disgust': 0.0027247956403269754, 'ugliness': 0.0027247956403269754, 'nervousness': 0.0, 'pain': 0.0027247956403269754, 'joy': 0.0, 'healing': 0.0, 'friends': 0.013623978201634877, 'celebration': 0.0027247956403269754, 'negative_emotion': 0.008174386920980926, 'sadness': 0.0027247956403269754, 'social_media': 0.008174386920980926, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.008174386920980926, 'positive_emotion': 0.0027247956403269754, 'affection': 0.0027247956403269754}



{'love': 0.01256281407035176, 'lust': 0.002512562814070352, 'shame': 0.01507537688442211, 'sleep': 0.002512562814070352, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.002512562814070352, 'hate': 0.007537688442211055, 'cheerfulness': 0.002512562814070352, 'aggression': 0.002512562814070352, 'irritability': 0.0, 'breaking': 0.002512562814070352, 'health': 0.0, 'attractive': 0.002512562814070352, 'disgust': 0.0, 'ugliness': 0.002512562814070352, 'nervousness': 0.01507537688442211, 'pain': 0.01507537688442211, 'joy': 0.005025125628140704, 'healing': 0.002512562814070352, 'friends': 0.01507537688442211, 'celebration': 0.005025125628140704, 'negative_emotion': 0.007537688442211055, 'sadness': 0.007537688442211055, 'social_media': 0.007537688442211055, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.002512562814070352, 'positive_emotion': 0.010050251256281407, 'affection': 0.007537688442211055}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.003861003861003861, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.007722007722007722, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.003861003861003861, 'friends': 0.007722007722007722, 'celebration': 0.003861003861003861, 'negative_emotion': 0.011583011583011582, 'sadness': 0.003861003861003861, 'social_media': 0.003861003861003861, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.003861003861003861, 'positive_emotion': 0.011583011583011582, 'affection': 0.0}



{'love': 0.0038910505836575876, 'lust': 0.0038910505836575876, 'shame': 0.0019455252918287938, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0019455252918287938, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0019455252918287938, 'attractive': 0.0038910505836575876, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0019455252918287938, 'joy': 0.0019455252918287938, 'healing': 0.0019455252918287938, 'friends': 0.0, 'celebration': 0.0019455252918287938, 'negative_emotion': 0.0019455252918287938, 'sadness': 0.0, 'social_media': 0.0038910505836575876, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0019455252918287938, 'positive_emotion': 0.0019455252918287938, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.022222222222222223, 'sadness': 0.0, 'social_media': 0.022222222222222223, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.010752688172043012, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.01652892561983471, 'lust': 0.0, 'shame': 0.03305785123966942, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.01652892561983471, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.008264462809917356, 'attractive': 0.008264462809917356, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01652892561983471, 'pain': 0.01652892561983471, 'joy': 0.0, 'healing': 0.0, 'friends': 0.008264462809917356, 'celebration': 0.0, 'negative_emotion': 0.024793388429752067, 'sadness': 0.01652892561983471, 'social_media': 0.008264462809917356, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.01652892561983471, 'positive_emotion': 0.008264462809917356, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.013245033112582781, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.006622516556291391, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.006622516556291391, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.006622516556291391, 'healing': 0.006622516556291391, 'friends': 0.006622516556291391, 'celebration': 0.0, 'negative_emotion': 0.013245033112582781, 'sadness': 0.0, 'social_media': 0.006622516556291391, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.033112582781456956, 'affection': 0.0}



{'love': 0.004310344827586207, 'lust': 0.0, 'shame': 0.004310344827586207, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.004310344827586207, 'health': 0.0, 'attractive': 0.008620689655172414, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.004310344827586207, 'friends': 0.05603448275862069, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.004310344827586207, 'social_media': 0.02586206896551724, 'disappointment': 0.0, 'fun': 0.004310344827586207, 'emotional': 0.004310344827586207, 'positive_emotion': 0.008620689655172414, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.05555555555555555, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.05555555555555555, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.05555555555555555, 'sadness': 0.0, 'social_media': 0.05555555555555555, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.010582010582010581, 'lust': 0.0013227513227513227, 'shame': 0.009259259259259259, 'sleep': 0.006613756613756613, 'anger': 0.0013227513227513227, 'anonymity': 0.0, 'fear': 0.0013227513227513227, 'hate': 0.005291005291005291, 'cheerfulness': 0.0013227513227513227, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.005291005291005291, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.006613756613756613, 'pain': 0.007936507936507936, 'joy': 0.0026455026455026454, 'healing': 0.003968253968253968, 'friends': 0.007936507936507936, 'celebration': 0.0013227513227513227, 'negative_emotion': 0.021164021164021163, 'sadness': 0.003968253968253968, 'social_media': 0.0013227513227513227, 'disappointment': 0.0013227513227513227, 'fun': 0.0, 'emotional': 0.0026455026455026454, 'positive_emotion': 0.009259259259259259, 'affection': 0.005291005291005291}



{'love': 0.005660377358490566, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0037735849056603774, 'irritability': 0.0, 'breaking': 0.0037735849056603774, 'health': 0.0, 'attractive': 0.007547169811320755, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0018867924528301887, 'pain': 0.0018867924528301887, 'joy': 0.0, 'healing': 0.0018867924528301887, 'friends': 0.013207547169811321, 'celebration': 0.0, 'negative_emotion': 0.0018867924528301887, 'sadness': 0.0, 'social_media': 0.0018867924528301887, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.005660377358490566, 'positive_emotion': 0.005660377358490566, 'affection': 0.007547169811320755}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.047619047619047616, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.09523809523809523, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.020833333333333332, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.020833333333333332, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.020833333333333332, 'affection': 0.0}



{'love': 0.003770028275212064, 'lust': 0.0, 'shame': 0.003770028275212064, 'sleep': 0.000942507068803016, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.000942507068803016, 'hate': 0.003770028275212064, 'cheerfulness': 0.0, 'aggression': 0.000942507068803016, 'irritability': 0.000942507068803016, 'breaking': 0.000942507068803016, 'health': 0.0, 'attractive': 0.000942507068803016, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.002827521206409048, 'pain': 0.005655042412818096, 'joy': 0.0, 'healing': 0.005655042412818096, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.008482563619227144, 'sadness': 0.0, 'social_media': 0.000942507068803016, 'disappointment': 0.0, 'fun': 0.001885014137606032, 'emotional': 0.000942507068803016, 'positive_emotion': 0.00471253534401508, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.010309278350515464, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.020618556701030927, 'disappointment': 0.0, 'fun': 0.020618556701030927, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.005025125628140704, 'lust': 0.0, 'shame': 0.005025125628140704, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.010050251256281407, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.005025125628140704, 'attractive': 0.005025125628140704, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.005025125628140704, 'pain': 0.005025125628140704, 'joy': 0.005025125628140704, 'healing': 0.005025125628140704, 'friends': 0.010050251256281407, 'celebration': 0.005025125628140704, 'negative_emotion': 0.03015075376884422, 'sadness': 0.010050251256281407, 'social_media': 0.01507537688442211, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.010050251256281407, 'positive_emotion': 0.010050251256281407, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.017094017094017096, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.05714285714285714, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.03333333333333333, 'lust': 0.011111111111111112, 'shame': 0.06666666666666667, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.011111111111111112, 'hate': 0.022222222222222223, 'cheerfulness': 0.011111111111111112, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.011111111111111112, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.044444444444444446, 'pain': 0.05555555555555555, 'joy': 0.011111111111111112, 'healing': 0.0, 'friends': 0.022222222222222223, 'celebration': 0.022222222222222223, 'negative_emotion': 0.03333333333333333, 'sadness': 0.03333333333333333, 'social_media': 0.011111111111111112, 'disappointment': 0.0, 'fun': 0.011111111111111112, 'emotional': 0.022222222222222223, 'positive_emotion': 0.044444444444444446, 'affection': 0.011111111111111112}



{'love': 0.025210084033613446, 'lust': 0.0, 'shame': 0.04201680672268908, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.01680672268907563, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.025210084033613446, 'pain': 0.03361344537815126, 'joy': 0.0, 'healing': 0.008403361344537815, 'friends': 0.03361344537815126, 'celebration': 0.0, 'negative_emotion': 0.03361344537815126, 'sadness': 0.008403361344537815, 'social_media': 0.01680672268907563, 'disappointment': 0.008403361344537815, 'fun': 0.0, 'emotional': 0.01680672268907563, 'positive_emotion': 0.04201680672268908, 'affection': 0.0}



{'love': 0.00625, 'lust': 0.009375, 'shame': 0.015625, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.009375, 'hate': 0.0125, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015625, 'pain': 0.015625, 'joy': 0.009375, 'healing': 0.0, 'friends': 0.021875, 'celebration': 0.021875, 'negative_emotion': 0.00625, 'sadness': 0.009375, 'social_media': 0.00625, 'disappointment': 0.0, 'fun': 0.00625, 'emotional': 0.00625, 'positive_emotion': 0.021875, 'affection': 0.009375}



{'love': 0.006825938566552901, 'lust': 0.0, 'shame': 0.009101251422070534, 'sleep': 0.005688282138794084, 'anger': 0.0011376564277588168, 'anonymity': 0.0, 'fear': 0.007963594994311717, 'hate': 0.004550625711035267, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0022753128555176336, 'health': 0.0, 'attractive': 0.0011376564277588168, 'disgust': 0.0011376564277588168, 'ugliness': 0.0011376564277588168, 'nervousness': 0.012514220705346985, 'pain': 0.009101251422070534, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017064846416382253, 'celebration': 0.0011376564277588168, 'negative_emotion': 0.01478953356086462, 'sadness': 0.0022753128555176336, 'social_media': 0.011376564277588168, 'disappointment': 0.0011376564277588168, 'fun': 0.0011376564277588168, 'emotional': 0.0022753128555176336, 'positive_emotion': 0.004550625711035267, 'affection': 0.0011376564277588168}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.1111111111111111, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0196078431372549, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0196078431372549, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.017543859649122806, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.017543859649122806, 'affection': 0.0}



{'love': 0.017699115044247787, 'lust': 0.0, 'shame': 0.017699115044247787, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.017699115044247787, 'pain': 0.017699115044247787, 'joy': 0.0, 'healing': 0.008849557522123894, 'friends': 0.05309734513274336, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.017699115044247787, 'disappointment': 0.0, 'fun': 0.017699115044247787, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.05, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.05, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.00980392156862745, 'shame': 0.00980392156862745, 'sleep': 0.0, 'anger': 0.00980392156862745, 'anonymity': 0.0, 'fear': 0.029411764705882353, 'hate': 0.00980392156862745, 'cheerfulness': 0.0, 'aggression': 0.00980392156862745, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.00980392156862745, 'attractive': 0.0, 'disgust': 0.00980392156862745, 'ugliness': 0.0, 'nervousness': 0.0392156862745098, 'pain': 0.00980392156862745, 'joy': 0.00980392156862745, 'healing': 0.0, 'friends': 0.0392156862745098, 'celebration': 0.0, 'negative_emotion': 0.00980392156862745, 'sadness': 0.029411764705882353, 'social_media': 0.049019607843137254, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.00980392156862745, 'affection': 0.00980392156862745}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.07142857142857142, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.07142857142857142, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.009433962264150943, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.014150943396226415, 'pain': 0.009433962264150943, 'joy': 0.0, 'healing': 0.0047169811320754715, 'friends': 0.018867924528301886, 'celebration': 0.0, 'negative_emotion': 0.014150943396226415, 'sadness': 0.0, 'social_media': 0.014150943396226415, 'disappointment': 0.0, 'fun': 0.0047169811320754715, 'emotional': 0.0, 'positive_emotion': 0.0047169811320754715, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.037037037037037035, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.02857142857142857, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.009708737864077669, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.009708737864077669, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.009708737864077669, 'nervousness': 0.0, 'pain': 0.009708737864077669, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.038834951456310676, 'sadness': 0.0, 'social_media': 0.009708737864077669, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.009708737864077669, 'positive_emotion': 0.009708737864077669, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.014285714285714285, 'negative_emotion': 0.014285714285714285, 'sadness': 0.0, 'social_media': 0.014285714285714285, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.02857142857142857, 'affection': 0.0}



{'love': 0.002036659877800407, 'lust': 0.0, 'shame': 0.002036659877800407, 'sleep': 0.0, 'anger': 0.002036659877800407, 'anonymity': 0.0, 'fear': 0.002036659877800407, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.004073319755600814, 'irritability': 0.0, 'breaking': 0.004073319755600814, 'health': 0.0, 'attractive': 0.002036659877800407, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004073319755600814, 'pain': 0.0, 'joy': 0.002036659877800407, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.008146639511201629, 'sadness': 0.002036659877800407, 'social_media': 0.002036659877800407, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.002036659877800407, 'positive_emotion': 0.008146639511201629, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.013888888888888888, 'sadness': 0.0, 'social_media': 0.013888888888888888, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.02631578947368421, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02631578947368421, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.013157894736842105, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013157894736842105, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.028037383177570093, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.009345794392523364, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.058823529411764705, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0136986301369863, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.00684931506849315, 'irritability': 0.0, 'breaking': 0.00684931506849315, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.00684931506849315, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02054794520547945, 'celebration': 0.0, 'negative_emotion': 0.0136986301369863, 'sadness': 0.0, 'social_media': 0.00684931506849315, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0055248618784530384, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.011049723756906077, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0055248618784530384, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.011049723756906077, 'celebration': 0.0, 'negative_emotion': 0.0055248618784530384, 'sadness': 0.011049723756906077, 'social_media': 0.0055248618784530384, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.005025125628140704, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.005025125628140704, 'celebration': 0.0, 'negative_emotion': 0.005025125628140704, 'sadness': 0.0, 'social_media': 0.005025125628140704, 'disappointment': 0.005025125628140704, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.010050251256281407, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.04, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.006535947712418301, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0196078431372549, 'negative_emotion': 0.0196078431372549, 'sadness': 0.0, 'social_media': 0.013071895424836602, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.006535947712418301, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.011627906976744186, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.011627906976744186, 'negative_emotion': 0.011627906976744186, 'sadness': 0.0, 'social_media': 0.023255813953488372, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.016129032258064516, 'sleep': 0.0, 'anger': 0.016129032258064516, 'anonymity': 0.0, 'fear': 0.016129032258064516, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.016129032258064516, 'disgust': 0.0, 'ugliness': 0.03225806451612903, 'nervousness': 0.0, 'pain': 0.016129032258064516, 'joy': 0.0, 'healing': 0.0, 'friends': 0.016129032258064516, 'celebration': 0.0, 'negative_emotion': 0.016129032258064516, 'sadness': 0.016129032258064516, 'social_media': 0.016129032258064516, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.004273504273504274, 'lust': 0.0, 'shame': 0.004273504273504274, 'sleep': 0.002136752136752137, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.002136752136752137, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.002136752136752137, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004273504273504274, 'pain': 0.004273504273504274, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.010683760683760684, 'negative_emotion': 0.010683760683760684, 'sadness': 0.0, 'social_media': 0.002136752136752137, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.002136752136752137, 'affection': 0.0}



{'love': 0.004395604395604396, 'lust': 0.0, 'shame': 0.004395604395604396, 'sleep': 0.002197802197802198, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.002197802197802198, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.002197802197802198, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004395604395604396, 'pain': 0.004395604395604396, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.01098901098901099, 'negative_emotion': 0.01098901098901099, 'sadness': 0.0, 'social_media': 0.002197802197802198, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.002197802197802198, 'affection': 0.0}



{'love': 0.0043859649122807015, 'lust': 0.0, 'shame': 0.006578947368421052, 'sleep': 0.0, 'anger': 0.0021929824561403508, 'anonymity': 0.0, 'fear': 0.0043859649122807015, 'hate': 0.0043859649122807015, 'cheerfulness': 0.0, 'aggression': 0.0021929824561403508, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0021929824561403508, 'attractive': 0.006578947368421052, 'disgust': 0.0021929824561403508, 'ugliness': 0.006578947368421052, 'nervousness': 0.008771929824561403, 'pain': 0.006578947368421052, 'joy': 0.0, 'healing': 0.0021929824561403508, 'friends': 0.006578947368421052, 'celebration': 0.0021929824561403508, 'negative_emotion': 0.008771929824561403, 'sadness': 0.0043859649122807015, 'social_media': 0.0043859649122807015, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0021929824561403508, 'positive_emotion': 0.010964912280701754, 'affection': 0.0}



{'love': 0.013605442176870748, 'lust': 0.0, 'shame': 0.0017006802721088435, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.003401360544217687, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.003401360544217687, 'health': 0.0, 'attractive': 0.003401360544217687, 'disgust': 0.0017006802721088435, 'ugliness': 0.00510204081632653, 'nervousness': 0.0, 'pain': 0.0017006802721088435, 'joy': 0.0, 'healing': 0.0, 'friends': 0.030612244897959183, 'celebration': 0.003401360544217687, 'negative_emotion': 0.006802721088435374, 'sadness': 0.0017006802721088435, 'social_media': 0.00510204081632653, 'disappointment': 0.0, 'fun': 0.0017006802721088435, 'emotional': 0.003401360544217687, 'positive_emotion': 0.011904761904761904, 'affection': 0.003401360544217687}



{'love': 0.01232394366197183, 'lust': 0.0, 'shame': 0.0017605633802816902, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00528169014084507, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0035211267605633804, 'health': 0.0, 'attractive': 0.0035211267605633804, 'disgust': 0.0017605633802816902, 'ugliness': 0.007042253521126761, 'nervousness': 0.0, 'pain': 0.0017605633802816902, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03169014084507042, 'celebration': 0.0035211267605633804, 'negative_emotion': 0.008802816901408451, 'sadness': 0.0017605633802816902, 'social_media': 0.0035211267605633804, 'disappointment': 0.0, 'fun': 0.0017605633802816902, 'emotional': 0.0035211267605633804, 'positive_emotion': 0.01232394366197183, 'affection': 0.0035211267605633804}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.004329004329004329, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.012987012987012988, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004329004329004329, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.008658008658008658, 'celebration': 0.0, 'negative_emotion': 0.004329004329004329, 'sadness': 0.0, 'social_media': 0.004329004329004329, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.024390243902439025, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.024390243902439025, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.04878048780487805, 'disappointment': 0.0, 'fun': 0.024390243902439025, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.009615384615384616, 'lust': 0.0, 'shame': 0.009615384615384616, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.004807692307692308, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.014423076923076924, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009615384615384616, 'pain': 0.009615384615384616, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.004807692307692308, 'negative_emotion': 0.009615384615384616, 'sadness': 0.0, 'social_media': 0.004807692307692308, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004807692307692308, 'positive_emotion': 0.004807692307692308, 'affection': 0.004807692307692308}



{'love': 0.006289308176100629, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.012578616352201259, 'disgust': 0.0, 'ugliness': 0.006289308176100629, 'nervousness': 0.0, 'pain': 0.006289308176100629, 'joy': 0.0, 'healing': 0.0, 'friends': 0.018867924528301886, 'celebration': 0.0, 'negative_emotion': 0.006289308176100629, 'sadness': 0.0, 'social_media': 0.006289308176100629, 'disappointment': 0.0, 'fun': 0.006289308176100629, 'emotional': 0.0, 'positive_emotion': 0.006289308176100629, 'affection': 0.006289308176100629}



{'love': 0.004301075268817204, 'lust': 0.0, 'shame': 0.004301075268817204, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.010752688172043012, 'disgust': 0.002150537634408602, 'ugliness': 0.015053763440860216, 'nervousness': 0.002150537634408602, 'pain': 0.0, 'joy': 0.0, 'healing': 0.004301075268817204, 'friends': 0.008602150537634409, 'celebration': 0.002150537634408602, 'negative_emotion': 0.0064516129032258064, 'sadness': 0.0, 'social_media': 0.004301075268817204, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.021505376344086023, 'affection': 0.004301075268817204}



{'love': 0.008695652173913044, 'lust': 0.008695652173913044, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.017391304347826087, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.008695652173913044, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017391304347826087, 'celebration': 0.0, 'negative_emotion': 0.017391304347826087, 'sadness': 0.0, 'social_media': 0.017391304347826087, 'disappointment': 0.0, 'fun': 0.02608695652173913, 'emotional': 0.0, 'positive_emotion': 0.008695652173913044, 'affection': 0.0}



{'love': 0.0, 'lust': 0.006666666666666667, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.006666666666666667, 'health': 0.0, 'attractive': 0.006666666666666667, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.006666666666666667, 'disappointment': 0.0, 'fun': 0.006666666666666667, 'emotional': 0.0, 'positive_emotion': 0.006666666666666667, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.01694915254237288, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.011299435028248588, 'celebration': 0.011299435028248588, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.011299435028248588, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.009259259259259259, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.009259259259259259, 'celebration': 0.009259259259259259, 'negative_emotion': 0.009259259259259259, 'sadness': 0.0, 'social_media': 0.018518518518518517, 'disappointment': 0.0, 'fun': 0.009259259259259259, 'emotional': 0.0, 'positive_emotion': 0.009259259259259259, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.010362694300518135, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.004878048780487805, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.004878048780487805, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.004878048780487805, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.004878048780487805, 'negative_emotion': 0.004878048780487805, 'sadness': 0.0, 'social_media': 0.014634146341463415, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.004132231404958678, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.004132231404958678, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.004132231404958678, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.004132231404958678, 'negative_emotion': 0.004132231404958678, 'sadness': 0.0, 'social_media': 0.012396694214876033, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.04, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.04, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04, 'sadness': 0.0, 'social_media': 0.04, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.038461538461538464, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.07692307692307693, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.038461538461538464, 'sadness': 0.0, 'social_media': 0.038461538461538464, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.004761904761904762, 'disgust': 0.0, 'ugliness': 0.004761904761904762, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.009523809523809525, 'celebration': 0.004761904761904762, 'negative_emotion': 0.009523809523809525, 'sadness': 0.0, 'social_media': 0.009523809523809525, 'disappointment': 0.0, 'fun': 0.004761904761904762, 'emotional': 0.004761904761904762, 'positive_emotion': 0.004761904761904762, 'affection': 0.0}



{'love': 0.006802721088435374, 'lust': 0.006802721088435374, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.006802721088435374, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.008403361344537815, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.008403361344537815, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.008403361344537815, 'cheerfulness': 0.0, 'aggression': 0.008403361344537815, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.008403361344537815, 'disgust': 0.008403361344537815, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.008403361344537815, 'disappointment': 0.0, 'fun': 0.01680672268907563, 'emotional': 0.0, 'positive_emotion': 0.01680672268907563, 'affection': 0.0}



{'love': 0.008620689655172414, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.008620689655172414, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.008620689655172414, 'cheerfulness': 0.0, 'aggression': 0.008620689655172414, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.008620689655172414, 'disgust': 0.008620689655172414, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.008620689655172414, 'disappointment': 0.0, 'fun': 0.017241379310344827, 'emotional': 0.0, 'positive_emotion': 0.017241379310344827, 'affection': 0.0}



{'love': 0.008620689655172414, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.008620689655172414, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.008620689655172414, 'cheerfulness': 0.0, 'aggression': 0.008620689655172414, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.008620689655172414, 'disgust': 0.008620689655172414, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.008620689655172414, 'disappointment': 0.0, 'fun': 0.017241379310344827, 'emotional': 0.0, 'positive_emotion': 0.017241379310344827, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.006493506493506494, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.006493506493506494, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.006493506493506494, 'sadness': 0.0, 'social_media': 0.012987012987012988, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.012048192771084338, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03614457831325301, 'celebration': 0.0, 'negative_emotion': 0.024096385542168676, 'sadness': 0.0, 'social_media': 0.012048192771084338, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.012048192771084338, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.01, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.01, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.01, 'sadness': 0.0, 'social_media': 0.02, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01, 'affection': 0.0}



{'love': 0.008333333333333333, 'lust': 0.0, 'shame': 0.008333333333333333, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.008333333333333333, 'nervousness': 0.008333333333333333, 'pain': 0.008333333333333333, 'joy': 0.0, 'healing': 0.008333333333333333, 'friends': 0.008333333333333333, 'celebration': 0.0, 'negative_emotion': 0.016666666666666666, 'sadness': 0.0, 'social_media': 0.008333333333333333, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.016666666666666666, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.013513513513513514, 'sleep': 0.0, 'anger': 0.013513513513513514, 'anonymity': 0.0, 'fear': 0.013513513513513514, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.02702702702702703, 'disgust': 0.013513513513513514, 'ugliness': 0.02702702702702703, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.013513513513513514, 'social_media': 0.02702702702702703, 'disappointment': 0.013513513513513514, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.020833333333333332, 'lust': 0.0, 'shame': 0.020833333333333332, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.020833333333333332, 'nervousness': 0.020833333333333332, 'pain': 0.020833333333333332, 'joy': 0.0, 'healing': 0.020833333333333332, 'friends': 0.041666666666666664, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.041666666666666664, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.05263157894736842, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.05263157894736842, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.006060606060606061, 'lust': 0.0, 'shame': 0.006060606060606061, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.006060606060606061, 'aggression': 0.006060606060606061, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.012121212121212121, 'nervousness': 0.006060606060606061, 'pain': 0.006060606060606061, 'joy': 0.0, 'healing': 0.0, 'friends': 0.030303030303030304, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.006060606060606061, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.006060606060606061, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.024096385542168676, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012048192771084338, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.012048192771084338, 'disappointment': 0.0, 'fun': 0.012048192771084338, 'emotional': 0.0, 'positive_emotion': 0.012048192771084338, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.008, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.008, 'attractive': 0.008, 'disgust': 0.0, 'ugliness': 0.008, 'nervousness': 0.008, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.016, 'celebration': 0.016, 'negative_emotion': 0.04, 'sadness': 0.008, 'social_media': 0.008, 'disappointment': 0.0, 'fun': 0.008, 'emotional': 0.0, 'positive_emotion': 0.008, 'affection': 0.0}



{'love': 0.0, 'lust': 0.007751937984496124, 'shame': 0.023255813953488372, 'sleep': 0.0, 'anger': 0.015503875968992248, 'anonymity': 0.0, 'fear': 0.046511627906976744, 'hate': 0.015503875968992248, 'cheerfulness': 0.0, 'aggression': 0.007751937984496124, 'irritability': 0.0, 'breaking': 0.007751937984496124, 'health': 0.007751937984496124, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.031007751937984496, 'pain': 0.031007751937984496, 'joy': 0.007751937984496124, 'healing': 0.0, 'friends': 0.007751937984496124, 'celebration': 0.0, 'negative_emotion': 0.03875968992248062, 'sadness': 0.031007751937984496, 'social_media': 0.007751937984496124, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.007751937984496124, 'positive_emotion': 0.015503875968992248, 'affection': 0.007751937984496124}



{'love': 0.004739336492890996, 'lust': 0.0, 'shame': 0.009478672985781991, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.014218009478672985, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.009478672985781991, 'nervousness': 0.004739336492890996, 'pain': 0.009478672985781991, 'joy': 0.0, 'healing': 0.014218009478672985, 'friends': 0.018957345971563982, 'celebration': 0.004739336492890996, 'negative_emotion': 0.004739336492890996, 'sadness': 0.004739336492890996, 'social_media': 0.014218009478672985, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.023696682464454975, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.014705882352941176, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.014705882352941176, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.014705882352941176, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.010845986984815618, 'lust': 0.0, 'shame': 0.010845986984815618, 'sleep': 0.004338394793926247, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0021691973969631237, 'hate': 0.004338394793926247, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0021691973969631237, 'health': 0.004338394793926247, 'attractive': 0.004338394793926247, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008676789587852495, 'pain': 0.010845986984815618, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.006507592190889371, 'negative_emotion': 0.008676789587852495, 'sadness': 0.0, 'social_media': 0.008676789587852495, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0021691973969631237, 'positive_emotion': 0.004338394793926247, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.007042253521126761, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.028169014084507043, 'negative_emotion': 0.007042253521126761, 'sadness': 0.0, 'social_media': 0.007042253521126761, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.007042253521126761, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.021739130434782608, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.021739130434782608, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.021739130434782608, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.006514657980456026, 'lust': 0.003257328990228013, 'shame': 0.006514657980456026, 'sleep': 0.003257328990228013, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.006514657980456026, 'hate': 0.006514657980456026, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009771986970684038, 'pain': 0.009771986970684038, 'joy': 0.003257328990228013, 'healing': 0.0, 'friends': 0.013029315960912053, 'celebration': 0.006514657980456026, 'negative_emotion': 0.009771986970684038, 'sadness': 0.003257328990228013, 'social_media': 0.009771986970684038, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.009771986970684038, 'affection': 0.006514657980456026}



{'love': 0.0, 'lust': 0.0, 'shame': 0.013333333333333334, 'sleep': 0.006666666666666667, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.013333333333333334, 'cheerfulness': 0.0, 'aggression': 0.006666666666666667, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.013333333333333334, 'joy': 0.0, 'healing': 0.013333333333333334, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.013333333333333334, 'sadness': 0.0, 'social_media': 0.006666666666666667, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.013333333333333334, 'positive_emotion': 0.013333333333333334, 'affection': 0.0}



{'love': 0.014705882352941176, 'lust': 0.007352941176470588, 'shame': 0.03676470588235294, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.014705882352941176, 'hate': 0.014705882352941176, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.007352941176470588, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.029411764705882353, 'pain': 0.029411764705882353, 'joy': 0.007352941176470588, 'healing': 0.0, 'friends': 0.022058823529411766, 'celebration': 0.0, 'negative_emotion': 0.007352941176470588, 'sadness': 0.022058823529411766, 'social_media': 0.007352941176470588, 'disappointment': 0.0, 'fun': 0.007352941176470588, 'emotional': 0.007352941176470588, 'positive_emotion': 0.007352941176470588, 'affection': 0.007352941176470588}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.015151515151515152, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.015151515151515152, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.013888888888888888, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.013888888888888888, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.013888888888888888, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.013888888888888888, 'disgust': 0.013888888888888888, 'ugliness': 0.027777777777777776, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.027777777777777776, 'celebration': 0.0, 'negative_emotion': 0.013888888888888888, 'sadness': 0.0, 'social_media': 0.013888888888888888, 'disappointment': 0.013888888888888888, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013888888888888888, 'affection': 0.0}



{'love': 0.017391304347826087, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.008695652173913044, 'hate': 0.008695652173913044, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.017391304347826087, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.008695652173913044, 'friends': 0.017391304347826087, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.008695652173913044, 'social_media': 0.008695652173913044, 'disappointment': 0.008695652173913044, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.008695652173913044, 'affection': 0.008695652173913044}



{'love': 0.0064516129032258064, 'lust': 0.0, 'shame': 0.0064516129032258064, 'sleep': 0.0064516129032258064, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0064516129032258064, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0064516129032258064, 'nervousness': 0.0064516129032258064, 'pain': 0.0064516129032258064, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03225806451612903, 'celebration': 0.012903225806451613, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0064516129032258064, 'disappointment': 0.0, 'fun': 0.0064516129032258064, 'emotional': 0.0, 'positive_emotion': 0.012903225806451613, 'affection': 0.0}



{'love': 0.0064516129032258064, 'lust': 0.0, 'shame': 0.0064516129032258064, 'sleep': 0.0064516129032258064, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0064516129032258064, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0064516129032258064, 'nervousness': 0.0064516129032258064, 'pain': 0.0064516129032258064, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03225806451612903, 'celebration': 0.012903225806451613, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0064516129032258064, 'disappointment': 0.0, 'fun': 0.0064516129032258064, 'emotional': 0.0, 'positive_emotion': 0.012903225806451613, 'affection': 0.0}



{'love': 0.00641025641025641, 'lust': 0.0, 'shame': 0.00641025641025641, 'sleep': 0.00641025641025641, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.00641025641025641, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.00641025641025641, 'nervousness': 0.00641025641025641, 'pain': 0.00641025641025641, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03205128205128205, 'celebration': 0.01282051282051282, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.00641025641025641, 'disappointment': 0.0, 'fun': 0.00641025641025641, 'emotional': 0.0, 'positive_emotion': 0.01282051282051282, 'affection': 0.0}



{'love': 0.010351966873706004, 'lust': 0.006211180124223602, 'shame': 0.004140786749482402, 'sleep': 0.0, 'anger': 0.002070393374741201, 'anonymity': 0.0, 'fear': 0.002070393374741201, 'hate': 0.002070393374741201, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.002070393374741201, 'disgust': 0.0, 'ugliness': 0.008281573498964804, 'nervousness': 0.002070393374741201, 'pain': 0.004140786749482402, 'joy': 0.0, 'healing': 0.002070393374741201, 'friends': 0.014492753623188406, 'celebration': 0.006211180124223602, 'negative_emotion': 0.004140786749482402, 'sadness': 0.002070393374741201, 'social_media': 0.008281573498964804, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.002070393374741201, 'positive_emotion': 0.0, 'affection': 0.002070393374741201}



{'love': 0.004739336492890996, 'lust': 0.0, 'shame': 0.004739336492890996, 'sleep': 0.0, 'anger': 0.004739336492890996, 'anonymity': 0.0, 'fear': 0.004739336492890996, 'hate': 0.009478672985781991, 'cheerfulness': 0.0, 'aggression': 0.004739336492890996, 'irritability': 0.0, 'breaking': 0.004739336492890996, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.004739336492890996, 'ugliness': 0.004739336492890996, 'nervousness': 0.004739336492890996, 'pain': 0.004739336492890996, 'joy': 0.0, 'healing': 0.0, 'friends': 0.023696682464454975, 'celebration': 0.004739336492890996, 'negative_emotion': 0.018957345971563982, 'sadness': 0.004739336492890996, 'social_media': 0.004739336492890996, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.004739336492890996, 'positive_emotion': 0.004739336492890996, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.02564102564102564, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.01282051282051282, 'friends': 0.038461538461538464, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.038461538461538464, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0121765601217656, 'lust': 0.0030441400304414, 'shame': 0.0030441400304414, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0015220700152207, 'hate': 0.0015220700152207, 'cheerfulness': 0.0015220700152207, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0015220700152207, 'health': 0.0015220700152207, 'attractive': 0.0121765601217656, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0045662100456621, 'pain': 0.0060882800608828, 'joy': 0.0, 'healing': 0.0015220700152207, 'friends': 0.0121765601217656, 'celebration': 0.0045662100456621, 'negative_emotion': 0.0091324200913242, 'sadness': 0.0015220700152207, 'social_media': 0.0015220700152207, 'disappointment': 0.0, 'fun': 0.0030441400304414, 'emotional': 0.0, 'positive_emotion': 0.0106544901065449, 'affection': 0.0076103500761035}



{'love': 0.0053475935828877, 'lust': 0.0, 'shame': 0.0053475935828877, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0053475935828877, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0053475935828877, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0213903743315508, 'sadness': 0.0106951871657754, 'social_media': 0.0106951871657754, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0053475935828877, 'positive_emotion': 0.0106951871657754, 'affection': 0.0}



{'love': 0.00510204081632653, 'lust': 0.0, 'shame': 0.01020408163265306, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.00510204081632653, 'hate': 0.0, 'cheerfulness': 0.00510204081632653, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.00510204081632653, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01020408163265306, 'pain': 0.00510204081632653, 'joy': 0.0, 'healing': 0.0, 'friends': 0.02040816326530612, 'celebration': 0.01020408163265306, 'negative_emotion': 0.0, 'sadness': 0.01020408163265306, 'social_media': 0.04591836734693878, 'disappointment': 0.0, 'fun': 0.01020408163265306, 'emotional': 0.00510204081632653, 'positive_emotion': 0.01020408163265306, 'affection': 0.00510204081632653}



{'love': 0.006535947712418301, 'lust': 0.006535947712418301, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.006535947712418301, 'health': 0.0, 'attractive': 0.006535947712418301, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.006535947712418301, 'pain': 0.006535947712418301, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.006535947712418301, 'sadness': 0.0, 'social_media': 0.006535947712418301, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.006535947712418301, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.005, 'health': 0.0, 'attractive': 0.005, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.01, 'sadness': 0.0, 'social_media': 0.005, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.01, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.008130081300813009, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.008130081300813009, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.008130081300813009, 'pain': 0.008130081300813009, 'joy': 0.0, 'healing': 0.0, 'friends': 0.008130081300813009, 'celebration': 0.0, 'negative_emotion': 0.008130081300813009, 'sadness': 0.0, 'social_media': 0.008130081300813009, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.008130081300813009, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.027777777777777776, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.027777777777777776, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.043478260869565216, 'celebration': 0.0, 'negative_emotion': 0.014492753623188406, 'sadness': 0.0, 'social_media': 0.028985507246376812, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.014492753623188406, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.02702702702702703, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.04054054054054054, 'sadness': 0.0, 'social_media': 0.013513513513513514, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.013513513513513514, 'affection': 0.0}



{'love': 0.022727272727272728, 'lust': 0.0, 'shame': 0.022727272727272728, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.022727272727272728, 'pain': 0.022727272727272728, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.022727272727272728, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0016207455429497568, 'shame': 0.0032414910858995136, 'sleep': 0.0016207455429497568, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0032414910858995136, 'hate': 0.008103727714748784, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0032414910858995136, 'breaking': 0.0, 'health': 0.008103727714748784, 'attractive': 0.0016207455429497568, 'disgust': 0.0, 'ugliness': 0.0016207455429497568, 'nervousness': 0.006482982171799027, 'pain': 0.0032414910858995136, 'joy': 0.0016207455429497568, 'healing': 0.0, 'friends': 0.0016207455429497568, 'celebration': 0.0016207455429497568, 'negative_emotion': 0.009724473257698542, 'sadness': 0.004862236628849271, 'social_media': 0.011345218800648298, 'disappointment': 0.0, 'fun': 0.0016207455429497568, 'emotional': 0.0032414910858995136, 'positive_emotion': 0.004862236628849271, 'affection': 0.0016207455429497568}



{'love': 0.007731958762886598, 'lust': 0.002577319587628866, 'shame': 0.007731958762886598, 'sleep': 0.002577319587628866, 'anger': 0.002577319587628866, 'anonymity': 0.0, 'fear': 0.002577319587628866, 'hate': 0.005154639175257732, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.010309278350515464, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.007731958762886598, 'pain': 0.010309278350515464, 'joy': 0.0, 'healing': 0.005154639175257732, 'friends': 0.0, 'celebration': 0.002577319587628866, 'negative_emotion': 0.023195876288659795, 'sadness': 0.005154639175257732, 'social_media': 0.002577319587628866, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.002577319587628866, 'affection': 0.0}



{'love': 0.01935483870967742, 'lust': 0.0, 'shame': 0.025806451612903226, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.012903225806451613, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01935483870967742, 'pain': 0.01935483870967742, 'joy': 0.0, 'healing': 0.0, 'friends': 0.012903225806451613, 'celebration': 0.0, 'negative_emotion': 0.012903225806451613, 'sadness': 0.0, 'social_media': 0.012903225806451613, 'disappointment': 0.0, 'fun': 0.0064516129032258064, 'emotional': 0.0, 'positive_emotion': 0.0064516129032258064, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.008130081300813009, 'joy': 0.0, 'healing': 0.0, 'friends': 0.06504065040650407, 'celebration': 0.0, 'negative_emotion': 0.016260162601626018, 'sadness': 0.0, 'social_media': 0.024390243902439025, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.008130081300813009, 'positive_emotion': 0.008130081300813009, 'affection': 0.0}



{'love': 0.004909983633387889, 'lust': 0.0, 'shame': 0.004909983633387889, 'sleep': 0.009819967266775777, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0016366612111292963, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0016366612111292963, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004909983633387889, 'pain': 0.008183306055646482, 'joy': 0.0, 'healing': 0.004909983633387889, 'friends': 0.0016366612111292963, 'celebration': 0.0016366612111292963, 'negative_emotion': 0.006546644844517185, 'sadness': 0.0016366612111292963, 'social_media': 0.0032733224222585926, 'disappointment': 0.0, 'fun': 0.0032733224222585926, 'emotional': 0.0016366612111292963, 'positive_emotion': 0.008183306055646482, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.015625, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03125, 'celebration': 0.0, 'negative_emotion': 0.015625, 'sadness': 0.0, 'social_media': 0.015625, 'disappointment': 0.0, 'fun': 0.015625, 'emotional': 0.015625, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0625, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0625, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.02040816326530612, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.01048951048951049, 'lust': 0.01048951048951049, 'shame': 0.02097902097902098, 'sleep': 0.0, 'anger': 0.0034965034965034965, 'anonymity': 0.0, 'fear': 0.01048951048951049, 'hate': 0.017482517482517484, 'cheerfulness': 0.0034965034965034965, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0034965034965034965, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.02097902097902098, 'pain': 0.02097902097902098, 'joy': 0.01048951048951049, 'healing': 0.0, 'friends': 0.013986013986013986, 'celebration': 0.006993006993006993, 'negative_emotion': 0.02097902097902098, 'sadness': 0.013986013986013986, 'social_media': 0.013986013986013986, 'disappointment': 0.0, 'fun': 0.006993006993006993, 'emotional': 0.006993006993006993, 'positive_emotion': 0.017482517482517484, 'affection': 0.01048951048951049}



{'love': 0.0078125, 'lust': 0.0, 'shame': 0.015625, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0078125, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0078125, 'pain': 0.015625, 'joy': 0.0, 'healing': 0.0078125, 'friends': 0.0234375, 'celebration': 0.0, 'negative_emotion': 0.0078125, 'sadness': 0.0, 'social_media': 0.015625, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0078125, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.017543859649122806, 'lust': 0.017543859649122806, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03508771929824561, 'celebration': 0.0, 'negative_emotion': 0.017543859649122806, 'sadness': 0.0, 'social_media': 0.017543859649122806, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.014285714285714285, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.014285714285714285, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.03260869565217391, 'celebration': 0.0, 'negative_emotion': 0.010869565217391304, 'sadness': 0.0, 'social_media': 0.043478260869565216, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0078125, 'lust': 0.0, 'shame': 0.0078125, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.015625, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.015625, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.03125, 'pain': 0.015625, 'joy': 0.0, 'healing': 0.0078125, 'friends': 0.015625, 'celebration': 0.0, 'negative_emotion': 0.0234375, 'sadness': 0.0, 'social_media': 0.0078125, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0078125, 'affection': 0.0}



{'love': 0.004201680672268907, 'lust': 0.0, 'shame': 0.004201680672268907, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.004201680672268907, 'pain': 0.004201680672268907, 'joy': 0.0, 'healing': 0.004201680672268907, 'friends': 0.037815126050420166, 'celebration': 0.0, 'negative_emotion': 0.02100840336134454, 'sadness': 0.0, 'social_media': 0.012605042016806723, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.008403361344537815, 'positive_emotion': 0.004201680672268907, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0051813471502590676, 'hate': 0.0051813471502590676, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0051813471502590676, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015544041450777202, 'pain': 0.010362694300518135, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0051813471502590676, 'celebration': 0.0, 'negative_emotion': 0.025906735751295335, 'sadness': 0.0, 'social_media': 0.015544041450777202, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0051813471502590676, 'affection': 0.0}



{'love': 0.005063291139240506, 'lust': 0.0, 'shame': 0.005063291139240506, 'sleep': 0.0, 'anger': 0.002531645569620253, 'anonymity': 0.0, 'fear': 0.007594936708860759, 'hate': 0.0, 'cheerfulness': 0.002531645569620253, 'aggression': 0.002531645569620253, 'irritability': 0.002531645569620253, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.002531645569620253, 'ugliness': 0.0, 'nervousness': 0.015189873417721518, 'pain': 0.007594936708860759, 'joy': 0.0, 'healing': 0.0, 'friends': 0.010126582278481013, 'celebration': 0.002531645569620253, 'negative_emotion': 0.012658227848101266, 'sadness': 0.002531645569620253, 'social_media': 0.002531645569620253, 'disappointment': 0.0, 'fun': 0.002531645569620253, 'emotional': 0.002531645569620253, 'positive_emotion': 0.005063291139240506, 'affection': 0.0}



{'love': 0.007042253521126761, 'lust': 0.0, 'shame': 0.01056338028169014, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.007042253521126761, 'hate': 0.0035211267605633804, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.007042253521126761, 'health': 0.0, 'attractive': 0.0035211267605633804, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.014084507042253521, 'pain': 0.017605633802816902, 'joy': 0.0, 'healing': 0.0035211267605633804, 'friends': 0.017605633802816902, 'celebration': 0.0, 'negative_emotion': 0.028169014084507043, 'sadness': 0.0, 'social_media': 0.007042253521126761, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.007042253521126761, 'positive_emotion': 0.007042253521126761, 'affection': 0.0}



{'love': 0.0, 'lust': 0.01282051282051282, 'shame': 0.038461538461538464, 'sleep': 0.01282051282051282, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.01282051282051282, 'hate': 0.038461538461538464, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.01282051282051282, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.01282051282051282, 'pain': 0.038461538461538464, 'joy': 0.01282051282051282, 'healing': 0.0, 'friends': 0.01282051282051282, 'celebration': 0.0, 'negative_emotion': 0.0641025641025641, 'sadness': 0.01282051282051282, 'social_media': 0.01282051282051282, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.02564102564102564, 'positive_emotion': 0.01282051282051282, 'affection': 0.01282051282051282}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.005555555555555556, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.005555555555555556, 'negative_emotion': 0.016666666666666666, 'sadness': 0.0, 'social_media': 0.005555555555555556, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.011111111111111112, 'affection': 0.0}



{'love': 0.006493506493506494, 'lust': 0.0, 'shame': 0.006493506493506494, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.006493506493506494, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.012987012987012988, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.012987012987012988, 'pain': 0.006493506493506494, 'joy': 0.0, 'healing': 0.006493506493506494, 'friends': 0.0, 'celebration': 0.012987012987012988, 'negative_emotion': 0.025974025974025976, 'sadness': 0.012987012987012988, 'social_media': 0.006493506493506494, 'disappointment': 0.0, 'fun': 0.006493506493506494, 'emotional': 0.0, 'positive_emotion': 0.012987012987012988, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.00980392156862745, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.004901960784313725, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.004901960784313725, 'disgust': 0.0, 'ugliness': 0.004901960784313725, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.004901960784313725, 'friends': 0.00980392156862745, 'celebration': 0.00980392156862745, 'negative_emotion': 0.00980392156862745, 'sadness': 0.0, 'social_media': 0.004901960784313725, 'disappointment': 0.0, 'fun': 0.004901960784313725, 'emotional': 0.0, 'positive_emotion': 0.004901960784313725, 'affection': 0.0}



{'love': 0.010822510822510822, 'lust': 0.0, 'shame': 0.006493506493506494, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.004329004329004329, 'cheerfulness': 0.0, 'aggression': 0.0021645021645021645, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0021645021645021645, 'attractive': 0.004329004329004329, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.006493506493506494, 'pain': 0.006493506493506494, 'joy': 0.0, 'healing': 0.008658008658008658, 'friends': 0.045454545454545456, 'celebration': 0.0, 'negative_emotion': 0.006493506493506494, 'sadness': 0.0, 'social_media': 0.015151515151515152, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.03463203463203463, 'affection': 0.004329004329004329}



{'love': 0.015384615384615385, 'lust': 0.0, 'shame': 0.023076923076923078, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.007692307692307693, 'hate': 0.007692307692307693, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.015384615384615385, 'attractive': 0.007692307692307693, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.015384615384615385, 'pain': 0.023076923076923078, 'joy': 0.0, 'healing': 0.0, 'friends': 0.007692307692307693, 'celebration': 0.0, 'negative_emotion': 0.03076923076923077, 'sadness': 0.015384615384615385, 'social_media': 0.007692307692307693, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.007692307692307693, 'positive_emotion': 0.007692307692307693, 'affection': 0.023076923076923078}



{'love': 0.009259259259259259, 'lust': 0.0, 'shame': 0.009259259259259259, 'sleep': 0.0, 'anger': 0.009259259259259259, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.009259259259259259, 'irritability': 0.009259259259259259, 'breaking': 0.0, 'health': 0.009259259259259259, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.009259259259259259, 'pain': 0.018518518518518517, 'joy': 0.0, 'healing': 0.0, 'friends': 0.027777777777777776, 'celebration': 0.018518518518518517, 'negative_emotion': 0.009259259259259259, 'sadness': 0.0, 'social_media': 0.027777777777777776, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.009259259259259259, 'positive_emotion': 0.018518518518518517, 'affection': 0.0}



{'love': 0.013793103448275862, 'lust': 0.0022988505747126436, 'shame': 0.004597701149425287, 'sleep': 0.0022988505747126436, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0022988505747126436, 'hate': 0.0022988505747126436, 'cheerfulness': 0.0022988505747126436, 'aggression': 0.0022988505747126436, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.006896551724137931, 'disgust': 0.0, 'ugliness': 0.0022988505747126436, 'nervousness': 0.011494252873563218, 'pain': 0.006896551724137931, 'joy': 0.0, 'healing': 0.0022988505747126436, 'friends': 0.013793103448275862, 'celebration': 0.0022988505747126436, 'negative_emotion': 0.009195402298850575, 'sadness': 0.0, 'social_media': 0.004597701149425287, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0022988505747126436, 'positive_emotion': 0.009195402298850575, 'affection': 0.011494252873563218}



{'love': 0.006756756756756757, 'lust': 0.0, 'shame': 0.01126126126126126, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0045045045045045045, 'hate': 0.024774774774774775, 'cheerfulness': 0.0, 'aggression': 0.009009009009009009, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0045045045045045045, 'attractive': 0.0045045045045045045, 'disgust': 0.0, 'ugliness': 0.009009009009009009, 'nervousness': 0.01126126126126126, 'pain': 0.01126126126126126, 'joy': 0.0, 'healing': 0.006756756756756757, 'friends': 0.009009009009009009, 'celebration': 0.0, 'negative_emotion': 0.033783783783783786, 'sadness': 0.009009009009009009, 'social_media': 0.0045045045045045045, 'disappointment': 0.0, 'fun': 0.0022522522522522522, 'emotional': 0.02027027027027027, 'positive_emotion': 0.018018018018018018, 'affection': 0.0045045045045045045}



{'love': 0.0, 'lust': 0.0, 'shame': 0.007380073800738007, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0036900369003690036, 'fear': 0.0, 'hate': 0.01107011070110701, 'cheerfulness': 0.007380073800738007, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0036900369003690036, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0036900369003690036, 'nervousness': 0.0, 'pain': 0.007380073800738007, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0036900369003690036, 'celebration': 0.007380073800738007, 'negative_emotion': 0.007380073800738007, 'sadness': 0.0, 'social_media': 0.007380073800738007, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.007380073800738007, 'positive_emotion': 0.007380073800738007, 'affection': 0.0}



{'love': 0.011494252873563218, 'lust': 0.0, 'shame': 0.011494252873563218, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.011494252873563218, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.011494252873563218, 'health': 0.011494252873563218, 'attractive': 0.022988505747126436, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.011494252873563218, 'pain': 0.022988505747126436, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.034482758620689655, 'sadness': 0.0, 'social_media': 0.011494252873563218, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0017064846416382253, 'lust': 0.0008532423208191126, 'shame': 0.0034129692832764505, 'sleep': 0.0008532423208191126, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0017064846416382253, 'hate': 0.0017064846416382253, 'cheerfulness': 0.0008532423208191126, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0008532423208191126, 'health': 0.0008532423208191126, 'attractive': 0.0017064846416382253, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.002559726962457338, 'pain': 0.0017064846416382253, 'joy': 0.0008532423208191126, 'healing': 0.0017064846416382253, 'friends': 0.025597269624573378, 'celebration': 0.004266211604095563, 'negative_emotion': 0.010238907849829351, 'sadness': 0.002559726962457338, 'social_media': 0.005972696245733789, 'disappointment': 0.0017064846416382253, 'fun': 0.0017064846416382253, 'emotional': 0.002559726962457338, 'positive_emotion': 0.017918088737201365, 'affection': 0.0017064846416382253}



{'love': 0.009940357852882704, 'lust': 0.0, 'shame': 0.013916500994035786, 'sleep': 0.0, 'anger': 0.0019880715705765406, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.007952286282306162, 'cheerfulness': 0.0, 'aggression': 0.003976143141153081, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.007952286282306162, 'attractive': 0.0019880715705765406, 'disgust': 0.0, 'ugliness': 0.003976143141153081, 'nervousness': 0.009940357852882704, 'pain': 0.02186878727634195, 'joy': 0.0, 'healing': 0.0, 'friends': 0.003976143141153081, 'celebration': 0.0019880715705765406, 'negative_emotion': 0.015904572564612324, 'sadness': 0.0, 'social_media': 0.0019880715705765406, 'disappointment': 0.0, 'fun': 0.0019880715705765406, 'emotional': 0.009940357852882704, 'positive_emotion': 0.003976143141153081, 'affection': 0.0019880715705765406}



{'love': 0.0, 'lust': 0.0, 'shame': 0.004830917874396135, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.00966183574879227, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.004830917874396135, 'joy': 0.0, 'healing': 0.004830917874396135, 'friends': 0.024154589371980676, 'celebration': 0.0, 'negative_emotion': 0.028985507246376812, 'sadness': 0.0, 'social_media': 0.00966183574879227, 'disappointment': 0.0, 'fun': 0.004830917874396135, 'emotional': 0.004830917874396135, 'positive_emotion': 0.00966183574879227, 'affection': 0.0}



{'love': 0.0016652789342214821, 'lust': 0.0, 'shame': 0.004163197335553705, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.010824313072439634, 'cheerfulness': 0.0, 'aggression': 0.0016652789342214821, 'irritability': 0.0, 'breaking': 0.0016652789342214821, 'health': 0.002497918401332223, 'attractive': 0.002497918401332223, 'disgust': 0.0, 'ugliness': 0.0033305578684429643, 'nervousness': 0.0008326394671107411, 'pain': 0.00749375520399667, 'joy': 0.0, 'healing': 0.002497918401332223, 'friends': 0.010824313072439634, 'celebration': 0.004163197335553705, 'negative_emotion': 0.01665278934221482, 'sadness': 0.0, 'social_media': 0.002497918401332223, 'disappointment': 0.0, 'fun': 0.0008326394671107411, 'emotional': 0.002497918401332223, 'positive_emotion': 0.00832639467110741, 'affection': 0.0016652789342214821}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.008547008547008548, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.008547008547008548, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.017094017094017096, 'celebration': 0.0, 'negative_emotion': 0.017094017094017096, 'sadness': 0.0, 'social_media': 0.008547008547008548, 'disappointment': 0.008547008547008548, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.007874015748031496, 'lust': 0.0, 'shame': 0.007874015748031496, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.007874015748031496, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.007874015748031496, 'pain': 0.007874015748031496, 'joy': 0.0, 'healing': 0.007874015748031496, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.007874015748031496, 'sadness': 0.0, 'social_media': 0.007874015748031496, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.023622047244094488, 'affection': 0.0}



{'love': 0.008097165991902834, 'lust': 0.0, 'shame': 0.008097165991902834, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.004048582995951417, 'cheerfulness': 0.0, 'aggression': 0.004048582995951417, 'irritability': 0.0, 'breaking': 0.0020242914979757085, 'health': 0.0, 'attractive': 0.006072874493927126, 'disgust': 0.0, 'ugliness': 0.0020242914979757085, 'nervousness': 0.006072874493927126, 'pain': 0.006072874493927126, 'joy': 0.0, 'healing': 0.006072874493927126, 'friends': 0.010121457489878543, 'celebration': 0.004048582995951417, 'negative_emotion': 0.006072874493927126, 'sadness': 0.0020242914979757085, 'social_media': 0.0020242914979757085, 'disappointment': 0.0, 'fun': 0.0020242914979757085, 'emotional': 0.010121457489878543, 'positive_emotion': 0.008097165991902834, 'affection': 0.0020242914979757085}



{'love': 0.0, 'lust': 0.006802721088435374, 'shame': 0.006802721088435374, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.013605442176870748, 'hate': 0.006802721088435374, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.006802721088435374, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.013605442176870748, 'pain': 0.013605442176870748, 'joy': 0.006802721088435374, 'healing': 0.006802721088435374, 'friends': 0.013605442176870748, 'celebration': 0.0, 'negative_emotion': 0.02040816326530612, 'sadness': 0.006802721088435374, 'social_media': 0.013605442176870748, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.006802721088435374, 'positive_emotion': 0.013605442176870748, 'affection': 0.006802721088435374}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.024390243902439025, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.058823529411764705, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.01818181818181818, 'sadness': 0.0, 'social_media': 0.01818181818181818, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.1, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.023255813953488372, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.01818181818181818, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.01818181818181818, 'social_media': 0.01818181818181818, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.01818181818181818, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.010638297872340425, 'lust': 0.010638297872340425, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.010638297872340425, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.010638297872340425, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.010638297872340425, 'healing': 0.0, 'friends': 0.02127659574468085, 'celebration': 0.0, 'negative_emotion': 0.010638297872340425, 'sadness': 0.010638297872340425, 'social_media': 0.010638297872340425, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.010638297872340425, 'affection': 0.010638297872340425}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.016666666666666666, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.09090909090909091, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.023255813953488372, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.023255813953488372, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.023255813953488372, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.003401360544217687, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.003401360544217687, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.006802721088435374, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.003401360544217687, 'positive_emotion': 0.003401360544217687, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0392156862745098, 'celebration': 0.0, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.0196078431372549, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.00847457627118644, 'health': 0.0, 'attractive': 0.00847457627118644, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.0, 'celebration': 0.0, 'negative_emotion': 0.00847457627118644, 'sadness': 0.0, 'social_media': 0.00847457627118644, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.00847457627118644, 'positive_emotion': 0.0, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.001272264631043257, 'cheerfulness': 0.001272264631043257, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.008905852417302799, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.002544529262086514, 'celebration': 0.002544529262086514, 'negative_emotion': 0.0, 'sadness': 0.0, 'social_media': 0.015267175572519083, 'disappointment': 0.0, 'fun': 0.002544529262086514, 'emotional': 0.0, 'positive_emotion': 0.001272264631043257, 'affection': 0.0}



{'love': 0.0, 'lust': 0.0, 'shame': 0.0, 'sleep': 0.0, 'anger': 0.0, 'anonymity': 0.0, 'fear': 0.0, 'hate': 0.0, 'cheerfulness': 0.0, 'aggression': 0.0, 'irritability': 0.0, 'breaking': 0.0, 'health': 0.0, 'attractive': 0.0, 'disgust': 0.0, 'ugliness': 0.0, 'nervousness': 0.0, 'pain': 0.0, 'joy': 0.0, 'healing': 0.0, 'friends': 0.045454545454545456, 'celebration': 0.0, 'negative_emotion': 0.045454545454545456, 'sadness': 0.0, 'social_media': 0.045454545454545456, 'disappointment': 0.0, 'fun': 0.0, 'emotional': 0.0, 'positive_emotion': 0.0, 'affection': 0.0}



'''
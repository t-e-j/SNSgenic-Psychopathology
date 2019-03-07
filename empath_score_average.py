from empath import Empath
import pickle


def empath_average_values():

    total_dict = {"love" : 0.0, "lust" : 0.0, "shame" : 0.0, "sleep" : 0.0, "anger" : 0.0 , "anonymity" : 0.0, "fear" : 0.0, "hate" : 0.0,
                    "cheerfulness" : 0.0, "aggression" : 0.0, "irritability" : 0.0, "breaking" : 0.0, "health" : 0.0, "attractive" : 0.0,
                    "disgust" : 0.0, "ugliness" : 0.0, "nervousness" : 0.0, "pain" : 0.0, "joy" : 0.0, "healing" : 0.0, "friends" : 0.0,
                    "celebration" : 0.0, "negative_emotion" : 0.0, "sadness" : 0.0, "social_media" : 0.0, "disappointment" : 0.0, "fun" : 0.0,
                    "emotional" : 0.0, "positive_emotion" : 0.0, "affection" : 0.0}

    average_dict = {}

    with open("empath_non_relevant.pickle", "r") as f:
        data = pickle.load(f)

    for everyData in data:
        total_dict["love"] = total_dict["love"] + everyData["love"]
        total_dict["lust"] = total_dict["lust"] + everyData["lust"]
        total_dict["shame"] = total_dict["shame"] + everyData["shame"]
        total_dict["sleep"] = total_dict["sleep"] + everyData["sleep"]
        total_dict["anger"] = total_dict["anger"] + everyData["anger"]
        total_dict["anonymity"] = total_dict["anonymity"] + everyData["anonymity"]
        total_dict["fear"] = total_dict["fear"] + everyData["fear"]
        total_dict["hate"] = total_dict["hate"] + everyData["hate"]
        total_dict["cheerfulness"] = total_dict["cheerfulness"] + everyData["cheerfulness"]
        total_dict["aggression"] = total_dict["aggression"]+ everyData["aggression"]
        total_dict["irritability"] = total_dict["irritability"] + everyData["irritability"]
        total_dict["breaking"] = total_dict["breaking"] + everyData["breaking"]
        total_dict["health"] = total_dict["health"] + everyData["health"]
        total_dict["attractive"] = total_dict["attractive"] + everyData["attractive"]
        total_dict["disgust"] = total_dict["disgust"] + everyData["disgust"]
        total_dict["ugliness"] = total_dict["ugliness"] + everyData["ugliness"]
        total_dict["nervousness"] = total_dict["nervousness"] + everyData["nervousness"]
        total_dict["pain"] = total_dict["pain"] + everyData["pain"]
        total_dict["joy"] = total_dict["joy"] + everyData["joy"]
        total_dict["healing"] = total_dict["healing"] + everyData["healing"]
        total_dict["friends"] = total_dict["friends"] + everyData["friends"]
        total_dict["celebration"] = total_dict["celebration"] + everyData["celebration"]
        total_dict["negative_emotion"] = total_dict["negative_emotion"] + everyData["negative_emotion"]
        total_dict["sadness"] = total_dict["sadness"] + everyData["sadness"]
        total_dict["social_media"] = total_dict["social_media"] + everyData["social_media"]
        total_dict["disappointment"] = total_dict["disappointment"] + everyData["disappointment"]
        total_dict["fun"] = total_dict["fun"] + everyData["fun"]
        total_dict["emotional"] = total_dict["emotional"] + everyData["emotional"]
        total_dict["positive_emotion"] = total_dict["positive_emotion"] + everyData["positive_emotion"]
        total_dict["affection"] = total_dict["affection"] + everyData["affection"]

    # print ("total_love =" + str(total_love))
    # print ("total_lust =" + str(total_lust))
    # print ("total_shame =" + str(total_shame))
    # print ("total_sleep =" + str(total_sleep))
    # print ("total_anger =" + str(total_anger))
    # print ("total_anonymity =" + str(total_anonymity))
    # print ("total_fear =" + str(total_fear))
    # print ("total_hate =" + str(total_hate))
    # print ("total_cheerfulness =" + str(total_cheerfulness))
    # print ("total_aggression =" + str(total_aggression))
    # print ("total_irritability =" + str(total_irritability))
    # print ("total_breaking =" + str(total_breaking))
    # print ("total_health =" + str(total_health))
    # print ("total_attractive =" + str(total_attractive))
    # print ("total_disgust =" + str(total_disgust))
    # print ("total_ugliness =" + str(total_ugliness))
    # print ("total_nervousness =" + str(total_nervousness))
    # print ("total_pain =" + str(total_pain))
    # print ("total_joy =" + str(total_joy))
    # print ("total_healing =" + str(total_healing))
    # print ("total_friends =" + str(total_friends))
    # print ("total_celebration =" + str(total_celebration))
    # print ("total_negative_emotion =" + str(total_negative_emotion))
    # print ("total_sadness =" + str(total_sadness))
    # print ("total_social_media =" + str(total_social_media))
    # print ("total_disappointment =" + str(total_disappointment))
    # print ("total_fun =" + str(total_fun))
    # print ("total_emotional =" + str(total_emotional))
    # print ("total_positive_emotion =" + str(total_positive_emotion))
    # print ("total_affection =" + str(total_affection))

    print ("\n\n Total values :")
    print total_dict

    print ("\n\n As values are too small multiplying by 100 and getting average for number of authors i.e. 20")

    for everyKey,everyValue in total_dict.items():
        average_dict[everyKey] = total_dict[everyKey] * 1000 / 1322

    print ("\n\n Average values :")
    print average_dict

    # print ("average_love =" + str(total_love * 5))
    # print ("average_lust =" + str(total_lust * 5))
    # print ("average_shame =" + str(total_shame * 5))
    # print ("average_sleep =" + str(total_sleep * 5))
    # print ("average_anger =" + str(total_anger * 5))
    # print ("average_anonymity =" + str(total_anonymity * 5))
    # print ("average_fear =" + str(total_fear * 5))
    # print ("average_hate =" + str(total_hate * 5))
    # print ("average_cheerfulness =" + str(total_cheerfulness * 5))
    # print ("average_aggression =" + str(total_aggression * 5))
    # print ("average_irritability =" + str(total_irritability * 5))
    # print ("average_breaking =" + str(total_breaking * 5))
    # print ("average_health =" + str(total_health * 5))
    # print ("average_attractive =" + str(total_attractive * 5))
    # print ("average_disgust =" + str(total_disgust * 5))
    # print ("average_ugliness =" + str(total_ugliness * 5))
    # print ("average_nervousness =" + str(total_nervousness * 5))
    # print ("average_pain =" + str(total_pain * 5))
    # print ("average_joy =" + str(total_joy * 5))
    # print ("average_healing =" + str(total_healing * 5))
    # print ("average_friends =" + str(total_friends * 5))
    # print ("average_celebration =" + str(total_celebration * 5))
    # print ("average_negative_emotion =" + str(total_negative_emotion * 5))
    # print ("average_sadness =" + str(total_sadness * 5))
    # print ("average_social_media =" + str(total_social_media * 5))
    # print ("average_disappointment =" + str(total_disappointment * 5))
    # print ("average_fun =" + str(total_fun * 5))
    # print ("average_emotional =" + str(total_emotional * 5))
    # print ("average_positive_emotion =" + str(total_positive_emotion * 5))
    # print ("average_affection =" + str(total_affection * 5))


def main():
    """ create a database connection to a SQLite database """
    # conn = sqlite3.connect("submissions.db")

    empath_average_values()
    # conn.commit()
    # conn.close()


if __name__ == "__main__":
    # calling main function
    main()



##############################################


'''

relevant count = 245

non relevant count= 1322


Result :

Relevant :

 Total values :
{'love': 1.0926993483570726, 'lust': 0.3572854156196608, 'shame': 1.138887987558708, 'sleep': 0.2681766915830847, 'anger': 0.20481265594136658,
 'anonymity': 0.08789739630440076, 'fear': 0.4822743563641124, 'hate': 0.9952846566896562, 'cheerfulness': 0.15940807724648343, 
 'aggression': 0.2598881467436565, 'irritability': 0.06845190969000248, 'breaking': 0.2895825403472196, 'health': 0.5368615919525782, 
 'attractive': 0.6416647386645272, 'disgust': 0.1308063421381061, 'ugliness': 0.4815796345198831, 'nervousness': 1.0715371615412033, 
 'pain': 1.3578868974565936, 'joy': 0.1744538208010907, 'healing': 0.39524514973798225, 'friends': 2.609842467794085, 
 'celebration': 0.6136768030895642, 'negative_emotion': 2.7027912874919426, 'sadness': 0.6984885393472042, 'social_media': 4.59264061687002, 
 'disappointment': 0.10576235338071291, 'fun': 0.49011729343715477, 'emotional': 0.683775325697792, 'positive_emotion': 1.6674570245486962, 
 'affection': 0.3343387921358123}


 As values are too small multiplying by 100 and getting average for number of authors i.e. 20

 Average values :
{'love': 5.463496741785363, 'lust': 1.786427078098304, 'shame': 5.69443993779354, 'sleep': 1.3408834579154236, 'anger': 1.024063279706833,
 'anonymity': 0.4394869815220038, 'fear': 2.411371781820562, 'hate': 4.97642328344828, 'cheerfulness': 0.7970403862324171, 
 'aggression': 1.2994407337182825, 'irritability': 0.3422595484500124, 'breaking': 1.447912701736098, 'health': 2.684307959762891,
  'attractive': 3.2083236933226362, 'disgust': 0.6540317106905305, 'ugliness': 2.4078981725994155, 'nervousness': 5.357685807706016, 
  'pain': 6.789434487282968, 'joy': 0.8722691040054535, 'healing': 1.9762257486899113, 'friends': 13.049212338970424, 'celebration': 3.068384015447821, 
  'negative_emotion': 13.513956437459713, 'sadness': 3.4924426967360214, 'social_media': 22.963203084350102, 'disappointment': 0.5288117669035646, 
  'fun': 2.450586467185774, 'emotional': 3.41887662848896, 'positive_emotion': 8.33728512274348, 'affection': 1.6716939606790615}

Non-relevant :

 Total values :
{'love': 3.260512697961849, 'lust': 0.5692249612005897, 'shame': 3.7475521912780314, 'sleep': 0.7555694487005642, 'anger': 0.48394665487755495, 
'anonymity': 0.1112789859425688, 'fear': 1.9891768068874212, 'hate': 4.875999145269467, 'cheerfulness': 0.3921926305011721, 
'aggression': 1.1386896540100804, 'irritability': 0.33660108853743625, 'breaking': 1.212592093378144, 'health': 2.0041192689759226, 
'attractive': 2.662895635165805, 'disgust': 0.4219153633827512, 'ugliness': 3.8322505119532315, 'nervousness': 3.7890892189774004, 
'pain': 4.760379043575385, 'joy': 0.30568002976631453, 'healing': 1.5623070349443735, 'friends': 5.2238850482714625, 
'celebration': 3.3628857855670446, 'negative_emotion': 12.164188989189949, 'sadness': 1.954546807674255, 'social_media': 0.0, 
'disappointment': 0.18168963266576588, 'fun': 1.796592639996581, 'emotional': 2.8713508440664532, 'positive_emotion': 6.342722349033068, 
'affection': 1.3429587211964436}

 As values are too small multiplying by 100 and getting average for number of authors i.e. 20

 Average values :
{'love': 16.302563489809245, 'lust': 2.8461248060029485, 'shame': 18.737760956390158, 'sleep': 3.777847243502821, 'anger': 2.4197332743877746,
 'anonymity': 0.556394929712844, 'fear': 9.945884034437105, 'hate': 24.379995726347335, 'cheerfulness': 1.9609631525058604, 
 'aggression': 5.693448270050402, 'irritability': 1.6830054426871812, 'breaking': 6.06296046689072, 'health': 10.020596344879614, 
 'attractive': 13.314478175829025, 'disgust': 2.109576816913756, 'ugliness': 19.161252559766158, 'nervousness': 18.945446094887004, 
 'pain': 23.801895217876925, 'joy': 1.5284001488315726, 'healing': 7.811535174721867, 'friends': 26.119425241357312, 
 'celebration': 16.814428927835223, 'negative_emotion': 60.82094494594975, 'sadness': 9.772734038371274, 'social_media': 0.0, 
 'disappointment': 0.9084481633288294, 'fun': 8.982963199982905, 'emotional': 14.356754220332267, 'positive_emotion': 31.71361174516534, 
 'affection': 6.7147936059822175}




'''



'''

average on basis of number of posts:

 Total values :
{'love': 1.0926993483570726, 'lust': 0.3572854156196608, 'shame': 1.138887987558708, 'sleep': 0.2681766915830847, 'anger': 0.20481265594136658,
 'anonymity': 0.08789739630440076, 'fear': 0.4822743563641124, 'hate': 0.9952846566896562, 'cheerfulness': 0.15940807724648343, 
 'aggression': 0.2598881467436565, 'irritability': 0.06845190969000248, 'breaking': 0.2895825403472196, 'health': 0.5368615919525782, 
 'attractive': 0.6416647386645272, 'disgust': 0.1308063421381061, 'ugliness': 0.4815796345198831, 'nervousness': 1.0715371615412033, 
 'pain': 1.3578868974565936, 'joy': 0.1744538208010907, 'healing': 0.39524514973798225, 'friends': 2.609842467794085,
  'celebration': 0.6136768030895642, 'negative_emotion': 2.7027912874919426, 'sadness': 0.6984885393472042, 'social_media': 4.59264061687002,
   'disappointment': 0.10576235338071291, 'fun': 0.49011729343715477, 'emotional': 0.683775325697792, 'positive_emotion': 1.6674570245486962,
    'affection': 0.3343387921358123}

 As values are too small multiplying by 1000 and getting average for number of posts i.e. 245

 Average values :
{'love': 4.45999734023295, 'lust': 1.4583078188557583, 'shame': 4.648522398198808, 'sleep': 1.0945987411554479, 'anger': 0.8359700242504758, 
'anonymity': 0.3587648828751051, 'fear': 1.9684667606698465, 'hate': 4.062386353835331, 'cheerfulness': 0.6506452132509528, 
'aggression': 1.0607679458924757, 'irritability': 0.27939554975511216, 'breaking': 1.181969552437631, 'health': 2.1912718038880743, 
'attractive': 2.6190397496511317, 'disgust': 0.5339034372983922, 'ugliness': 1.9656311613056454, 'nervousness': 4.373621067515115, 
'pain': 5.542395499822831, 'joy': 0.7120564114330232, 'healing': 1.6132455091346216, 'friends': 10.652418235894224, 'celebration': 2.5048032779165883,
 'negative_emotion': 11.0318011734365, 'sadness': 2.8509736299885886, 'social_media': 18.74547190559192, 'disappointment': 0.431683075023318, 
 'fun': 2.0004787487230806, 'emotional': 2.7909196967256817, 'positive_emotion': 6.80594703897427, 'affection': 1.3646481311665808}

 Total values :
{'love': 3.260512697961849, 'lust': 0.5692249612005897, 'shame': 3.7475521912780314, 'sleep': 0.7555694487005642, 'anger': 0.48394665487755495,
 'anonymity': 0.1112789859425688, 'fear': 1.9891768068874212, 'hate': 4.875999145269467, 'cheerfulness': 0.3921926305011721, 
 'aggression': 1.1386896540100804, 'irritability': 0.33660108853743625, 'breaking': 1.212592093378144, 'health': 2.0041192689759226, 
 'attractive': 2.662895635165805, 'disgust': 0.4219153633827512, 'ugliness': 3.8322505119532315, 'nervousness': 3.7890892189774004, 
 'pain': 4.760379043575385, 'joy': 0.30568002976631453, 'healing': 1.5623070349443735, 'friends': 5.2238850482714625, 
 'celebration': 3.3628857855670446, 'negative_emotion': 12.164188989189949, 'sadness': 1.954546807674255, 'social_media': 0.0, 
 'disappointment': 0.18168963266576588, 'fun': 1.796592639996581, 'emotional': 2.8713508440664532, 'positive_emotion': 6.342722349033068, 
 'affection': 1.3429587211964436}

 As values are too small multiplying by 1000 and getting average for number of posts i.e. 1322
 Average values :
{'love': 2.466348485598978, 'lust': 0.430578639334788, 'shame': 2.834759600059025, 'sleep': 0.5715351351744056, 
'anger': 0.36607159975609305, 'anonymity': 0.08417472461616399, 'fear': 1.5046723198845848, 'hate': 3.6883503368150277, 
'cheerfulness': 0.2966661350235795, 'aggression': 0.8613386187670805, 'irritability': 0.2546150442794526, 'breaking': 0.9172406152633464, 
'health': 1.515975241282846, 'attractive': 2.0142932187335894, 'disgust': 0.31914929151494037, 'ugliness': 2.8988279212959394, 
'nervousness': 2.866179439468533, 'pain': 3.6008918635214715, 'joy': 0.23122543855243158, 'healing': 1.1817753668263038, 
'friends': 3.9515015493732695, 'celebration': 2.5437865246346782, 'negative_emotion': 9.20135324447046, 'sadness': 1.4784771616295422, 
'social_media': 0.0, 'disappointment': 0.1374354256170695, 'fun': 1.3589959455344789, 'emotional': 2.171974919868724, 
'positive_emotion': 4.797823259480384, 'affection': 1.0158537981818787}

'''


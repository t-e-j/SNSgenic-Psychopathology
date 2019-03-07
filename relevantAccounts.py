# get relevant comments- submission ids from data

import pickle

allAnnotationsTejasvi = ["tejasvi0_annotations.pickle",
                  "tejasvi0b_annotations.pickle",
                  "tejasvi100_annotations.pickle",
                  "tejasvi100b_annotations.pickle",
                  "tejasvi150_annotations.pickle",
                  "tejasvi150b_annotations.pickle",
                  "tejasvi200_annotations.pickle",
                  "tejasvi200b_annotations.pickle",
                  "tejasvi250_annotations.pickle",
                  "tejasvi250b_annotations.pickle",
                  "tejasvi300_annotations.pickle",
                  "tejasvi350_annotations.pickle",
                  "tejasvi400_annotations.pickle",
                  "tejasvi50_annotations.pickle",
                  "tejasvi50b_annotations.pickle"]

submissionIDTejasvi = []
relevantAuthors = []
for j in allAnnotationsTejasvi:

    with open(j) as f : annotations = pickle.load(f)

    i = 0
    while i < len(annotations):
        if annotations.values()[i]== 'y':
             submissionIDTejasvi.append(annotations.keys()[i])                 # get list of all relevant submission IDs
        i = i+1

# print submissionID
with open("tejasvi.pickle") as f : data = pickle.load(f)
for i,entry in enumerate(data["separate"]):
    #print "\n\n\n"
    # id = entry["submission_id"]
    if entry["submission_id"] in submissionIDTejasvi :
        relevantAuthors.append(entry["author"])
   #print entry
   # print entry["submission_id"]
   # print entry["submission_body"]
print "Done with Tejasvi!"


allAnnotations1 = ["kriti0_common_annotations.pickle",
                       "kriti100_common_annotations.pickle",
                       "kriti150_common_annotations.pickle",
                       "kriti200_common_annotations.pickle",
                       "kriti250_common_annotations.pickle",
                       "kriti300_common_annotations.pickle",
                       "kriti350_common_annotations.pickle",
                       "kriti400_common_annotations.pickle",
                       "kriti450_common_annotations.pickle",
                       "kriti50_common_annotations.pickle",
                       "kriti_common_annotations.pickle"]

submissionID1 = []
for j in allAnnotations1:

    with open(j) as f : annotations1 = pickle.load(f)

    i = 0
    while i < len(annotations1):
        if annotations1.values()[i]== 'y':
             submissionID1.append(annotations1.keys()[i])                 # get list of all relevant submission IDs
        i = i+1

# print submissionID

### collecting for common data
with open("kriti.pickle") as f : data = pickle.load(f)
for i,entry in enumerate(data["common"]):
    #print "\n\n\n"
    # id = entry["submission_id"]
    if entry["submission_id"] in submissionID1 :
         relevantAuthors.append(entry["author"])                    # get list of all relevant authors

###### collecting for separate data
# with open("kriti.pickle") as f : data = pickle.load(f)
# for i,entry in enumerate(data["separate"]):
#     #print "\n\n\n"
#     # id = entry["submission_id"]
#     if entry["submission_id"] in submissionID1 :
#          relevantAuthors.append(entry["author"])

print "done!"
#
# print "Printing relevant authors!"
# print relevantAuthors

submissionID2 = []


with open("john_common_annotations.pickle") as f : annotations2 = pickle.load(f)

i = 0
while i < len(annotations2):
    if annotations2.values()[i]== 'y':
        submissionID2.append(annotations2.keys()[i])                 # get list of all relevant submission IDs
    i = i+1

# print submissionID

### collecting for common data
with open("john.pickle") as f : data = pickle.load(f)
for i,entry in enumerate(data["common"]):
    #print "\n\n\n"
    # id = entry["submission_id"]
    if entry["submission_id"] in submissionID2 :
         relevantAuthors.append(entry["author"])          # get list of all relevant authors

###### collecting for separate data
# with open("john.pickle") as f : data = pickle.load(f)
# for i,entry in enumerate(data["separate"]):
#     #print "\n\n\n"
#     # id = entry["submission_id"]
#     if entry["submission_id"] in submissionID2 :
#          relevantAuthors.append(entry["author"])

print "Printing relevant submission ID of Tejasvi"
# print submissionIDTejasvi
print len(submissionIDTejasvi)

print "Printing pending relevant submission ID"
# print submissionID1, submissionID2
print len(submissionID1)
print len(submissionID2)

print "Printing relevant authors!"
print relevantAuthors
print len(relevantAuthors)

###############################################################

'''
Relevant authors
=================

[u'Wred27', u'jllxxp', u'expressivewords', u'miriamurphy', u'MyLifelines', u'PRS501', u'bikramxo', u'idontknowanymore3500',
 u'wh3reismym1nd', u'Lazentro', u'TheRealTayler', u'Zorkats1', u'stereotypicalbritish', u'Runechi', u'Onikouzou', 
 u'9754213680632', u'CanNotLiveLikeThis', u'Snedwardowden', u'jxseyrae_', u'SadiMasta', u'Shadowing234', u'Violetsuger', 
 u'dragonwarrior09', u'4dolfin', u'Jaybo78', u'jakey3209', u'ruckanoise88', u'mertensmen14', u'myusernamebeatsyours', u'Joesuds', 
 u'albundy12345', u'spooky-mermaid', u'dkjones05', u'velociraptor94', u'likeroscoe', u'Radoslaw76', u'AVZ_Gone', u'No1stupid', 
 u'ProfessorTurtlez', u'large255', u'jhmillard', u'Flowersformybutt', u'campycynic', u'kisyy', u'spagootinurpoot', u'MrRebornX', 
 u'turbochickenkiev', u'bluegrassinthebreeze', u'blenda_mae', u'VroomBrapBrap', u'liam_a1', u'imthepotatoqueen', u'Tettrabyte',
  u'turbochickenkiev', u'SPD87', u'isolatedesolate', u'JillyBoel69', u'pakelis_vafliuku', u'KastMigVaek', u'MinimalSass',
   u'warners919', u'DoSexTheConspiracy', u'VioletteRose29', u'bookloverphile', u'undercover_intern', u'hellohereiamok', u'Anxmess',
    u'LolaIsLoud', u'Ds3y', u'meiniemoon', u'throwaway0817161616', u'paynexkiller', u'fifimcg', u'agoldfish378', u'jockcel',
     u'burritos4me', u'waitingdaisy', u'quirilon', u'LivelyWallflower', u'klotzonater420', u'TheSaltySeaDog22', u'riot-nerf-red-buff',
      u'Webimpulse', u'ayesmyownaccount', u'KnowThat205', u'thatshawtyp', u'OldManoftheNorth', u'VolgaSvetlana', u'oIndiex', 
      u'69SaggyButtCheeks69', u'andrewerdna100', u'corvith', u'IsAFailure', u'YoIGotASoulVoice', u'neurosthetic', u'wheresmyadventure',
       u'AhoyThereFancypants', u'ashleyoglesby', u'Mazzy1978', u'tristdog27', u'AnonymousButterfly01', u'DeadHands26',
        u'caillou_getsgrounded', u'mitsukiowl', u'anyc84_m', u'Damn_Madame', u'cuernodechivos2', u'BotFarm_drone1134', u'X_Dragonkill',
         u'glowigoo88', u'OldManoftheNorth', u'TeacherJuana', u'lonesomesoul95', u'an_on_ym_ou_s', u'adannytoremember', u'BAJJAB001',
          u'Throwaway124522', u'dVNsp', u'honey2190', u'WinterWitch89', u'Zephandrypus', u'equilibrium21', u'fasttradeboyman', 
          u'moomooboo', u'Lily1018', u'Eric2517', u'hauntedhillswhore', u'Ganxious', u'MelonyHope', u'pinkgirlystuffjody', 
          u'Bronzehawkattack', u'cobo3388', u'piyopyoko', u'sicaspeak', u'PorSiempreSolo', u'Cri1654', u'CinnamonThePig',
           u'AdvancedFish', u'peeblicity', u'Ivoriy', u'PanTostadoo', u'BestOldExFriendRay', u'bulldozer9999999999', u'jefflucas',
            u'SilentHuman', u'rayj33', u'macproafro', u'Carpbeat24', u'RnLraep', u'redfern962', u'7_Pixel_7', u'throwaway19941984', 
            u'minusman652', u'HandMeMyThinkingPipe', u'AbstrakThought', u'Kookie_212', u'bellavita1577', u'LogiCparty', u'SPD87',
             u'ShittyNoodle', u'jdawg7780', u'seeingwishes', u'ekek26', u'reallyloudcrier', u'playingtricksonme', u'Zedevile', 
             u'undercovur', u'scryptx', u'Jellolmao124', u'ratcatching', u'KriegRipper', u'Faithlee26', u'IAmTheScarBrother', 
             u'mostdietwater', u'herolance', u'TimorousCharles', u'danielmann862', u'furmthewurm', u'studentstudylife', u'Gtj_2036',
              u'JohnV318', u'anonymous4226', u'dannythfc', u'kwassa7', u'Millennial_Ennui', u'Nocturnalonerr', u'satuza', u'thegamerrr',
               u'kumadoki', u'HerThoughts88', u'keepit-ethereal', u'Messedupmesss', u'Soopa_dude', u'grossko19', u'RedishZipper', 
               u'notoriousOLG', u'jamlesstoast', u'Damn_Madame', u'cuernodechivos2', u'BotFarm_drone1134', u'glowigoo88', u'OldManoftheNorth', 
               u'khaledur01', u'an_on_ym_ou_s', u'subcuta', u'tar4ntula', u'BAJJAB001', u'EDPostRequests', u'jibberjabbery', u'nehway', 
               u'Throwaway124522', u'haymansafc', u'Encoraskrc', u'Zephandrypus', u'Mohankumar12345', u'robuttnikinin', u'moldybritches',
                u'Ge0rgeBr0ughton', u'moomooboo', u'selfdxaries', u'Lily1018', u'Eric2517', u'hauntedhillswhore', u'Ganxious', u'MelonyHope',
                 u'FeelThePower999', u'elton_johns_glasses', u'piyopyoko', u'PorSiempreSolo', u'Cri1654', u'AdvancedFish', u'Cheesycreature', 
                 u'kenndot', u'Ivoriy', u'PanTostadoo', u'speak721', u'hesback_inpogform', u'BestOldExFriendRay', u'jefflucas', u'SilentHuman',
                  u'Angle-of-depression', u'macproafro', u'Shanbae', u'AgitatedAdvantage', u'is_reddit_useful', u'Carpbeat24', u'RnLraep', 
                  u'redfern962', u'7_Pixel_7', u'felipe5083', u'WellDeserved101', u'minusman652', u'HandMeMyThinkingPipe', u'AbstrakThought',
                   u'Kookie_212']

'''


# "Wred27"
# "jllxxp"
# "expressivewords"
# "miriamurphy"
# "MyLifelines"
# "PRS501"
# "bikramxo"
# idontknowanymore3500
# wh3reismym1nd
# Lazentro
# TheRealTayler
# Zorkats1
# stereotypicalbritish
# Runechi
# Onikouzou
# 9754213680632
# CanNotLiveLikeThis
# Snedwardowden
# jxseyrae_
# SadiMasta
# Shadowing234
# Violetsuger
# dragonwarrior09
# 4dolfin
# Jaybo78
# jakey3209
# ruckanoise88
# mertensmen14
# myusernamebeatsyours
# Joesuds
# albundy12345
# spooky-mermaid
# dkjones05
# velociraptor94
# likeroscoe
# Radoslaw76
# AVZ_Gone
# No1stupid
# ProfessorTurtlez
# large255
# jhmillard
# Flowersformybutt
# campycynic
# kisyy
# spagootinurpoot
# MrRebornX
# turbochickenkiev
# bluegrassinthebreeze
# blenda_mae
# VroomBrapBrap
# liam_a1
# imthepotatoqueen
# Tettrabyte
# turbochickenkiev
# SPD87
# isolatedesolate
# JillyBoel69
# pakelis_vafliuku
# KastMigVaek
# MinimalSass
# warners919
# DoSexTheConspiracy
# VioletteRose29
# bookloverphile
# undercover_intern
# hellohereiamok
# Anxmess
# LolaIsLoud
# Ds3y
# meiniemoon
# throwaway0817161616
# paynexkiller
# fifimcg
# agoldfish378
# jockcel
# burritos4me
# waitingdaisy
# quirilon
# LivelyWallflower
# klotzonater420
# TheSaltySeaDog22
# riot-nerf-red-buff
# Webimpulse
# ayesmyownaccount
# KnowThat205
# thatshawtyp
# OldManoftheNorth
# VolgaSvetlana
# oIndiex
# 69SaggyButtCheeks69
# andrewerdna100
# corvith
# IsAFailure
# YoIGotASoulVoice
# neurosthetic
# wheresmyadventure
# AhoyThereFancypants
# ashleyoglesby
# Mazzy1978
# tristdog27
# AnonymousButterfly01
# DeadHands26
# Done with Tejasvi!
# caillou_getsgrounded
# mitsukiowl
# anyc84_m
# Damn_Madame
# cuernodechivos2
# BotFarm_drone1134
# X_Dragonkill
# glowigoo88
# OldManoftheNorth
# TeacherJuana
# lonesomesoul95
# an_on_ym_ou_s
# adannytoremember
# BAJJAB001
# Throwaway124522
# dVNsp
# honey2190
# WinterWitch89
# Zephandrypus
# equilibrium21
# fasttradeboyman
# moomooboo
# Lily1018
# Eric2517
# hauntedhillswhore
# Ganxious
# MelonyHope
# pinkgirlystuffjody
# Bronzehawkattack
# cobo3388
# piyopyoko
# sicaspeak
# PorSiempreSolo
# Cri1654
# CinnamonThePig
# AdvancedFish
# peeblicity
# Ivoriy
# PanTostadoo
# BestOldExFriendRay
# bulldozer9999999999
# jefflucas
# SilentHuman
# rayj33
# macproafro
# Carpbeat24
# RnLraep
# redfern962
# 7_Pixel_7
# throwaway19941984
# minusman652
# HandMeMyThinkingPipe
# AbstrakThought
# Kookie_212
# bellavita1577
# LogiCparty
# SPD87
# ShittyNoodle
# jdawg7780
# seeingwishes
# ekek26
# reallyloudcrier
# playingtricksonme
# Zedevile
# undercovur
# scryptx
# Jellolmao124
# ratcatching
# KriegRipper
# Faithlee26
# IAmTheScarBrother
# mostdietwater
# herolance
# TimorousCharles
# danielmann862
# furmthewurm
# studentstudylife
# Gtj_2036
# JohnV318
# anonymous4226
# dannythfc
# kwassa7
# Millennial_Ennui
# Nocturnalonerr
# satuza
# thegamerrr
# kumadoki
# HerThoughts88
# keepit-ethereal
# Messedupmesss
# Soopa_dude
# grossko19
# RedishZipper
# notoriousOLG
# jamlesstoast



#
# select author, subreddit, count(*) from dayAverageSubmissions where author in ("Wred27", "jllxxp", "expressivewords", "miriamurphy", "MyLifelines",
#                                                                                "PRS501", "bikramxo", "idontknowanymore3500", "wh3reismym1nd",
#                                                                                "Lazentro", "TheRealTayler",  "Zorkats1", "stereotypicalbritish",
#                                                                                "Runechi", "Onikouzou", "9754213680632", "CanNotLiveLikeThis",
#                                                                                "Snedwardowden", "jxseyrae_", "SadiMasta", "Shadowing234",
#                                                                                "Violetsuger", "dragonwarrior09","4dolfin", "Jaybo78",
#                                                                                "jakey3209", "ruckanoise88", "mertensmen14", "myusernamebeatsyours",
#                                                                                "Joesuds", "albundy12345", "spooky-mermaid", "dkjones05",
#                                                                                "velociraptor94", "likeroscoe", "Radoslaw76", "AVZ_Gone",
#                                                                                "No1stupid", "ProfessorTurtlez", "large255", "jhmillard",
#                                                                                "Flowersformybutt", "campycynic", "kisyy", "spagootinurpoot",
#                                                                                "MrRebornX", "turbochickenkiev", "bluegrassinthebreeze",
#                                                                                "blenda_mae", "VroomBrapBrap", "liam_a1", "imthepotatoqueen",
#                                                                                "Tettrabyte", "turbochickenkiev", "SPD87", "isolatedesolate",
#                                                                                "JillyBoel69", "pakelis_vafliuku", "KastMigVaek", "MinimalSass",
#                                                                                "warners919", "DoSexTheConspiracy", "VioletteRose29", "bookloverphile",
#                                                                                "undercover_intern", "hellohereiamok", "Anxmess", "LolaIsLoud",
#                                                                                "Ds3y", "meiniemoon", "throwaway0817161616", "paynexkiller", "fifimcg",
#                                                                                "agoldfish378", "jockcel", "burritos4me", "waitingdaisy", "quirilon",
#                                                                                "LivelyWallflower", "klotzonater420", "TheSaltySeaDog22",
#                                                                                "riot-nerf-red-buff", "Webimpulse", "ayesmyownaccount", "KnowThat205",
#                                                                                "thatshawtyp", "OldManoftheNorth", "VolgaSvetlana", "oIndiex",
#                                                                                "69SaggyButtCheeks69", "andrewerdna100", "corvith", "IsAFailure",
#                                                                                "YoIGotASoulVoice", "neurosthetic", "wheresmyadventure",
#                                                                                "AhoyThereFancypants", "ashleyoglesby", "Mazzy1978", "tristdog27",
#                                                                                "AnonymousButterfly01", "DeadHands26", "caillou_getsgrounded",
#                                                                                "mitsukiowl", "anyc84_m", "Damn_Madame", "cuernodechivos2",
#                                                                                "BotFarm_drone1134", "X_Dragonkill", "glowigoo88", "OldManoftheNorth",
#                                                                                "TeacherJuana", "lonesomesoul95", "an_on_ym_ou_s", "adannytoremember",
#                                                                                "BAJJAB001", "Throwaway124522", "dVNsp", "honey2190", "WinterWitch89",
#                                                                                "Zephandrypus", "equilibrium21", "fasttradeboyman", "moomooboo",
#                                                                                "Lily1018","Eric2517","hauntedhillswhore","Ganxious","MelonyHope",
#                                                                                "pinkgirlystuffjody", "Bronzehawkattack", "cobo3388", "piyopyoko",
#                                                                                "sicaspeak", "PorSiempreSolo", "Cri1654", "CinnamonThePig",
#                                                                                "AdvancedFish", "peeblicity", "Ivoriy", "PanTostadoo",
#                                                                                "BestOldExFriendRay", "bulldozer9999999999", "jefflucas",
#                                                                                "SilentHuman", "rayj33", "macproafro", "Carpbeat24", "RnLraep",
#                                                                                "redfern962", "7_Pixel_7", "throwaway19941984", "minusman652",
#                                                                                "HandMeMyThinkingPipe", "AbstrakThought","Kookie_212","bellavita1577",
#                                                                                "LogiCparty","SPD87","ShittyNoodle","jdawg7780","seeingwishes",
#                                                                                "ekek26","reallyloudcrier","playingtricksonme","Zedevile",
#                                                                                "undercovur","scryptx","Jellolmao124","ratcatching","KriegRipper",
#                                                                                "Faithlee26","IAmTheScarBrother","mostdietwater","herolance",
#                                                                                "TimorousCharles","danielmann862","furmthewurm","studentstudylife",
#                                                                                "Gtj_2036","JohnV318","anonymous4226","dannythfc","kwassa7",
#                                                                                "Millennial_Ennui","Nocturnalonerr","satuza","thegamerrr",
#                                                                                "kumadoki","HerThoughts88","keepit-ethereal","Messedupmesss",
#                                                                                "Soopa_dude", "grossko19", "RedishZipper", "notoriousOLG",
#                                                                                "jamlesstoast") group by author,subreddit;


select author, subreddit, count(*) from dayAverageSubmissions where author in ('Wred27', 'jllxxp', 'expressivewords', 'miriamurphy', 'MyLifelines',
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
                                                                               'MelonyHope', 'pinkgirlystuffjody',  'Bronzehawkattack', 'cobo3388',
                                                                               'piyopyoko', 'sicaspeak', 'PorSiempreSolo', 'Cri1654', 'CinnamonThePig',
                                                                               'AdvancedFish', 'peeblicity', 'Ivoriy', 'PanTostadoo',
                                                                               'BestOldExFriendRay', 'bulldozer9999999999', 'jefflucas', 'SilentHuman',
                                                                               'rayj33', 'macproafro', 'Carpbeat24', 'RnLraep', 'redfern962',
                                                                               '7_Pixel_7', 'throwaway19941984', 'minusman652', 'HandMeMyThinkingPipe',
                                                                               'AbstrakThought', 'Kookie_212', 'bellavita1577', 'LogiCparty',
                                                                               'SPD87',  'ShittyNoodle', 'jdawg7780', 'seeingwishes', 'ekek26',
                                                                               'reallyloudcrier', 'playingtricksonme', 'Zedevile', 'undercovur',
                                                                               'scryptx', 'Jellolmao124', 'ratcatching', 'KriegRipper', 'Faithlee26',
                                                                               'IAmTheScarBrother', 'mostdietwater', 'herolance', 'TimorousCharles',
                                                                               'danielmann862', 'furmthewurm', 'studentstudylife', 'Gtj_2036',
                                                                               'JohnV318', 'anonymous4226', 'dannythfc', 'kwassa7', 'Millennial_Ennui',
                                                                               'Nocturnalonerr', 'satuza', 'thegamerrr',  'kumadoki', 'HerThoughts88',
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
                                                                               'Carpbeat24', 'RnLraep',  'redfern962', '7_Pixel_7', 'felipe5083',
                                                                               'WellDeserved101', 'minusman652', 'HandMeMyThinkingPipe',
                                                                               'AbstrakThought', 'Kookie_212') group by author,subreddit;



select * from dayAverageSubmissions where author in ('Wred27', 'jllxxp', 'expressivewords', 'miriamurphy', 'MyLifelines',
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
                                                                               'MelonyHope', 'pinkgirlystuffjody',  'Bronzehawkattack', 'cobo3388',
                                                                               'piyopyoko', 'sicaspeak', 'PorSiempreSolo', 'Cri1654', 'CinnamonThePig',
                                                                               'AdvancedFish', 'peeblicity', 'Ivoriy', 'PanTostadoo',
                                                                               'BestOldExFriendRay', 'bulldozer9999999999', 'jefflucas', 'SilentHuman',
                                                                               'rayj33', 'macproafro', 'Carpbeat24', 'RnLraep', 'redfern962',
                                                                               '7_Pixel_7', 'throwaway19941984', 'minusman652', 'HandMeMyThinkingPipe',
                                                                               'AbstrakThought', 'Kookie_212', 'bellavita1577', 'LogiCparty',
                                                                               'SPD87',  'ShittyNoodle', 'jdawg7780', 'seeingwishes', 'ekek26',
                                                                               'reallyloudcrier', 'playingtricksonme', 'Zedevile', 'undercovur',
                                                                               'scryptx', 'Jellolmao124', 'ratcatching', 'KriegRipper', 'Faithlee26',
                                                                               'IAmTheScarBrother', 'mostdietwater', 'herolance', 'TimorousCharles',
                                                                               'danielmann862', 'furmthewurm', 'studentstudylife', 'Gtj_2036',
                                                                               'JohnV318', 'anonymous4226', 'dannythfc', 'kwassa7', 'Millennial_Ennui',
                                                                               'Nocturnalonerr', 'satuza', 'thegamerrr',  'kumadoki', 'HerThoughts88',
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
                                                                               'Carpbeat24', 'RnLraep',  'redfern962', '7_Pixel_7', 'felipe5083',
                                                                               'WellDeserved101', 'minusman652', 'HandMeMyThinkingPipe',
                                                                               'AbstrakThought', 'Kookie_212')


select author, subreddit, strftime('%Y%W', day), count(*) from dayAverageSubmissions where author in ('Wred27', 'jllxxp', 'expressivewords', 'miriamurphy', 'MyLifelines',
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
                                                                               'MelonyHope', 'pinkgirlystuffjody',  'Bronzehawkattack', 'cobo3388',
                                                                               'piyopyoko', 'sicaspeak', 'PorSiempreSolo', 'Cri1654', 'CinnamonThePig',
                                                                               'AdvancedFish', 'peeblicity', 'Ivoriy', 'PanTostadoo',
                                                                               'BestOldExFriendRay', 'bulldozer9999999999', 'jefflucas', 'SilentHuman',
                                                                               'rayj33', 'macproafro', 'Carpbeat24', 'RnLraep', 'redfern962',
                                                                               '7_Pixel_7', 'throwaway19941984', 'minusman652', 'HandMeMyThinkingPipe',
                                                                               'AbstrakThought', 'Kookie_212', 'bellavita1577', 'LogiCparty',
                                                                               'SPD87',  'ShittyNoodle', 'jdawg7780', 'seeingwishes', 'ekek26',
                                                                               'reallyloudcrier', 'playingtricksonme', 'Zedevile', 'undercovur',
                                                                               'scryptx', 'Jellolmao124', 'ratcatching', 'KriegRipper', 'Faithlee26',
                                                                               'IAmTheScarBrother', 'mostdietwater', 'herolance', 'TimorousCharles',
                                                                               'danielmann862', 'furmthewurm', 'studentstudylife', 'Gtj_2036',
                                                                               'JohnV318', 'anonymous4226', 'dannythfc', 'kwassa7', 'Millennial_Ennui',
                                                                               'Nocturnalonerr', 'satuza', 'thegamerrr',  'kumadoki', 'HerThoughts88',
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
                                                                               'Carpbeat24', 'RnLraep',  'redfern962', '7_Pixel_7', 'felipe5083',
                                                                               'WellDeserved101', 'minusman652', 'HandMeMyThinkingPipe',
                                                                               'AbstrakThought', 'Kookie_212') group by author,subreddit, strftime('%Y%W', day);
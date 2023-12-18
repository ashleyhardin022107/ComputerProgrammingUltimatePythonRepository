import csv
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")


def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count = count + 1
    return count


def word_with_most_vowels(wordlist):
    most_vowels = ""
    for word in wordlist:
        if count_vowels(word) > count_vowels(most_vowels):
             most_vowels = word
    return most_vowels

#count_vowels()


def average_word_length(wordlist):
    average = ""
    for word in wordlist:
        average = len(word) + len(wordlist) / len(wordlist)
    return average

#average_word_length()


#def most_common_starting_letter(wordlist):
#    letter_count = 0
#    most_common_letter = ""
#    for letter in word:
#        if


f = open("../data/gradebook_data.csv", "r")
count_a = 0
count_b = 0
count_c = 0
count_d = 0
count_f = 0
reader = csv.reader(f)
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    if percent >= 90:
        count_a = count_a + 1
    elif percent >= 80 and percent < 90:
        count_b = count_b + 1
    elif percent >= 70 and percent < 80:
        count_c = count_c + 1
    elif percent >= 60 and percent < 70:
        count_d = count_d + 1
    elif percent < 60:
        count_f = count_f + 1


print("Number of A's: ", count_a)
print("Number of B's: ", count_b)
print("number of C's: ", count_c)
print("number of D's: ", count_d)
print("Number of F's: ", count_f)     


f = open("../data/gradebook_data.csv", "r")
freshmen_count = 0
freshmen_total = 0
sophomore_count = 0
sophomore_total = 0
junior_count = 0
junior_total = 0
senior_count = 0
senior_total = 0

reader = csv.reader(f)
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    gradelevel = int(gradelevel)
    if gradelevel == 9:
        freshmen_count = freshmen_count + 1
        freshmen_total = freshmen_total + percent
    if gradelevel == 10:
        sophomore_count = sophomore_count + 1
        sophomore_total = sophomore_total + percent
    if gradelevel == 11:
        junior_count = junior_count + 1
        freshmen_total = freshmen_total + percent
    if gradelevel == 12:
        senior_count = senior_count + 1
        senior_total = senior_total + percent
freshmen_average = freshmen_total / freshmen_count
sophomore_average = sophomore_total / sophomore_count
junior_average = junior_total / junior_count
senior_average = senior_total / senior_count
print("freshmen average: ", freshmen_average)
print("sophomore aveage: ", sophomore_average)
print("junior average: ", junior_average)
print("senior average: ", senior_average)


f.close()




# def failing_seniors(list):
#   for row in reader:
#     namelist = ["names"]
#     name, gradelevel, percent = row
#     percent = int(percent)
#     if percent < 60:
#         namelist = namelist + name
        

f = open("../data/1000-largest-us-cities.json", "r")
data = json.load(f)
state = json.load(f)
f.close()

cities_in_kansas = 0
for city in data:
    if data["state"] == "Kansas":
        all_cities = all_cities + state

#print("Cities in Kansas: ", cities_in_kansas)


f = open("../data/1000-largest-us-cities.json", "r")
data = json.open(f)
f.close()

def find_longest_city_name(wordlist): 
    longest_city_name = ""
    for city_name in data:
        if len(city_name) > len(longest_city_name):
            longest_city_name = city_name
    return longest_city_name

find_longest_city_name()


f = open("..?data?1000-largest-us-cities.json", "r")
growth_from_2000_to_2013 = json.open(f)
f.close()

def fastest_growth(data_list):
    growth = 0
    for growth_data in data_list:
        if len(growth_data) > len(growth):
            growth = growth_data
    return growth

fastest_growth()

def fastest_shrinking(data_list):
    shrinkage = 0
    for shrinkage_data in data_list:
        if len(shrinkage_data) < len(shrinkage):
            shrinkage = shrinkage_data
    return shrinkage

fastest_growth()



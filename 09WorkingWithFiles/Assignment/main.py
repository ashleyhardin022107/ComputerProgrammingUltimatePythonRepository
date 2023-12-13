import csv
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


def is_alliteration(word1, word2):
        if word1[0] == word2[0]:
            return True
        else:
            return False
    

print(is_alliteration("blue", "bird"))
print(is_alliteration("red", "bird"))


def count_vowels(word):
     count = 0
     for letter in word:
          if letter in "aeiou":
               count = count + 1
     return count

print(count_vowels("great"))
print(count_vowels("supercalifragilisticexpialidocious"))
print(count_vowels("ugh"))


def count_numbers(string):
     count = 0
     for character in string:
          if character in "1234567890":
               count = count + 1
     return count

print(count_numbers("a1b2c3d4"))
print(count_numbers("oisa34jlk5"))



def count_target_letters(word, character):
     count = 0
     character = "e"
     for letter in word:
          if letter == character:
               count = count + 1
     return count

input = "elephant"
returnvalue = count_target_letters(input)
print(returnvalue)


def in_alphabetical_order(string):
     for letter in string:
          
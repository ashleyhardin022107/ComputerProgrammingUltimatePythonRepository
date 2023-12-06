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



#def count_target_letters(word, character):
#     count = 0
#     character = "e"
#     for letter in word:
#          if letter == character:
#               count = count + 1
#     return count

#input = "elephant"
#returnvalue = count_target_letters(input)
#print(returnvalue)


def alternate_case(string):
     currently_uppercase = True
     result  = ""
     for letter in string:
          if letter == True:
               result = result + letter
          elif letter == False:
               result = result + letter.upper()
     return result

print(alternate_case("elephant"))


def remove_vowels(string):
     result = []
     for letter in string:
          if letter in "aeiou":
               pass
          else:
               result.append(letter)
     return result

print(remove_vowels("great"))


def to_snake_case(string):
     for letter in string:
          if letter == " ":
               
               :(


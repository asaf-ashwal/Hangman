import random
from DB import words
def word_lodory(words):
    word_loc = words[random.randint(0, len(words))]
    return word_loc
# print(word_lodory(words))
    
def game_init():
    pass
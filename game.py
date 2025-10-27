import random
from DB import words
def word_lodory():
    word_loc = words[random.randint(0, len(words))]
    return word_loc
# print(word_lodory(words))


def empty_func(word,start_point = 0):
    underscore = ''
    for i in range(len(word)):
        if i >= start_point:
            underscore += ' _'
        else: underscore += word[i]
    return underscore


def leter_examination(leter, word, user_all_word, loc = 0):
    return word[loc] == leter
        

def get_user_leter(empty_word,mistakes, wrong_leters):
    while True:
        users_leter = input(f'enter leter \n {empty_word}\nlast mistakes {mistakes}\nwrong leters: {wrong_leters}: ')
        if len(users_leter) == 1 and users_leter.isalpha():
            return users_leter
        print('enter only one str leter ')
        continue 
        



def game_init():
    mistakes = 7
    new_word =  'test'
    # word_lodory()
    user_all_word = ''
    wrong_leters = []
    for i in range(7):
        empty_word = empty_func(new_word,len(user_all_word))
        users_leter = get_user_leter(empty_word,mistakes,wrong_leters)
        result = leter_examination(users_leter,new_word,user_all_word,len(user_all_word))
        if result: 
            user_all_word += users_leter
        elif not result: 
            wrong_leters.append(users_leter)
            mistakes -= 1
        if user_all_word == new_word:
            print(f'!!! congagoletion !!!\n   The leter is: {new_word}')
            return ' '
        
    
    
  
  
        
  
  
  
    
# print(leter_examination('H','Hangman','',0))
import random
from DB import words
def word_lodory():
    word_loc = words[random.randint(0, len(words))]
    return word_loc


def empty_func(word,start_point = 0):
    underscore = ''
    for i in range(len(word)):
        if i >= start_point:
            underscore += ' _'
        else: underscore += word[i]
    return underscore


def leter_examination(leter, word, ):
    print('list: ',list(word))
    print('leter: ',leter)
    return  leter in list(word)
        

def get_user_leter(empty_word,mistakes, wrong_leters):
    while True:
        users_leter = input(f'enter leter \n {empty_word}\nlast mistakes {mistakes}\nwrong leters: {wrong_leters}: ')
        if users_leter in wrong_leters:
            print('you all ready gest it')
            continue
        if len(users_leter) == 1 and users_leter.isalpha():
            return users_leter
        print('enter only one str leter ')
        continue 
        

def word_to_print(word,user_leter=''):
    new_list = ''
    for i in range(len(word)):
        if  word[i] in list(user_leter):
            new_list += ' ' + word[i]   
        else:  new_list += ' _'
    return new_list

def game_init():
    mistakes = 7
    new_word = 'test'
    # word_lodory()
    user_all_word = ''
    wrong_leters = []
    for i in range(7):
        empty_word = word_to_print(new_word,user_all_word)
        users_leter = get_user_leter(empty_word,mistakes,wrong_leters)
        result = leter_examination(users_leter,new_word)
        if result: 
            user_all_word += (len([i for i, val in enumerate(list(new_word)) if val == users_leter]) * users_leter)
            print
        elif not result: 
            # indexes = 
            wrong_leters.append(users_leter)
            mistakes -= 1
        if len(user_all_word) == len(new_word):
            print(f'!!! congagoletion !!!\n   The leter is: {new_word}')
            return ' '
        

        
# print(word_to_print('result',))
  
  
    
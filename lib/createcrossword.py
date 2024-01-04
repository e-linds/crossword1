from models import *
from sqlalchemy.orm import Session
import random

with Session(engine) as session:


    line_full = ('+ ' * 3)
    line_empty = ('+ ' + ' ' * 4)
    # letter_space = (' ' * 3)
    line_letter = ("+" + (' ' * 2) +("L") + (" " * 2) + "+")
    box_end = ('+')




    def add_horiz_word(newword):

        def print_word_horiz(newword):
            boxes = []
            for each in list(newword):
                newbox = ("+" + (' ' * 2) +(f"{each.upper()}") + (" " * 2))
                boxes.append(newbox)
            print("".join(boxes) + box_end)

        word_len = len(newword)
        print(line_full * word_len + box_end) 
        # print(line_empty * word_len + box_end)
        print_word_horiz(newword)
        # print(line_empty * word_len + box_end)
        print(line_full * word_len + box_end) 



    def add_vert_word(newword, index):
            
            spaces = (' ' * (index * 6))

            for each in list(newword):
                print(spaces + line_full + box_end)
                # print(line_empty + box_end)
                print(spaces + "+" + (' ' * 2) +(f"{each.upper()}") + (" " * 2) + "+")
                # print(line_empty + box_end)
                # print(line_full + box_end)


    word_list = []
    grand_array = []


    # word1 = input("What word would you like to add to the crossword? ")
    # word2 = input("What word would you like to add to the crossword? ")


    # word_list.append(list(word1))
    # word_list.append(list(word2))

    # temporary function until I get word table up and running
    def add_word(input):
         word_list.append(list(input))

    # add_word("hello")
    # add_word("goodbye")
    # add_word("yellow")
    # add_word("nugget")
    word1 = "yellow"
    word2 = "noodle"
    add_word(word1)
    add_word(word2)


 

    count = 2
    matches = []
    for each in list(word2):
        count -= 1
        if count >= 0:
            for letter in word_list[count]:
                if word_list[count] != list(word2):
                    if each == letter:   
                        match = [count, word_list[count].index(letter)]
                        #this means match will be [index of matching word, index of matching letter within word]
                        matches.append(match)

    selected_match = random.choice(matches)
    match_word = word_list[selected_match[0]]
    match_letter = match_word[selected_match[1]]

    list_new_word = list(word2)
    
   

    # def split_word():
    split_index = list_new_word.index(match_letter)
    first_half = list_new_word[0:split_index]
    second_half = list_new_word[split_index+1: len(list_new_word)+1]


    # split_word()



    #[index of matching word: currently we assume it is across and that we are adding a down]
    #[index of matching letter within word - this will dictate how many spaces we need to add before the word is printed]

    add_vert_word(first_half, selected_match[1])
    add_horiz_word(match_word)
    add_vert_word(second_half, selected_match[1])
    




        
        
             

    # print(word_list)



    # add_horiz_word(word1)
    # add_vert_word(word2)





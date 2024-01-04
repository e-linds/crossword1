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
        print_word_horiz(newword)
        print(line_full * word_len + box_end) 



    def add_vert_word(newword, index = None):
            
            if index:
                spaces = (' ' * (index * 6))
            else:
                spaces = ""

            for each in list(newword):
                print(spaces + line_full + box_end)
                print(spaces + "+" + (' ' * 2) +(f"{each.upper()}") + (" " * 2) + "+")
               


    word_list = []

    ui1 = input("What word would you like to add? ")
    firstword = ((ui1).strip()).lower()

    word_list.append(list(firstword))
    

    add_horiz_word(firstword)

    while True:

        uinext = input("What word would you like to add? ")

        uiword = ((uinext).strip()).lower()
        word_list.append(list(uiword))


        count = len(word_list) - 1
        matches = []
        for each in list(uiword):
            count = count - 1
            if count >= 0:
                for letter in word_list[count]:
                    if word_list[count] != list(uiword):
                        if each == letter:  
                            match = [count, word_list[count].index(letter)]
                            #this means match will be [index of matching word, index of matching letter within word]
                            matches.append(match)

     

        selected_match = random.choice(matches)
        match_word = word_list[selected_match[0]]
        match_letter = match_word[selected_match[1]]

      
        #[index of matching word within wordlist]
        #[index of matching letter within word - this will dictate how many spaces we need to add before the word is printed]

        # add vertical word to existing horizontal
        def display_two_words(vertword, horizword, letter):

            split_index = vertword.index(letter)
            first_half = vertword[0:split_index]
            second_half = vertword[split_index+1: len(vertword)+1]

            add_vert_word(first_half, horizword.index(letter))
            add_horiz_word(horizword)
            add_vert_word(second_half, horizword.index(letter))


        # if new word is an even number, display horizontally
        if (word_list.index(list(uiword)) % 2) == 0:
            display_two_words(match_word, uiword, match_letter)
        #if new word is an odd number, display vertically
        else:
            display_two_words(uiword, match_word, match_letter)


        # we'll assume that the first word was added horizonally and now the third word is too
        def display_three_words(newword, oldword, letter):

            add_vert_word(first_half, horizword.index(letter))
            add_horiz_word(horizword)
            add_vert_word(second_half, horizword.index(letter))
            



        
        
    







from models import *
from sqlalchemy.orm import Session


line_full = ('+ ' * 3)
line_empty = ('+ ' + ' ' * 4)
# letter_space = (' ' * 3)
line_letter = ("+" + (' ' * 2) +("L") + (" " * 2) + "+")
box_end = ('+')


word_list = []

ui1 = input("What word should be added?")
word_list.append(list(ui1))

grand_array = 


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



def add_vert_word(newword):

        for each in list(newword):
            print(line_full + box_end)
            # print(line_empty + box_end)
            print("+" + (' ' * 2) +(f"{each.upper()}") + (" " * 2) + "+")
            # print(line_empty + box_end)
            # print(line_full + box_end)



word1 = input("What word would you like to add to the crossword? ")

add_horiz_word(word1)

word2 = input("What word would you like to add to the crossword? ")

add_vert_word(word2)





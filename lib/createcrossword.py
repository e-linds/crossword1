from models import *
from sqlalchemy.orm import Session

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



    def add_vert_word(newword, relatedword, spaces):
            

            


            for each in list(newword):
                print(line_full + box_end)
                # print(line_empty + box_end)
                print("+" + (' ' * 2) +(f"{each.upper()}") + (" " * 2) + "+")
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

    add_word("hello")
    add_word("goodbye")
    add_word("yellow")
    add_word("nugget")
    noodle = "noodle"
    add_word(noodle)

    count = 5
    for each in list(noodle):
        count -= 1
        for letter in word_list[count]:
             if each == letter:
                  print(letter)
                  print(count)
                  print(word_list[count].index(letter))
        
             

    # print(word_list)



    # add_horiz_word(word1)
    # add_vert_word(word2)





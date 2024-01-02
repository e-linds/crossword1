#Still to do....
# right now this is for one puzzle over and over again. Need to be able to select a puzzle to solve, probably from puzzle class. 
# obviously also need to get the data from the tables after creating and running the seed file
# puzzle class will have the puzzle name and be related to words. Right now, puzzle will mean only 5x5. If we get to creating full crosswords, I might name tht something different. 
# word class will have all words, and which row they are associated with (and that row is associated with a puzzle). If there are duplicates, I think we will not acknolwedge it. 
# clue class will be a 1:1 relationship with word. 
# row class - maybe the most important one. Many rows to one puzzle. Will have five positions. I think we can associate word ids with the rows.....also has an order number, boolean to show whether or not it's a solution. Maybe only solution rows have associated words?

# from seed import Session

#below are some placeholder arrays. 
#irl, we will session.query("RowClass").filter()



#solution array

solution_row1 = ["C", "O", "U", "C", "H"]
solution_row2 = ["A", "x", "M", None, "A"]
solution_row3 = ["S", "O", "B", "E", "R"]
solution_row4 = ["T", None, "E", None, "S"]
solution_row5 = ["E", "A", "R", "T", "H"]

solution_array = [solution_row1, solution_row2, solution_row3, solution_row4, solution_row5]



# display array
display_row1 = ["?", "?", "?", "?", "?"]
display_row2 = ["?", "x", "?", None, "?"]
display_row3 = ["?", "?", "B", "?", "?"]
display_row4 = ["?", None, "?", None, "?"]
display_row5 = ["?", "?", "?", "?", "?"]

# display_row1 = [None, "?", "?", "?", None]
# display_row2 = ["?", "?", "?", "?", None]
# display_row3 = ["?", "?", "?", "?", None]
# display_row4 = ["?", "?", "?", "?", None]
# display_row5 = [None, "?", "?", "?", "?"]

display_array = [display_row1, display_row2, display_row3, display_row4, display_row5]

# order number, spot number == index plus one, index plus one


def find_in_array(ord_num, cell_num):
    return display_array[ord_num - 1][cell_num -1]

line_full = ('+ ' * 4)
line_empty = ('+ ' + ' ' * 6)
letter_space = (' ' * 3)
line_letter = ((' ' * 2) +("L") + (" " * 3))
box_end = ('+')

# this whole big old function is what displays the grid and letters----------------------------------------------------------------------------
def display_puzzle():

    
    cell1_top = ""
    cell1_mid = ""
    cell1_bottom = ""
    cell2_top = ""
    cell2_mid = ""
    cell2_bottom = ""
    cell3_top = ""
    cell3_mid = ""
    cell3_bottom = ""
    cell4_top = ""
    cell4_mid = ""
    cell4_bottom = ""
    cell5_top = ""
    cell5_mid = ""
    cell5_bottom = ""

    ord_num = 0

    for each in display_array:
        # because rows might be identical to each other when everything is blank, I can't actually search for line by index. This ord_num will keep track of which row we're one and serves the same purpose. 
        ord_num += 1
        
        #I think there's a way to use range to only write this if else once. Struggling to think of how I'd interpolate the number into the variable names. 
        #maybe another array and then print the indices of the array?

        if find_in_array(ord_num, 1):
            cell1_top = line_empty
            cell1_mid = (box_end + letter_space +(f"{find_in_array(ord_num, 1)}") + letter_space)
            cell1_bottom = line_empty
            
        else: 
            cell1_top = line_full
            cell1_mid = line_full
            cell1_bottom = line_full

        if find_in_array(ord_num, 2):
            cell2_top = line_empty
            cell2_mid = (box_end + letter_space +(f"{find_in_array(ord_num, 2)}") + letter_space)
            cell2_bottom = line_empty
                
        else: 
            cell2_top = line_full
            cell2_mid = line_full
            cell2_bottom = line_full

        if find_in_array(ord_num, 3):
            cell3_top = line_empty
            cell3_mid = (box_end + letter_space +(f"{find_in_array(ord_num, 3)}") + letter_space)
            cell3_bottom = line_empty
                
        else: 
            cell3_top = line_full
            cell3_mid = line_full
            cell3_bottom = line_full

        if find_in_array(ord_num, 4):
            cell4_top = line_empty
            cell4_mid = (box_end + letter_space +(f"{find_in_array(ord_num, 4)}") + letter_space)
            cell4_bottom = line_empty
                
        else: 
            cell4_top = line_full
            cell4_mid = line_full
            cell4_bottom = line_full

        if find_in_array(ord_num, 5):
            cell5_top = line_empty
            cell5_mid = (box_end + letter_space +(f"{find_in_array(ord_num, 5)}") + letter_space)
            cell5_bottom = line_empty
                
        else: 
            cell5_top = line_full
            cell5_mid = line_full
            cell5_bottom = line_full

        
        if ord_num == 1:
            print("1 " + "+ " * 7 + "2 " + "+ " * 7 + "3 " + '+ ' * 4)
        elif ord_num == 3:
            print("4 " + '+ ' * 20)
        elif ord_num== 5:
            print("5 " + '+ ' * 20)
        else:
            print('+ ' * 21)

        print(cell1_top + cell2_top + cell3_top + cell4_top + cell5_top + box_end)
        print(cell1_mid + cell2_mid + cell3_mid + cell4_mid + cell5_mid + box_end)
        print(cell1_bottom + cell2_bottom + cell3_bottom + cell4_bottom + cell5_bottom + box_end)



#PRINT CLUES. These will eventually come from a table
def display_clues():   
    print("1 across: test")
    print("4 across: test")
    print("5 across: test")
    print("1 down: test")
    print("2 down: test")
    print("3 down: test")



def display_all():
    display_puzzle()
    print(box_end + " " + f"{line_full}" * 5)
    display_clues()

display_all()




# USER INPUTS


while display_array != solution_array:
    ui1 = input("Select a number and direction ")

    if ui1 != "1 across" and ui1 != "4 across" and ui1 != "5 across" and ui1 != "1 down" and ui1 != "2 down" and ui1 != "3 down":
        print("please input valid choice")
    else:
        ui2 = input("What word would you like to guess? ")
        if len(ui2) != 5:
                print("please enter five-letter word")
        else:
            sep_word = list(ui2)

            def extract_all():
                array = []
                for each in display_array:
                    for each in each:
                        array.append(each)
                return array
    
        
            def place_letters(index):
                if "across" in ui1:
                    for each in range(len(sep_word)):
                        display_array[index][each] = (sep_word[each]).upper()
                elif "down" in ui1:
                    for each in range(len(sep_word)):
                        display_array[each][index] = (sep_word[each]).upper()   
                display_all() 
                
                        
            if ui1 == "1 across":
                place_letters(0)
                #top row, all positions

            elif ui1 == "4 across":
                place_letters(2)
                #third row, all positions

            elif ui1 == "5 across":
                place_letters(4)
                #fifth row, all positions

            elif ui1 == "1 down":
                place_letters(0)
                #first column, all positions
                            
            elif ui1 == "2 down":
                place_letters(2)
                #third column, all positions

            elif ui1 == "3 down":
                place_letters(4)
                #fifth column, all positions

            display_all()


    extracted = extract_all()

    solved = False
    try_again = False


    while display_array == solution_array and solved == False:
        print('''
    You've solved it!''') 
        solved = True

    while "?" not in extracted and solved == False and try_again == False:
        print("Not quite, try again!")
        try_again = True

                

        


display_all()









   


        


        











#THIS IS HOW I ORIGINALLY PRINTED THE BOXES. REFACTORED CODE IS ABOVE BUT WANT TO KEEP THIS

#original box function
    
    # def draw_box(height, width):
        #   print(f"{number} " + '+ ' * (width - 1))
    #     for s in range(height-2):
    #         print('+ ' + ' ' * (2*(width-2)) + '+')
    #     print('+ ' * width)



# def draw_box(order_number):
    # pass

#     def insert_order(input):

#         return (('+ ' + ' ' * 2) +
#                    (f"{input}") + 
#                    (" " * 3))
           
#     if order_number == 1:
        # print("+ " * 4 + f"1 " + "+ " * 3 + f"2 " + "+ " * 3 + f"3 " +'+ ' * 8)
#         print(line_full + f"{line_empty}" * 3 + line_full + box_end)
#         print(line_full + 
#               insert_order(solution_array[0][1]) + 
#               insert_order(solution_array[0][2]) + 
#               insert_order(solution_array[0][3]) + 
#               line_full +
#               box_end)
#         print(line_full + f"{line_empty}" * 3 + line_full + box_end)


#     elif order_number == 2:
#         print(f"4 " + '+ ' * 20)
#         print(f"{line_empty}" * 4 + line_full + box_end)
#         print(
#             insert_order(solution_array[1][0]) +
#             insert_order(solution_array[1][1]) +
#             insert_order(solution_array[1][2]) +
#             insert_order(solution_array[1][3]) + 
#             line_full +
#             box_end)
#         print(f"{line_empty}" * 4 + line_full + box_end)


#     elif order_number == 3:
#         print(f"5 " + '+ ' * 20)
#         print(f"{line_empty}" * 4 + line_full + box_end)
#         print(
#             insert_order(solution_array[2][0]) +
#             insert_order(solution_array[2][1]) +
#             insert_order(solution_array[2][2]) +
#             insert_order(solution_array[2][3]) + 
#             line_full +
#             box_end)
#         print(f"{line_empty}" * 4 + line_full + box_end)

#     elif order_number == 4:
#         print(f"6 " + '+ ' * 20)
#         print(f"{line_empty}" * 4 + line_full + box_end)
#         print(
#             insert_order(solution_array[3][0]) +
#             insert_order(solution_array[3][1]) +
#             insert_order(solution_array[3][2]) +
#             insert_order(solution_array[3][3]) + 
#             line_full +
#             box_end)
#         print(f"{line_empty}" * 4 + line_full + box_end)


#     elif order_number == 5:
#         print("+ " * 4 + f"7 " + '+ ' * 16)
#         print(line_full + f"{line_empty}" * 4 + box_end)
#         print(line_full + 
#                insert_order(solution_array[4][1]) +
#                insert_order(solution_array[4][2]) +
#                insert_order(solution_array[4][3]) +
#                insert_order(solution_array[4][4]) +
#                box_end
#                 )
#         print(line_full + f"{line_empty}" * 4 + box_end)

      
    


# def display_puzzle():
#         draw_box(1)
#         draw_box(2)
#         draw_box(3)
#         draw_box(4)
#         draw_box(5)
     
     
# display_puzzle()





# if ui1 == "1":
#     print("you chose 1")
# elif ui1 == "2":
#     print("you chose 2")
# elif ui1 == "3":
#     print("you chose 3")
    


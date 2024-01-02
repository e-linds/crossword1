# here is where the user can build a brand new puzzle. I think the ui will be similar - the grid should pop up each new time, and they can input a word for each spot. 
#The only difference will be that instead of comparing their inputs to a solution array, they will be building a solution array. 
#Maybe I could build it so that for each new solution row, a new empty display row is added too. 


in_progress_row1 = ["c", "o", "u", "c", "h"]
in_progress_row2 = ["a", None, "m", None, "a"]
in_progress_row3 = ["s", "o", "b", "e", "r"]
in_progress_row4 = ["t", None, "e", None, "s"]
in_progress_row5 = ["?", "?", "r", "?", "h"]



puzzle_in_progress = [in_progress_row1, in_progress_row2, in_progress_row3, in_progress_row4, in_progress_row5] 
    


def find_in_array(ord_num, cell_num):
    return puzzle_in_progress[ord_num - 1][cell_num -1]

line_full = ('+ ' * 4)
line_empty = ('+ ' + ' ' * 6)
letter_space = (' ' * 3)
line_letter = ((' ' * 2) +("L") + (" " * 3))
box_end = ('+')



def display_grid():

    
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

    for each in puzzle_in_progress:
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
# def display_clues():   
#     print("1 across: test")
#     print("4 across: test")
#     print("5 across: test")
#     print("1 down: test")
#     print("2 down: test")
#     print("3 down: test")



def display_all():
    display_grid()
    print(box_end + " " + f"{line_full}" * 5)
    # display_clues()

def build_puzzle():

    finished = False

    while finished == False:
        ui1 = input("Select a number and direction to add word ")
        # num_dir_selected = False

        if ui1 != "1 across" and ui1 != "4 across" and ui1 != "5 across" and ui1 != "1 down" and ui1 != "2 down" and ui1 != "3 down":
            print("please input valid choice")

        else:
            # num_dir_selected = True
            ui2 = input("What word would you like to add? ")
            if len(ui2) != 5:
                print("please enter five-letter word")
            else:
                sep_word = list(ui2)

                def extract_all():
                    array = []
                    for each in puzzle_in_progress:
                        for each in each:
                            array.append(each)
                    return array
                
                
                def place_letters(index):
                    if "across" in ui1:
                        for each in range(len(sep_word)):
                            puzzle_in_progress[index][each] = (sep_word[each]).upper()
                    elif "down" in ui1:
                        for each in range(len(sep_word)):
                            puzzle_in_progress[each][index] = (sep_word[each]).upper()    
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
                    

                extracted = extract_all()

                ready_to_save = False
                if "?" not in extracted:
                    finished = True
                    
                while finished == True and ready_to_save == False:
                    ui3 = input("Would you like to submit your puzzle? ")
                    
                    if ui3 == "yes" or ui3 == "y":
                        ui4 = input("What would you like to name the puzzle? ")
                            #take ui4 and store as puzzle instance name
                        print(f"saving {ui4} to database ")
                        ready_to_save = True
                        #save puzzle_in_progress to a puzzle instance and row instances
                    elif ui3 == "no" or ui3 == "n":
                        finished = False
                        ready_to_save = False
                    else:
                        print("please submit valid input")
                


         

display_all()
build_puzzle()



   





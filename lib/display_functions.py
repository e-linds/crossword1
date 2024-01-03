from models import *
from sqlalchemy.orm import Session

with Session(engine) as session:



    line_full = ('+ ' * 4)
    line_empty = ('+ ' + ' ' * 6)
    letter_space = (' ' * 3)
    line_letter = ((' ' * 2) +("L") + (" " * 3))
    box_end = ('+')


    # takes argument: array to be displayed in cli--------------------------------------------------------------------
    def display_grid(display_array):

            def find_in_array(ord_num, cell_num):
                # order number, spot number == index plus one, index plus one
                return display_array[ord_num - 1][cell_num -1]

            
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

            print(box_end + " " + f"{line_full}" * 5)



    # takes argument: id of puzzle whose clues should be diplayed in cli----------------------------------------------------------------
    def display_clues(input):   

            clues = session.query(ClueClass).filter(ClueClass.puzzle_id == input)
            clue_array = []
            for each in clues:
                string = f"{each.num_and_direction}: {each.text}"
                clue_array.append(string)
            for each in sorted(clue_array):
                print(each)
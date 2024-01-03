#Still to do....
# right now this is for one puzzle over and over again. Need to be able to select a puzzle to solve, probably from puzzle class. 
# obviously also need to get the data from the tables after creating and running the seed file
# puzzle class will have the puzzle name and be related to words. Right now, puzzle will mean only 5x5. If we get to creating full crosswords, I might name tht something different. 
# word class will have all words, and which row they are associated with (and that row is associated with a puzzle). If there are duplicates, I think we will not acknolwedge it. 
# clue class will be a 1:1 relationship with word. 
# row class - maybe the most important one. Many rows to one puzzle. Will have five positions. I think we can associate word ids with the rows.....also has an order number, boolean to show whether or not it's a solution. Maybe only solution rows have associated words?

      






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
    


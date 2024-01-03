from models import *
from sqlalchemy.orm import Session
from solve5x5 import display_all

if __name__ == "__main__":

    with Session(engine) as session:

        started = False

        while started == False:
            
            ui1 = input('''
Would you like to:
                        
1: Create a 5x5 puzzle
2: Solve a 5x5 puzzle
3: Create a crossword puzzle
4: Solve a crossword puzzle
                                                
''')

            if ui1 == "1":
                pass
                #create 5x5 code
            elif ui1 == "2":
                #if I later come back and add crossword functionality, I will need to separate puzzles into 5x5s and otherwise
                all_5x5s = session.query(PuzzleClass).all()
                        
                for each in all_5x5s:
                    print(f"{each.id}: {each.name}")

                ui2 = input("Which puzzle would you like to solve? ")

                chosen_puzzle = session.query(PuzzleClass).filter(PuzzleClass.id == ui2).first()

                solution_array = []

                for each in chosen_puzzle.rows:
                    solution_row = [each.p1, each.p2, each.p3, each.p4, each.p5]
                    solution_array.append(solution_row)

                print(solution_array)
                    

                display_row1 = ["?", "?", "?", "?", "?"]
                display_row2 = ["?", None, "?", None, "?"]
                display_row3 = ["?", "?", "?", "?", "?"]
                display_row4 = ["?", None, "?", None, "?"]
                display_row5 = ["?", "?", "?", "?", "?"]

                display_array = [display_row1, display_row2, display_row3, display_row4, display_row5]

                display_all(display_array)

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
                                display_all(display_array) 
                                
                                        
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

                    solved = False
                    try_again = False


                    while display_array == solution_array and solved == False:
                        print("You've solved it!") 
                        solved = True

                    while "?" not in extracted and solved == False and try_again == False:
                        print("Not quite, try again!")
                        try_again = True

                    

            elif ui1 == "3":
                pass
                #create crossword
            elif ui1 == "4":
                pass
                #solve crossword
            else: print("please input 1, 2, 3 or 4")

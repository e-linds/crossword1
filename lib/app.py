from models import *
from sqlalchemy.orm import Session
from display_functions import display_grid, display_clues

if __name__ == "__main__":

    with Session(engine) as session:

        started = False

        while started == False:
            
            ui1 = input('''
Would you like to:
                        
1: Create a 5x5 puzzle
2: Solve a 5x5 puzzle
3: Edit or delete an existing 5x5 puzzle
4: Create a crossword puzzle
5: Solve a crossword puzzle
                                                
''')

            if ui1 == "1":
                
                in_progress_row1 = ["?", "?", "?", "?", "?"]
                in_progress_row2 = ["?", None, "?", None, "?"]
                in_progress_row3 = ["?", "?", "?", "?", "?"]
                in_progress_row4 = ["?", None, "?", None, "?"]
                in_progress_row5 = ["?", "?", "?", "?", "?"]

                puzzle_in_progress = [in_progress_row1, in_progress_row2, in_progress_row3, in_progress_row4, in_progress_row5] 
                        
                finished = False
                
                display_grid(puzzle_in_progress)

                while finished == False:
                    ui2 = input("Select a number and direction to add word ")

                    if "1 across" not in ui2 and "4 across" not in ui2 and "5 across" not in ui2 and "1 down" not in ui2 and "2 down" not in ui2 and "3 down" not in ui2:
                        print("please input valid choice")

                    else:
                        num_dir_selected = False
                        while num_dir_selected == False: 
                            ui3 = input("What word would you like to add? ")
                            if len(ui3) != 5:
                                print("please enter five-letter word")
                            else:
                                num_dir_selected = True
                                sep_word = list(ui3)

                                def extract_all():
                                    array = []
                                    for each in puzzle_in_progress:
                                        for each in each:
                                            array.append(each)
                                    return array
                                
                                
                                def place_letters(index):
                                    if "across" in ui2:
                                        for each in range(len(sep_word)):
                                            puzzle_in_progress[index][each] = (sep_word[each]).upper()
                                    elif "down" in ui2:
                                        for each in range(len(sep_word)):
                                            puzzle_in_progress[each][index] = (sep_word[each]).upper()    
                                    display_grid(puzzle_in_progress)

                                def collect_clue():
                                    ui43 = input("What clue would you like to provide for this word? ")
                                    newclue  = ClueClass(
                                        text = ui43,
                                        num_and_direction = ui2,
                                        puzzle_id = None
                                    )
                                    session.add(newclue)
                                    session.commit()

                                    
                                if "1 across" in ui2:
                                    place_letters(0)
                                    #top row, all positions
                                    collect_clue()

                                elif "4 across" in ui2:
                                    place_letters(2)
                                    #third row, all positions
                                    collect_clue()


                                elif "5 across" in ui2:
                                    place_letters(4)
                                    #fifth row, all positions
                                    collect_clue()

                                elif "1 down" in ui2:
                                    place_letters(0)
                                    #first column, all positions
                                    collect_clue()
                                    
                                elif "2 down" in ui2:
                                    place_letters(2)
                                    #third column, all positions
                                    collect_clue()

                                elif "3 down" in ui2:
                                    place_letters(4)
                                    #fifth column, all positions
                                    collect_clue()
                                    

                                extracted = extract_all()

                                ready_to_save = False
                                if "?" not in extracted:
                                    finished = True
                                    
                                while finished == True and ready_to_save == False:
                                    ui4 = input("Would you like to submit your puzzle? ")
                                    
                                    if ui4 == "yes" or ui4 == "y":
                                        ui5 = input("What would you like to name the puzzle? ")

                                        newpuzzle = PuzzleClass(name = f"{ui5}")
                                        session.add(newpuzzle)
                                        session.commit()

                                        clues = session.query(ClueClass).filter(ClueClass.puzzle_id == None).all()
                                        for each in clues:
                                            each.puzzle_id = newpuzzle.id

                                        count = 0
                                        for each in puzzle_in_progress:
                                            count += 1
                                            newrow = RowClass(
                                                p1 = each[0],
                                                p2 = each[1],
                                                p3 = each[2],
                                                p4 = each[3],
                                                p5 = each[4],
                                                order_number = count,
                                                solution_row = True,
                                                puzzle_id = newpuzzle.id
                                        )
                                            session.add(newrow)
                                            session.commit()


                                        print(f"saving {ui5} to database ")
                                        ready_to_save = True
                                    elif ui4 == "no" or ui4== "n":
                                        finished = False
                                        ready_to_save = False
                                    else:
                                        print("please submit valid input")
                                










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

                display_row1 = ["?", "?", "?", "?", "?"]
                display_row2 = ["?", None, "?", None, "?"]
                display_row3 = ["?", "?", "?", "?", "?"]
                display_row4 = ["?", None, "?", None, "?"]
                display_row5 = ["?", "?", "?", "?", "?"]

                display_array = [display_row1, display_row2, display_row3, display_row4, display_row5]

                # this function takes two arguments: 1, the array to display as guesses are made; and 2, the id of the puzzle which is currently being solved
                display_grid(display_array)
                display_clues(ui2)
                
       
                while display_array != solution_array:
                    print(" ")
                    ui3 = (input("Select a number and direction ")).strip()

                    while ui3 != "1 across" and ui3 != "4 across" and ui3 != "5 across" and ui3 != "1 down" and ui3 != "2 down" and ui3 != "3 down" or ui3 == None:
                        ui18 = input("Please input valid choice ")
                        ui3 = (ui18).strip()
                    
                    if ui3 == "1 across" or ui3 == "4 across" or ui3 == "5 across" or ui3 == "1 down" or ui3 == "2 down" or ui3 == "3 down":
                        
                        ui4 = input("What word would you like to guess? ")
                        while len(ui4) != 5:
                            ui19 = input("Please enter five-letter word ")
                            ui4 = ui19
                        if len(ui4) == 5:
                            sep_word = list(ui4)

                            def extract_all():
                                array = []
                                for each in display_array:
                                    for each in each:
                                        array.append(each)
                                return array
                    
                        
                            def place_letters(index):
                                if "across" in ui3:
                                    for each in range(len(sep_word)):
                                        display_array[index][each] = (sep_word[each]).upper()
                                elif "down" in ui3:
                                    for each in range(len(sep_word)):
                                        display_array[each][index] = (sep_word[each]).upper()   
                                display_grid(display_array) 
                                display_clues(ui2)
                                
                            if ui3 == "1 across":
                                place_letters(0)
                                #top row, all positions

                            elif ui3 == "4 across":
                                place_letters(2)
                                #third row, all positions

                            elif ui3 == "5 across":
                                place_letters(4)
                                #fifth row, all positions

                            elif ui3 == "1 down":
                                place_letters(0)
                                #first column, all positions
                                            
                            elif ui3 == "2 down":
                                place_letters(2)
                                #third column, all positions

                            elif ui3 == "3 down":
                                place_letters(4)
                                #fifth column, all positions

                    extracted = extract_all()

                    solved = False
                    try_again = False


                    while display_array == solution_array and solved == False:
                        print(" ")
                        print("You've solved it!")
                        
                        solved = True

                    while "?" not in extracted and solved == False and try_again == False:
                        print(" ")
                        print("Not quite, try again!")
                        
                        try_again = True
            
            elif ui1 == "3":
                #IN THE MIDDLE OF FIGURING OUT HOW TO EDIT AN EXISTING PUZZLE - PULLING LOTS OF LOGIC FROM #1
                
                all_5x5s = session.query(PuzzleClass).all()
                        
                for each in all_5x5s:
                    print(f"{each.id}: {each.name}")

                ui2 = input("Which puzzle would you like to select? ")

                chosen_puzzle = session.query(PuzzleClass).filter(PuzzleClass.id == ui2).first()

                ui3 = input("Would you like to edit or delete this puzzle? ")

                if (ui3.strip()).lower() == "delete":
                    session.query(PuzzleClass).filter(PuzzleClass.id == chosen_puzzle.id).delete()
                    session.commit()
                    print("puzzle successfully deleted")
                elif (ui3.strip()).lower() == "edit":
                
                    solution_array = []

                    for each in chosen_puzzle.rows:
                        solution_row = [each.p1, each.p2, each.p3, each.p4, each.p5]
                        solution_array.append(solution_row)   

                    # display_grid(solution_array)
                    # display_clues(chosen_puzzle.id)

                    # in_progress_row1 = ["?", "?", "?", "?", "?"]
                    # in_progress_row2 = ["?", None, "?", None, "?"]
                    # in_progress_row3 = ["?", "?", "?", "?", "?"]
                    # in_progress_row4 = ["?", None, "?", None, "?"]
                    # in_progress_row5 = ["?", "?", "?", "?", "?"]

                    puzzle_in_progress = solution_array
                            
                    finished = False
                    
                    display_grid(puzzle_in_progress)

                    while finished == False:
                        ui4 = (input("Select a number and direction to edit word or clue ")).strip()

                        if ui4 != "1 across" and ui4 != "4 across" and ui4 != "5 across" and ui4 != "1 down" and ui4 != "2 down" and ui4 != "3 down":
                            print("please input valid choice")

                        else:
                            num_dir_selected = False
                            while num_dir_selected == False: 
                                ui5 = input("Enter new word here, or type existing word to continue ")
                                if len(ui5) != 5:
                                    print("please enter five-letter word")
                                else:
                                    num_dir_selected = True
                                    sep_word = list(ui5)

                                    def extract_all():
                                        array = []
                                        for each in puzzle_in_progress:
                                            for each in each:
                                                array.append(each)
                                        return array
                                    
                                    
                                    def place_letters(index):
                                        if "across" in ui4:
                                            for each in range(len(sep_word)):
                                                puzzle_in_progress[index][each] = (sep_word[each]).upper()
                                        elif "down" in ui4:
                                            for each in range(len(sep_word)):
                                                puzzle_in_progress[each][index] = (sep_word[each]).upper()    
                                        display_grid(puzzle_in_progress)

                                    # def edit_clue():
                                    #     current_clue = session.query(ClueClass).filter(ClueClass.puzzle_id == chosen_puzzle.id, ClueClass.num_and_direction == ui4)
                                    #     ui43 = input(f"Would you like to edit the clue for this word? Current clue is {current_clue.text} ")
                                    #     if ui43 == "yes" or ui43 == "y":
                                    #         ui44 = input("What would you like the new clue to be? ")
                                    #         current_clue.text = ui44
                                        # newclue  = ClueClass(
                                        #     text = ui43,
                                        #     num_and_direction = ui4,
                                        #     puzzle_id = None
                                        # )
                                        # session.add(newclue)
                                        # session.commit()

                                        
                                    if "1 across" in ui4:
                                        place_letters(0)
                                        #top row, all positions
                                        # collect_clue()

                                    elif "4 across" in ui4:
                                        place_letters(2)
                                        #third row, all positions
                                        # collect_clue()


                                    elif "5 across" in ui4:
                                        place_letters(4)
                                        #fifth row, all positions
                                        # collect_clue()

                                    elif "1 down" in ui4:
                                        place_letters(0)
                                        #first column, all positions
                                        # collect_clue()
                                        
                                    elif "2 down" in ui4:
                                        place_letters(2)
                                        #third column, all positions
                                        # collect_clue()

                                    elif "3 down" in ui4:
                                        place_letters(4)
                                        #fifth column, all positions
                                        # collect_clue()

                                    current_clue = session.query(ClueClass).filter(ClueClass.puzzle_id == chosen_puzzle.id, ClueClass.num_and_direction == ui4)
                                    print(current_clue)
                                    print(current_clue.text)


                                        

                                    extracted = extract_all()

                                    ready_to_save = False
                                    if "?" not in extracted:
                                        finished = True
                                        
                                    while finished == True and ready_to_save == False:
                                        ui6 = input("Would you like to submit your edits? ")
                                        
                                        if ui6 == "yes" or ui6 == "y":
                                            ui7 = input(f"Would you like to re-name the puzzle? Current name is {chosen_puzzle.name} ")

                                            if ui7 == "yes" or ui7 == "y":
                                                ui8 = input("What would you like the new name to be? ")
                                                chosen_puzzle.name == ui8
                                            
                                        #     elif ui7 == "no" or ui7 == "n":

                                        

                                        #     newpuzzle = PuzzleClass(name = f"{ui7}")
                                        #     session.add(newpuzzle)
                                        #     session.commit()

                                        #     clues = session.query(ClueClass).filter(ClueClass.puzzle_id == None).all()
                                        #     for each in clues:
                                        #         each.puzzle_id = newpuzzle.id

                                        #     count = 0
                                        #     for each in puzzle_in_progress:
                                        #         count += 1
                                        #         newrow = RowClass(
                                        #             p1 = each[0],
                                        #             p2 = each[1],
                                        #             p3 = each[2],
                                        #             p4 = each[3],
                                        #             p5 = each[4],
                                        #             order_number = count,
                                        #             solution_row = True,
                                        #             puzzle_id = newpuzzle.id
                                        #     )
                                        #         session.add(newrow)
                                        #         session.commit()


                                        #     print(f"saving {ui7} to database ")
                                        #     ready_to_save = True
                                        # elif ui6 == "no" or ui6== "n":
                                        #     finished = False
                                        #     ready_to_save = False
                                        # else:
                                        #     print("please submit valid input")
                                    

                    

            elif ui1 == "4":
                pass
                #create crossword
            elif ui1 == "5":
                pass
                #solve crossword
            else: print("please input 1, 2, 3 or 4")

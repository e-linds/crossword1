from models import *
from sqlalchemy.orm import Session
from display_functions import display_grid, display_clues
import sys, random, time
import cowsay


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
5: Exit
                                                
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
                    ui2 = (input("Select a number and direction to add word ")).strip()

                    if ui2 != "1 across" and ui2 != "4 across" and ui2 != "5 across" and ui2 != "1 down" and ui2 != "2 down" and ui2 != "3 down":
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
                                    clue_exist = session.query(ClueClass).filter(ClueClass.num_and_direction == ui2, ClueClass.puzzle_id == None).first()
                                    if clue_exist:
                                        clue_exist.text = ui43
                                    else:
                                        newclue  = ClueClass(
                                            text = ui43,
                                            num_and_direction = ui2,
                                            puzzle_id = None
                                        )
                                        session.add(newclue)
                                        session.commit()

                                    
                                if "1 across" in ui2:
                                    place_letters(0)
                                    collect_clue()

                                elif "4 across" in ui2:
                                    place_letters(2)
                                    collect_clue()

                                elif "5 across" in ui2:
                                    place_letters(4)
                                    collect_clue()

                                elif "1 down" in ui2:
                                    place_letters(0)
                                    collect_clue()
                                    
                                elif "2 down" in ui2:
                                    place_letters(2)
                                    collect_clue()

                                elif "3 down" in ui2:
                                    place_letters(4)
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

                            elif ui3 == "4 across":
                                place_letters(2)

                            elif ui3 == "5 across":
                                place_letters(4)

                            elif ui3 == "1 down":
                                place_letters(0)
                                            
                            elif ui3 == "2 down":
                                place_letters(2)

                            elif ui3 == "3 down":
                                place_letters(4)

                    extracted = extract_all()

                    solved = False
                    try_again = False


                    while display_array == solution_array and solved == False:
                        print(" ")
                        cowsay.cow("Congrats, you've solved it!")
                        time.sleep(2)

                        
                        solved = True

                    while "?" not in extracted and solved == False and try_again == False:
                        print(" ")
                        print("Not quite! One or more letters are incorrect. Try again!")
                        time.sleep(2)

                        
                        try_again = True
            
            elif ui1 == "3":
                
                all_5x5s = session.query(PuzzleClass).all()
                        
                for each in all_5x5s:
                    print(f"{each.id}: {each.name}")

                ui2 = input("Which puzzle would you like to select? ")

                chosen_puzzle = session.query(PuzzleClass).filter(PuzzleClass.id == ui2).first()

                ui3 = input("Would you like to edit or delete this puzzle? ")

                if (ui3.strip()).lower() == "delete":
                    session.query(PuzzleClass).filter(PuzzleClass.id == chosen_puzzle.id).delete()
                    session.query(RowClass).filter(RowClass.puzzle_id == chosen_puzzle.id).delete()
                    session.query(ClueClass).filter(ClueClass.puzzle_id == chosen_puzzle.id).delete()
                    session.commit()
                    print("puzzle successfully deleted")
                elif (ui3.strip()).lower() == "edit":
                
                    solution_array = []

                    for each in chosen_puzzle.rows:
                        solution_row = [each.p1, each.p2, each.p3, each.p4, each.p5]
                        solution_array.append(solution_row)   
                    
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

                                    def edit_clue():
                                        current_clue = session.query(ClueClass).filter(ClueClass.puzzle_id == chosen_puzzle.id, ClueClass.num_and_direction == ui4).first()
                                        ui43 = input(f"Would you like to edit the clue for this word? Current clue is '{current_clue.text}' ")
                                        if ui43 == "yes" or ui43 == "y":
                                            ui44 = input("What would you like the new clue to be? ")
                                            current_clue.text = ui44
                                            session.add(current_clue)
                                            session.commit()
                                        
                                    if "1 across" in ui4:
                                        place_letters(0)
                                        edit_clue()

                                    elif "4 across" in ui4:
                                        place_letters(2)
                                        edit_clue()

                                    elif "5 across" in ui4:
                                        place_letters(4)
                                        edit_clue()

                                    elif "1 down" in ui4:
                                        place_letters(0)
                                        edit_clue()
                                        
                                    elif "2 down" in ui4:
                                        place_letters(2)
                                        edit_clue()

                                    elif "3 down" in ui4:
                                        place_letters(4)
                                        edit_clue()

                                                                          

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
                                                chosen_puzzle.name = ui8
                                                session.add(chosen_puzzle)
                                                session.commit()
                                            
                                            rows = session.query(RowClass).filter(RowClass.puzzle_id == chosen_puzzle.id).all()
                                            count = -1
                                            for each in rows:
                                                count += 1
                                                each.p1= puzzle_in_progress[count][0]
                                                each.p2= puzzle_in_progress[count][1]
                                                each.p3= puzzle_in_progress[count][2]
                                                each.p4= puzzle_in_progress[count][3]
                                                each.p5= puzzle_in_progress[count][4]
                                                session.add(each)
                                                session.commit()

                                        
                                            print("Changed are saved! ")
                                            ready_to_save = True
                                        elif ui6 == "no" or ui6== "n":
                                            finished = False
                                            ready_to_save = False
                                        else:
                                            print("please submit valid input")
                                    

                    
            # create crossword puzzle
            elif ui1 == "4":
                
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
                # word_list.append("test")
                # word_list.append("goodbye")
                

                add_horiz_word(firstword)

                def add_word(input):

                    matches = []
                    for word in word_list:
                        for letter in word:
                            if word != list(input):
                                for each in list(input):
                                    if each == letter:
                                        match = [word_list.index(word), word.index(letter)]
                        #                 #this means match will be [index of matching word, index of matching letter within word]
                                        matches.append(match)
                    # print(matches)
                    # print(word_list)

            
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


                while True:

                    uinext = input("What word would you like to add? ")

                    uiword = ((uinext).strip()).lower()
                    word_list.append(list(uiword))

                    add_word(uiword)

                    


                    # we'll assume that the first word was added horizonally and now the third word is too
                    # def display_three_words(newword, oldword, letter):

                    #     add_vert_word(first_half, horizword.index(letter))
                    #     add_horiz_word(horizword)
                    #     add_vert_word(second_half, horizword.index(letter))
                        

            # elif ui1 == "5":
            #     print("Crossword: coming soon!")
            elif ui1 == "5":
                sys.exit(0)
                            
            else: print("please input a valid number option")

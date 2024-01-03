from models import *
from sqlalchemy.orm import Session

if __name__ == "__main__":

    with Session(engine) as session:

        PuzzleClass.__table__.drop(engine)
        WordClass.__table__.drop(engine)
        ClueClass.__table__.drop(engine)
        RowClass.__table__.drop(engine)

        Base.metadata.create_all(engine)
        


        # puzzle1 = PuzzleClass(name = "Demo Puzzle")
        # session.add(puzzle1)

        # print("session")

        # row1 = RowClass(
        #     p1 = "c",
        #     p2 = "o",
        #     p3 = "u",
        #     p4 = "c",
        #     p5 = "h",
        #     order_number = 1,
        #     solution_row = True,
        #     puzzle_id = 1
        # )
        # session.add(row1)
        # session.commit()


        # word1 = WordClass(
        #     name = "couch",
        #     puzzle_id = 1,
        #     row_id = 1
        #     )
        # session.add(word1)
        # session.commit()

        
        # clue1 = ClueClass(
        #     text = "Free if you come get it",
        #     word_id = "1"
        # )
        # session.add(clue1)
        # session.commit()

    

    









    




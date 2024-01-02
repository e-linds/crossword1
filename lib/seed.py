from models import *
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///crossword.db")


with Session(engine) as session:

    # session.query(PuzzleClass).delete()
    # session.query(WordClass).delete()
    # session.query(ClueClass).delete()
    # session.query(RowClass).delete()


    # PuzzleClass.__table__.drop(engine)
    # WordClass.__table__.drop(engine)
    # ClueClass.__table__.drop(engine)
    # RowClass.__table__.drop(engine)


    Base.metadata.create_all(engine)


    puzzle1 = PuzzleClass(name = "Puzzle 1")
    session.add(puzzle1)

    row1 = RowClass(
        p1 = "c",
        p2 = "o",
        p3 = "u",
        p4 = "c",
        p5 = "h",
        order_number = 1,
        solution_row = True,
        puzzle_id = 1
    )
    session.add(row1)


    word1 = WordClass(
        name = "couch",
        puzzle_id = 1,
        row_id = 1
        )
    session.add(word1)

    
    clue1 = ClueClass(
        text = "Free if you come get it",
        word_id = "1"
    )
    session.add(clue1)

    









    




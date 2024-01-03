from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, engine, create_engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

engine = create_engine("sqlite:///crossword.db")
Base.metadata.create_all(engine)


class PuzzleClass(Base):
    __tablename__ = "puzzles_table"

    id = Column(Integer, primary_key = True)
    name = Column(String)

    # words = relationship("WordClass", back_populates = "PuzzleClass")
    rows = relationship("RowClass", back_populates = "puzzles")

    def __repr__(self):
        return f"{self.name}"

#a row can exist without a word, but a word cannot exist without a row
class WordClass(Base):
    __tablename__ = "words_table"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    # length = Column(Integer)
    # direction = Column(String)
    puzzle_id = Column(Integer, ForeignKey("puzzles_table.id"))
    row_id = Column(Integer, ForeignKey("rows_table.id"))

    def __repr__(self):
        return f"{self.name}"


class ClueClass(Base):
    __tablename__ = "clues_table"

    id = Column(Integer, primary_key = True)
    text = Column(String)
    word_id = Column(String, ForeignKey("words_table.id"))

    def __repr__(self):
        return f"{self.text}"
    

class RowClass(Base):
    __tablename__ = "rows_table"

    id = Column(Integer, primary_key = True)
    p1 = Column(String)
    p2 = Column(String)
    p3 = Column(String)
    p4 = Column(String)
    p5 = Column(String)
    order_number = Column(Integer)
    solution_row = Column(Boolean)
    puzzle_id = Column(Integer, ForeignKey("puzzles_table.id"))

    puzzles = relationship("PuzzleClass", back_populates = "rows" )

    def __repr__(self):
        return f'''{self.p1}, {self.p2}, {self.p3}, {self.p4}, {self.p5}
        order_number: {self.order_number}, solution?: {self.solution_row}'''
    
    





# script to find out how many answers exist in a given text, then populate
# the FTC table's total_answers field because it wasn't done already.

from sqlalchemy.orm import registry
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, DateTime, String
from sqlalchemy.orm import Session
import datetime


now = datetime.datetime.now()
engine = create_engine('sqlite:///db.sqlite3')
mapper_registry = registry()

first_time_correct = Table(
    "first_time_correct_firsttimecorrect",
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('correct_answers', Integer),
    Column('student_id', Integer),
    Column('text_id', Integer),
    Column('end_dt', DateTime),
    Column('total_answers', Integer)
)

text_section = Table(
    "text_textsection",
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('created_dt', DateTime),
    Column('modified_dt', DateTime),
    Column('order', Integer),
    Column('body', String),
    Column('text_id', Integer),
    Column('translation_service_processed', Integer)
)

question = Table(
    "question_question",
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('created_dt', DateTime),
    Column('modified_dt', DateTime),
    Column('body', String),
    Column('order', Integer),
    Column('type', String),
    Column('text_section_id', Integer)
)

class FirstTimeCorrect:
    pass

class TextSection:
    pass

class Question:
    pass

mapper_registry.map_imperatively(FirstTimeCorrect, first_time_correct)
mapper_registry.map_imperatively(TextSection, text_section)
mapper_registry.map_imperatively(Question, question)

with Session(engine) as session:

    ftc = session.query(FirstTimeCorrect).all()
    questions = session.query(Question).all()
    sections = session.query(TextSection).all()

    for f in ftc:
        same_sections = []
        question_count = 0
        for s in sections:
            if f.text_id == s.text_id:
                same_sections.append(s.id)

        for q in questions:
            if q.text_section_id in same_sections:
                question_count += 1

        f.total_answers = question_count

    session.commit()

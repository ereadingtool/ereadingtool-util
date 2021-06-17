from sqlalchemy.orm import registry
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, DateTime
from sqlalchemy.orm import Session
# import django.utils.timezone
import datetime

now = datetime.datetime.now()
engine = create_engine('sqlite:///db.sqlite3')
mapper_registry = registry()

first_time_correct = Table(
    "first_time_correct_firsttimecorrect",
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('num_correct', Integer),
    Column('student_id', Integer),
    Column('text_id', Integer),
    Column('end_dt', DateTime)
)

class FirstTimeCorrect:
    pass

mapper_registry.map_imperatively(FirstTimeCorrect, first_time_correct)

with Session(engine) as session:

    ftc = session.query(FirstTimeCorrect).all()

    for row in ftc:
        row.end_dt = now
    
    session.commit()
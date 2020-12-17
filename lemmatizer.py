from typing import Text
import pymorphy2
from sqlalchemy.orm import registry
from sqlalchemy import select
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import Session


engine = create_engine('sqlite:///db.sqlite3')
mapper_registry = registry()

text_textphrase = Table(
    "text_textphrase",
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('pos', String),
    Column('tense', String),
    Column('aspect', String),
    Column('form', String),
    Column('mood', String),
    Column('instance', Integer, nullable=False),
    Column('phrase', String, nullable=False),
    Column('text_section_id', Integer, nullable=False),
    Column('lemma', String)
)

class TextPhrase:
    pass

# build table relative to this program, outside of project
mapper_registry.map_imperatively(TextPhrase, text_textphrase)

# engine that does phrase analysis
morph = pymorphy2.MorphAnalyzer()

# open a connection with DB
with Session(engine) as session:

    # query every phrase
    text_phrases = session.query(TextPhrase).all()

    # iterate through each row in the table
    for row in text_phrases:

        # grab the first analyzed phrase returned from analyzer
        parsed_phrase = morph.parse(row.phrase)[0]
        
        # store the lemma in the row, we wantz it
        row.lemma = parsed_phrase.normal_form

    # v expensive to keep in loop, but if your program is barfing
    # due to uncleaned data (perhaps violating UNIQUE), move it
    # inside and you'll be given the problem row in the stack trace
    session.commit()


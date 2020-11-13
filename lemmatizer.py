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

mapper_registry.map_imperatively(TextPhrase, text_textphrase)

morph = pymorphy2.MorphAnalyzer()

with Session(engine) as session:
    text_phrases = session.query(TextPhrase).all()
    for row in text_phrases:
        parsed_phrase = morph.parse(row.phrase)[0]
        row.lemma = parsed_phrase.normal_form

    session.commit()
# connection = engine.connect()
# # result = connection.execute('select * from text_textphrase')
# result = connection.execute('select * from text_textphrase')


#   # the phrases may already be merged, this gives us the phrase as the lemma
#   phrase = row['phrase']

#   # we may be able to add a column to text_textphrase for the lemma
#   # and add each of the lemmas to the database

#   print(parsed_phrase.normal_form)

#   row.lemma = parsed_phrase.normal_form

# connection.commit()

# i = 0
# for row in result:
#   print(row['lemma'])
#   i+=1
#   if i > 10:
    # break
  # SQL statement
  #
  #  UPDATE text_textphrase
  #  SET lemma = phrase.normal_form
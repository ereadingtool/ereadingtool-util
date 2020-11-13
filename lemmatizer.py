import pymorphy2
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('sqlite:///db.sqlite3')

connection = engine.connect()
morph = pymorphy2.MorphAnalyzer()
result = connection.execute('select * from text_textphrase')

for row in result:

  # the phrases may already be merged, this gives us the phrase as the lemma
  phrase = row['phrase']
  parsed_phrase = morph.parse(phrase)[0]

  # we may be able to add a column to text_textphrase for the lemma
  # and add each of the lemmas to the database

  print(parsed_phrase.normal_form)

  # how do we update the table to add the column? What does Django need for a database migration?
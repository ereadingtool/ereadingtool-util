# Lemmatizer

### Purpose

We needed to add a column to the database for the ereadingtool project. 
The column's values are dependent on that `phrase` column, since they're
the lemma of phrase itself. If they're equivalent or one cannot be found,
the phrase is used itself. 

#### Adding a new column

If you find yourself in need of a new column, this command will add one 
to your database table.
```
ALTER TABLE {tableName} ADD COLUMN COLNew {type};
```

#### Complications

If you're working with something as finicky as Django migrations, it may
be the case that you need to manually edit them. In my case, I needed to 
comment out an existing migration that specified the `unique_together` 
property. This allowed me to both add the column to the model as well as 
update the `unique_together` property.
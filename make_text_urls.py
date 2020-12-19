import csv

a = []
with open("./text_text_dump.csv") as f:
    t = csv.reader(f)
    i = 0
    for row in t:
        entry = f"{row[5]}\n  https://step2ar.org/text/{row[0]}\n\n"
        a.append(entry)

# get rid of column names
a = a[1:]

with open("./text_urls.txt", "w") as f:
    for entry in a:
        f.write(entry)

import json
import csv

str_csv = 'source-for-exercise/final-exercise-4/books.csv'

with open('source-for-exercise/final-exercise-4/books.json') as file:
    books = json.load(file)

book_cat = dict()

for book in books:
    for categories in book["categories"]:
        if categories in book_cat:
            book_cat[categories] += 1
        else:
            book_cat[categories] = 1

categories_porcentage_list = [
  {categorie: book_cat[categorie] / len(books)} for categorie in book_cat
]

with open(str_csv, 'w', encoding='utf-8') as file:
    writer = csv.writer(file)

    headers = [
      'categoria',
      'porcentagem',
    ]

    writer.writerow(headers)

    for x in categories_porcentage_list:
        for category in x:
            row = [
                category,
                x[category],
            ]
            writer.writerow(row)

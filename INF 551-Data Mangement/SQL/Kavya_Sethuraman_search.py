import mysql.connector
import sys
cnx = mysql.connector.connect(user='root', password='root',
host='127.0.0.1',
database='sakila')
cursor = cnx.cursor()
keyword = []
keyword = sys.argv[1]
keyword = keyword.lower()
query = " select c.name from film f, category c,film_category fc where f.film_id = fc.film_id and c.category_id = fc.category_id;"
cursor.execute(query)
count = 0
for name in cursor:
    if name[0].lower() == keyword:
                count = count +1
print count
cursor.close()
cnx.close()


import mysql.connector
mysqlconnect = mysql.connector.connect(

  host="127.0.0.1",

  user="root",

  passwd="madhupass",

  database="sakila",

  auth_plugin='mysql_native_password'

)

my_cursor = mysqlconnect.cursor()

my_cursor.execute("select c.city,co.country from sakila.city c, sakila.country co where c.country_id=co.country_id and co.country='Canada'")

output= my_cursor.fetchall()

for i in output:

  print(i)

  #Print every 3rd letter 

 sentence = "The Python programming language makes manipulating strings very easy!"

words_combined = sentence.replace(" ","")

words_combined 
a= 2
b = len(words_combined)
for i in words_combined:
    if b >3:
        print (words_combined[a])
        a += 3
        b -= 3
    


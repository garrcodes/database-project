import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='toot',
    passwd='gadmint',
    database='books'
)

cart = {}

if mydb.is_connected():
    print("Hello Dear Bibliophile! Welcome to the BookWorm Shack! Get a book that is perfect for you or donate a book that you no longer require but can be of use to others. Please note that all the donations made are used to provide relief to the Covid-19 victims in India.")

mycursor = mydb.cursor()

choice = input("For purchasing a book, type 'Get', and for donating a book, type 'Donate': ")

if choice == 'Get':
    j= input('Enter the book genre you want to search for: ')

if j == 'fiction':
    print("Books available under this genre are:-")
    print('\n')
    display = 'SELECT * FROM fiction'
    mycursor.execute(display)
    output = mycursor.fetchall()
    for i in output:
        print(i)
    c = input('Enter the book name you want to search for: ')
    quer = "SELECT * FROM fiction WHERE book_name=%s"%(c)
    mycursor.execute(quer)
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

if j == 'biographies':
    display = 'SELECT * FROM biographies'
    mycursor.execute(display)
    output = mycursor.fetchall()
    for i in output:
        print(i)
    c = input('Enter the book name you want to search for: ')
    quer = "SELECT * FROM biographies WHERE book_name=%s"%(c)
    mycursor.execute(quer)
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

if j == 'NCERT':
    display = "SELECT * FROM NCERT"
    mycursor.execute(display)
    output = mycursor.fetchall()
    for i in output:
        print(i)
    c = input('Enter the book name you want to search for: ')
    quer = "SELECT * FROM NCERT WHERE book_name=%s"%(c)
    mycursor.execute(quer)
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

if j == 'poetry':
    display = 'SELECT * FROM poetry'
    mycursor.execute(display)
    output = mycursor.fetchall()
    for i in output:
        print(i)
    c = input('Enter the book name you want to search for: ')
    quer = "SELECT * FROM poetry WHERE book_name=%s"%(c)
    mycursor.execute(quer)
    myresult = mycursor.fetchall()
    for i in myresult:
        print(i)

name = input('Please enter your name: ')
address = input('Please enter your address: ')
phoneno = int(input('Please enter your phone number: '))

L = [name, address, phoneno]

print('Your personal information will be kept confidential:', L)
print("Thank you for choosing the BookWorm Shack. Your book will be delivered within 5-7 days. Payment method is 'Cash on Delivery'.")

elif choice == 'Donate':
    print('Use this link:', "https://forms.gle/cw6j3NFK4HuHX6FY6")




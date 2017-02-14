import sqlite3

conn = sqlite3.connect('f:/invsys/converted.sqlite')
artconn =
keyword = input("Enter a string to look for: ")
lookup = '%' + keyword + '%'
print(lookup)
c = conn.cursor()

table_name = 'art'

if len(keyword) > 0:
    my_list = c.execute('SELECT title, memo_prov FROM art WHERE memo_prov LIKE ?', (lookup,))
else:
    my_list = c.execute('SELECT title, memo_prov FROM art')



while True:
    row = my_list.fetchone()
    if row == None:
        break
    print(row[0] +'\n'+row[1])

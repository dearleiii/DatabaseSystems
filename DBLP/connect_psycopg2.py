import psycopg2
conn = psycopg2.connect("dbname=dblp user=postgres password=201211")
cur = conn.cursor()
print('PostgreSQL database version: ')
cur.execute('SELECT version()')
db_version = cur.fetchone()
print(db_version)

import os
root = '/Users/dearleiii/Desktop/2018Autumn/DataBase/Homeworks/hw1'
print(root)
xml_f_name = 'dblp-2018-08-01.xml'
print(os.path.join(root, xml_f_name))

xml_file = open(os.path.join(root, xml_f_name)).read()



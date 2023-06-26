import mysql.connector
from mysql.connector.locales.eng import client_error
from mysql.connector import Error

import os
db_pass = os.environ.get('db_pass')


class Database():
   def __init__(self):
      self.mydb = mysql.connector.connect(
         host = "127.0.0.1",
         user = "root",
         passwd = db_pass,
         database = "oop_methods"
      )
      
      self.c = self.mydb.cursor()
      
   def get_query(self, query):
      self.c.execute(query)
      query = self.c.fetchall()
      query = str(query).replace("(", "").replace(")", "")
      query = query.replace("[", "").replace("]", "").replace("'", "")
      return query.rstrip(query[-1])
   
   def get_listed_query(self, query):
      self.c.execute(query)
      query = list(self.c.fetchall())
      query = str(query).replace("(", "").replace(",)", "")
      return query
   
   def get_reg_query(self, query):
      print(query)
      self.c.execute(query)
      query = self.c.fetchall()
      return query
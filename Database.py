import os
from tkinter import *
from dotenv import load_dotenv
import mysql.connector

dotenv_path = '/storage/emulated/0/Python/.env' 

# Load the file using the full path
load_dotenv() 

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", "3306")

def get_db_connection():
	try:
		conn = mysql.connector.connect(
        	host=DB_HOST,
        	port=int(DB_PORT),
        	user=DB_USER,
        	password=DB_PASSWORD,
        	database=DB_NAME
		)
		return conn
	except mysql.connector.Error as err:
		print("DatabaseError: ", err)
		return None
	except Exception as err:
		print("Error: ", err)
		return None
	
print(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT)
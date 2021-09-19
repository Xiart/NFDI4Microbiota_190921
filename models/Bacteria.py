import sqlite3
import os
from datetime import datetime

currentdir = os.path.dirname(__package__)

def SaveBacteria(name):
    db_path = os.path.join(currentdir, "Microbiota")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    Query = "INSERT INTO tbl_Bacteria VALUES (null, '"+name+"', 1 , 1, DATE(), DATE(), 1)"
    cursor.execute(Query)
    connection.commit()

def GetBacteriaList():
    db_path = os.path.join(currentdir, "Microbiota")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    Query = "SELECT BacteriaId, BacteriaName FROM tbl_Bacteria WHERE Status  = 1"
    cursor.execute(Query)
    result = cursor.fetchall()
    return result


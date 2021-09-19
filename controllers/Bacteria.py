from flask import render_template, request
import sqlite3
import os
from datetime import datetime
from models.Bacteria import SaveBacteria, GetBacteriaList
currentdir = os.path.dirname(__package__)



def Index():
    result = GetBacteriaList()
    return render_template("Bacteria/Index.html", results = result)

def ABacteria():
    return render_template("Bacteria/ABacteria.html")

def Save():
    name = request.form["bactname"]
    SaveBacteria(name)
    return Index()
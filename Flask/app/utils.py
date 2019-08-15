from .models import WebAPI
from flask import json

def save(query):
    print(query)
    WebAPI.save(query)

def getAll():
    data = WebAPI.getAll()
    

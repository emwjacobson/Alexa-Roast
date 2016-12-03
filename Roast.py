from flask import Flask, render_template
from flask_ask import Ask, statement
import requests as r
import re

app = Flask(__name__)
ask = Ask(app, '/roast')

@ask.launch
def launch():
    roast()

@ask.intent('Roast')
def roast():
    response = r.get('http://www.insultgenerator.org/')
    roast = re.findall('<br><br>(.*?)<\/div>', response.text)
    roast = roast[0]
    return statement(roast)

app.run()

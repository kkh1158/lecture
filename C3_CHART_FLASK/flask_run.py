#------------------------------------------------
# pip install Flask,  requests
#------------------------------------------------

from flask import Flask, session, render_template, make_response, jsonify, request, redirect, url_for

import cx_Oracle
import pandas as pd
import numpy as np
import random

import folium
from folium import plugins
import re
import googlemaps
import pprint

app = Flask(__name__)
app.secret_key = "1111122222"

@app.route('/')
def index():
    m_list = ["LKHJJANG", "February", "March", "April", "May", "June"]
    d_list = [20000, 5312, 6251, 7841, 9821, 14984]

    return render_template('index.html'
                           , KEY_MLIST=m_list
                           , KEY_DLIST=d_list
                           )


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9985)
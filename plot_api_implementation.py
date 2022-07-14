# -*- coding: utf-8 -*-
"""
@author: Vaishali Ravindranath
"""


import json
import requests


url = 'http://127.0.0.1:8000/scatterplot'

input_data_for_model = {
    "df_link": "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv",
    "x": "sepal.length",
    "y": "sepal.width",
    "z": "petal.width",
    "color_attribute": "variety"
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)





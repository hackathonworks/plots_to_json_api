# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
class scatterjs(BaseModel):
    df_link:str
    x:str
    y:str
    z:str
    color_attribute:str
    

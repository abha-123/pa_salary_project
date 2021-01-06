# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:49:43 2021

@author: abhak
"""
import glassdoor_scraper as gs
import pandas as pd

path="C:/Users/abhak/Documents/ds_salary_proj/chromedriver"

df=gs.get_jobs('principle analyst',15,False,path,15)


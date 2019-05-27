#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:43:14 2019

@author: keltoskytoi
"""

# Exercise 3
from pathlib import Path
# import functions from utils here
import utils as ut # es gibt kein utils....
import csv

basedir = Path("/home/keltoskytoi/Python_Kurs/")
data_dir = basedir / "data"
output_dir = basedir / "solution"

# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]

path_file = data_dir / "cars.txt"
print(path_file)

# 2. Read the text file [2P]

with open(path_file, "r") as file:
     content = [line.rstrip() for line in file]
print(content)

# 3. Count the occurences of each item in the text file [2P]

cars_list = list(set(content))
carsfrequ = [] 
for car in cars_list:
    carsfrequ.append(content.count(car))    

print("frequencies\n" + str(carsfrequ) + "\n")

print(carsfrequ)

# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]
if output_dir.is_dir():
    print ("Directory exist")
else:
    output_dir.mkdir()
    
# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...

car_dict = dict(zip(cars_list, carsfrequ))
cars_frequency = output_dir / "cars_frequency.csv"

with open(cars_frequency, 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames =["item","count"])
    writer.writeheader()
    writer = csv.writer(csv_file)
    for key, value in car_dict.items():
        writer.writerow([key, value])
        
    
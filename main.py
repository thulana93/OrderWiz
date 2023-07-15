import pandas as pd
import numpy as np
from word2number import w2n
import math

from numpy import loadtxt

# Loading the order items from text files
with open('myfile.txt') as f:
    lines = [line.rstrip('\n') for line in f]

# print(lines)

df = pd.DataFrame(columns=['Item','Size','Quantity'])
size_list = ['small','medium','large']
items_list = ['coffee','latte','coffees','lattes']
# quantity_list = ?

for i,line in enumerate(lines):
    line_split = line.split()
    # print(line_split)

    for split in line_split:
        split = split.lower()
        if split in size_list:
            df.loc[i,'Size']= split
        elif split in items_list:
            df.loc[i,'Item']= split
        else:
            try:
                if split == 'a':
                    number = 1
                    df.loc[i, 'Quantity'] = number
                else:
                    number = w2n.word_to_num(split)
                    df.loc[i, 'Quantity'] = number
            except:
                print("Not available")
    # df = df.reset_index()
    for index, row in df.iterrows():
        print(row.values)
        for j, item in enumerate(row.values):
            print(index,j)
            if type(item) != int and type(item) != str and math.isnan(item):
                if j == 0:
                    print(f"{df.columns[j]} is not in the menu. Please order something from the menu")
                    break
                elif j == 1:
                    # print(index,j)
                    print(f"What is the size of the {df.loc[index,'Item']}?")
                else:
                    print(f"How many of {df.loc[index,'Item']} do you want to order?")

print(df)


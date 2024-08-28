import pandas as pd
import os

os.chdir("C:\\Users\\Dell\\Documents\\PythonConcepts\\FileConcept\\CSVConcept")

print(pd.read_csv("detail.csv"))

df=pd.DataFrame([["harish",30],["guru",27],["hari",29]],columns=["Name","Rollno"])
df.to_csv("newDetail.csv")
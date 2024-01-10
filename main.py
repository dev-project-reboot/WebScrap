import requests as req
from bs4 import BeautifulSoup as bs
import lxml
import pandas as pd

"""url = input("Enter the url of the html file :")"""
url = "HTML_FILE\Course_ AZ-900_ Microsoft Azure Fundamentals Exam Prep - OCT 2023 _ Udemy Business.html"
html_file = open(url, "r")
index = html_file.read()
soup = bs(index, 'lxml')

tag = soup.find("div", class_ = "ud-app-loader ud-component--course-taking--app ud-app-loaded")
box = tag.find_all("div", class_ = "section--flex--1MW7w")
set1 = []
for i in box :
    set2 = []
    for j in i: 
        set2.append(j.text)
    set1.append(set2)

duration = set1[0][1].split("completed")[1]
no =  set1[0][1].split("/")[1].split("|")[0]

us = [["Section","Duration","No of Lessons"]]
for set in set1 :
    data = []
    data.append(set[0])
    data.append(int(set[1].split("completed")[1].split("min")[0]))
    data.append(int(set[1].split("/")[1].split("|")[0]))
    us.append(data)

all_tasks = tag.find_all("div", class_="curriculum-item-link--item-container--1ptOz")

Sl_no = 0
tasks = [["Sl no","Title","Duration"]]
for w in all_tasks :
    t = []
    Sl_no += 1
    title = w.find("span", class_="truncate-with-tooltip--ellipsis--2-jEx")
    title = title.text
    time = w.find("div", class_="ud-text-xs curriculum-item-link--metadata--e17HG")
    
    if time is None :
        t1 = '10min'
    else :
        t1 = time.find("span").text
    t.append(Sl_no)
    t.append(title)
    t.append(t1)
    tasks.append(t)

us_1 = [["Sl No","Section","Duration","No of Lessons"]]
x = 0
for i in us :
    Sl_no = 0
    
    
    if type(i[2])==int :
        j=i[2]
        
        for k in range (j) :
            u=[]
            x+=1
            u.append(x)
            u.append(i[0])
            u.append(i[1])
            u.append(i[2])
            us_1.append(u)

df_us = pd.DataFrame(us_1)
df_tasks =  pd.DataFrame(tasks)

frame = [df_us,df_tasks]
result = pd.concat(frame,axis=1, join='inner')

result.columns = result.iloc[0]
result = result[1:]


fileName = 'Udemy.xlsx'
result.to_excel(fileName)
print('DataFrame is written to Excel File successfully.')

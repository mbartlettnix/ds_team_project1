import bs4 as bs
import urllib.request
import json
import pandas as pd
import numpy as np


with open("payscale_endpts.json", "r") as file:
    ps_json = json.load(file)

x = 0
for i in ps_json['States']:
    for _ in ps_json['States'][i]:
        x += 1

index = np.arange(x)
df = pd.DataFrame(columns=['occupation','state','city','total_cash_comp_md_pay','base_salary_md_pay','bonus_md_pay','sample_size','last_reviewed'], index=index)


counter = 0
for state in ps_json['States']:
    for city in ps_json['States'][state]:

        sauce = urllib.request.urlopen('https://www.payscale.com/research/US/Job=Data_Scientist%2c_IT/Salary' + city).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
        s = soup.find('script', type='application/ld+json')
        json_info = json.loads(s.text)

        row = []

        row.append(json_info['name'])
        row.append(json_info['occupationLocation'][2]['name'])
        row.append(json_info['occupationLocation'][1]['name'])
        row.append(json_info['estimatedSalary'][0]['median'])
        row.append(json_info['estimatedSalary'][1]['median'])

        try:
            row.append(json_info['estimatedSalary'][2]['median'])
        except:
            row.append(np.nan)

        row.append(json_info['sampleSize'])
        row.append(json_info['mainEntityOfPage']['lastReviewed'])


        df.iloc[counter] = row
        counter += 1

df.to_csv('payscale_ds_salary.csv')

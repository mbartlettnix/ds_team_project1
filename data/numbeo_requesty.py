import pandas as pd
import numpy as np
import config, requests, json

salary_df = pd.read_csv('./salary/payscale_ds_salary.csv')

# new york is used as the base for many indices according the numbeo's documentation
url = "https://www.numbeo.com/api/indices?api_key={}&query=New%20York".format(config.key)
response = requests.get(url)
json_data = json.loads(response.text)

col_select = [k for k, v in json_data.items()]

columns = ['state', 'city']
columns.extend(col_select)
index = np.arange(len(salary_df))

numbeo_indices_df = pd.DataFrame(columns=columns, index=index)


def try_list(lst, cols, numbeo):
    for item in cols:
        try:
            lst.append(numbeo['{}'.format(item)])
        except:
            lst.append(np.nan)


counter = 0
for index, row in salary_df.iterrows():
    url = "https://www.numbeo.com/api/indices?api_key={}&query={}".format(config.key, row['city'])
    response = requests.get(url)
    json_data = json.loads(response.text)

    row_ls = []

    row_ls.append(row['state'])
    row_ls.append(row['city'])


    try_list(row_ls, col_select, json_data)

    numbeo_indices_df.iloc[counter] = row_ls
    counter += 1

numbeo_indices_df.drop('name', axis=1, inplace=True)
numbeo_indices_df.to_csv('./indices/numbeo_ds_indices.csv')

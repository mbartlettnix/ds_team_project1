import pandas as pd
import numpy as np
import config, requests, json, os

# new york is used as the base for many indices according the numbeo's documentation
url = "https://www.numbeo.com/api/indices?api_key={}&query=New%20York".format(config.key)
response = requests.get(url)
json_data = json.loads(response.text)

col_select = [k for k, v in json_data.items()]

columns = ['city']
columns.extend(col_select)

file_path = './cities/'

def try_list(lst, cols, numbeo):
    for item in cols:
        try:
            lst.append(numbeo['{}'.format(item)])
        except:
            lst.append(np.nan)


for filename in os.listdir(file_path):
    if filename.endswith("vicinity.csv"):
        print(filename)
        df = pd.read_csv('{}{}'.format(file_path,filename))
        index = np.arange(len(df))
        numbeo_indices_df = pd.DataFrame(columns=columns, index=index)

        for row, column in df.iterrows():

            city_id = df['city_id'][row]
            url = "https://www.numbeo.com/api/indices?api_key={}&city_id={}".format(config.key, city_id)
            response = requests.get(url)
            json_data = json.loads(response.text)

            row_ls = []

            row_ls.append(df['short_name'][row])

            try_list(row_ls, col_select, json_data)

            numbeo_indices_df.iloc[row] = row_ls

        numbeo_indices_df.drop('name', axis=1, inplace=True)
        numbeo_indices_df.to_csv('./indices/nearby_cities/{}_ds_indices.csv'.format(filename[:-13]))

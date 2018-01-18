import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_single = pd.read_csv('../../../data/indices/benchmark_LA/monetary_conversion/top10_data_labnch_ds_single.csv')
df_family = pd.read_csv('../../../data/indices/benchmark_LA/monetary_conversion/top10_data_labnch_ds_family.csv')
df_la = pd.read_csv('../../../data/indices/benchmark_LA/monetary_conversion/converted_data_labnch.csv')

df_single.drop(['Unnamed: 0'], axis=1, inplace=True)
df_family.drop(['Unnamed: 0'], axis=1, inplace=True)
df_la.drop(['Unnamed: 0'], axis=1, inplace=True)

status = [df_single, df_family]


def monthly(series):
    series.iloc[3] = series.iloc[3] / 12


counter = 0
for df in status:
    countdown = [2, 1, 0]
    name = ['single', 'family']

    for count in countdown:
        city = df.loc[count, 'city']

        place = df.loc[count, ['restaurant_{}_usd'.format(name[counter]), 'groceries_{}_usd'.format(name[counter]), 'rent_{}_usd'.format(name[counter]), 'salary_usd', 'ds_{}_usd'.format(name[counter])]]
        benchmark = df_la.loc[2, ['restaurant_{}_usd'.format(name[counter]), 'groceries_{}_usd'.format(name[counter]), 'rent_{}_usd'.format(name[counter]), 'salary_usd', 'ds_{}_usd'.format(name[counter])]]

        monthly(place)
        monthly(benchmark)


        my_dpi = 96

        fig, ax = plt.subplots(figsize=(1000 / my_dpi, 600 / my_dpi), dpi=my_dpi)
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)


        index = np.arange(len(benchmark))
        bar_width = 0.35

        columns = [k[:-11]for k in place.keys()]
        columns[3] = 'salary'
        columns[4] = 'net living'



        rects1 = plt.barh(index, place, bar_width, color='#2149E8', label='place')

        rects2 = plt.barh(index + bar_width, benchmark, bar_width, color='lightgray', label=city)


        plt.yticks(index + bar_width / 2, columns, color='white', size=20)
        plt.xticks(color='white', size=16)
        ax.yaxis.tick_right()
        ax.vlines(0, -.2, 4.55, color='white')


        leg = plt.legend(loc=3, frameon=False)
        for text in leg.get_texts():
            text.set_color('white')
            text.set_size(16)

        for spine in plt.gca().spines.values():
            spine.set_visible(False)

        plt.tight_layout()
        plt.gca().invert_yaxis()
        plt.gca().invert_xaxis()

        plt.savefig('transparent_{}_{}_qol.png'.format(city, name[counter]))

    counter += 1

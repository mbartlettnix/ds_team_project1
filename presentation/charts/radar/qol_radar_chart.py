import pandas as pd
import matplotlib.pyplot as plt
from math import pi

df = pd.read_csv('./ds_team_project1/data/indices/benchmark_LA/la_benchmark_ds_indices.csv')

df_plot = df[['city', 'state', 'crime_index', 'traffic_index', 'climate_index', 'health_care_index', 'pollution_index']].reset_index(drop=True)


for i in df_plot.columns[2:]:
    df_plot.rename(columns={i: i[:-6]}, inplace=True)


top_threes = ['Cupertino', 'San Diego', 'San Jose', 'Richmond', 'Bellevue']

color = '#000000d0'
text_color = 'white'
cmap = 'README'


for city in top_threes:
    num = df_plot.loc[df_plot['city'] == '{}'.format(city)].index.item()

    categories = list(df_plot)[2:]
    N = len(categories)

    angles = [(n / float(N) * 2 * pi) + .3 for n in range(N)]
    angles += angles[:1]

    values = df_plot.loc[num].drop(['city', 'state']).values.flatten().tolist()
    values += values[:1]

    my_dpi = 96
    fig = plt.figure(figsize=(1000 / my_dpi, 1000 / my_dpi), dpi=my_dpi, facecolor=color)

    if color == '#00000000':
        fig.patch.set_alpha(0)
    else:
        pass

    ax = plt.subplot(111, polar=True)

    plt.xticks(angles[:-1], [])
    ax.set_rlabel_position(90)
    plt.yticks([30, 60, 90, 120, 150], ["30", "60", "90", "120", "150"], color=text_color, size=16)
    plt.ylim(0, 150)


    ax.plot(angles, values, linewidth=3, linestyle='solid')
    ax.set_facecolor(color)

    if color == '#00000000':
        ax.patch.set_alpha(0.2)
    else:
        pass

    ax.fill(angles, values, 'b', alpha=0.5)

    for i in range(N):
        angle_rad = (i / float(N) * 2 * pi) + .3
        ax.text(angle_rad, 168, categories[i], size=24, ha='center', va='center', color=text_color)


    plt.savefig('./ds_team_project1/presentation/charts/radar/{}_{}_qol.png'.format(cmap, city))

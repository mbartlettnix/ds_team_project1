import pandas as pd
import matplotlib.pyplot as plt
from math import pi


df = pd.read_csv('../../../data/indices/numbeo_ds_indices.csv')

df_plot = df[['city', 'state', 'crime_index', 'traffic_index', 'climate_index', 'health_care_index', 'safety_index', 'pollution_index']][1:5].reset_index(drop=True)

for i in df_plot.columns[2:]:
    df_plot.rename(columns={i: i[:-6]}, inplace=True)


def black_widow(row, title, color):
    categories = list(df_plot)[2:]
    N = len(categories)

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    ax = plt.subplot(2, 2, row + 1, polar=True, )

    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    plt.xticks(angles[:-1], categories, color='grey', size=8)

    ax.set_rlabel_position(0)
    plt.yticks([30, 60, 90, 120, 150], ["30", "60", "90", "120", "150"], color="grey", size=7)
    plt.ylim(0, 150)

    values = df_plot.loc[row].drop(['city', 'state']).values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    plt.title(title, size=11, color=color, y=1.1)
    plt.tight_layout()


# initialize the figure
my_dpi = 120
plt.figure(figsize=(1000 / my_dpi, 1000 / my_dpi), dpi=my_dpi)

# create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df_plot.index))

for row in range(0, len(df_plot.index)):
    black_widow(row=row, title=df_plot['city'][row] + ', ' + df_plot['state'][row], color=my_palette(row))

plt.savefig('./charts/test_img.png')

# check the plot
# plt.show()

import pandas as pd
import os

df = pd.read_csv('../ml_adjusted_ds_indices.csv')

# select the city to normalize to
# normalizing for monetary conversion values
w, x, y, z = df[2:3][['cpi_index', 'restaurant_price_index', 'rent_index', 'groceries_index']].values.tolist()[0]
cpi = 100 / w
rest = 100 / x
rent = 100 / y
groc = 100 / z


def monetary_translate(df):
    for r, v in df.iterrows():
        old_cpi = df['cpi_index'][r]
        old_rest = df['restaurant_price_index'][r]
        old_rent = df['rent_index'][r]
        old_groc = df['groceries_index'][r]

        df['cpi_index'][r] = old_cpi * cpi
        df['restaurant_price_index'][r] = old_rest * rest
        df['rent_index'][r] = old_rent * rent
        df['groceries_index'][r] = old_groc * groc


# normalize the non-monetary features to los angeles
a, b, c, d, e, f, g, h, i, j = df[2:3][['crime_index', 'traffic_time_index', 'climate_index', 'safety_index', 'traffic_co2_index', 'traffic_inefficiency_index', 'quality_of_life_index', 'health_care_index', 'traffic_index', 'pollution_index']].values.tolist()[0]

crm = 100 / a
trtm = 100 / b
clmt = 100 / c
sfty = 100 / d
trca = 100 / e
trin = 100 / f
qol = 100 / g
hcre = 100 / h
trfc = 100 / i
pltn = 100 / j


def non_monetary_translate(df):
    for r, v in df.iterrows():
        old_crm = df['crime_index'][r]
        old_trtm = df['traffic_time_index'][r]
        old_clmt = df['climate_index'][r]
        old_sfty = df['safety_index'][r]
        old_trca = df['traffic_co2_index'][r]
        old_trin = df['traffic_inefficiency_index'][r]
        old_qol = df['quality_of_life_index'][r]
        old_hcre = df['health_care_index'][r]
        old_trfc = df['traffic_index'][r]
        old_pltn = df['pollution_index'][r]

        df['crime_index'][r] = old_crm * crm
        df['traffic_time_index'][r] = old_trtm * trtm
        df['climate_index'][r] = old_clmt * clmt
        df['safety_index'][r] = old_sfty * sfty
        df['traffic_co2_index'][r] = old_trca * trca
        df['traffic_inefficiency_index'][r] = old_trin * trin
        df['quality_of_life_index'][r] = old_qol * qol
        df['health_care_index'][r] = old_hcre * hcre
        df['traffic_index'][r] = old_trfc * trfc
        df['pollution_index'][r] = old_pltn * pltn


# modify nearby cities to use benchmark
for filename in os.listdir('../nearby_cities/'):
    nearby_df = pd.read_csv('../nearby_cities/' + filename)
    monetary_translate(nearby_df)
    non_monetary_translate(nearby_df)
    nearby_df.drop(['Unnamed: 0', 'cpi_and_rent_index', 'purchasing_power_incl_rent_index', 'property_price_to_income_ratio'], axis=1, inplace=True)
    nearby_df.to_csv('./nearby_cities/{}_ds_labnch_indices.csv'.format(filename[:-15]))


# modify main 42 target cities dataset to use benchmark
monetary_translate(df)
non_monetary_translate(df)
df.drop(['Unnamed: 0', 'cpi_and_rent_index', 'purchasing_power_incl_rent_index', 'property_price_to_income_ratio'], axis=1, inplace=True)
df.to_csv('la_benchmark_ds_indices.csv')

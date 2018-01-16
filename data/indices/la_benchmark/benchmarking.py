import pandas as pd

df = pd.read_csv('../ml_adjusted_ds_indices.csv')

w, x, y, z = df[2:3][['cpi_index', 'restaurant_price_index', 'rent_index', 'groceries_index']].values.tolist()[0]
la_cpi = 100 / w
la_rest = 100 / x
la_rent = 100 / y
la_groc = 100 / z


for r, v in df.iterrows():
    old_cpi = df['cpi_index'][r]
    old_rest = df['restaurant_price_index'][r]
    old_rent = df['rent_index'][r]
    old_groc = df['groceries_index'][r]

    df['cpi_index'][r] = old_cpi * la_cpi
    df['restaurant_price_index'][r] = old_rest * la_rest
    df['rent_index'][r] = old_rent * la_rent
    df['groceries_index'][r] = old_groc * la_groc

df.to_csv('target42_ds_indices.csv')

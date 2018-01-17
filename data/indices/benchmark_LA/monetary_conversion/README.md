# Indices explanations:
We collect four different indices: 'cpi_index','rent_index','groceries_index','restaurant_price_index'.
These indices are relative to Los Angeles(LA). Which means that for Los Angeles, each index should be 100(%). 
If another city has, for example, rent index of 120, 
it means that on an average in that city rents are 20% more expensive than in Los Angeles. 
If a city has rent index of 70, that means on an average in that city rents are 30% less expensive than in Los Angeles.
* P.S. You may find out the indices of LA are not 100(%). Because we convert indices to prices based on LA((100)%)then take average of LA and its nearby cities. It will not affect the results.
     
# Columns explanations:
* cpi_single_usd = cpi_index / 100 * la_based_data
* cpi_family_usd = cpi_index / 100 * la_based_data
* rent_single_usd = rent_index / 100 * la_based_data
* rent_family_usd = rent_index / 100 * la_based_data
* groceries_single_usd = groceries_index / 100 * la_based_data
* groceries_family_usd = groceries_index / 100 * la_based_data
* restaurant_single_usd = restaurant_price_index / 100 * la_based_data
* restaurant_family_usd = restaurant_price_index / 100 * la_based_data
* col_single_usd = cpi_single_usd + rent_single_usd
* col_family_usd = cpi_family_usd + rent_family_usd
* ds_single_usd = base_salary_md_pay / 12 - col_single_usd
* ds_family_usd = base_salary_md_pay / 12 - col_family_usd


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

# Assumptions break down:
* 1. Single:
  * 1).Members of your household: 1
  * 2).Eating lunch or dinner in restaurants: 50% of the time
  * 3).When eating in restaurants you are chosing inexpensive restaurants: 80% of the time
  * 4).Drinking Coffee outside of your home: High
  * 5).Going out (cinema, night life, etc.): average(once per week per household member)
  * 6).Smoking (household overall):  0.0 packs of cigarettes per day
  * 7).Alcoholic beverages (consume): Moderate
  * 8).At home we are eating: Western food
  * 9).Driving car: Moderate
  * 10).Taking Taxi: No
  * 11).Paying for public transport tickets: None
  * 12).Sport Memberships: No
  * 13).Vacation and Travel:  Two per year (one week each), relatively expensive
  * 14).Buying Clothing and Shoes: Moderate 

* 2. Family:
  * 1).Members of your household: 4
  * 2).Eating lunch or dinner in restaurants: 25% of the time
  * 3).When eating in restaurants you are chosing inexpensive restaurants: 30% of the time
  * 4).Drinking Coffee outside of your home: High
  * 5).Going out (cinema, night life, etc.): very low(twice per month per household member)
  * 6).Smoking (household overall):  0.0 packs of cigarettes per day
  * 7).Alcoholic beverages (consume): low
  * 8).At home we are eating: Western food
  * 9).Driving car: Moderate
  * 10).Taking Taxi: No
  * 11).Paying for public transport tickets: None
  * 12).Sport Memberships: 2 Household members
  * 13).Vacation and Travel:  onece per year (one week each), relatively expensive
  * 14).Buying Clothing and Shoes: Moderate 


* Los Angeles as Benchmark (Monthly)
* Single: (https://www.numbeo.com/cost-of-living/city-estimator/in/Los-Angeles?displayCurrency=USD&members=1&restaurants_percentage=50.0&inexpensive_restaurants_percentage=80.0&drinking_coffee_outside=200.0&going_out_monthly=4.2&smoking_packs_per_day=0.0&alcoholic_drinks=25.0&type_of_food=0&driving_car=40.0&taxi_consumption=0.0&paying_for_public_transport=None&sport_memberships=0.0&vacation=100.0&clothing_and_shoes=50.0&rent=none&displayCurrency=USD&members=1&restaurants_percentage=50.0&inexpensive_restaurants_percentage=80.0&drinking_coffee_outside=200.0&going_out_monthly=4.2&smoking_packs_per_day=0.0&alcoholic_drinks=25.0&type_of_food=0&driving_car=40.0&taxi_consumption=0.0&paying_for_public_transport=None&sport_memberships=0.0&vacation=100.0&clothing_and_shoes=50.0&rent=none)
  * 1.cpi(life expense without rent): $1760.35
  * 2.rent: (2075.33+1582.08)/2 = $1828.705
  * 3.groceries: $241.80
  * 4.restaurant: $667.70

* Family: (https://www.numbeo.com/cost-of-living/city-estimator/in/Los-Angeles?displayCurrency=USD&members=4&restaurants_percentage=25.0&inexpensive_restaurants_percentage=30.0&drinking_coffee_outside=200.0&going_out_monthly=2&smoking_packs_per_day=0.0&alcoholic_drinks=10.0&type_of_food=0&driving_car=40.0&taxi_consumption=0.0&paying_for_public_transport=None&sport_memberships=2.0&vacation=51.0&clothing_and_shoes=50.0&rent=none&displayCurrency=USD&members=4&restaurants_percentage=25.0&inexpensive_restaurants_percentage=30.0&drinking_coffee_outside=200.0&going_out_monthly=2&smoking_packs_per_day=0.0&alcoholic_drinks=10.0&type_of_food=0&driving_car=40.0&taxi_consumption=0.0&paying_for_public_transport=None&sport_memberships=2.0&vacation=51.0&clothing_and_shoes=50.0&rent=none)
  * 1.cpi(life expense without rent): $4791.38
  * 2.rent: (3466.02+2722.98)/2 = $3094.5
  * 3.groceries: $1209.02
  * 4.restaurant: $1877.15

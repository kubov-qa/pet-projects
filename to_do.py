MORTGAGE_MONTHS = 240
MORTGAGE_SPREAD = 3.0 
MEDIAN_COEFFICIENT = 93 / 129 # ~0.72 (коэффициент приведения средней ЗП к медиане)

temp_rent_per_month = 39_000
temp_price_per_meter = 215_000
temp_salary = 129_000 * 0.87
temp_property_price = temp_price_per_meter * 40
temp_cbr_rate = 9
temp_total_mortage_percents = (temp_cbr_rate + MORTGAGE_SPREAD) / 100




def price_to_income_ratio(salary, property_price):
  return property_price / salary

def annual_rent_in_sqm(rent_price_1bedroom, price_per_sqm_secondary):
  return (rent_price_1bedroom * 12) / price_per_sqm_secondary 

def annual_salary_in_sqm(salary_average, price_per_sqm_secondary):
  return (salary_average * 12) / price_per_sqm_secondary

   

print(annual_rent_in_sqm(temp_rent_per_month, temp_price_per_meter))
print(annual_salary_in_sqm(temp_salary, temp_price_per_meter))
print(price_to_income_ratio(temp_salary, temp_property_price))








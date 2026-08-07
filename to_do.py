MORTGAGE_MONTHS = 240
MORTGAGE_SPREAD = 3.0 
MEDIAN_COEFFICIENT = 93 / 129 # ~0.72 (коэффициент приведения средней ЗП к медиане)

temp_rent_per_month = 39_000
temp_price_per_meter = 215_000
temp_salary = 129_000 * 0.87
temp_property_price = temp_price_per_meter * 40
temp_cbr_rate = 9
temp_total_mortage_percents = (temp_cbr_rate + MORTGAGE_SPREAD) / 100

def apply_tax(before_tax):
  return before_tax * 0.87

def remove_downpayment (price):
  return price * 0.80

def calculate_apartment_price(price_per_sqm, meters_qty=40):
  return price_per_sqm * meters_qty

def price_to_income_ratio(salary, property_price):
  return property_price / salary

def annual_rent_in_sqm(rent_price_1bedroom, price_per_sqm_secondary):
  return (rent_price_1bedroom * 12) / price_per_sqm_secondary 

def annual_salary_in_sqm(salary_average, price_per_sqm_secondary):
  return (salary_average * 12) / price_per_sqm_secondary

def mortgage_affordability_index(price_per_sqm, salary):
  apartment_price = price_per_sqm * 40
  monthly_mortgage_payment = apartment_price / MORTGAGE_MONTHS
  percentage_of_salary = (monthly_mortgage_payment / salary) * 100
  return percentage_of_salary
   

print(annual_rent_in_sqm(temp_rent_per_month, temp_price_per_meter))
print(annual_salary_in_sqm(temp_salary, temp_price_per_meter))
print(price_to_income_ratio(temp_salary, temp_property_price))
print(mortgage_affordability_index(temp_price_per_meter, temp_salary))








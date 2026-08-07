temp_rent_per_month = 39_000
temp_price_per_meter = 215_000
temp_salary = 129_000 * 0.87
temp_property_price = temp_price_per_meter * 40

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

print(annual_rent_in_sqm(temp_rent_per_month, temp_price_per_meter))
print(annual_salary_in_sqm(temp_salary, temp_price_per_meter))
print(price_to_income_ratio(temp_salary, temp_property_price))



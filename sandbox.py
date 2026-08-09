


temp_rent_per_month = 39_000
temp_price_per_meter = 215_000
temp_salary = 129_000
temp_cbr_rate = 9
temp_annual_rate_decimal = (temp_cbr_rate + MORTGAGE_SPREAD) / 100 #используется в mortgage_per_month()
temp_property_price = 10_000_000 #используется в mortgage_per_month()


#аппрув но пойдет на доработку
def mortgage_per_month(property_price, mortgage_percents, mortgage_months=240):
  i = mortgage_percents / 12
  numerator = i * (1 +i) ** mortgage_months
  denominator = (1 + i) ** mortgage_months - 1
  return property_price * numerator / denominator

print(mortgage_per_month(temp_property_price, temp_annual_rate_decimal, MORTGAGE_MONTHS))

#промежуточный финал
def mortgage_affordability_index(monthly_mortgage_payment, salary):
  percentage_of_salary = (monthly_mortgage_payment / salary) * 100
  return percentage_of_salary

#промежуточный финал
def price_after_downpayment(price, downpayment_percent=20):
  return price * (1 - (downpayment_percent / 100))

#промежуточный финал
def calculate_apartment_price(price_per_sqm, square_meters):
  return price_per_sqm * square_meters



#calculate_apartment_price(temp_price_per_meter, APARTMENT_SIZES_SQM.get("one_room"))

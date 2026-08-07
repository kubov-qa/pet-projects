MORTGAGE_MONTHS = 240 #используется в mortgage_per_month()
MORTGAGE_SPREAD = 3.0 
MEDIAN_COEFFICIENT = 93 / 129 # ~0.72 (коэффициент приведения средней ЗП к медиане)

temp_rent_per_month = 39_000
temp_price_per_meter = 215_000
temp_salary = 129_000 * 0.87
temp_property_price = temp_price_per_meter * 40
temp_cbr_rate = 9
temp_annual_rate_decimal = (temp_cbr_rate + MORTGAGE_SPREAD) / 100 #используется в mortgage_per_month()
temp_property_price = 10_000_000 #используется в mortgage_per_month()



def mortgage_per_month(property_price, mortgage_percents, mortgage_months=240):
  i = mortgage_percents / 12
  numerator = i * (1 +i) ** mortgage_months
  denominator = (1 + i) ** mortgage_months - 1
  return property_price * numerator / denominator

print(mortgage_per_month(temp_property_price, temp_annual_rate_decimal, MORTGAGE_MONTHS))


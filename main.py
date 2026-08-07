MORTGAGE_MONTHS = 240
MORTGAGE_SPREAD = 3.0 
MEDIAN_COEFFICIENT = 93 / 129 # ~0.72 (коэффициент приведения средней ЗП к медиане)

temp_rent_per_month = 39_000
temp_price_per_meter = 215_000
temp_salary = 129_000 * 0.87
temp_property_price = temp_price_per_meter * 40
temp_cbr_rate = 9
temp_total_mortage_percents = (temp_cbr_rate + MORTGAGE_SPREAD) / 100
temp_property_price = 10_000_000

print(temp_total_mortage_percents)

numerator = 0.01 * (1 + 0.01) ** 240
denominator = (1 + 0.01) ** 240 - 1
result = 10_000_000 * numerator / denominator
print(result)

def mortage_per_month(property_price, mortage_percents, mortage_months=240):
  numerator = (mortage_percents / 12) * (1 + (mortage_percents / 12)) ** 240
  denominator = (1 + (mortage_percents / 12)) ** mortage_months - 1
  result = property_price * (numerator / denominator)
  return result

print(mortage_per_month(temp_property_price, temp_total_mortage_percents, ))
def salary_tax(salary):
  return salary * 0.87

def remove_downpayment (property_price):
  return property_price * 0.80

def final_price(price_per_sqm, meters_qty=40):
  return price_per_sqm * meters_qty

def affordability(salary, property_price):
  return property_price / salary

zepka = 100_000
msk_price_per_sqm = 300_000

zepka_after_tax = salary_tax(zepka)
print(zepka_after_tax)
hata_price = remove_downpayment(final_price(msk_price_per_sqm))
print(hata_price)
how_much = affordability(zepka_after_tax, hata_price)
print(how_much)


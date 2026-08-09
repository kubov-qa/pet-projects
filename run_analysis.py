import housing_math as hm

avg_salary_gross = 129_000
avg_sqm_price = 215_000

median_salary_net = hm.convert_avg_to_median(hm.apply_tax(avg_salary_gross))

loan_amount = hm.price_after_downpayment(hm.calculate_apartment_price(avg_sqm_price, hm.APARTMENT_SIZES_SQM["one_room"]), 20)

print(loan_amount)

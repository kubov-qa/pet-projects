import housing_math as hm

avg_salary_gross = 129_000
avg_sqm_price = 215_000
temp_cbr_rate = 14
temp_annual_rate_decimal = (temp_cbr_rate + hm.MORTGAGE_SPREAD) / 100

median_salary_net = hm.convert_avg_to_median(hm.apply_tax(avg_salary_gross))

loan_amount = hm.price_after_downpayment(hm.calculate_apartment_price(avg_sqm_price, hm.APARTMENT_SIZES_SQM["one_room"]), 20)

monthly_mortgage_payment = hm.mortgage_per_month(loan_amount, temp_annual_rate_decimal, hm.MORTGAGE_MONTHS)

affordability_index = hm.mortgage_affordability_index(monthly_mortgage_payment, median_salary_net)

print(affordability_index)
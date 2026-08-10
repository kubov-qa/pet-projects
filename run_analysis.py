import json
import housing_math as hm

with open("historical_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for record in data:
    avg_salary_gross = record.get("salary_average")
    avg_sqm_price = record.get("price_per_sqm_secondary")
    cbr_rate = record.get("cbr_key_rate")
    annual_rate_decimal = (cbr_rate + hm.MORTGAGE_SPREAD) / 100

    median_salary_net = hm.convert_avg_to_median(
        hm.apply_tax(avg_salary_gross))

    loan_amount = hm.price_after_downpayment(hm.calculate_apartment_price(
        avg_sqm_price, hm.APARTMENT_SIZES_SQM["one_room"]), 20)

    monthly_mortgage_payment = hm.mortgage_per_month(
        loan_amount, annual_rate_decimal, hm.MORTGAGE_MONTHS)

    affordability_index = hm.mortgage_affordability_index(
        monthly_mortgage_payment, median_salary_net)

    print(f'Индекс доступности в {record.get("year")}: {affordability_index:.2f}%. Цена за м² — {avg_sqm_price:,.0f} ₽, платёж по ипотеке — {monthly_mortgage_payment:,.0f} ₽/мес, ЗП после налогов — {median_salary_net:,.0f} ₽')

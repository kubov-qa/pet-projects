


#промежуточный финал
def mortgage_affordability_index(monthly_mortgage_payment, salary):
  """Вычисляет индекс доступности ипотеки — долю ежемесячного платежа от зарплаты.
  Args:
    monthly_mortgage_payment (int | float): Размер ежемесячного платежа по ипотеке.
    salary (int | float): Зарплата (после вычета налога и приведения к медиане).
  Returns:
    float: Процент зарплаты, который уходит на ежемесячный платёж по ипотеке.
  """
  percentage_of_salary = (monthly_mortgage_payment / salary) * 100
  return percentage_of_salary





#calculate_apartment_price(temp_price_per_meter, APARTMENT_SIZES_SQM.get("one_room"))

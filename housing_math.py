MORTGAGE_MONTHS = 240 
MORTGAGE_SPREAD = 3.0
TAX_COEFFICIENT = 0.87
MEDIAN_COEFFICIENT = 93 / 129 # ~0.72 (коэффициент приведения средней ЗП к медиане)
APARTMENT_SIZES_SQM = {
    "one_room": 40,
    "two_room": 55,
}


def apply_tax(before_tax):
  """Применяет налоговый коэффициент к сумме до вычета налога.
  Args:
    before_tax (int | float): Сумма до вычета налога.
  Returns:
    float: Сумма после вычета налога.
  """
  return before_tax * TAX_COEFFICIENT


def convert_avg_to_median(average_salary):
  """Конвертирует среднюю ЗП в медианную.
  Args:
    average_salary (int | float): Средняя зарплата.
  Returns:
    float: Медианная зарплата.
  """
  return average_salary * MEDIAN_COEFFICIENT


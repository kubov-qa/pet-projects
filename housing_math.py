MORTGAGE_MONTHS = 240
MORTGAGE_SPREAD = 3.0
TAX_COEFFICIENT = 0.87
# ~0.72 (коэффициент приведения средней ЗП к медиане)
MEDIAN_COEFFICIENT = 93 / 129
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


def calculate_apartment_price(price_per_sqm, square_meters):
    """Вычисляет полную стоимость квартиры.

    Args:
      price_per_sqm (int | float): Цена за квадратный метр.
      square_meters (int | float): Площадь квартиры в квадратных метрах.

    Returns:
      float: Полная стоимость квартиры.
    """
    return price_per_sqm * square_meters


def price_after_downpayment(price, downpayment_percent=20):
    """Вычисляет сумму кредита за вычетом первоначального взноса.

    Args:
      price (int | float): Полная стоимость объекта.
      downpayment_percent (int | float): Размер первоначального взноса в процентах. По умолчанию 20.

    Returns:
      float: Сумма, которая идёт в кредит (после вычета ПВ).
    """
    return price * (1 - (downpayment_percent / 100))


def mortgage_per_month(property_price, mortgage_percents, mortgage_months=240):
    """Вычисляет ежемесячный аннуитетный платёж по ипотеке.

    Args:
      property_price (int | float): Сумма кредита (тело кредита).
      mortgage_percents (float): Годовая процентная ставка в долях (например, 0.12 для 12%).
      mortgage_months (int): Срок ипотеки в месяцах. По умолчанию 240.

    Returns:
      float: Размер ежемесячного платежа по ипотеке.
    """
    i = mortgage_percents / 12
    numerator = i * (1 + i) ** mortgage_months
    denominator = (1 + i) ** mortgage_months - 1
    return property_price * numerator / denominator


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

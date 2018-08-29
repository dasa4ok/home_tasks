# 14. Программа конвертер валют (для валют: евро, доллар, гривна, рубль, фунт) должна переводить из любой валюты в любую. Курсы хардкодим.
# Пример:
# —————————————— Введите валюту:
# UAH
# Введите сумму:
# 2600
# В какой валюте получить результат? USD
# 2600 UAH = 100 USD ———————————————
from_currency = input('Введите валюту(EUR, USD, UAH, RUB, GBP): ')
quantity = int(input('Введите сумму: '))
to_currency = input('В какой валюте получить результат? ')

def currency_converter(from_currency, quantity, to_currency):
    currency = {
        'EUR': {'USD': 1.1674,'UAH': 32.37115,'RUB': 78.49150,'GBP': 0.90574}, #сколько едениц можно купить на один евро (по порядку доллар, гривна, рубль, фунт)
        'USD': {'EUR': 0.85666,'UAH': 27.86705,'RUB': 67.22324,'GBP': 0.77592},
        'UAH': {'EUR': 0.03074,'USD': 0.03589,'RUB': 2.41090,'GBP': 0.02785},
        'RUB': {'EUR': 0.01275,'USD': 0.01489,'UAH': 0.41493,'GBP': 0.01155},
        'GBP': {'EUR': 1.10393,'USD': 1.28883,'UAH': 35.92883,'RUB': 86.68966}
    }
    result = (currency[from_currency.upper()][to_currency.upper()]) * quantity
    result_for_print = [quantity, from_currency.upper(), '=', result, to_currency.upper()]
    return (' '.join([str(i) for i in result_for_print]))

print(currency_converter(from_currency, quantity, to_currency))






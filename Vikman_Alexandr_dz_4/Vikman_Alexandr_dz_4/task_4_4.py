from utils import currency_rates
a=currency_rates('http://www.cbr.ru/scripts/XML_daily.asp','usd')
print(a)
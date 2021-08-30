from forex_python.converter import CurrencyRates

c = CurrencyRates()


print(c.get_rate('EUR','USD'))
print(c.convert('INR','USD',20))
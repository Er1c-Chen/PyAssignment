import pandas as pd

cart = pd.DataFrame([['1', '2', '3']], columns=['name', 'price', 'amount'])
cart.pd.append([['5', '6', '7']])
print(cart)
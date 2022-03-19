import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader as web

tickers = ['AAPL', 'TSLA', 'FB', 'NVDA', 'AMZN', 'GOOG']
amounts = [7, 5, 12,16,2,4]
prices = []
total = []

someboolean = True
while(someboolean):
    ticker = input("What stock do you want to add?")
    amount = input("How many shares?")
    tickers.append()

for ticker in tickers:
    df = web.DataReader(ticker, 'yahoo', dt.datetime(2019,8,1), dt.datetime.now())
    price = df[-1:]['Close'][0]
    prices.append(price)
    index = prices.index(price)
    total.append(price * amount)

print(prices)
print(total)

fig,ax = plt.subplots(figsize=(16,8))
ax.tick_params(axis='x', color = 'white')
ax.tick_params(axis='y', color = 'white')

ax.set_title('PORTFOLIO VISUALIZER', color = "#EF6C35", fontsize = 20)

patches, texts, autotexts =ax.pie(total, labels=tickers, autopct="%1.1f%%",pctdistance=0.8)
[text.set_color("white") for text in texts]

#makes it into a ring chart
my_circle = plt.Circle((0,0), 0.55, color="black")
plt.gca().add_artist(my_circle)

ax.text(-2, 1, 'PORTFOLIO OVERVIEW', fontsize=14, color='FFE536', verticalalignment='center', horizontalalignment='center')
ax.text(-2, 0.85, f'Total USD Amount: {sum(total):.2f}$', fontsize = 12, color='white', verticalalignment='center', horizontalalignment = 'center')
#.2f in the f string is decimal places

counter = 0.15
for ticker in tickers:
    ax.text(-2, 0.85 - counter, f'{ticker}: {total[tickers.index(ticker)]:.2f} $', fontsize=12, color='white', verticalalignment = 'center', horizontalalignment = 'center')
    counter += 0.15

plt.show()
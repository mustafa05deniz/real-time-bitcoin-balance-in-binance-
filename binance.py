

from binance.client import Client
client = Client("appkey", "appsecret")
import time
hepsi =  client.get_account()
first_dict = {}
second_dict = {}



for i in hepsi["balances"]:
    if(float(i["locked"]) != 0):
        first_dict[i["asset"]] = float(i["locked"])

print first_dict


for x in first_dict:
    print x,first_dict[x]


while True:
    balance = 0
    for assest in first_dict:
        tradess = client.get_recent_trades(symbol= assest+'BTC')
        balance = balance + (float(first_dict[assest]) * float(tradess[0]["price"]))


    usd_btc_last_trades = client.get_recent_trades(symbol='BTCUSDT')
    usd_btc = float(usd_btc_last_trades[0]["price"])

    estimated_value ="%.2f" % float(balance * usd_btc)

    print "estimated value " +str(estimated_value) + "$"

    time.sleep(1) 

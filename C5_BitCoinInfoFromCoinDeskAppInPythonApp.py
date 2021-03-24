import requests
resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
binfo = resp.json()
print("Value At Time:",binfo.get('time')['updated'])
print("1 Bitcoin: $",binfo.get('bpi').get('USD').get('rate'))
print("1 Bitcoin: GBP",binfo.get('bpi').get('GBP').get('rate'))
print("1 Bitcoin: EUR",binfo.get('bpi').get('EUR').get('rate'))

# **TradingApi - Flask REST API server with cryptocurrency data collected by hft_algo project**

SERVER: http://host:5000/

## **Endpoints**

### **/exchanges**

```python
{"exchanges":["zonda","wazirx","bitkub","huobi","gemini","bitso"]}
```

### **/markets**

```python
{"markets":[{"wazirx":"btcinr"},{"wazirx":"ethinr"},{"wazirx":"dogeinr"},{"wazirx":"maticinr"},{"wazirx":"adainr"},{"wazirx":"ftminr"},{"wazirx":"xrpinr"},{"wazirx":"sandinr"},{"wazirx":"usdtinr"},{"wazirx":"solinr"},{"wazirx":"manainr"},{"wazirx":"dotinr"},{"wazirx":"lunainr"},{"wazirx":"trxinr"},{"wazirx":"vetinr"},{"wazirx":"lunausdt"},{"wazirx":"ethusdt"},{"bitkub":"btcthb"},{"bitkub":"eththb"},{"bitkub":"dogethb"},{"bitkub":"manathb"},{"bitkub":"usdtthb"},{"bitkub":"adathb"},{"bitkub":"sandthb"},{"bitkub":"dotthb"},{"bitkub":"sushithb"},{"bitkub":"galathb"},{"bitkub":"yfithb"},{"bitkub":"linkthb"},{"bitkub":"imxthb"},{"bitkub":"nearthb"},{"bitkub":"crvthb"},{"bitkub":"unithb"},{"zonda":"btcpln"},{"zonda":"ethpln"},{"zonda":"lunapln"},{"zonda":"ftmpln"},{"zonda":"btceur"},{"zonda":"xrppln"},{"zonda":"etheur"},{"zonda":"adapln"},{"zonda":"maticpln"},{"zonda":"usdtpln"},{"zonda":"dotpln"},{"zonda":"avaxpln"},{"zonda":"dogepln"},{"zonda":"trxpln"},{"zonda":"manapln"},{"zonda":"linkpln"},{"huobi":"btcusdt"},{"huobi":"ethusdt"},{"huobi":"shibusdt"},{"huobi":"avaxusdt"},{"huobi":"filusdt"},{"huobi":"adausdt"},{"huobi":"solusdt"},{"huobi":"xrpusdt"},{"huobi":"trxusdt"},{"huobi":"galausdt"},{"huobi":"manausdt"},{"huobi":"dotusdt"},{"huobi":"lunausdt"},{"huobi":"sandusdt"},{"huobi":"dogeusdt"},{"huobi":"axsusdt"},{"huobi":"maticusdt"},{"gemini":"btcusd"},{"gemini":"ethusd"},{"gemini":"dogeusd"},{"gemini":"maticusd"},{"gemini":"sushiusd"},{"gemini":"ftmusd"},{"gemini":"linkusd"},{"gemini":"sandusd"},{"gemini":"filusd"},{"gemini":"galausd"},{"gemini":"manausd"},{"gemini":"lrcusd"},{"gemini":"lunausd"},{"gemini":"crvusd"},{"gemini":"aaveusd"},{"gemini":"uniusd"},{"gemini":"axsusd"},{"bitso":"xrpmxn"},{"bitso":"btcmxn"},{"bitso":"ethmxn"},{"bitso":"manamxn"},{"bitso":"ltcusd"},{"bitso":"btcbrl"},{"bitso":"linkusd"},{"bitso":"batmxn"},{"bitso":"btcusd"},{"bitso":"xrpusd"},{"bitso":"aaveusd"},{"bitso":"ethbrl"},{"bitso":"shibusd"},{"bitso":"sandusd"},{"bitso":"ftmusd"}]}
```

### **/trades&ex=exchange&market=market&limit=limit**

***example:*** "/trades&ex=zonda&market=btcpln&limit=5"

```python
{"data":[{"amount":0.00010239,"id":"d7f1ceb9-b3df-11ec-8d23-0242ac110011","price":195318.55,"timestamp":1649053452367},
         {"amount":0.00013853,"id":"a9da2f8d-b3df-11ec-8d23-0242ac110011","price":194908.87,"timestamp":1649053375037},
         {"amount":0.00136295,"id":"9894a52a-b3df-11ec-8d23-0242ac110011","price":194500.0,"timestamp":1649053346060},
         {"amount":0.00769577,"id":"131ed862-b3df-11ec-8d23-0242ac110011","price":194912.1,"timestamp":1649053122151},
         {"amount":0.02308728,"id":"ef4487fc-b3de-11ec-8d23-0242ac110011","price":194912.5,"timestamp":1649053062000}],"status":"ok"}
```

### **/orderbook&ex=exchange>&market=market>&limit=limit**

***example:*** "/orderbook&ex=zonda&market=btcpln&limit=2"

```python
{"data":[{"asks":[[195316.52,0.2503491],[195316.53,0.8133],
                  [195316.57,0.00109601],[195316.59,0.02580506],
                  [195316.96,0.78897189],[195320.99,0.03028583],
                  [195321.0,0.00171909],[195815.37,1.0],
                  [195962.94,8.1646],[196000.0,0.001]],
          "bids":[[193501.02,0.23950256],[193513.27,0.00071374],
                  [194000.0,0.00672095],[194000.1,0.0312414],
                  [194000.14,0.01879785],[194000.15,0.8133],
                  [194001.02,0.43580272],[194480.25,0.13333333],
                  [194500.0,0.02948538],[194500.01,0.00025077]],"timestamp":[1649053492754]},
         {"asks":[[195316.83,0.23678278],[195316.88,0.02580506],
                  [195316.94,0.8133],[195316.96,0.78897189],
                  [195317.72,0.0010698],[195320.99,0.03028583],
                  [195321.0,0.00171909],[195815.38,0.02882071],
                  [195815.39,1.0],[195962.94,8.1646]],
          "bids":[[193500.0,0.50129199],[193500.01,0.14327398],
                  [193509.19,0.0005871],[194000.0,0.00672095],
                  [194000.1,0.0312414],[194000.14,0.01879785],
                  [194000.15,0.8133],[194001.02,0.43580272],
                  [194500.0,0.02948538],[194500.01,0.1335841]],"timestamp":[1649053487455]}],"status":"ok"}
```


### **/orderbook_range&ex=exchange&market=market&ts_range=ts_from,ts_to**

***example:*** "/orderbook_range&ex=bitkub&market=adathb&ts_range=1644077417,1644077422"

```python
{"data":[{"asks":[[38.08,2605.8477119],[38.09,314.70480757],[38.09,167.5],[38.11,131.0255068],[38.11,65990.628],[38.12,17991.0],[38.14,314.70480757],[38.17,4413.06266548],[38.18,314.70480757],[38.19,1389.6]],"bids":[[38.0,0.03976178],[38.0,5e-05],[38.0,0.01999648],[37.97,0.0038437],[37.96,0.01195248],[37.94,0.0073783],[37.94,0.0073783],[37.93,4.21505105],[37.93,0.01193675],[37.91,0.00062575]],"timestamp":[1644077417]},{"asks":[[38.05,149.21],[38.06,2591.76069705],[38.08,660.69804097],[38.09,314.70480757],[38.11,131.0255068],[38.11,65990.628],[38.12,17991.0],[38.14,314.70480757],[38.17,4413.06266548],[38.18,314.70480757]],"bids":[[38.0,0.03976178],[38.0,5e-05],[38.0,0.01999648],[37.99,0.01195563],[37.98,0.00592601],[37.97,0.0038437],[37.97,0.00531655],[37.94,0.0073783],[37.94,0.0073783],[37.94,0.165813]],"timestamp":[1644077422]}],"status":"ok"}
```


# ... Next endpoints soon !

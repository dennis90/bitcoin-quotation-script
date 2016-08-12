import json, urllib2

class CoinQuotation:
    urls = None
    path_json = None
    
    def __init__(self):
        self.urls = {
                'usd': 'http://api.promasters.net.br/cotacao/v1/valores',
                'foxbit': 'https://api.blinktrade.com/api/v1/BRL/ticker?crypto_currency=BTC',
                'mercado': 'https://www.mercadobitcoin.net/api/v2/ticker/',
                'bitstamp': 'https://www.bitstamp.net/api/ticker/',
				'okcoin': 'https://www.okcoin.com/api/v1/ticker.do?symbol=btc_usd',
				'bitfinex': 'https://api.bitfinex.com/v1/pubticker/btcusd',
				'coindesk': 'http://api.coindesk.com/v1/bpi/currentprice.json',
				'b2u': 'https://www.bitcointoyou.com/api/ticker.aspx',
            }

        self.path_json = {
        			 'usd': 'valores/USD/valor',
        			 'foxbit': 'last',
					 'mercado': 'ticker/last',
					 'bitstamp': 'last',
                     'okcoin': 'ticker/last',
					 'bitfinex': 'last_price',
					 'coindesk': 'bpi/USD/rate',
					 'b2u': 'ticker/last',
            }

    def value_from_json(self, json, exchange):
    	path = self.path_json[exchange]
    	json_child = json
    	for idx in path.split('/'):
    		json_child = json_child[idx]
    	return json_child

    def url_to_json(self, url):
    	return json.load(urllib2.urlopen(url))

    def get_quotation(self, exchange):
    	url = self.urls[exchange]
    	json_file = self.url_to_json(url)
    	value = self.value_from_json(json_file, exchange)
    	return float(value)
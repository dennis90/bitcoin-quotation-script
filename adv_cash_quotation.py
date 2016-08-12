from lxml import html
import requests

class AdvCashQuotation:
	quotation_list = None

	def __init__(self):
		url = "http://advcash.com/en/"
		page = requests.get(url)
		tree = html.fromstring(page.content)
		btc_list = tree.xpath('//li[@class="btc"]')
		self.quotation_list = {}

		for item in btc_list:
			if item[0].text == "BTC/USD":
				self.quotation_list["usd"] = float(item[1].text)
			elif item[0].text == "BTC/EUR":
				self.quotation_list["eur"] = float(item[1].text)
			elif item[0].text == "BTC/GBP":
				self.quotation_list["gbp"] = float(item[1].text)

	def get_from_usd(self):
		return self.quotation_list["usd"]

	def get_from_eur(self):
		return self.quotation_list["eur"]

	def get_from_gbp(self):
		return self.quotation_list["gbp"]
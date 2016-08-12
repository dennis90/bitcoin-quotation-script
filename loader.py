# -*- coding: utf8 -*-

from coin_quotation import CoinQuotation
import datetime

moedas = CoinQuotation()

reimprime = "S"

while reimprime == "S":
    # Imprime data / hora da consulta
    print("Hora da Consulta: %s" % datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    # Imprime a cotação do dólar
    print(u"Dólar Comercial: %s" % moedas.get_quotation('usd'))
    print("=" * 30)

    # Imprime a cotação do bitcoin nas exchanges brasileiras
    print("\tBITCOIN EXCHANGES BRASILEIRAS")

    foxbit = moedas.get_quotation('foxbit')
    mercado = moedas.get_quotation('mercado')
    b2u  = moedas.get_quotation('b2u')

    menor = "Foxbit" if foxbit <= mercado and foxbit <= b2u \
                else "Mercado Bitcoin" if mercado <= b2u else "Bitcoin 2 You"

    print("       Foxbit : %.3f" % foxbit)
    print("  Mercado BTC : %.3f" % mercado)
    print("Bitcoin 2 You : %.3f" % b2u)
    print("")
    print(u"Menor Preço Brasil: %s" % menor)
    print("=" * 30)    

    # Imprime a cotação do bitcoin nas exchanges internacionais
    print("\tBITCOIN EXCHANGES INTERNACIONAIS")

    bitfinex = moedas.get_quotation('bitfinex')
    bitstamp = moedas.get_quotation('bitstamp')
    coindesk = moedas.get_quotation('coindesk')
    okcoin = moedas.get_quotation('okcoin')    

    menor = "Bitfinex" if bitfinex <= bitstamp and bitfinex <= coindesk  and bitfinex <= okcoin \
                else "Bitstamp" if bitstamp <= coindesk and bitstamp <= okcoin \
                else "Coin Desk" if coindesk <= okcoin \
                else "Ok Coin"

    print("     Bitfinex : %.3f" % bitfinex)
    print("     Bitstamp : %.3f" % bitstamp)
    print("    Coin Desk : %.3f" % coindesk)
    print("      Ok Coin : %.3f" % okcoin)
    print("")
    print(u"Menor Preço Internacional: %s" % menor)
    print("=" * 30)
    print("\n\n")

    reimprime = raw_input('Atualizar? (S/N)').upper()

    print("*" * 50)
    print("\n\n")
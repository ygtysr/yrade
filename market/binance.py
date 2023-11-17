import logging
from .base import Market
from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)

class BinanceMarket(Market):
    def __init__(self, api_key, api_secret):
        logger.info("binance client is initializing..")
        self.client = Client(api_key, api_secret)
        logger.info("binance client is initialized succesfully..")


    def fetch_order_book(self, symbol, depth=100):
        try:
            return self.client.get_order_book(symbol=symbol, limit=depth)
        except BinanceAPIException as e:
            print(f"Binance API Exception: {e}")
            return None

    def execute_trade(self, symbol, quantity, trade_type, price=None):
    
        pass

    def get_open_positions(self):
        pass

    def get_current_price(self, symbol):
        try:
            return float(self.client.get_symbol_ticker(symbol=symbol)['price'])
        except BinanceAPIException as e:
            print(f"Binance API Exception: {e}")
            return None

    def fetch_all_symbols(self):
        try:
            info = self.client.get_exchange_info()
            return [symbol['symbol'] for symbol in info['symbols']]
        except BinanceAPIException as e:
            print(f"Binance API Exception: {e}")
            return []



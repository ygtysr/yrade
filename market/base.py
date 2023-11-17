from abc import ABC, abstractmethod

class Market(ABC):
    @abstractmethod
    def fetch_order_book(self, symbol, depth):
        """Fetch the order book for a given symbol."""
        pass

    @abstractmethod
    def execute_trade(self, symbol, quantity, trade_type, price=None):
        """Execute a trade on the market."""
        pass

    @abstractmethod
    def get_open_positions(self):
        """Retrieve currently open positions."""
        pass

    @abstractmethod
    def get_current_price(self, symbol):
        """Fetch the current price of a symbol."""
        pass

    @abstractmethod
    def fetch_all_symbols(self):
        """Fetch all available trading symbols."""
        pass

import talib
import numpy as np

class TechnicalAnalysis:
    def __init__(self):
        """
        Initialize TechnicalAnalysis
        """

    def BTC_analysis(self, btc_data):
        """
        Perform analysis on BTC data.
        """
        moving_average = self.calculate_moving_average(btc_data)
        trend = self.determine_price_trend(btc_data)

        return {
            "BTC_Price_MA": moving_average[-1],
            "BTC_Price_Trend": trend,
        }

    def BTCDOM_analysis(self, btcdom_data):
        """
        Perform analysis on BTCDOM data.
        """
        moving_average = self.calculate_moving_average(btcdom_data)
        trend = self.determine_price_trend(btcdom_data)

        return {
            "BTC_DOM_MA": moving_average[-1],
            "BTC_DOM_Trend": trend
        }

    def analyze_market(self, btc_data, btcdom_data):
        """
        Analyze the market based on BTC and BTCDOM data.
        """
        btcdom_analysis = self.BTCDOM_analysis(btcdom_data)
        btc_analysis = self.BTC_analysis(btc_data)

        if btc_analysis is None or btcdom_analysis is None:
            return None

        btc_dom_trend = btcdom_analysis["BTC_DOM_Trend"]
        btc_price_trend = btc_analysis["BTC_Price_Trend"]

        print("Market Analysis:")
        print(f"BTC Dominance Trend: {btc_dom_trend}")
        print(f"BTC Price Trend: {btc_price_trend}")

        if btc_dom_trend == "Bullish" and btc_price_trend == "Bullish":
            print("LONG: Bitcoin Dominance Increasing + Bitcoin Price Increasing")
            return MarketPosition.LONG
        elif btc_dom_trend == "Bullish" and btc_price_trend == "Bearish":
            print("SHORT: Bitcoin Dominance Increasing + Bitcoin Price Decreasing")
            return MarketPosition.SHORT
        elif btc_dom_trend == "Bearish" and btc_price_trend == "Bullish":
            print("STRONG LONG: Bitcoin Dominance Decreasing + Bitcoin Price Increasing")
            return MarketPosition.STRONG_LONG
        elif btc_dom_trend == "Bearish" and btc_price_trend == "Bearish":
            print("STRONG SHORT: Bitcoin Dominance Decreasing + Bitcoin Price Decreasing")
            return MarketPosition.STRONG_SHORT
        else:
            print("NEUTRAL: Mixed condition: BTC dominance and BTC price trends are in opposite directions.")
            return MarketPosition.NEUTRAL    


    def calculate_indicators_async(self, historical_data, symbol):
            """
            Calculate various technical indicators for a symbol using historical data.
            """
            # Assuming historical_data is a DataFrame with columns ['Open', 'High', 'Low', 'Close', 'Volume']
            close_prices = historical_data['Close'].astype(float)

            # Indicator calculations
            macd, signal, _ = talib.MACD(close_prices)
            ema10 = talib.EMA(close_prices, timeperiod=10).iloc[-1]
            ema20 = talib.EMA(close_prices, timeperiod=20).iloc[-1]
            ema50 = talib.EMA(close_prices, timeperiod=50).iloc[-1]
            sma10 = talib.SMA(close_prices, timeperiod=10).iloc[-1]
            sma20 = talib.SMA(close_prices, timeperiod=20).iloc[-1]
            sma50 = talib.SMA(close_prices, timeperiod=50).iloc[-1]
            rsi = talib.RSI(close_prices, timeperiod=14).iloc[-1]
            momentum = talib.MOM(close_prices, timeperiod=10).iloc[-1]
            stochrsi_fastk, stochrsi_fastd = talib.STOCHRSI(close_prices, timeperiod=14)

            return {
                "symbol": symbol,
                "price": close_prices.iloc[-1],
                "macd": macd.iloc[-1],
                "signal": signal.iloc[-1],
                "ema10": ema10,
                "ema20": ema20,
                "ema50": ema50,
                "sma10": sma10,
                "sma20": sma20,
                "sma50": sma50,
                "rsi": rsi,
                "momentum": momentum,
                "stochrsi_fastk": stochrsi_fastk.iloc[-1],
                "stochrsi_fastd": stochrsi_fastd.iloc[-1]
            }

    # Additional methods for other technical indicators can be added here

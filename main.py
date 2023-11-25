import logging
import asyncio
from options_parser import OptionsParser
from utils import logger as logger_setup
from market.binance import BinanceMarket
from analysis.technicalAnalysis import TechnicalAnalysis

logger = logging.getLogger(__name__)

async def get_data(market):
        btc_data = await market.fetch_klines_async("BTCUSDT")
        btcdom_data = await market.fetch_klines_async("BTCDOMUSDT")
        return btc_data, btcdom_data

def main():

    options = OptionsParser()

    logger_setup.setup_logger(options.get_log_level())    
    logger.info("Options are parsed succesfully..")

    api_key = options.get_api_key()
    api_secret = options.get_api_secret()
    volume_threshold = options.get_volume_threshold()
    logger.info("Starting the application")
    
    market = BinanceMarket(api_key=api_key, api_secret=api_secret)
    analysis = TechnicalAnalysis()
    btc_data, btcdom_data = asyncio.run(get_data(market))


    # market_position = await analysis.analyze_market(btc_data, btcdom_data)


if __name__ == "__main__":
    main()
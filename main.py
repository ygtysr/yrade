import logging
from options_parser import OptionsParser
from utils import logger as logger_setup
from market.binance import BinanceMarket

logger = logging.getLogger(__name__)

def main():

    options = OptionsParser()

    logger_setup.setup_logger(options.get_log_level())    
    logger.info("Options are parsed succesfully..")

    api_key = options.get_api_key()
    api_secret = options.get_api_secret()
    volume_threshold = options.get_volume_threshold()
    logger.info("Starting the application")
    
    market = BinanceMarket(api_key=api_key, api_secret=api_secret)


if __name__ == "__main__":
    main()

import os
from dotenv import load_dotenv

class OptionsParser:
    
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file

        # Binance API Credentials
        self.api_key = os.getenv("API_KEY", "none")
        self.api_secret = os.getenv("API_SECRET", "none")

        # Trading Configuration
        self.volume_threshold = int(os.getenv("VOLUME_THRESHOLD", "100000"))
        self.profit_percentage_goal = float(os.getenv("PROFIT_PERCENTAGE_GOAL", "0.030"))
        self.stop_loss_percentage = float(os.getenv("STOP_LOSS_PERCENTAGE", "0.90"))
        self.leverage = int(os.getenv("LEVERAGE", "10"))
        self.short_position_count = int(os.getenv("SHORT_POSITION_COUNT", "3"))
        self.long_position_count = int(os.getenv("LONG_POSITION_COUNT", "0"))

        # General Configurations
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.cooldown_period_minutes = int(os.getenv("COOLDOWN_PERIOD_MINUTES", "15"))
        self.max_position_count = int(os.getenv("MAX_POSITION_COUNT", "6"))
        
    def __str__(self): 
        return "option_parser"

    # Getters for Binance API Credentials
    def get_api_key(self):
        return self.api_key

    def get_api_secret(self):
        return self.api_secret

    # Getters for Trading Configuration
    def get_volume_threshold(self):
        return self.volume_threshold

    def get_profit_percentage_goal(self):
        return self.profit_percentage_goal

    def get_stop_loss_percentage(self):
        return self.stop_loss_percentage

    def get_leverage(self):
        return self.leverage

    def get_short_position_count(self):
        return self.short_position_count

    def get_long_position_count(self):
        return self.long_position_count

    # Getters for General Configurations
    def get_log_level(self):
        return self.log_level

    def get_cooldown_period_minutes(self):
        return self.cooldown_period_minutes

    def get_max_position_count(self):
        return self.max_position_count

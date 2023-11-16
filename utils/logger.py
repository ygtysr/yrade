import logging

import logging

def setup_logger(log_level="INFO"):
    # Convert the log level to its numeric representation
    numeric_level = getattr(logging, log_level.upper(), None)

    # Check if the log level is valid
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Basic configuration for logging
    logging.basicConfig(level=numeric_level,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

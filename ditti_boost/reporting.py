# logging_config.py
import logging

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,  # Adjust the logging level as needed (e.g., DEBUG, WARNING, ERROR)
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()]
    )

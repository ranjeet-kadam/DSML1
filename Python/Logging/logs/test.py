# test.py

import logging

# Setup logging FIRST
logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def add(a, b):
    logging.debug("The addition operation is taking place")
    print(a + b)

logging.debug("Action is starting")
add(10, 13)
logging.debug("Action is completed")

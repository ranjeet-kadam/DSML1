import logging

logging.basicConfig(
    level= logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithematic App")

def add(a,b):
    result = a+b
    logger.debug(f"adding {a}+{b} ={result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"subtracting {a}+{b}={result}",)
    return result

def multiply(a,b):
    result = a*b
    logger.debug(f"multipying {a}*{b} = {result}",)
    return result

def division(a,b):
    try:
        result = a/b
        logger.debug(f"dividing {a} / {b} = {result}",)
        return result
    except:
        logger.error ("Division by zero error")
        return None
    
add(10,15)
subtract(15,10)
multiply(4,6)
division(10,5)
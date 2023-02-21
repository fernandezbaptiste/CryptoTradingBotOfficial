import tkinter as tk
import logging # used to tracking events that occur when the software runs
from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient
import pprint
from interface.root_component import Root
# hi

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# streamhandler is non persistent
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
# FileHandler is persistent
file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


# what is below the if statement won't be executed
# if main file is not executed here
# so if main file is imported on another file; it won'd be executed if the other file is executed
if __name__ == '__main__':
    binance = BinanceFuturesClient("",
                                   "",True)
    bitmex = BitmexClient("",
                          "", True)

    # initialise the tkinter app
    root = Root(binance, bitmex)
    #  makes the application run forever unless you stop it
    root.mainloop()

# logger.info() seems like a "print()"
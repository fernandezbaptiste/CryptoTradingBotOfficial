import tkinter as tk
import logging

from connectors.binance_futures import BinanceFuturesClient


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("0ec26c7d1625fb9133863ca37e12faf9a7d1381c6174fc304f4776d3ec96c5f1",
                                   "ace97e7353e7d559d18467a7710627c7379b1985aca858b3123e82bd5b4294ce",True)

    root = tk.Tk()
    root.mainloop()
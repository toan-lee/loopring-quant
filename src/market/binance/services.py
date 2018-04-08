from binance.client import Client
from market import Market


class BinanceService(Market):

    def __init__(self, **params):
        Market.__init__(self, **params)
        # self.__client = Client
        # super(BinanceService, self).__init__(params)

    def get_price(self):
        print(self.get_api_key())

    def get_depth(self):
        pass

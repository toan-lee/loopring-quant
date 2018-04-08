import abc


class MarketException(Exception):
    """
      Custom Market Exception
    """

    def __init__(self, msg):
        super(MarketException, self).__init__(msg)
        self.__msg = msg


class Market(object):
    """
        abstract Market class
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, **params):
        # self.params = params

        self.__api_key = params['api_key']
        self.__api_secret = params['api_secret']
        self.__proxies = params.get('proxies', None)

    def get_api_key(self):
        """
            return api_key
        :return: string, api_key
        """
        return self.__api_key

    def get_api_secret(self):
        """
            return api_secret
        :return: string, api_secret
        """
        return self.__api_secret

    def get_proxies(self):
        return self.__proxies

    @abc.abstractmethod
    def get_price(self):
        """
            get current symbol market price
        :return:
        """
        return

    @abc.abstractmethod
    def get_depth(self):
        """
            get current symbol market depth
        :return:
        """
        return


class MakertFactory:

    @staticmethod
    def instance(market_name='Binance', **params):
        from market.binance.services import BinanceService
        if market_name == 'Binance':
            from market.binance.services import BinanceService
            return BinanceService(**params)
        elif market_name == 'Loopr':
            from market.loopr.services import LooprService
            return LooprService()
        else:
            raise MarketException('can create market instance whith name [%s]' % market_name)
        # from market.binance import BinanceService



import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2))
        self.assertEqual(getDataPoint(quotes[1]), ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 122.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        self.assertEqual(getDataPoint(quotes[0]), ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2))
        self.assertEqual(getDataPoint(quotes[1]), ('DEF', 122.87, 121.68, (122.87 + 121.68) / 2))

    def test_getRatio(self):
        self.assertEqual(getRatio(120.48, 119.2), 120.48 / 119.2)
        self.assertEqual(getRatio(121.68, 122.87), 121.68 / 122.87)
        self.assertIsNone(getRatio(121.68, 0))

    def test_getRatio_zeroDenominator(self):
        self.assertIsNone(getRatio(120.48, 0))

    def test_getDataPoint_emptyQuote(self):
        empty_quote = {'top_ask': {'price': 0, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 0}, 'id': '0.109974697771', 'stock': 'ABC'}
        self.assertEqual(getDataPoint(empty_quote), ('ABC', 0, 0, 0))

if __name__ == '__main__':
    unittest.main()

from src.MainSchema import ObResponse, TradesResponse
import unittest
from unittest.mock import patch



class TestMainSchema(unittest.TestCase):

    def setUp(self):
        self.ob_class = ObResponse
        self.trades_class = TradesResponse

    def tearDown(self):
        pass



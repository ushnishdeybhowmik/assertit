import unittest
from main import *

test_output1 = [['New York', '$10150', [['8XLarge', 7],['XLarge', 1], ['Large', 1]]], ['India', '$9520', [['8XLarge', 7], ['Large', 3]]], ['China', '$8570', [['8XLarge',7], ['XLarge', 1],['Large', 1]]]]
test_output2 = 'Enter positive and meaningful numeric data.'
class TestMain(unittest.TestCase):
    def test_optimized_cost_output(self):
        self.assertEqual(optimized_cost_output(1150, 1, region_cost_table, locations, capacity), test_output1)
        self.assertEqual(optimized_cost_output(-113, 1, region_cost_table, locations, capacity), test_output2)

if __name__ == '__main__':
    unittest.main()
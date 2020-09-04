import unittest
from HelperFunctions import *
from Items import *

class MyTestCase(unittest.TestCase):
    def test_list_to_string(self):
        apple = Item("apple", 1, "player")
        banana = Item("banana", 1, "player")
        grape = Item("grape", 1, "player")
        self.assertEqual(list_to_string([apple, banana, grape]), "an apple, a banana and a grape")


if __name__ == '__main__':
    unittest.main()

import unittest
from solution import seven_segmentify  # Certifique-se de que o arquivo solution.py esteja no mesmo diretório

class TestSevenSegmentify(unittest.TestCase):
    def test_13_24(self):
        """should work on 13:24"""
        self.assertEqual(seven_segmentify("13:24"), """
    _     _    
  | _| .  _||_|
  | _| . |_   |"""[1:])

    def test_08_56(self):
        """should work on 08:56"""
        self.assertEqual(seven_segmentify("08:56"), """
    _     _  _ 
   |_| . |_ |_ 
   |_| .  _||_|"""[1:])

    def test_21_49(self):
        """should work on 21:49"""
        self.assertEqual(seven_segmentify("21:49"), """
 _           _ 
 _|  | . |_||_|
|_   | .   | _|"""[1:])

    def test_07_00(self):
        """should work on 07:00"""
        self.assertEqual(seven_segmentify("07:00"), """
    _     _  _ 
     | . | || |
     | . |_||_|"""[1:])

    def test_06_03(self):
        """should work on 06:03"""
        self.assertEqual(seven_segmentify("06:03"), """
    _     _  _ 
   |_  . | | _|
   |_| . |_| _|"""[1:])

    def test_00_00(self):
        """should work on 00:00"""
        self.assertEqual(seven_segmentify("00:00"), """
    _     _  _ 
   | | . | || |
   |_| . |_||_|"""[1:])

    def test_10_59(self):
        """should work on 10:59"""
        self.assertEqual(seven_segmentify("10:59"), """
    _     _  _ 
  || | . |_ |_|
  ||_| .  _| _|"""[1:])

if __name__ == '__main__':
    unittest.main()

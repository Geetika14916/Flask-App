import unittest
from machinetranslation.translator import english_to_french
from machinetranslation.translator import french_to_english

class TestTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    
    def test2(self):
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")
    
    def test3(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    
    def test4(self):
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")

if __name__ == '__main__':
    unittest.main()
import unittest
import translator


class Test(unittest.TestCase):
    def testNull(self):
        self.assertEqual(translator.englishToFrench(""),"Please enter english text")
        self.assertEqual(translator.frenchToEnglish(""),"Please enter french text")

    def testEnglishToFrench(self):
        self.assertEqual(translator.englishToFrench("Hello"),"Bonjour")

    def test(self):
        self.assertEqual(translator.frenchToEnglish("Bonjour"),"Hello")


unittest.main()
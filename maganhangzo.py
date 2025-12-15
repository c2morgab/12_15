import unittest

def maganhangzo_torol(szoveg):
    maganhangzok = "aeiouAEIOU"
    
    eredmeny = ''.join([karakter for karakter in szoveg if karakter not in maganhangzok])
    
    return eredmeny

class TestMaganhangzoTorol(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(maganhangzo_torol(""), "")
    
    def test_no_vowels(self):
        self.assertEqual(maganhangzo_torol("bcdfghjklmnpqrstvwxyz"), "bcdfghjklmnpqrstvwxyz")
    
    def test_all_vowels(self):
        self.assertEqual(maganhangzo_torol("aeiouAEIOU"), "")
    
    def test_mixed_case(self):
        self.assertEqual(maganhangzo_torol("Hello World!"), "Hll Wrld!")
    
    def test_mixed_text(self):
        self.assertEqual(maganhangzo_torol("Csabi szereti a Githubot"), "Csb szrt  Gthbt")

if __name__ == "__main__":
    unittest.main()

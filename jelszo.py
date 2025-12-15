import unittest

# A jelszó-erősség mérő függvény
def jelszo_erosseg(jelszo: str) -> int:
    if len(jelszo) == 0:
        return 0
    if 'jelszo' in jelszo or '123' in jelszo:
        return 0
    erosseg = 1
    if len(jelszo) >= 5:
        erosseg += 1
    if len(jelszo) >= 8:
        erosseg += 2
    for char in jelszo:
        if char in ['_', '-', '.']:
            erosseg += 2
    return erosseg

class TestJelszoErosseg(unittest.TestCase):
    
    def test_empty_password(self):
        self.assertEqual(jelszo_erosseg(''), 0)
        
    def test_contains_jelszo(self):
        self.assertEqual(jelszo_erosseg('jelszo123'), 0)
        self.assertEqual(jelszo_erosseg('myjelszo'), 0)
        
    def test_contains_123(self):
        self.assertEqual(jelszo_erosseg('123abc'), 0)
        
    def test_basic_strength(self):
        self.assertEqual(jelszo_erosseg('abc'), 1)
        self.assertEqual(jelszo_erosseg('abcd'), 1)
        self.assertEqual(jelszo_erosseg('abcde'), 2)
        self.assertEqual(jelszo_erosseg('abcdefgh'), 4)
    
    def test_special_characters(self):
        self.assertEqual(jelszo_erosseg('hazi_macska_4_life'), 10)
        self.assertEqual(jelszo_erosseg('hazi-macska.4-life'), 10)
        self.assertEqual(jelszo_erosseg('test-123'), 0)
    
    def test_long_password(self):
        self.assertEqual(jelszo_erosseg('longpasswordwithspecial_character_-'), 10)


if __name__ == '__main__':
    unittest.main()

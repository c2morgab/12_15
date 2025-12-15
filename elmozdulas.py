import unittest

def elmozdulas(utvonal):
    x, y = 0, 0

    for irany in utvonal:
        if irany == 'F':
            y += 1 
        elif irany == 'L':
            y -= 1
        elif irany == 'J':
            x += 1
        elif irany == 'B':
            x -= 1


    if x == 0 and y == 0:
        return 'Nem mentunk sehova'
    
    if x > 0:
        vizszintes = f'{x} lepes jobbra'
    elif x < 0:
        vizszintes = f'{-x} lepes balra'
    else:
        vizszintes = None
    
    if y > 0:
        fuggoleges = f'{y} lepes fel'
    elif y < 0:
        fuggoleges = f'{-y} lepes le'
    else:
        fuggoleges = None
    
    if vizszintes and fuggoleges:
        return f'{vizszintes}, {fuggoleges}'
    elif vizszintes:
        return vizszintes
    elif fuggoleges:
        return fuggoleges

class TestElmozdulas(unittest.TestCase):
    def test_1(self):
        self.assertEqual(elmozdulas('JJFBFFFFFFBBBL'), '2 lepes balra, 6 lepes fel')

    def test_2(self):
        self.assertEqual(elmozdulas('FBLLLJLLJ'), '1 lepes jobbra, 4 lepes le')

    def test_3(self):
        self.assertEqual(elmozdulas('FFF'), '3 lepes fel')

    def test_4(self):
        self.assertEqual(elmozdulas(''), 'Nem mentunk sehova')

    def test_5(self):
        self.assertEqual(elmozdulas('JJJJJJJ'), '7 lepes jobbra')

    def test_6(self):
        self.assertEqual(elmozdulas('BBBBBB'), '6 lepes balra')

    def test_7(self):
        self.assertEqual(elmozdulas('FFLL'), 'Nem mentunk sehova')

    def test_8(self):
        self.assertEqual(elmozdulas('LJFFBB'), '1 lepes balra, 1 lepes fel')

    def test_9(self):
        self.assertEqual(elmozdulas('JJBLLF'), '1 lepes jobbra, 1 lepes le')

    def test_10(self):
        self.assertEqual(elmozdulas('BBJJFLFFJL'), '1 lepes jobbra, 1 lepes fel')

if __name__ == '__main__':
    unittest.main()
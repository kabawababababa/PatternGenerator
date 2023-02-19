import unittest
from ..sweaterNo8 import sweaterNo8

# READ ME:
# IF YOU ADD TESTS HERE, MAKE SURE TO REGISTER THEM TO ALL_TESTS.PY
knitGauge=[10,10]
validGauges = [[10,10],[11,11],[12,12],[13,13],[14,14]]
class sweaterNo8Test(unittest.TestCase):

    def test_validSizes(self):
        for size in sweaterNo8.validSizes:
            sweater = sweaterNo8(size,knitGauge)
            self.assertEqual(sweater.get_size(), size)

    def test_invalidSizes(self):
        invalidSizes=['$','abc','124']
        for size in invalidSizes:
            self.assertRaises(ValueError, sweaterNo8,size,knitGauge)

    def test_validGauge(self):
        size='S'
        for gauge in validGauges:
            sweater = sweaterNo8(size,gauge)
            self.assertEqual(sweater.get_new_gauge(),gauge)

    def test_invalidGauge(self):
        size='S'
        invalidGauges =[[0,0],['fd',12],[True,'False'],['35','43'],[34,56,63]]
        for gauge in invalidGauges:
            self.assertRaises(ValueError,sweaterNo8,size,gauge)


if __name__ == '__main__':
    unittest.main()

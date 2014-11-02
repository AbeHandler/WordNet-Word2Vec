import random
import unittest
import sys

sys.path.append("../")

from wordnetter import synononymous
from wordnetter import hypernomous
from wordnetter import not_in_wordnet
from wordnetter import holonymous
from wordnetter import meronymous
from wordnetter import hyoponomous
from wordnetter import hyoponomous

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_syn(self):
        self.assertEqual(synononymous("hot", "spicy"), 0.043478260869565216)


    def test_hyper(self):
        self.assertGreater(hypernomous("decisions", "choice"), 0)


    def test_hypo(self):
        self.assertGreater(hyoponomous("protected", "guarded"), 0)


    def test_not_in_wordnet(self):
        self.assertEqual(not_in_wordnet("hot"), False)


    def test_mero(self):
        self.assertGreater(meronymous("Redwoods", "Sequoia"), 0)


    def test_holo(self):
        self.assertGreater(holonymous("IRAQ" , "Baghdad"), 0)

if __name__ == '__main__':
    unittest.main()
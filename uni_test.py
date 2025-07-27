import unittest
import unitesttarget


class mytest(unittest.TestCase):
    def test_one(self):
        text = "leaning"
        result = unitesttarget.unitest_target(text)
        self.assertEqual(result, "Leaning")

    def test_two(self):
        text = "just leaning"
        result = unitesttarget.unitest_target(text)
        self.assertEqual(result, "Just Leaning")


if __name__ == "__main__":
    unittest.main()

import unittest
import chip_sim1

class TestChipotleSim(unittest.TestCase):
    """Test chipotle simulator"""
    def SetUp(self):
        """Test whether SetUp works as expected"""
        self.order1 = chip_sim1.burrito({})
        self.order2 = chip_sim1.Bowl({})
    def test_init(self):
        self.assertEqual(self.order1.name, "Gabby")
        self.assertNotEqual(self.order1.name, "5")
    def test_customer_pref(self):
        self.assertEqual(self.order1.customer_pref, [])
    def test_calories_count(self):
        self.assertGreater(2,0)
        self.assertNotEqual(self.order1.caloriescount, 0)
    def test_dietary(self):
        self.assertEqual("vegan, vegetarian")
        self.assertNotEqual("vegan, vegeterian")     
    def test_tor_pref(self):
        self.assertEqual(order2.tor_pref , True)   
    def test_extra(self):
        self.assertEqual(order1.extra[price], 5)   
    def test_price_cal(self):
        self.assertEqual(order1.price_cal, 15)

        
if __name__ == "__main__":
    unittest.main()
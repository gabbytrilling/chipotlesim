import unittest
import chip_sim1

class TestChipotleSim(unittest.TestCase):
    """Test chipotle simulator"""
    def setUp(self):
        """Test whether SetUp works as expected"""
        self.order1 = chip_sim1.Burrito("Gabby")
        self.order2 = chip_sim1.Bowl("Joe")
    def test_init(self):
        self.assertEqual(self.order1.name, "Gabby")
        self.assertEqual(self.ingredients, [])
        self.assertEqual(self.order, {"Name": "Gabby"})
    def test_customer_pref(self):
        self.assertEqual(self.order1.customer_pref, [])
        #added test code bellow
        self.oreder1.customer_pref("bowl")
        self.assertEquals("bowl")
        self.order1.customer_pref("burrito")
        self.assertEquals("burrito")
    def test_calories_count(self):
        self.assertGreater(2,0)
        self.assertNotEqual(self.order1.caloriescount, 0)
    def test_dietary(self):
        self.order1.dietary("keto")
        self.assertEquals(["lettuce", "steak","red chili salsa", "cheese",
                          "guacamole"], self.order1.ingredients)
        self.order1.dietary("vegan")
        self.assertEquals(["brown rice", "sofritas", "black beans", 
                      "tomatillo salsa", "corn salsa", 
                      "lettuce"], self.order1.ingredients)
        self.order1.dietary("vegetarian")
        self.assertEquals(["lettuce", "brown rice", "black beans", "fajitas", 
                           "tomato salsa","guacamole"], self.order1.ingredients)
        #self.assertEqual("vegan, vegetarian")
        #self.assertNotEqual("vegan, vegeterian")     
    def test_tor_pref(self):
        self.assertEqual(order1.tor_pref , True)   
    def test_extra(self):
        self.assertEqual(order1.extra[price], 5)   
    def test_price_cal(self):
        self.assertEqual(order1.price_cal, 15)

        
if __name__ == "__main__":
    unittest.main()
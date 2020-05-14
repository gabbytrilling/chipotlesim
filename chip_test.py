import unittest
import chip_sim1

class TestChipotleSim(unittest.TestCase):
    """Test chipotle simulator"""
    def setUp(self):
        """Test whether SetUp works as expected"""
        self.order1 = chip_sim1.Burrito("gabby")
        self.order2 = chip_sim1.Bowl("joe")
        self.order3 = chip_sim1.Bowl("bob")
        self.order4 = chip_sim1.Burrito("john")
    def test_init(self):
        self.assertEqual(self.order1.name, "gabby")
        self.assertEqual(self.order1.ingredients, [])
    def test_customer_pref(self):
        self.assertEqual(chip_sim1.customer_pref("bowl"), 'bowl')
        self.assertEqual(chip_sim1.customer_pref('burrito'), 'burrito')
    def test_calories_count(self):
        self.assertEqual(self.order1.calories_count, 525)
        self.assertEqual(self.order2.calories_count, 725)
        self.assertEqual(self.order3.calories_count, 850)
        self.assertEqual(self.order4.calories_count, 755)
        
        self.assertNotEqual(self.order1.calories_count, 0)
    def test_dietary(self):
        self.order1.dietary("keto")
        self.assertEquals(["lettuce", "steak","red chili salsa", "cheese",
                          "guacamole"], self.order1.ingredients)
        self.order2.dietary("vegan")
        self.assertEquals(["brown rice", "sofritas", "black beans", 
                      "tomatillo salsa", "corn salsa", 
                      "lettuce"], self.order2.ingredients)
        self.order3.dietary("vegetarian")
        self.assertEquals(["lettuce", "brown rice", "black beans", "fajitas", 
                           "tomato salsa","guacamole"], self.order3.ingredients)
        self.order4.dietary("None")
        self.assertEqual([], self.order4.ingredients)
        #self.assertEqual("vegan, vegetarian")
        #self.assertNotEqual("vegan, vegeterian") 
    def test_tortilla(self):
        self.assertEqual(self.order2.tortilla('yes'), True)
        self.assertEqual(self.order3.tortilla('no'), False)  
    def test_extra(self):
        self.order1.extra("none")
        self.assertEquals(["lettuce", "steak","red chili salsa", "cheese",
                          "guacamole"], self.order1.ingredients)
        self.order2.extra("sofritas")
        self.assertEquals(["brown rice", "sofritas", "black beans", 
                      "tomatillo salsa", "corn salsa", 
                      "lettuce", "sofritas"], self.order2.ingredients)
        self.assertEqual(self.order2.extra, 10.5)
        self.order3.extra("guacamole")
        self.assertEquals(["lettuce", "brown rice", "black beans", "fajitas", 
                           "tomato salsa","guacamole", "guacamole"], self.order3.ingredients)
        self.assertEqual(self.order3.extra, 10)
        self.order4.extra("chicken")
        self.assertEquals(["brown rice","pinto", "steak", "corn salsa",
                            "lettuce", "chicken"], self.order4.ingredients)
        self.assertEqual(self.order4.extra, 11.5)
        #self.assertEqual(order1.extra[price], 5)   
    def test_price_cal(self):
        self.assertEqual(self.order1.price_cal(), 8.7)
        self.assertEqual(self.order2.price_cal(), 7.70)
        self.assertEqual(self.order3.price_cal(), 7.70)
        self.assertEqual(self.order4.price_cal(), 8.7)

        
if __name__ == "__main__":
    unittest.main()
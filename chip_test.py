import unittest
import chip_sim1

class TestChipotleSim(unittest.TestCase):
    """Test chipotle simulator"""
    def setUp(self):
        """Test whether SetUp works as expected"""
        self.order1 = chip_sim1.Burrito("gabby")
        self.order2 = chip_sim1.Bowl("joe")
        self.order3 = chip_sim1.Bowl("bob")
    def test_init(self):
        """Test whether init works as expected"""
        self.assertEqual(self.order1.name, "gabby")
        self.assertEqual(self.order1.ingredients, [])
    def test_customer_pref(self):
        """Test whether customer_pref works as expected"""
        self.assertEqual(chip_sim1.customer_pref("bowl"), 'bowl')
        self.assertEqual(chip_sim1.customer_pref('burrito'), 'burrito')
    def test_calories_count(self):
        """Tests if calories_count works as expected"""
        self.order1.dietary("keto")
        self.assertEqual(self.order1.calories_count(), 525)
        self.order2.dietary("vegan")
        self.assertEqual(self.order2.calories_count(), 575)
        self.order3.dietary("vegetarian")
        self.assertEqual(self.order3.calories_count(), 620)
        self.assertNotEqual(self.order1.calories_count(), 0)
    def test_dietary(self):
        """Tests whether dietary works as expected"""
        self.order1.dietary("keto")
        self.assertEquals(["lettuce", "steak","red chili salsa", "cheese",
                          "guacamole"], self.order1.ingredients)
        self.order2.dietary("vegan")
        self.assertEquals(["brown rice", "sofritas", "black beans", 
                      "tomatillo salsa", "corn salsa", 
                      "lettuce"], self.order2.ingredients)
        self.order3.dietary("vegetarian")
        self.assertEquals(['veggie',"lettuce", "brown rice", "black beans",
                           "fajitas", "tomato salsa","guacamole"],
                           self.order3.ingredients)
    def test_tortilla(self):
        """Test whether tortilla works as expected"""
        self.assertEqual(self.order2.tortilla('yes'), True)
        self.assertEqual(self.order3.tortilla('no'), False)  
    def test_extra(self):
        """Tests whether extra works as expected"""
        self.order1.dietary("keto")
        self.assertEqual(self.order1.extra(), 8.70)
        self.order2.dietary("vegan")
        order2 = self.order2.extra(['guacamole'])
        self.assertEqual(order2, 10.0)
        self.order3.dietary("vegetarian")
        self.assertEqual(self.order3.extra(['chicken']), 10.5)
    def test_price_cal(self):
        """Tests whether price_cal works as expected"""
        self.order1.dietary('keto')
        self.assertEqual(self.order1.price_cal(), 8.7)
        self.order2.dietary('vegan')
        self.assertEqual(self.order2.price_cal(), 7.70)
        self.order3.dietary('vegetarian')
        self.assertEqual(self.order3.price_cal(), 7.70)

        
if __name__ == "__main__":
    unittest.main()
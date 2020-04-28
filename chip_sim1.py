      
""" Simulates a person ordering food at Chipotle.
"""

class Burrito:
    """ Simulates a person ordering food at Chipotle
    
    Attributes:
        name(str): the person ordering
    """
    
    def __init__(self, name):
        """ Initializes the customer object and set the name attribute to the
         name  
        
        Args:
            name (str): the customer name
        
        Side effects:
            Initializes self.name
        """
        self.name = name
        self.ingredients = []
        self.order = {}
        self.order["Name"] = self.name
        
    def dietary(self, type1 = None ):
        """ Finds out what dietary bowl the customer wants and inputs it
        into their bowl.
        
        Args:
            type (str): type of base ingredients
        """
        
        keto_salad_bowl = ["lettuce", "steak",
                            "red chili salsa", "cheese", "guacamole"]
        vegan_bowl = ["brown rice", "sofritas", "black beans", 
                      "tomatillo salsa", "corn salsa", 
                      "lettuce"]
        vegetarian_bowl = ["lettuce", "brown rice", 
                           "black beans", "fajitas", 
                           "tomato salsa","guacamole"]
        if type1 == "keto":
            self.ingredients += keto_salad_bowl
        elif type1 == "vegan":
            self.ingredients += vegan_bowl
        elif type1 == "vegetarian":
            self.ingredients += vegetarian_bowl
        else:
            self.assemble()
        
        self.order['Price'] = self.price_cal
        self.order['Calories'] = self.calories_count
    
    def assemble (self):
        base = input("Brown Rice, White Rice, or Lettuce? ")
        self.ingredients.append(base)
        beans = input("pinto or black")
        self.ingredients.append(beans)
        protein = input("chicken, steak, carnitas, sofritas (vegan),"
                        "veggies (vegan), barbacoa")
        protein = protein.strip().split(",")
        self.ingredients += protien
        salsa = input("red chili salsa, tomatillo salsa, corn salsa,"
                       "green chili salsa")
        salsa = salsa.strip().split(",")
        self.ingredients += salsa
        toppings = input("cheese, guacamole, lettuce, sour cream")
        toppings = toppings.strip().split(",")
        self.ingredients += toppings  
        
    def extra(self, type1, amount):
        """ updates self.order price based on extras ordered 
    
        Args:
            Type (str): type of topping and amount being add
            amount (int): the amount of extra toppings the customer wishes to
            order 
        """
        extra_price = {'chicken': 2.80, 'steak': 3.55, 'barbacoa': 3.55,
                   'carnitas': 3.00, 'sofritas': 2.80}
        price = self.price_cal()
        extra_amt = extras[type1] * amount
        price += extra_amt
        
        return price
        
        
        
    def calories_count(self):
        """ Determines the number of calories per order
        
        
        Return (int): 
            return the calories count
        """ 
        calorie_list = {'chicken': 180,'steak': 150, 'barbacoa': 170,
                        'carnitas': 210,'sofritas': 150,'fajitas': 20,
                         'white rice': 210, 'brown rice': 210,
                         'black beans': 130,'pinto': 130,'guacamole': 230,
                         'tomato salsa': 25,'corn salsa': 80,
                         'green chili salsa': 15,
                         'red chili salsa': 30,'sour cream': 110,
                         'fajita': 20,'cheese': 110,'lettuce': 5,
                         'queso blanco': 120}
        
        calorie_total = 0
        for i in self.ingredients:
            if i in calorie_list:
                calorie_total += calorie_list[i]
        
        return calorie_total
                
        
    def price_cal(self):
        """ Determines the price of the customer order
        
        Return (int): 
            return the price of the order 
        """
        prices = {"chicken" : 7.70, "steak" : 8.70 , "barbacoa" : 8.70, 
                "carnitas" : 8.20, "sofritas" : 7.70, "veggie" : 7.70, 
                "guacamole" : 2.30, "queso blanco" : 1.30}
        
        price = 0
        for i in self.ingredients:
            if i in prices:
                price += prices[i]
        
        return price

      
      
class Bowl(Burrito):
    """class for a burrito bowl order if selected.
    """
    def __init__(self):
        """initializes a burrito bowl.
        """
        super().__init__()
        
    def tor_pref(self,option):
        """ Find whether the customer is getting a tortilla
        
        Args (str): 
            customer indicates yes or no
        
        Return (Bool): 
            whether true of false  
        """
        
    #def tortilla(self,)

def customer_pref(type1):
    """ Identifies whether the customer wants a bowl or burrito.
        
    Args:
        type (str): determines whether the customer wants a bowl or burrito
             
    """
    if type1 != "bowl" or type1 != "burrito":
        raise TypeError("This is not a valid option")
    else:
        return type1

if __name__ == "__main__":

  
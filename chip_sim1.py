      
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
        
    def customer_pref(self, type1):
        """ Identifys wheather the customer wants a bowl or burrito.
        
        Args:
            type (str): determines whether the customer wants a bowl or burrito
             
        """
        if type1 != "bowl" or type1 != "burrito":
            raise TypeError("This is not a valid option")
        else:
            return type1

    def dietary(self, type1 = None ):
        """ Determines if the ingredients selected fit the restrictions
        comparir order within the dietary restrictions
        
        Args:
            type (str): type of base ingredients
        
        return:
            retuns a dictionary of list: price, calorie count,
            and contents of the bowl.
        """
        
        keto_salad_bowl = ["supergreens lettuce blend", "steak",
                            "tomatillo-red chili salsa", "cheese", "guacamole"]
        vegan_bowl = ["brown rice", "sofritas", "black beans", 
                      "fresh tomatillo salsa", "roasted chili- corn salsa", 
                      "shredded romaine lettuce"]
        vegetarian_bowl = ["super greens lettuce blend", "brown rice", 
                           "black beans", "fajita veggies", 
                           "fresh tomato salsa and guacamole"]
        if type1 == "keto":
            self.ingredients += keto_salad_bowl
        elif type1 == "vegan":
            self.ingredients += vegan_bowl
        elif type1 == "vegetarian":
            self.ingredients += vegetarian_bowl
        else:
            self.assemble()
        return self.ingredients
    
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
        toppings = input("cheese, guacamole, lettuce, sour cream, corn chips")
        toppings = toppings.strip().split(",")
        self.ingredients += toppings
        
        
            
        
    def extra(self, type, amount):
        """ Takes into account additional toppings such as duplicates 
        to the list
    
        Args:
            Type (str): type of topping and amount being add 
        
        Retruns dictionary: 
            returns a dictonary of prices and calories for items
        """

    def calories_count(self):
        """ Determines the number of calories per order
        
        
        Return (int): 
            return the calories count
        """    
    
    def price_cal(self):
        """ Determines the price of the customer order
        
        Return (int): 
            return the price of the order 
        """
      
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
           
if __name__ = "__main__":

  
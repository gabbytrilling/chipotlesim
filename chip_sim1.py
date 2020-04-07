""" Simulates a person ordering food at Chipotle.
"""
class Chipotle:
    """Simulates a person ordering food at Chipotle
    Attributes:
        name(str): the person ordering
    """
    
    def __init__(self, name):
        """Initializes the customer object and set the name attribute to the name  sets on type of food offered like 
        
        Args:
            name (str): the customer name
        
        Side effects:
            Initializes self.name
        """
    
    def customer_pref(self, bowl, burrito):
        """customer determines what kind of burrito he wants narrowing his options for toppings
        dictionary of option and prices
        """
    def calories_count(self):
        """ determines the number of calories per order"
        use dictionary
        put in end of class key value pair, last
        """
    def customer_budget(self):
        """customers can select id they have a budget and if the customer
         surpasses the budget they will start the order again or can remove items, before price
        """
    def dietary(self, paleo, ):
        """determines if the ingredients selected fit the restrictions
        comparir order within the dietary restrictions, set
        """
    def extra_topings(self,guac, queso,protein,chips):
        """takes into account additional toppings such as duplicates to the list
        combine with next method"""
    def sides_option( self, chips, drink):
        """ asks for sides
        """
    def price_cal(self):
        """determines the price of the customer order
        """
        
        
""" Simulates a person ordering food at Chipotle.
"""

class Burrito:
    """Simulates a person ordering food at Chipotle
    Attributes:
        name(str): the person ordering
    """
    def __init__(self, name):
        """Initializes the customer object and set the name attribute to the name  sets on type of food offered like 
        
        Args:
            name (str): the customer name
        
        Side effects:
            Initializes self.name
        """
    
    def dietary(self, paleo, ):
        """determines if the ingredients selected fit the restrictions
        comparir order within the dietary restrictions, set
        """
    def extra(self,guac, queso,protein,chips,drink):
        """takes into account additional toppings such as duplicates to the list
        combine with next method"""
        
     def customer_budget(self):
        """customers can select id they have a budget and if the customer
         surpasses the budget they will start the order again or can remove items, before price
        """ 
    def price_cal(self):
        """determines the price of the customer order
        """
      
class Bowl(Burrito):
    
if __name__ = "__main__":
  
      
""" Simulates a person ordering food at Chipotle.
"""

class Burrito:
    """Simulates a person ordering food at Chipotle
    Attributes:
        name(str): the person ordering
    """
    def __init__(self, name):
        """Initializes the customer object and set the name attribute to the
         name  sets on type of food offered like 
        
        Args:
            name (str): the customer name
        
        Side effects:
            Initializes self.name
        """
    
    def dietary(self, type ):
        """determines if the ingredients selected fit the restrictions
        comparir order within the dietary restrictions, set
        
        Args:
            type (str): type of base ingredients
        
        return:
            retuns a dictionary of list: price, calorie count,
            and contents of the bowl.
        """
    def extra(self, type, amount):
        """takes into account additional toppings such as duplicates to the list
        combine with next method
        
        Args:
            Type (str): type of topping and amount being add 
        
        Retruns dictionary: 
            returns a dictonary of prices and calories for items
        """

    def calories_count(self):
        """ determines the number of calories per order"
        use dictionary
        put in end of class key value pair, last
        
        Return (int): return the calories count
        """    
    
    def price_cal(self):
        """determines the price of the customer order
        
        Return (int): return the price of the order 
        """
      
class Bowl(Burrito):
    """class for a burrito bowl order if selected.
    """
    def __init__(self):
        """initializes a burrito bowl.
        """
        super().__init__()
        
    def tor_pref(self,option):
        """find whether the customer is getting a tortilla
        
        Args
        
        Return Bool: whether true of false  
        """
    def tortilla(self,)
        
    
    
if __name__ = "__main__":
  
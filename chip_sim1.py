      
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
        
    def customer_pref(self, type):
        """ Identifys wheather the customer wants a bowl or burrito.
        
        Args:
            type (str): determines whether the customer wants a bowl or burrito
             
        """
    def dietary(self, type ):
        """ Determines if the ingredients selected fit the restrictions
        comparir order within the dietary restrictions
        
        Args:
            type (str): type of base ingredients
        
        return:
            retuns a dictionary of list: price, calorie count,
            and contents of the bowl.
        """
        
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

  
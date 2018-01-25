"""
    This file consists of a class that extracts data 
    From the Baseball Records. 
"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

from Extract.Records.AbstractRecord import AbstractRecord

class BaseballRecord(AbstractRecord):
    
    """
        Constructor Method
        @param p_name -> THe name of the player
        @param g_played -> Games Played
        @param salary -> The salary of the player
        @param avg -> Player Batting Average
    """
    def __init__(self, p_name, salary, g_played, avg):
        try:
            # initialize from the parent class constructor 
            super().__init__(p_name)
             
            # initialize attributes from this class
            self._salary = salary 
            self._g_played = g_played
            self._avg = avg
        except Exception as e:
            print("There was an error when trying to instantiate a class")
            print(e)

    
    """
        Override the default __str__ method 
    """
    def __str__(self):
        return "Baseball Records -> \n Player Name: {} \n Salary: ${:.2f}\n Games Played: {}\n Batting Average: {:.3f}\n".format(self._name, self._salary, self._g_played, self._avg)
    

# use this to write the test code
if __name__ == "__main__":
    b_rec = Baseball("Aman Nagpal", 100000, 100, 12)
    print(b_rec)

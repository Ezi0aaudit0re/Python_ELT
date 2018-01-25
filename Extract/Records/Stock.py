"""
    This file consists of a class that extracts data 
    From the Stock Records. 
"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

from Extract.Records.AbstractRecord import AbstractRecord


class StockRecord(AbstractRecord):

   """
       This constructor method initializes the various instance variables
       The instance variables set to private _ 
       @param Stock symbol (ticker)→ this should be stored in the “name” member
       @param company_name -> Name of the company 
       @param exchange_contry 
       @param shares_outstanding 
       @param net_income
       @param market_value_usd 
       @param pe_ratio
   """
   def __init__(self, tkier, company_name, exchange_country, price, exchange_rate, shares_outstanding,
               net_income, market_value_usd, pe_ratio):
        try:
             super().__init__(tkier) # instantiate variable from parent class

             # instantiate remaining variables
             self._company_name = company_name
             self._exchange_country = exchange_country
             self._price = price
             self._exchange_rate = exchange_rate
             self._shares_outstanding = shares_outstanding
             self._net_income = net_income
             self._market_value_usd = market_value_usd
             self._pe_ratio = pe_ratio
        # default exception handling
        except Exception as e:
            print("An exception occured while instantiating Stock class")
            print(e)

        """
            Override the default __str__ method
        """
   def __str__(self):
       str =  "Stock Record ->\n Stock Stymbol:{}\n Comapy Name: {}\n Exchange Country: {}\n Price: ${:.2f}\n Exchange Rate: ${:.2f}\n Outstanding Shares: {:.3f}\n Net Income: ${:.2f}\n Market Value In USD: ${:.2f}\n Pe Ratio: {:.3f} \n".format(self._name, self._company_name, self._exchange_country, self._price, self._exchange_rate, self._shares_outstanding, self._net_income, self._market_value_usd, self._pe_ratio)
       return str



# write test in this 
if __name__ == "__main__":
    s_record = StockRecord("Aman", "APL", "India", 100, 100.12, 200, 1000000, 123, 10.11)
    print(s_record)



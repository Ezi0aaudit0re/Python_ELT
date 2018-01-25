"""
    This file contains the StockCSVReader class. 
    THis class inherits from the AbstractCSVReader class.
    It contains methods that deals with the stock CSV file
"""

__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

import sys
from Extract.CSVReaders.AbstractCsvReader import AbstractCSVReader

sys.path.insert(0, "../Records")
from Extract.Records.Stock import StockRecord

class StockCSVReader(AbstractCSVReader):

    _KEYS = ("ticker", "company_name", "exchange_country", "exchange_rate", "price", "shares_outstanding", "net_income" )

    """
        Implementation of row_to_record method for stocks
        THis method also validates the row that is passed to it 
        @param row -> The row from csv file
    """
    def row_to_record(self, row):

        try:

            # check if the row has all the keys 
            # loop through _KEYS and check all keys are in the row
            if all([True if k in row.keys() else k for k in self._KEYS]):
                # we try adding the values to the record
                # if there is a problem then exception is raised and there we return false
                market_value_usd = eval(row["price"]) * eval(row["exchange_rate"]) * eval(row["shares_outstanding"])
                pe_ratio = eval(row["price"]) / eval(row["net_income"])

                return StockRecord(row["ticker"], row["company_name"], row["exchange_country"], eval(row["price"]), eval(row["exchange_rate"]), eval(row["shares_outstanding"]), eval(row["net_income"]), market_value_usd, pe_ratio)




        except (SyntaxError, NameError) as e:
            # this code block runs if float or int number cannot be parsed
            # we return False so that that row is not added
            return False 

        except KeyError as e:
            # We come across this error if the value at a particular key is not given
            return False

        except Exception as e:
            # this is if we come across a general error
            # we cannot return false for this might be logic error 
            print(e)
            print(e.__class__.__name__)
            exit(0)


if __name__ == "__main__":
    stock_reader = StockCSVReader("../../CSV Files/StockValuations.csv")
    result = stock_reader.load()
    for r in result:
        print(r)

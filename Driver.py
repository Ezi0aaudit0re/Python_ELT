"""
    This file acts as the driver for the extract part of the program  
"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

import sys 

# insert to the paths here otherwise file not found error
sys.path.insert(0, "./Extract/CSVReaders") # to import csv readers
sys.path.insert(0, "./Extract") # for exceptions
sys.path.insert(0, "./Extract/Records") # to import records to be used

from Extract.CSVReaders.BaseballCSVReader import BaseballCSVReader
from Extract.CSVReaders.StockCSVReader import StockCSVReader

"""
    This is the main driver of the program
"""
def main():

    print("------------------------------ Stocks -----------------------------")
    # print the records of Stocks
    stocks = StockCSVReader("./CSV Files/StockValuations.csv").load()
    for stock in stocks:
        print(stock)

    print("---------------------------------------------------------------------\n")

    print("------------------------------ Baseball -----------------------------")
    baseball = BaseballCSVReader("./CSV Files/MLB2008.csv").load()
    for data in baseball:
        print(data)

    print("---------------------------------------------------------------------\n")

    exit(0)



if __name__ == "__main__":
    main()
    

"""
    This is the Abstract Class for reading from the CSV file 
    This file contains a Parent Reader class
"""

__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"


import csv
import os
import sys 

# to use exceptions
sys.path.insert(0, "../") 
from Extract.Exceptions import BadDataError, NoFileError


class AbstractCSVReader:

    """
        Constructor method 
        @param f_path -> Path of the file
    """
    def __init__(self, f_path):
        try:
            # store it in the instance variable
            if os.path.isfile(f_path):
                self._f_path = f_path
            else:
                raise NoFileError("The name of the file was incorrect")

        except NoFileError as e:
            print(e)
            print("Quiting the program")
            exit(1)

        except Exception as e:
            print("The following exception has occured")
            print(e)
            print("Quiting the program")
            exit(1)
        finally:
            pass


    """
        This method is not implemented and should be implemented in the child class
        @param row -> The row in the csv file
    """
    def row_to_record(self, row):
        raise NotImplementedError("This method is not implemented in the parent class")


    """
        This method opens the csv file and reads from it 
        @return records -> a list of records
    """
    def load(self):
        try:
            with open(self._f_path, "r") as file:
                records = []
                reader = csv.DictReader(file)
                for row in reader:
                    if(row):
                        # we pass the row to row_to_record method 
                        record = self.row_to_record(row)
                        if record:
                            records.append(record)
                    else:
                        raise BadDataError(row);


        except BadDataError as e:
            # this makes sure the program doesnot crash if we come across a bad data 
            pass
        except Exception as e:
            raise BadDataError(row)
            print("An unknown exception occured")
            print(e)

        finally:
            # return the loaded records in the list 
            # we add it in the finally clause so that even the program comes across an exception 
            # we can use this to see which record did the error occur at 
            return records




# here we write our test code 
if __name__ == "__main__":
    reader = AbstractCSVReader("../CSV Files/StockValuations.csv")
    reader.load()


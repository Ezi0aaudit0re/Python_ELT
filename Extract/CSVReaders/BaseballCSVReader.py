"""
    This file contains the BaseballCSVReader class. 
    THis class inherits from the AbstractCSVReader class.
    It contains methods that deals with the baseball CSV file
"""

__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

import sys
from Extract.CSVReaders.AbstractCsvReader import AbstractCSVReader

sys.path.insert(0, "../Records")
from Extract.Records.Baseball import BaseballRecord
from Extract.Exceptions import BadDataError, NoFileError



class BaseballCSVReader(AbstractCSVReader):

    _KEYS = ("PLAYER" , "SALARY", "G", "AVG")


    # this method takes in the path of the file and calls the super method to init in parent class
    def __init__(self, f_path):
        super().__init__(f_path)


    """
        Here we implement the row to record method from the parent class
        THis method validates the data saves it in record and returns it 
        @param row -> row from the csv file
    """
    def row_to_record(self, row):
        try:
            # validate if keys are in the dict
            if all([True if k in row.keys() else False for k in self._KEYS ]):
                if(eval(row["SALARY"]) and eval(row["G"]) and eval(row["AVG"])):
                    return BaseballRecord(row["PLAYER"], eval(row["SALARY"]), eval(row["G"]), eval(row["AVG"]))

        except (SyntaxError, NameError) as e:
            # this code block runs if float or int number cannot be parsed
            # we return False so that that row is not added
            raise BadDataError()
            return False 

        except KeyError as e:
            # We come across this error if the value at a particular key is not given
            raise BadDataError()
            return False

        except Exception as e:
            # this is if we come across a general error
            # we cannot return false for this might be logic error 
            raise BadDataError()
            print(e)
            print(e.__class__.__name__)
            exit(0)
        



if __name__ == "__main__":
    baseball_reader = BaseballCSVReader("../../CSV Files/MLB2008.csv")
    result = baseball_reader.load()
    for r in result:
        print(r)

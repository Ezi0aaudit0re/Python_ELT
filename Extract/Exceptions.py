"""
    This file contains the custom exception classes
"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

# This exception occurs when the name of the file provided doesnot exist
class NoFileError(Exception): pass

# Exception handles Bad data in the csv file
class BadDataError(Exception): pass

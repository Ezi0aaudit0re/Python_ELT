"""
    This file has the context manager class "createConnection"
    This class is used to establish a connection to  a databse
"""
__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"


import sqlite3

class createConnection:

    """
    Constructor to initialize instance variables file and method 
    :param: file -> the name of the file
    """
    def __init__(self, file,):
        self.file = file

    def __enter__(self):
        try:
            if self.file:
                self.conn = sqlite3.connect(self.file)
                return self.conn
            else:
                raise Exception("There was some problem creating the connection")
        except Exception as e:
            print("Connection could not be established")
            exit(1)

    def __exit__(self, type, value, traceback):
        print("Database: '{}' has been created".format(self.file))
        self.conn.close()

        if traceback:
            print("An exception occured: {ex}".format(ex=str(type)))

if __name__ == "__main__":
    with createConnection("test.db") as conn:
        print(conn)
    



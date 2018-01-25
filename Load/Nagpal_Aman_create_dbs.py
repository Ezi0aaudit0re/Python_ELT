"""
    This file creates the tables and the database file 
    Creates a table for Stocks with the following colums 
        stock_stats
    ========================
    company_name       text
    ticker                       text
    country                    text
    price                        real
    exchange_rate         real
    shares_outstanding  real
    net_income              real
    market_value_usd   real
    pe_ratio                   real

    It also creates a table for baseball stats with the following data 

     Baseball_stats
    ========================
    player_name          text
    games_played        int
    average                  real
    salary                     real
"""

__author__ = "Aman Nagpal"
__email__ = "amannagpal4@gmail.com"

import sqlite3
import os
import sys 

sys.path.append("../Helper")
from create_connection import createConnection

baseball_info = [{"colum": "player_name", "type": "text"},
                 {"colum": "games_played", "type": "int"},
                 {"colum": "average", "type": "real"},
                 {"colum": "salaray", "type": "real"},
                ]

stat_info = [{"colum": "company_name", "type": "text"},
             {"colum": "ticker", "type": "text"},
             {"colum": "country", "type": "text"},
             {"colum": "price", "type": "real"},
             {"colum": "exchange_rate", "type": "real"},
             {"colum": "shares_outstanding", "type": "real"},
             {"colum": "net_income", "type": "real"},
             {"colum": "market_value_usd", "type": "real"},
             {"colum": "pe_ratio", "type": "real"},
                ]


"""
    This function creates the table for baseball.db
"""
def createBaseballTable():
    with createConnection("baseball.db") as conn:
        cursor = conn.cursor()
        query = "CREATE TABLE if not exists baseball_stats ({col1} {col1_type}, {col2} {col2_type}, {col3} {col3_type}, {col4} {col4_type})".format(
                col1 = baseball_info[0]["colum"], col1_type= baseball_info[0]["type"],
                col2 = baseball_info[1]["colum"], col2_type= baseball_info[1]["type"],
                col3 = baseball_info[2]["colum"], col3_type= baseball_info[2]["type"],
                col4 = baseball_info[3]["colum"], col4_type= baseball_info[3]["type"])
        cursor.execute(query)



"""
    This function creates the table for stock.db
"""
def createStocksTable():
    with createConnection("stocks.db") as conn:
        cursor = conn.cursor()
        query = "CREATE TABLE if not exists stock_stats ({col1} {col1_type}, {col2} {col2_type}, {col3} {col3_type}, {col4} {col4_type}, {col5} {col5_type}, {col6} {col6_type}, {col7} {col7_type}, {col8} {col8_type}, {col9} {col9_type})".format(
                col1 = stat_info[0]["colum"], col1_type= stat_info[0]["type"],
                col2 = stat_info[1]["colum"], col2_type= stat_info[1]["type"],
                col3 = stat_info[2]["colum"], col3_type= stat_info[2]["type"],
                col4 = stat_info[3]["colum"], col4_type= stat_info[3]["type"],
                col5 = stat_info[4]["colum"], col5_type= stat_info[4]["type"],
                col6 = stat_info[5]["colum"], col6_type= stat_info[5]["type"],
                col7 = stat_info[6]["colum"], col7_type= stat_info[6]["type"],
                col8 = stat_info[7]["colum"], col8_type= stat_info[7]["type"],
                col9 = stat_info[8]["colum"], col9_type= stat_info[8]["type"],)
        cursor.execute(query)


if __name__ == "__main__":
    createBaseballTable()
    createStocksTable()
    






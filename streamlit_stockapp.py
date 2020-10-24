import streamlit as st
import time
import numpy as np
import pandas as pd
import stock_class
import stock_streamlit_functions as div

START, END = '2020-01-01', '2020-06-01'

st.beta_set_page_config(page_title='Stock Analysis', initial_sidebar_state="expanded")
ticker = st.sidebar.text_input("Enter Stock Ticker", value='TSLA')

stock = stock_class.Stock(ticker, START, END)

# Quick Function to Clean Data
def pull_info(stock, key):
    try: return stock.info[key]
    except: return 'Data Not Found'

# Write Title and General Company Information to the Report
#
st.title("Stock Analysis - " + str(pull_info(stock, 'longName')))
st.write("This is an autogenerated Stock Analysis for " + pull_info(stock, 'longName') + ' \n' 
          + "The company is located in " + pull_info(stock, 'city') + ', ' + pull_info(stock, 'state') 
          + ', ' + pull_info(stock, 'country') + ". \n" +  pull_info(stock, 'longName') + " is in the " 
          + pull_info(stock, 'sector') + ' and the ' + pull_info(stock, 'industry'))
st.write('Website Link: ' + pull_info(stock, 'website'))

# Create SideBar Objects to Choose What to Include In the Report
#
st.sidebar.title("Create Your Stock Report")
graphs_multiselect = st.sidebar.multiselect(
    "Graph A Relationship",
    ("Price/Time",), default='Price/Time')

show_df = st.sidebar.checkbox('Show DataFrames')

stmt_multiselect = st.sidebar.multiselect(
    "Pull Financial Statement Information",
    ("Income Statement", "Balance Sheet", "Statement of Cash Flows"), default="Income Statement")
show_explanations = st.sidebar.checkbox('Show Descriptions')


div.show_graphs(graphs_multiselect, stock, show_df)

div.show_fin_stmts(stmt_multiselect, stock, show_explanations)
    
st.button("Re-run")

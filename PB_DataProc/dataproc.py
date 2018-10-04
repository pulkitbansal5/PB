"""
This python library contains different user defined methods to perform different data processing techniques using pandas and numpy.
Author@PulkitBansal
Version 0.1
Created On: 4-Oct-2018 12:50 PM
Last Updated: 4-Oct-2018 12:50 PM
Last Modified By: @PulkitBansal

"""
import pandas as pd

#Converting a list to a series object
ls=['Pulkit','Shubham','Rohit','Rahul','Akshay','Suraj']
series = pd.Series(ls)
print(series)
print(type(series))

print("---------------------------------------------------")
#Converting a tuple to a series object
tu = ('Sun','Mon','Tue','Wed','Thru','Fri','Sat')
ser = pd.Series(ls)
print(ser)
print(type(ser))

print("---------------------------------------------------")
#Converting a dictionary to a series object
dict = {'Name':'Pulkit','Occupation':'Software Engineer','Company Name':'Cians Analytics'}
ser_dic = pd.Series(dict)
print(ser_dic)
print(type(ser_dic))
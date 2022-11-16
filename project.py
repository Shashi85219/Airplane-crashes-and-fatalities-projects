
# develop a console based project of like username and password of the user
# and admin according to that data will be visible to the console.
# from pickletools import pybytes_or_str

'''
*****************************************************
***   PROJECT REPORT ON AIRPALNE FATALITIES AND DEATHS   ***
*****************************************************
'''

from ctypes.wintypes import HINSTANCE
from logging import makeLogRecord
from turtle import title
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("***********************************************************************")
data=pd.read_excel('data.xlsx') # dataset import
print("All DataSet Information")
print("***********************************************************************")
print(data)
print("----------------------------------------------------------------------\n")

print("Please ! Login here For know total fatlitates and Death in Airplane Services: -")

print("----------------------------------------------------------------------\n")
userName = input("Enter user Name:\t")
passsword = input("Enter password:\t")
print("------------------------------------------------------------------\n")
if userName == "kumar" and passsword == "kumar143@":
    print("User Login successfully")
    print("------------------------------------------------------------------\n")
    
    while (1):
        print("[1]. Press one for Know the total Deaths in during the travel :")
        print("[2]. Press two for know total Accident like year wise :")
        print("[3]. Press Three for know How many total airline fatalities in during take off")
        print("[4]. Press four for know the places where people dead :- ")
        print("[Else key]. Press Else key for exits :")
        print("----------------------------------")

        option = int(input("Enter your option :"))

        if option == 1:
            print("These are total deaths in during the travel...")
            plt.figure(figsize= (10, 10))
            plt.plot(data['Deaths'],data['flight_name'] , marker= 'o',ms=20,mfc='r')
            plt.title("These are total deaths in during the travel.")
            plt.xlabel('Deaths')
            plt.ylabel('Flight_name ')
            # plt.legend()
            plt.legend(["blue", "green"], loc ="lower right")
            plt.show()
            print("----------------------------------")
            
        elif option == 2:
            print("These are total Accident like year wise :")
            plt.figure(figsize= (12, 10))
            plt.bar(data['fatalities'], data['year'],color="red")
            plt.title("These are total Accident like year wise :")
            plt.xlabel('fatalities')
            plt.ylabel('Year')
            plt.show()
            print("----------------------------------")

        elif option == 3:
            print("These are the total airline fatalities in during take off")
            plt.figure(figsize= (10, 9))
            plt.plot(data['fatalities'], data['flight_name'], marker='*',ms=20,mfc='hotpink')
            plt.title("These are total Accident like year wise :")
            plt.xlabel('fatalities')
            plt.ylabel('flight_name')
            plt.grid()
            plt.legend("red",loc="upper right")
            plt.show()
            print("----------------------------------")
         
        elif option == 4:
            print("These are the places where people dead :")
            plt.figure(figsize= (12, 10))
            plt.plot(data['Deaths'], data['Location'],marker='H',ms=20,mfc='g',linestyle='dashed')
            plt.title("These are the places where people dead :")
            plt.xlabel('Deaths')
            plt.ylabel('Location')
            plt.grid()
            plt.show()
            print("----------------------------------")   
        
        # program continue for menu option  :
         
        else:
            exit(1)

else:
    if userName != "kumar" or passsword != "kumar143@":
        print("invalid userName and password")
        
        #  END 




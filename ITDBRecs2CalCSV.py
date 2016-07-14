import argparse
import pyodbc
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser(description='Read file names')
parser.add_argument('--model', help='Module type')
parser.add_argument('--mac', help='MAC address')
parser.add_argument('--wo', help='Work order')

args = parser.parse_args()

MODEL = args.model
MAC = args.mac.lower()
WORK_ORDER = args.wo

conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=pe1.summit.local;DATABASE=Ops_Staging;UID=ops-it-ro;PWD=v3xaNAgeP')

sqlstring = '''
SELECT Table_TestInfo.*
FROM OPS_Staging.dbo.Table_TestInfo Table_TestInfo
WHERE
    (Table_TestInfo.Model='%s') AND 
    (Table_TestInfo.MAC_Address='%s') AND 
    (Table_TestInfo.Test_Type='InitialTest') AND
    (Table_TestInfo.Work_Order='%s')
''' % (MODEL, MAC, WORK_ORDER)

testinfo_data = pd.read_sql(sqlstring, conn)

for i in testinfo_data.index:
    print("%d:\t%s\t%s\t%s\t%s" %
        (
            i,
            testinfo_data.irow(i)['MAC_Address'],
            testinfo_data.irow(i)['Work_Order'],
            testinfo_data.irow(i)['Hard_Bin'],
            testinfo_data.irow(i)['Soft_BIN'],
        )
    )
    
choice = input("Enter your choice: ")

sqlstring = '''
SELECT
    Table_Test_Calibration.*
FROM
    OPS_Staging.dbo.Table_Test_Calibration Table_Test_Calibration
WHERE
    (Table_Test_Calibration.GUID = '%s')
ORDER BY Table_Test_Calibration.Step
''' % (testinfo_data.irow(choice)['GUID'],)

cal_data = pd.read_sql(sqlstring, conn)

calfile = open(MAC + '_' + testinfo_data.irow(choice)['GUID'] + '_cal_table.csv', 'w')
cal_data.to_csv(calfile)
calfile.close()
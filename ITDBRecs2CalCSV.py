import pyodbc
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt
import numpy as np

conn = pyodbc.connect(r'DRIVER={SQL Server};SERVER=pe1.summit.local;DATABASE=Ops_Staging;UID=ops-it-ro;PWD=v3xaNAgeP')
sqlstring = '''
SELECT
    Table_Test_Calibration.*
FROM
    OPS_Staging.dbo.Table_TestInfo Table_TestInfo,
    OPS_Staging.dbo.Table_Test_Calibration Table_Test_Calibration
WHERE
    (Table_TestInfo.Model='Athena4XC') AND 
    (Table_TestInfo.MAC_Address='02ea3100ae9f') AND 
    (Table_TestInfo.Test_Type='InitialTest') AND
    (Table_TestInfo.Work_Order='1536917305-L10') AND
    (Table_TestInfo.GUID = Table_Test_Calibration.GUID)
ORDER BY Table_Test_Calibration.Step
'''

cal_data = pd.read_sql(sqlstring, conn)
from sub import run_q
import pandas as pd
 
# import the StrinIO function
# from io module
from io import StringIO
 
query="total number of employees"
cmd,fin=run_q(query)
# wrap the string data in StringIO function
if type(cmd) is int:
    print(type(cmd))
else:
    print(cmd.columns)
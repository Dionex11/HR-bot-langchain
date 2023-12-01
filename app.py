from sub import run_q
import pandas as pd
 
query="senior most frontend developer"
cmd,fin=run_q(query)
print(cmd)
if type(cmd) is int:
    print(cmd)
<<<<<<< HEAD
elif isinstance(cmd,pd.core.series.Series):
    print(cmd)
elif isinstance(cmd,pd.core.frame.DataFrame):
    print(type(cmd))
    dict_format={"columns":[],"data":[]}
    c=cmd.columns
    d=cmd.values.tolist()
    columns_list=[]
    for col in c:
        columns_list.append(col)
    dict_format["columns"]=columns_list
    dict_format["data"]=d
    print(dict_format)
    print(cmd.columns)
else:
    print(cmd)
=======
else:
    print(cmd)
>>>>>>> 534fb3825cd512f65e34c6e59f89cd632860933a

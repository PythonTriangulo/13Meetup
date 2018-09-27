#Lendo um arquivo cvs e tirando a média

import pandas as pd                     
df = pd.read_csv('2015-01-01.csv')      
df.groupby(df.user_id).value.mean()

import dask.dataframe as dd
df = dd.read_csv('2015-*-*.csv')
df.groupby(df.user_id).value.mean().compute()

#lendo um arquivo e tirando a média de um array

import numpy as np                       
f = h5py.File('myfile.hdf5')             
x = np.array(f['/small-data'])      
x - x.mean(axis=1)     

import dask.array as da
f = h5py.File('myfile.hdf5')
x = da.from_array(f['/big-data'], chunks=(1000, 1000))
x - x.mean(axis=1).compute()


import dask.bag as db
#lendo um arquivo json comprimido e aplicando a função load em cada item do json
b = db.read_text('2015-*-*.json.gz').map(json.loads)
#
b.pluck('name').frequencies().topk(10, lambda pair: pair[1]).compute()



from dask import delayed
L = []
for fn in filenames:                  # Use for loops to build up computation
    data = delayed(load)(fn)          # Delay execution of function
    L.append(delayed(process)(data))  # Build connections between variables

result = delayed(summarize)(L)
result.compute()
import pandas as pd
import numpy as np

df = pd.DataFrame({ 
  'A' : 1.,
  'B' : pd.Timestamp('20130102'),
  'C' : pd.Series(1 ,index = list(range(4)), dtype = 'float32'),
  'D' : np.array([3] * 4, dtype = 'int32'),
  'E' : pd.Categorical([ "test", "train", "test", "train" ]),
  'F' : 'foo' 
})


print df

print ""

# dataframe types
print df.dtypes


print ""

# head
print df.head(1)

print ""

# head
print df.tail(1)



print "index"
print df.index


print "columns"
print df.columns

print "values"
print df.values



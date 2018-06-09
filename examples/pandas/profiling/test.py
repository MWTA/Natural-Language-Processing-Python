import pandas as pd
import pandas_profiling
import numpy as np


df = pd.read_csv("examples/Meteorite_Landings.csv",
                 parse_dates=['year'], encoding='UTF-8')

# Note: Pandas does not support dates before 1880, so we ignore these for this analysis
df['year'] = pd.to_datetime(df['year'], errors='coerce')

# Example: Constant variable
df['source'] = "NASA"

# Example: Boolean variable
df['boolean'] = np.random.choice([True, False], df.shape[0])

# Example: Mixed with base types
df['mixed'] = np.random.choice([1, "A"], df.shape[0])

# Example: Highly correlated variables
df['reclat_city'] = df['reclat'] + np.random.normal(scale=5, size=(len(df)))

# Example: Duplicate observations
duplicates_to_add = pd.DataFrame(df.iloc[0:10])
duplicates_to_add[u'name'] = duplicates_to_add[u'name'] + " copy"

df = df.append(duplicates_to_add, ignore_index=True)

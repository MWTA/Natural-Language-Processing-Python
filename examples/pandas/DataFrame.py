import pandas as pd

df_data = {
    'pais': ['Brasil', 'Argentina', 'Argentina', 'Brasil', 'Chile', 'Chile'],
    'ano': [2005, 2006, 2005, 2006, 2007, 2008],
    'populacao': [170.1, 30.5, 32.2, 172.6, 40.8, 42.0]
}

df = pd.DataFrame(df_data)
print(df)

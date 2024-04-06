import pandas as pd 

countries_info = pd.DataFrame({'USA': ['Washington, D.C.', '333.3 million'], 'UAE': ['Abu Dhabi', '1.45 million'],\
              'Germany': ['Berlin', '3.645 million'], 'France': ['Paris', '2.161 million']}, index = ['Capital', 'Population'])

print(countries_info)
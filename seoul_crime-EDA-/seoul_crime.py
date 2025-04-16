import pandas as pd
import numpy as np

seoul_crime_data = pd.read_excel('data/seoul_crime_data.xlsx', header=2)
seoul_crime_data = seoul_crime_data.dropna()
seoul_crime_data = seoul_crime_data.rename(columns={'강간·강제추행': '성범죄',
                                                    '강간·강제추행.1': '성범죄.1',
                                                    '소계': '합계',
                                                    '소계.1': '합계.1'})

seoul_crime_data.columns = ['자치구별(1)', '자치구별'] +[
    col.replace('.1', '') + '검거' if '.1' in col else col + '발생'
    for col in seoul_crime_data.columns
    if col not in ['자치구별(1)', '자치구별']
]
print(seoul_crime_data.columns)

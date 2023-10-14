import pandas as pd
from difflib import SequenceMatcher
import numpy as np
import os

class Comparison():
    def __init__(self, yt:list, sp:list, missing:list) -> None:
        self.missing = missing
        self.data = {
            'yt': yt,
            'sp': sp,
        }
        self.df = pd.DataFrame(data=self.data)

    def ratio(self):
        ratios = []
        for index, row in self.df.iterrows():
            ratios.append(SequenceMatcher(None, row['yt'], row['sp']).ratio())
        
        self.df['ratio'] = ratios
        

    def export(self, dir:str, name:str):
        if not os.path.exists(dir):
            os.mkdir(dir)
        
        if not name.endswith('.xlsx'): name += '.xlsx'
        export = os.path.join(dir, name)
        #print(self.df)
        self.df = self.df.sort_values(['ratio'])
        self.df.to_excel(export)

if __name__ == "__main__":
    pass
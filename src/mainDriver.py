from data_analyzer import Data_analyze
#from data_handler import
#from model_evaluator import 
#from model_trainer import 
#from visualizer import 

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    lung_cancer_csv = 'lung_cancer_prediction.csv'
    
    #data_analyzer1 = Data_analyze(lung_cancer_csv)
    
    lung = pd.DataFrame(lung_cancer_csv)
    
    print(lung)
    
    #data_analyzer1.reading_data()

if __name__ == '__main__':
    main()
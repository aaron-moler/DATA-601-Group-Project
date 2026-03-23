from libraries_used import pd
from libraries_used import np 

class Data_analyze:
    
    def __init__(self, lung_cancer_csv):
        self.lung_cancer_csv = lung_cancer_csv
        self.lung_cancer_df = None
        
    def load_data(self):
        self.lung_cancer_df = pd.read_csv(self.lung_cancer_csv)
        return self.lung_cancer_df
    
    def reading_data(self):

        df = self.load_data()

        while True:
            print("\n===== DATA MENU =====\n"
              "\t1  - Head\n"
              "\t2  - Tail\n"
              "\t3  - Info\n"
              "\t4  - Describe\n"
              "\t5  - Value Counts\n"
              "\t6  - Shape\n"
              "\t7  - Columns\n"
              "\t8  - Null Values\n"
              "\t9  - Data Types\n"
              "\t10 - Sample Rows\n"
              "\t11 - Null %\n"
              "\t0  - Exit\n")

            choice = input("Enter choice: ")

            actions = {
            "1": lambda: print(df.head()),
            "2": lambda: print(df.tail()),
            "3": lambda: df.info(),
            "4": lambda: print(df.describe()),
            "5": lambda: self.value_counts(df),
            "6": lambda: print(df.shape),
            "7": lambda: print(df.columns),
            "8": lambda: print(df.isnull().sum()),
            "9": lambda: print(df.dtypes),
            "10": lambda: print(df.sample(5)),
            "11": lambda: print((df.isnull().sum() / len(df)) * 100),
        }

            if choice == "0":
                print("Exiting...")
                break

            if choice in actions:
                actions[choice]()
            else:
                print("Invalid choice")


    def value_counts(self, df):
        col = input("Enter column name: ")
        if col in df.columns:
            print(df[col].value_counts())
        else:
            print("Column not found")
        

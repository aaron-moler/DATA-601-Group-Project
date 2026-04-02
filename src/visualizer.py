from libraries_used import pd
from libraries_used import plt
from libraries_used import sns
from sklearn.feature_selection import mutual_info_classif

class DataVisualizer:

    def __init__(self,df):
        self.df = df

    #histograms - int/float value variables
    def histogram(self, var, bins=None):
        self.df[var].hist(bins)
        plt.title(f'{var} Histogram')
        plt.xlabel(var)
        plt.ylabel("Amount")
        plt.show()

    #bar plot - categorical variables
    def bar_chart(self, var):
        self.df[var].value_counts().plot(kind='bar')
        plt.title(f'{var} Bar Chart')
        plt.xlabel(var)
        plt.ylabel("Amount")
        plt.show()

    #variable vs target box plot
    def variable_vs_target(self, var, target):
        sns.boxplot(x=target, y=var, data=self.df)
        plt.title(f'{var} Versus {target}')
        plt.xlabel(target)
        plt.ylabel(var)
        plt.show()

    #correlation heatmap
    def corr_matrix(self):
        corr_mtx = self.df.corr()
        sns.heatmap(corr_mtx, square=True)
        plt.title("Correlation Matrix")
        plt.show()

    #find missing values w/ heatmap
    def missing(self):
        sns.heatmap(self.df.isnull(), cbar=False, square=True)
        plt.title("Missing Value Matrix")
        plt.show()

    #pie chart
    def pie_chart(self, var):
        self.df[var].value_counts().plot(kind='pie')
        plt.title(f'{var} Pie Chart')
        plt.xlabel(var)
        plt.ylabel("Amount")
        plt.show()


    #stacked bar
    def stacked_bar_chart(self, varTop, varBottom):
        fTable = pd.crosstab(self.df[varBottom], self.df[varTop])
        fTable.plot(kind='bar', stacked=True)
        plt.title(f'{varTop} and {varBottom} Bar Chart')
        plt.xlabel(varBottom)
        plt.ylabel("Amount")
        plt.legend(title=varTop)
        plt.show()

    #grouped bar
    def grouped_bar_chart(self, var1, var2):
        fTable = pd.crosstab(self.df[var2], self.df[var1])
        fTable.plot(kind='bar', stacked=False)
        plt.title(f'{var1} and {var2} Bar Chart')
        plt.xlabel(var2)
        plt.ylabel("Amount")
        plt.legend(title=var1)
        plt.show()


    # Mutual Information Correlation Chart
    def mutual_info_corr(self, target_column, additional_drop = []):

        drop = additional_drop + [target_column]
        X = self.df.drop(columns=drop)

        Y = self.df[target_column]

        mi_scores = mutual_info_classif(X, Y, discrete_features = True)

        mi_df = pd.DataFrame({'Variables': X.columns, 'Mutual Information Scores': mi_scores})
        mi_df = mi_df.sort_values(by='Mutual Information Scores', ascending=False).head(20)

        plt.figure(figsize=(10, 8))
        sns.barplot(data=mi_df, x='Mutual Information Scores', y='Variables')
        plt.title(f"Features Impacting {target_column} using Mutual Information")
        plt.xlabel("Impact")
        plt.show()
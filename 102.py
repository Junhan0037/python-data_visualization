#Checking the null values in the data fields
marathon_2017.isnull().sum(axis=0)

#Show columns of the data frame
marathon_2017.columns

#Drop some columns with null values
marathon_2017_clean = marathon_2017.drop(['Unnamed: 0','Bib','Unnamed: 9'], axis='columns')

# Display the first five initial rows using the .head() method
print(marathon_2017_clean.head())

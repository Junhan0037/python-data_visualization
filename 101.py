# Import pandas as a alias 'pd'
import pandas as pd

# Load the CSV file "marathon_results_2017.csv" under "data" folder
marathon_2017 = pd.read_csv("./data/marathon_results_2017.csv")

# Display the first five initial rows using the .head() method
print(marathon_2017.head())

# Display data frame structure using the .info() method
print(marathon_2017.info())

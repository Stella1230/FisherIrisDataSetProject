# Load the Pandas Libraries with the alias of pd
import pandas as pd
# Load the NumPy Libraries with the alias of np
import numpy as np

# Data visualization 
import seaborn as sb

#When using the below code to view the data will work but wont have headings See the with open section for the update. 
#Update on this is that I had to add a line naming the columns. See line 11 
'''
# Load the CSV file
f = pd.read_csv("iris_data_set.csv")
f.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']  Refereance : (DataFrame, Protopopov and Joshi, 2019)

# Print the contents of the CSV file
print(f)
'''

# Open the CSV file and call is ds. We also will add headings to each column and print the results. 
with open ("iris_data_set.csv") as ds: #
    cols = ["Sepal Length", "Sepal Width" , "Petal Length", "Petal Width", "Species"]
    data = pd.read_csv(ds, names=cols)
print(data)
print("\n")

# Print the number of rows in the dataset.
print(data["Species"].count)
print("\n")

# Display the amount of rows and columns in the set
print(data.shape)
print("\n")

print(type(data))
print("\n")

# Print the first 10 rows
print(data.head(10))
print("\n")

'''
# Just like the finding rows from the beginning, we can also find rows from the end
print(data.tail(10))
'''

# Print the unique values of the data set and display the amount
data['Species'].unique()
print(data.groupby('Species').size())
print("\n")


# summary of each attribute
print(data.describe())
print("\n")

# Below commented out code does the same as the above describe command but is not visually a good option for all of them together.
'''
print(data.min())
print(data.max())
print(data.median())
print(data.mean())
print(data.std())
'''

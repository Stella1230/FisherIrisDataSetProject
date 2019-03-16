# Load the Pandas Libraries with the alias of pd
import pandas as pd
# Load the NumPy Libraries with the alias of np
import numpy as np

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



# Print the number of rows in the dataset.
print(data["Species"].count)

# Display the amount of rows and columns in the set
print(data.shape)

print(type(data))

#print(data.groupby("class").size())



# Print the first 10 rows
print(data.head(10))


'''
# Just like the finding rows from the beginning, we can also find rows from the end
print(data.tail(10))
'''




#print(data.describe())
# Load the Pandas Libraries with the alias of pd
import pandas as pd
# Load the NumPy Libraries with the alias of np
import numpy as np

# statistical data visualization 
import seaborn as sns
import matplotlib.pyplot as plt


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

# Print the unique values of the data set and display the number of rows that belong to each
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

# Output n number of random rows from the set
print(data.sample(5))
print("\n")

# Find if the set has any null values. 
print(data.isnull())
print("\n")

# Find if the set has any null values that are grouped.
print(data.isnull().sum())
print("\n")




# Histagram for Sepal Length
 #plt.grid(True)               # Used sns.set instead to display the grid and set a background color
sns.set_style("darkgrid")      # Use seaborn on background
plt.figure(figsize = (10, 7))  # Adjust the size of the graph
x = data["Sepal Length"]       # Find the Sepal Length and store in x
# Bin based on Sepal Length
# Bins are set to 10 by default. I have included is for view purposes
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram - Sepal Length(cm)")# Title of graph
plt.xlabel("Sepal_Length_cm")       # Xlabel 
plt.ylabel("Count")                 # Ylabel
plt.grid(True)
plt.show()                          # Show graph


# Histagram for Sepal Width
 #plt.grid(True)                # Used sns.set instead to display the grid and set a background color
sns.set()                       # Use default seaborn on background
plt.figure(figsize = (10, 7))   # Adjust the size of the graph
x = data["Sepal Width"]         # Find the Sepal Length and store in x
# Bin based on Sepal Length
# Bins are set to 10 by default. I have included is for view purposes
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram- Sepal Width (cm)")# Title of graph
plt.xlabel("Sepal_width_cm")            # Xlabel 
plt.ylabel("Count")                     # Ylabel
plt.show()                              # Show graph



# Histagram for Petal Length
 #plt.grid(True)                # Used sns.set instead to display the grid and set a background color
sns.set()                       # Use default seaborn on background
plt.figure(figsize = (10, 7))   # Adjust the size of the graph
x = data["Petal Length"]        # Find the Sepal Length and store in x
# Bin based on Sepal Length
# Bins are set to 10 by default. I have included is for view purposes
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram - Petal Length(cm)")# Title of graph
plt.xlabel("Petal_Length_cm")            # Xlabel 
plt.ylabel("Count")                     # Ylabel
plt.show()                              # Show graph



# Histagram for Petal Width
 #plt.grid(True)                # Used sns.set instead to display the grid and set a background color
sns.set()                       # Use default seaborn on background
plt.figure(figsize = (10, 7))   # Adjust the size of the graph
x = data["Petal Width"]         # Find the Sepal Length and store in x
# Bin based on Sepal Length
# Bins are set to 10 by default. I have included is for view purposes
sns.distplot(x, bins = 20, color = "blue")  # Plot the graph with x, give a color blue  and set the bins using seaborn
plt.title("Histagram - Petal Width(cm)")# Title of graph
plt.xlabel("Petal_Width_cm")            # Xlabel 
plt.ylabel("Count")                     # Ylabel
plt.show()                              # Show graph


#The four histograms together.
data.hist(bins = 20, figsize = (10, 7))  # Display graphs and resize window
plt.grid(True)        # Display a grid
plt.show()            # Show graph


# Box plot. 
plt.figure(figsize = (10, 7)) # Adjust the size of the graph
sns.set_style("ticks")        # Use seaborn on background
plt.title("Box Plot")         # Title of graph
sns.boxplot(data=data)        # Use seaborn to generate a box plot
plt.show()                    # Show graph

# Box Plot Grouped By Species
data.boxplot(by='Species',figsize=(10,7)) # GroupBy Species and set window size
plt.show()   # Show graph


        
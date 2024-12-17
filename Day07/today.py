# import numpy as np
# a = np.array([1, 2, 3, 4])  
# print(a)
# print(type(a))


# //////////////////////////////////////////////////////////////////////////////////////////////

# import pandas as pd
# data = {'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35],'City': ['New York', 'Los Angeles', 'Chicago']}

# df = pd.DataFrame(data)

# print(df)
# print(type(df))

# //////////////////////////////////////////////////////////////////////////////////////////////

# import pandas as pd

# df = pd.DataFrame({'A': [1, 2], 'B': [2, 3], 'C': [4, 5]})
# print(df.size)


# //////////////////////////////////////////////////////////////////////////////////////////////

# import pandas as pd

# df = pd.DataFrame({'A': [1, 2], 'B': [2, 3], 'C': [4, 5]})
# print(df.values)


# containing sales data your task is to analize the set of Deta using python and pandas to answer some questions calculate the reach of order add the new columns total revanive to store the  toatal revanue for eeach order identify the best selling product find the product with the highest total sales revanue 


# your the data analic the compant abou table contsing service data your task is the analice the data using pythion and pands to answer sume busness quwstion 
# calculate the protle the 
#  add the new colums total revenew to store the total revelo the foe each order 
# identyfy th r bsset element 
# find proudut with the hirset total salfe


# //////////////////////////////////////////////////////////////////////////////////////////////


import pandas as pd

data = {"Order ID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Smartphone", "Desk chair", "Monitor", "Bookshelf"],
      "Category": ["Electronics", "Electronics", "Furniture", "Electronics", "Furniture"],
      "Quantity": [2, 5, 10, 4, 2],
     "Price per Unit": [1000, 800, 150, 200, 300],
    "Region": ["North", "South", "East", "West", "North"]
}

df = pd.DataFrame(data)

df["Total Revenue"] = df["Quantity"] * df["Price per Unit"]

best_product = df.loc[df["Quantity"].idxmax(), "Product"]

high_revenue = df.loc[df["Total Revenue"].idxmax(), "Product"]

print("Sales Data:")
print(df)
print("\nHighest Quantity:", best_product)
print("Highest Total Revenue:", high_revenue)

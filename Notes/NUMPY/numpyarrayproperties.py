import numpy as np

sales = [[0, 5, 155, 0, 518], [0, 1827, 616, 317, 325]]
sales_array = np.array(sales)


print(sales)
print(sales_array)


print(f"ndim :{sales_array.ndim}")
print(f"ndim :{sales_array.shape}")
print(f"ndim :{sales_array.size}")
print(f"ndim :{sales_array.dtype}")

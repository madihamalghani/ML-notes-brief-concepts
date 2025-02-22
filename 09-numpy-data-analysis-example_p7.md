Learning NumPy through a practical project will help reinforce key concepts like arrays, indexing, broadcasting, and operations. Let's build a **"Data Analysis and Visualization Project"** using NumPy step by step.

## Analyzing and Visualizing Sales Data with NumPy

### **Step 1: Install Dependencies**

If you haven't already, install NumPy and Matplotlib:

```bash

pip install numpy matplotlib

```

---

### **Step 2: Generate Fake Sales Data**

Let's assume we have sales data for **5 products** over **12 months** (Jan-Dec).

```python
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate sales data: 5 products, 12 months
sales_data = np.random.randint(50, 500, size=(5, 12))
 #This creates a 5×12 matrix of random integers between 50 and 500.

# Product names
products = np.array(["Product A", "Product B", "Product C", "Product D", "Product E"])

print("Sales Data (Rows: Products, Columns: Months)")
print(sales_data)

```

---

### **Step 3: Basic Array Operations**

Find **total, average, min, and max sales** per product.

```python
# Total sales per product
total_sales = np.sum(sales_data, axis=1)

# Average sales per product
avg_sales = np.mean(sales_data, axis=1)

# Min and max sales per product
min_sales = np.min(sales_data, axis=1)
max_sales = np.max(sales_data, axis=1)

print("\nTotal Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Min Sales:", min_sales)
print("Max Sales:", max_sales)

```

---

**Explanation:**

In NumPy, `axis=1` refers to operations performed **along the rows** (i.e., across columns).

- **`axis=0`** → Operates **downward**, across rows (column-wise calculation).
- **`axis=1`** → Operates **horizontally**, across columns (row-wise calculation).

### **Step 4: Sales Trend Over Time**

Find total sales per month and compute the best & worst months.

```python
# Total sales per month
monthly_sales = np.sum(sales_data, axis=0)

# Best & worst months
best_month = np.argmax(monthly_sales)  # Index of max sales
worst_month = np.argmin(monthly_sales)  # Index of min sales

print("\nTotal Monthly Sales:", monthly_sales)
print(f"Best Month: {best_month+1}, Worst Month: {worst_month+1}") #index start with 0

# I Love adding my name to my code. Sorry for inconvenience. So, @madihamalghani. Just kidding. 
```

---

### **Step 5: Filtering Data**

Find products that sold more than **400 units** in any month.

```python
high_sales = sales_data > 400
print("\nMonths with sales > 400 units per product:\n", high_sales)

```

---

### **Step 6: Broadcasting & Reshaping**

Let’s assume we want to apply a **10% discount** to all sales.

```python
discounted_sales = sales_data * 0.9  # Broadcasting
print("\nDiscounted Sales Data:\n", discounted_sales)

```

---

### **Step 7: Visualizing Sales Data**

Now, let's visualize the **monthly sales trend** using Matplotlib.

```python
import matplotlib.pyplot as plt

months = np.arange(1, 13)

plt.figure(figsize=(10, 5))

for i in range(5):
    plt.plot(months, sales_data[i], marker='o', label=products[i])

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.legend()
plt.grid()
plt.show()

```

---

**Explanation:**

1. **Import Matplotlib for plotting**
    - Imports `matplotlib.pyplot` as `plt` to create visualizations.
2. **Define months**
    - Creates an array `[1, 2, ..., 12]` representing the 12 months.
3. **Create a figure with a specific size**
    - Sets up a plot canvas with a size of 10x5 inches.
4. **Loop through each product to plot sales data**
    - Iterates over 5 products and plots their sales trend.
    
    For `i = 0`, the function plots:
    
    ```python
    
    plt.plot(months, [100, 200, 150, ..., 250], marker='o', label="Product A")
    
    ```
    
    This creates a line graph for **Product A** with markers at each month.
    
5. **Plot sales data for each product**
    - Uses `plt.plot()` to draw a line graph for each product with markers (`'o'`) and labels.
6. **Label the x-axis as "Month"**
    - Sets the x-axis label to "Month".
7. **Label the y-axis as "Sales"**
    - Sets the y-axis label to "Sales".
8. **Set the plot title**
    - Titles the graph as "Monthly Sales Trend".
9. **Add a legend to distinguish products**
    - Displays product names corresponding to each line.
10. **Enable grid lines for readability**
- Adds grid lines to the plot for better visualization.
1. **Show the final plot**
- Displays the graph using `plt.show()`.

**What You’ve Learned:**

✅ Creating NumPy arrays

✅ Indexing, slicing, and filtering

✅ Summation, mean, min, max, and broadcasting

✅ Reshaping and condition-based filtering

✅ Visualizing data with Matplotlib

## **Whole Code:**

```python
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate sales data: 5 products, 12 months
sales_data = np.random.randint(50, 500, size=(5, 12))

# Product names
products = np.array(["Product A", "Product B", "Product C", "Product D", "Product E"])

print("Sales Data (Rows: Products, Columns: Months)")
print(sales_data)
# Total sales per product
total_sales = np.sum(sales_data, axis=1)

# Average sales per product
avg_sales = np.mean(sales_data, axis=1)

# Min and max sales per product
min_sales = np.min(sales_data, axis=1)
max_sales = np.max(sales_data, axis=1)

print("\nTotal Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Min Sales:", min_sales)
print("Max Sales:", max_sales)
# Total sales per month
monthly_sales = np.sum(sales_data, axis=0)

# Best & worst months
best_month = np.argmax(monthly_sales)  # Index of max sales
worst_month = np.argmin(monthly_sales)  # Index of min sales

print("\nTotal Monthly Sales:", monthly_sales)
print(f"Best Month: {best_month+1}, Worst Month: {worst_month+1}")
high_sales = sales_data > 400
print("\nMonths with sales > 400 units per product:\n", high_sales)
discounted_sales = sales_data * 0.9  # Broadcasting
print("\nDiscounted Sales Data:\n", discounted_sales)

import matplotlib.pyplot as plt

months = np.arange(1, 13)

plt.figure(figsize=(10, 5))

for i in range(5):
    plt.plot(months, sales_data[i], marker='o', label=products[i])

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.legend()
plt.grid()
plt.show()

```
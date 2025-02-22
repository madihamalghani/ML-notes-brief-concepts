What can we do with pandas:

- Merge Data
- Join Data
- Reshape Data
- Data loading from different databases and data storage(Data Tsanfering)
- Data exploration
- Data Cleansing

### **🔍 Pandas vs. NumPy: Key Differences**

| Feature | **Pandas** 🐼 | **NumPy** 🔢 |
| --- | --- | --- |
| **Data Structure** | Works with **DataFrames (tables) and Series (columns)** | Works with **multi-dimensional arrays (ndarrays)** |
| **Data Type Handling** | Supports **heterogeneous data types** (string, int, float, datetime) in a single DataFrame | Supports only **homogeneous numerical data** |
| **Performance** | Slightly slower due to additional functionalities and flexibility | Faster for numerical computations (optimized C-based operations) |
| **Ease of Use** | More intuitive for **structured data (like Excel tables or databases)** | Best for **numerical computations** and matrix operations |
| **Indexing** | Supports **labeled indexing** (rows & columns with names) | Uses **positional indexing** (like a list: `[0,1,2]`) |
| **Operations** | Powerful data manipulation tools: **groupby, filtering, merging, pivot tables** | Optimized mathematical operations: **linear algebra, broadcasting, element-wise operations** |
| **Use Case** | Best for **data analysis, statistics, machine learning preprocessing** | Best for **scientific computing, numerical simulations, deep learning** |

---

### **📌 When to Use What?**

- Use **NumPy** for **fast numerical operations** (e.g., large datasets, machine learning).
- Use **Pandas** for **data manipulation & analysis** (e.g., spreadsheets, CSV, databases).
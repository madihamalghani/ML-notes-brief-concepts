## How is a model being Trained using Linear Regression?

We are providing feature and actual values to the model. It compares the actual value with the predicted value. And update it’s parameters to reduce loss. 

In **linear regression**, we:

1. **Plot the dataset values** (features vs. target) to visualize the relationship.
2. **Fit a straight line** (regression line) that best represents the data.
3. **Minimize the error** (difference between actual and predicted values) by adjusting parameters m (slope) and b (intercept).

**Note: Gradient Descent** is used in **linear regression** to **update the parameters (weights and bias)** in a way that **minimizes the loss function** (error).

---

***Terms Explanation in simple way:***

- **Feature Values:**
    
    These are the inputs to your model (e.g., the values in your dataset).
    
- **Parameter Values:**
    
    These are the values (e.g., weights in linear regression) that the model adjusts in order to make accurate predictions. They essentially determine how much influence each feature has on the final prediction.
    
    In y=mX + b
    
    **here: ***b is bias and m is weight*
    

### **In the Case of Linear Regression:**

The **parameters** of the model are:

1️⃣ **Weight(s) ( m or w )** → Also called **coefficients**

- Determines how much the feature affects the output.
- If multiple features exist, each feature has its own weight.
- Example: In y=mX+b, m is the weight.

2️⃣ **Bias ( b or w0 )** → Also called **intercept**

- A constant value that shifts the output.
- Ensures that the model can make correct predictions even when feature values are zero.

---

### **Example 1: Simple Linear Regression (One Feature)**

Equation:  y= mX + b

**Parameters:**

- **m**→ Weight (slope)
- **b**→ Bias (intercept)

---
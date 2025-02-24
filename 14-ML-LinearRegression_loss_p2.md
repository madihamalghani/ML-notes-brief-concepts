**Loss** is a numerical metric that describes how wrong a model's **predictions** are. Loss measures the distance between the model's predictions and the actual labels. The goal of training a model is to minimize the loss, reducing it to its lowest possible value.

### **Example of Loss in Linear Regression**

Let’s continue with the **house price prediction** example to understand **loss** better.

### **Step 1: Model Makes Predictions**

Suppose we have a simple linear regression model that predicts house prices based on size. The model's equation is:

Predicted Price=500×Size+50,000\text{Predicted Price} = 500 \times \text{Size} + 50,000

Predicted Price=500×Size+50,000

Now, let’s say we have real data:

| **House Size (sq ft)** | **Actual Price ($)** | **Predicted Price ($)** |
| --- | --- | --- |
| 1,500 | 800,000 | 800,000 |
| 2,000 | 950,000 | 1,050,000 |
| 2,500 | 1,100,000 | 1,250,000 |

### **Step 2: Calculate the Loss**

Loss is the difference between the **actual price** and the **predicted price**. One common way to measure loss is **Mean Squared Error (MSE)**:

**MSE=n/1∑(Actual Price−Predicted Price)^2**

Now, let’s calculate it:

1. **First house:** (800,000−800,000)2=0
    
    (800,000−800,000)2=0(800,000 - 800,000)^2 = 0
    
2. **Second house:** (950,000−1,050,000)2=(−100,000)2=10,000,000,000
    
    (950,000−1,050,000)2=(−100,000)2=10,000,000,000(950,000 - 1,050,000)^2 = (-100,000)^2 = 10,000,000,000
    
3. **Third house:** (1,100,000−1,250,000)2=(−150,000)2=22,500,000,000
    
    (1,100,000−1,250,000)2=(−150,000)2=22,500,000,000(1,100,000 - 1,250,000)^2 = (-150,000)^2 = 22,500,000,000
    

MSE=(0+10,000,000,000+22,500,000,000)/3=332,500,000,000/3=10,833,333,333

### **Step 3: Reduce the Loss**

The model should adjust its equation (by changing the coefficients) to **reduce the loss**. A lower loss means the model's predictions are closer to actual prices.

👉 **The goal of training is to adjust the model so that the loss gets as small as possible!**

## Distance of loss

In statistics and machine learning, loss measures the difference between the predicted and actual values. Loss focuses on the *distance* between the values, not the direction. For example, if a model predicts 2, but the actual value is 5, we don't care that the loss is negative −3 (2−5=−3). Instead, we care that the *distance* between the values is 3. Thus, all methods for calculating loss remove the sign.

The two most common methods to remove the sign are the following:

- Take the absolute value of the difference between the actual value and the prediction.
- Square the difference between the actual value and the prediction.

## Types of loss

In linear regression, there are four main types of loss:

### **1. L1 Loss:**

The sum of the absolute values of the difference between the predicted values and the actual values.

$$
∑|actual value - predicted value |
$$

---

### **2. Mean absolute error (MAE):**

The average of L1 losses across a set of examples.

$$
1/N∑|actual value - predicted value |
$$

---

### 3. L2 Loss:

The sum of the squared difference between the predicted values and the actual values.

$$
∑(actual value - predicted value )^2
$$

---

### **4. Mean squared error (MSE):**

The average of L2 losses across a set of examples.

$$
1/N∑(actual value - predicted value )^2
$$

---

The functional difference between L1 loss and L2 loss (or between MAE and MSE) is squaring. When the difference between the prediction and label is large, squaring makes the loss even larger. When the difference is small (less than 1), squaring makes the loss even smaller.

When processing multiple examples at once, we recommend averaging the losses across all the examples, whether using MAE or MSE.

### **Example to Calculate L2 Loss :**

### **Given Data:**

| **Actual Value (Y_actual)** | **Predicted Value (Y_predicted)** |
| --- | --- |
| 10 | 8 |
| 15 | 14 |
| 20 | 18 |

### **Step 1: Compute Squared Errors**

((10 - 8)^2 = 4

(15 - 14)^2 = 1

(20 - 18)^2 = 4

### **Step 2: Compute Total L2 Loss**

L2 Loss=4+1+4=9

### **What Are Outliers?**

An **outlier** is a data point that is **significantly different** from the other observations in a dataset. It is either **much higher or much lower** than the typical range of values.

- **MSE**. The model is closer to the outliers but further away from most of the other data points.
- **MAE**. The model is further away from the outliers but closer to most of the other data points.

### **Choosing Between MAE and MSE – Simple Example**

### **Scenario:**

Imagine you are predicting **student exam scores** based on study hours.

| **Student** | **Actual Score** | **Predicted Score** | **Error (Actual - Predicted)** |
| --- | --- | --- | --- |
| A | 85 | 80 | 5 |
| B | 90 | 88 | 2 |
| C (Outlier) | 100 | 80 | 20 |

### **1. Using MAE (L1 Loss)**

- **Absolute Errors:**
    - Student A: **|85 - 80| = 5**
    - Student B: **|90 - 88| = 2**
    - Student C: **|100 - 80| = 20**
- **MAE = (5 + 2 + 20) / 3 = 9**

✅ **MAE treats all errors equally, so the outlier (Student C) doesn’t affect the model too much.**

### **2. Using MSE (L2 Loss)**

- **Squared Errors:**
    - Student A: **(85 - 80)² = 25**
    - Student B: **(90 - 88)² = 4**
    - Student C: **(100 - 80)² = 400**
- **MSE = (25 + 4 + 400) / 3 = 143**

❌ **MSE gives a much higher penalty for the outlier, making the model shift more toward it.**

### **Key Takeaway:**

- **Use MAE** if you want a stable model that ignores outliers.
- **Use MSE** if you want the model to be more sensitive to large errors.
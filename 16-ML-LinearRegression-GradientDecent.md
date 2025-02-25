### **Definition**

A mathematical technique to minimize **loss**. Gradient descent iteratively adjusts **weights** and **biases**, gradually finding the best combination to minimize loss.

Gradient descent is older—much, much older—than machine learning

### Steps:

The model begins training with randomized weights and biases near zero, and then repeats the following steps:

1. Calculate the loss with the current weight and bias.
2. Determine the direction to move the weights and bias that reduce loss.
3. Move the weight and bias values a small amount in the direction that reduces loss.
4. Return to step one and repeat the process until the model can't reduce the loss any further.

**Let’s Understand it using easiest way:**

Imagine you are trying to find the lowest point in a valley while blindfolded. You can only "feel" the slope of the ground under your feet. If the slope is steep, you take bigger steps downhill; if it's shallow, you take smaller steps. Eventually, you'll reach the lowest point.

This is exactly what **Gradient Descent** does—finding the lowest point (the minimum of a function) by taking small steps in the direction where the function decreases the fastest.

---

### **1. What Are We Trying to Do?**

We are training a simple model, as **linear regression**, which tries to fit a straight line to data.

y=wx+b

Here:

- y = predicted value
- x = input feature (like a person's height)
- w = weight (how much height affects weight)
- b = bias (a constant shift)

Our goal is to find the **best** values for w and b so that the line best fits the data.

---

### **2. What is the "Best" Fit?**

The best fit is when the error (difference between predicted and actual values) is as small as possible.

We measure this using a **Loss Function**, often the **Mean Squared Error (MSE)**:

$$
J(w,b)= \frac{1}{m} \sum_{i=1}^{m} (y_i - (w x_i + b))^2
$$

where:

- J(w, b) = total error (loss)
- m = number of data points
- yi = actual value
- wxi+b = predicted value

We want to minimize J(w,b)

---

### **3. What is Gradient?**

A **gradient** is just a fancy word for "slope." It tells us the direction in which we should move to decrease J(w,b)

The two things we can adjust are:

- w (weight)
- b (bias)

To find how much they should change, we compute **partial derivatives**:

### **Weight Slope (Gradient for w):**

$$
∂J∂w= -\frac{2}{m} \sum x_i (y_i - (w x_i + b))
$$

This tells us how much the error changes when we change w.

### **Bias Slope (Gradient for b):**

$$
∂J∂b= -\frac{2}{m} \sum (y_i - (w x_i + b))
$$

This tells us how much the error changes when we change b.

---

### **4. Gradient Descent: Moving Downhill**

Once we have the slopes, we update w and b using a small step called the **learning rate** (α):

$$
w:=w - \alpha \frac{\partial J}{\partial w}
$$

$$
b:= b - \alpha \frac{\partial J}{\partial b}
$$

This means:

- If the slope is **positive**, we move **left (decrease w)**
- If the slope is **negative**, we move **right (increase w)**
- The **larger** the slope, the **bigger** the step
- The **smaller** the slope, the **smaller** the step

---

### **5. Keep Repeating Until the Error is Small**

We repeat this process until the slope becomes close to zero, meaning we've reached the lowest point.

---

### **Example**

Imagine you have just one data point:

- x=2 , y=5
- Start with w=0, b = 0
- Suppose we compute:
    
    $$
    \frac{\partial J}{\partial w} = -8
    $$
    
    $$
    \frac{\partial J}{\partial b} = -4
    $$
    
- If the learning rate is α=0.1:
    
    $$
    w := 0 - (0.1 \times -8) = 0.8
    $$
    
    $$
    b:= 0 - (0.1 \times -4) = 0.4
    $$
    
- The new line is: y= 0.8x + 0.4

We repeat this until we reach the best w and b.

---

### **Key Intuition**

1. **Slope (gradient) tells us where to move.**
2. **We take small steps to get to the minimum error.**
3. **The process stops when the slope is almost zero.**

---

## Model convergence and loss curves

When training a machine learning model, we track its progress using a **loss curve**, which helps us determine if the model has **converged** (i.e., reached an optimal or near-optimal solution).

### **1. What is Model Convergence?**

A model is said to have **converged** when the loss function stops decreasing significantly with further training. This means the model has learned a good approximation of the data pattern and won't improve much by continuing training.

---

### **2. Understanding Loss Curves**

A **loss curve** is a graph that plots the **loss function value** over **epochs (iterations of training)**.

- **X-axis** → Epochs (number of times the model sees the full dataset)
- **Y-axis** → Loss value (error of the model)

A loss curve helps diagnose if the model is learning correctly or if there are issues like **overfitting** or **underfitting**.

### **Common Loss Curves & What They Mean**

| Loss Curve | Meaning |
| --- | --- |
| 📉 **Decreasing & Stabilized** | Model converged well ✅ |
| 📈 **Increasing Loss** | Model is diverging ❌ |
| 🎢 **Training ↓ but Validation ↑** | Overfitting ❌ |
| 📊 **Flat Line (No Change)** | Learning rate too low, or underfitting ❌ |
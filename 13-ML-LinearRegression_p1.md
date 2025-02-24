As we have learned Regression deals with numeric data.

### Definition

**Linear regression** is a statistical technique used to find the relationship between variables. In an ML context, linear regression finds the relationship between **features** and a **label**.

## **Real-Life Example:**

Let’s take a real-life example to make linear regression easy to understand:

Here: Price is the label.

### **House Price Prediction**

Imagine you are a real estate agent, and you want to predict the price of a house based on certain features like:

- **Size of the house (square feet)**
- **Number of bedrooms**
- **Age of the house**
- **Location**

**(Above 4 features)**

You collect data from past house sales and observe that **as the size of a house increases, the price also tends to increase**. Similarly, houses with more bedrooms or in better locations tend to be more expensive.

Using **linear regression**, you can create a formula that helps you predict the price of a house based on these factors. The formula might look like this:

Price=(Size×500)+(Bedrooms×10,000)+(Age×(−2000))+Constant\text{Price} = (\text{Size} \times 500) + (\text{Bedrooms} \times 10,000) + (\text{Age} \times (-2000)) + \text{Constant}

Price=(Size×500)+(Bedrooms×10,000)+(Age×(−2000))+Constant

**This means:**

- Each additional square foot increases the price by **$500**
- Each extra bedroom adds **$10,000**
- Older houses reduce the price by **$2,000** per year

Now, if you input the details of a new house, the linear regression model can **predict its price** based on past data.

**Another Example:**

**For example,**

 Suppose we want to predict a car's fuel efficiency in miles per gallon based on how heavy the car is.

we have the following dataset:

| **Pounds in 1000s (feature)** | **Miles per gallon (label)** |
| --- | --- |
| 3.5 | 18 |
| 3.69 | 15 |
| 3.44 | 18 |
| 3.43 | 16 |
| 4.34 | 15 |
| 4.42 | 14 |
| 2.37 | 24 |

## Linear regression equation

In algebraic terms, the model would be defined as **y=mx+b,** where

- is miles per gallon—the value we want to predict.
    
    y
    
- is the slope of the line.
    
    m
    
- is pounds—our input value.
    
    x
    
- is the y-intercept.
    
    b
    

![image.png](attachment:366e7a40-da0a-443e-b959-46ded4be4d30:image.png)

So basically, wo graph bna kr predicted value dae ga (on the basis of trained input feature values)
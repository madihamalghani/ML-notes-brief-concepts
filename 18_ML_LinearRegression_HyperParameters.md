## Hyper Parameters

**Hyperparameters** are variables that control different aspects of training. Three common hyperparameters are:

- **Learning rate**
- **Batch size**
- **Epochs**

In contrast, **parameters** are the variables, like the weights and bias, that are part of the model itself. In other words, hyperparameters are values that you control; parameters are values that the model calculates during training.

### Learning Rate:

**The learning rate** is a floating point number you set that influences how quickly the model converges. If the learning rate is too low, the model can take a long time to converge. However, if the learning rate is too high, the model never converges, but instead bounces around the weights and bias that minimize the loss. The goal is to pick a learning rate that's not too high nor too low so that the model converges quickly.

### **1. How the Learning Rate Affects Updates**

Each step in gradient descent updates the parameters using the equation:

$$
θnew=\theta_{\text{old}} - \alpha \cdot \nabla J(\theta)

$$

Where:

- θ represents the model parameters (weights and bias).
- α is the **learning rate**.
- ∇J(θ) is the gradient (slope) of the loss function.

### **2. How the Learning Rate Affects Step Size**

- **If the gradient is large** → The update is larger.
- **If the gradient is small** → The update is smaller.

For example:

- If the gradient is **2.5** and the learning rate is **0.01**, the parameter updates by:
2.5×0.01=0.025
    
    2.5×0.01=0.0252.5 \times 0.01 = 0.025
    
- A small gradient leads to **small adjustments**, preventing overshooting.

---

### **3. Choosing the Right Learning Rate**

| Learning Rate | Effect |
| --- | --- |
| **Too Large** (e.g., 1.0) | The model may overshoot and never converge ❌ |
| **Too Small** (e.g., 0.0001) | The model learns too slowly and takes too long to converge ⏳ |
| **Optimal** (e.g., 0.01) | The model learns efficiently and converges quickly ✅ |

---

### **4. Loss Curve and Convergence**

- The loss curve typically **drops quickly at first** as the model improves.
- Over time, the loss **gradually levels off**, showing convergence.
- A well-chosen learning rate **helps the model converge in fewer iterations**.

## Batch size:

**Batch size** is a hyperparameter that refers to the number of **examples** the model processes before updating its weights and bias. You might think that the model should calculate the loss for *every* example in the dataset before updating the weights and bias. However, when a dataset contains hundreds of thousands or even millions of examples, using the full batch isn't practical.

Two common techniques to get the right gradient on *average* without needing to look at every example in the dataset before updating the weights and bias are **stochastic gradient descent** and **mini-batch stochastic gradient descent.**

- **Stochastic gradient descent (SGD)**: Stochastic gradient descent uses only a single example (a batch size of one) per iteration. Given enough iterations, SGD works but is very noisy. "Noise" refers to variations during training that cause the loss to increase rather than decrease during an iteration. The term "stochastic" indicates that the one example comprising each batch is chosen at random.
- **Mini-batch stochastic gradient descent (mini-batch SGD):** Mini-batch stochastic gradient descent is a compromise between full-batch and SGD. For N number of data points, the batch size can be any number greater than 1 and less than N. The model chooses the examples included in each batch at random, averages their gradients, and then updates the weights and bias once per iteration.   Determining the number of examples for each batch depends on the dataset and the available compute resources. In general, small batch sizes behaves like SGD, and larger batch sizes behaves like full-batch gradient descent.

### **Note**:

<aside>
💡

When training a model, you might think that noise is an undesirable characteristic that should be eliminated. However, a certain amount of noise can be a good thing.  Noise can help a model **generalize** better and find the optimal weights and bias in a **neural network**.

</aside>

## Epochs:

During training, an **epoch** means that the model has processed every example in the training set *once*. For example, given a training set with 1,000 examples and a mini-batch size of 100 examples, it will take the model 10 **iterations** to complete one epoch.

Training typically requires many epochs. That is, the system needs to process every example in the training set multiple times.

The number of epochs is a hyperparameter you set before the model begins training. In many cases, you'll need to experiment with how many epochs it takes for the model to converge. In general, more epochs produces a better model, but also takes more time to train.

The following table describes how batch size and epochs relate to the number of times a model updates its parameters.

| **Batch type** | **When weights and bias updates occur** |
| --- | --- |
| Full batch | After the model looks at all the examples in the dataset. For instance, if a dataset contains 1,000 examples and the model trains for 20 epochs, the model updates the weights and bias 20 times, once per epoch. |
| Stochastic gradient descent | After the model looks at a single example from the dataset. For instance, if a dataset contains 1,000 examples and trains for 20 epochs, the model updates the weights and bias 20,000 times. |
| Mini-batch stochastic gradient descent | After the model looks at the examples in each batch. For instance, if a dataset contains 1,000 examples, and the batch size is 100, and the model trains for 20 epochs, the model updates the weights and bias 200 times. |

### **Hyperparameters Simplified:**

Hyperparameters control how a model learns. The main ones are:

1. **Learning Rate** – Decides how fast the model updates.
    - Too high → Model jumps around and doesn’t learn.
    - Too low → Learning is very slow.
    - Just right → Efficient learning and quick convergence.
2. **Batch Size** – Number of examples used before updating model weights.
    - **SGD (Batch = 1)** → Very noisy but updates fast.
    - **Mini-batch (Batch > 1 but < total data)** → Balances speed and stability.
    - **Full-batch (All data at once)** → Slow but precise.
3. **Epochs** – How many times the model sees the entire dataset.
    - More epochs → Better learning but longer training.
    - Too many → Risk of overfitting.
    - Right balance → Optimal performance.
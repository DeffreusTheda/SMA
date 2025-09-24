In neural network, {1:vanishing gradients} refers to {2:the **loss of gradient**} due to {2:**cumulative multiplication** of weights} during [[backpropagation through time]].
Example:
$$\begin{align}
0.99^{100} = 0.3660323413
\end{align}$$
<!--ID: 1741570833313-->


Vanishing gradient negatively effect [[Recurrent Neural Networks|RNNs]] ability to {1:update weight and biases} closer to {1:input layer},
thus {1:forgetting long-term dependencies},
or even {1:preventing learning altogether}.
<!--ID: 1741570833314-->


On BPPT, the **gradient** flows backward through each time step.
For {1:loss L} at {1:final time step T}, the **gradient with respect to the hidden state** involves a {1:**chain of derivates**}.
Each term involves multiplying {1:the **weight matrix**} and {1:the **derivative** of the **activation function**}.
The derivative of tan function ({2:$1 - \tanh^2(x)$}), has a maximum value of {2:1} and {2:approaches 0} as x increases, whereas the derivative of sigmoid function ({2:$\sigma(x)(1 - \sigma(x))$}) has a maximum value of {2:$0.25$}.
There derivative are {2:**always $\le 1$**}, where multiplying them {2:**reduce the magnitude**} for each time step.
<!--ID: 1741576238561-->


On BPPT, the {1:**eigenvalues**} of the {1:**weight matrix**} are commonly {2:**less than 1**} (when weights are initialized with small values), causing repeated multiplication by the weight matrix to {2:**exponentially shrink**} the {2:**gradient**}.
<!--ID: 1741576238563-->


## Solution to Vanishing Gradient
- {1:[[Rectified Linear Unit|ReLU]]} activation function
- Implementing {1:batch normalization} to stabilize the learning process
- {1:[[Long Short-Term Memory|LSTM]]} model
- {1:**Residual** (skip) **connection**}, e.g. in [[Natural Language Understanding Pipeline]]
<!--ID: 1741570833316-->

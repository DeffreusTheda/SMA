RNN implement a variant of back-propagation, called the [[Backpropagation|Back-propagation Through Time]].

Process:
- **Forward pass**: the input moves forward through the neural network to generate output.
- **[[Loss Function|Loss calculation]]**: compare expected and predicted value to calculate extent of errors.
- **Backward pass**: goes from output layer to input layer.
- **Weight update**: update weight and biases according the calculated loss, controlled by the learning rate.

### RNNs Pros
- {1:Sequence Handling}: designed to handle {2:sequential} data.
- {1:Memory}: capability to {2:retain} information from {2:previous} inputs due to their internal state.
- {1:Flexibility}: can be applied to various types of sequential data, including {1:text, audio, video, and time series data.}
<!--ID: 1738813841436-->

### RNNs Cons
- {1:Vanishing} and {1:Exploding} Gradients: difficulty to capture long-term dependencies.
- {1:Training Time}: {2:computationally intensive} and time-{2:consuming} for long sequences or large datasets.
- {1:Complexity in Parallelization}: sequential, leading to {2:slower training time}.
<!--ID: 1738821783731-->

### Compared to [[Transformer Neural Networks#compared to RNNs|TNNs]]
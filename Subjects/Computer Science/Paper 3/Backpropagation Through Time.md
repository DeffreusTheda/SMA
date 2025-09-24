{1:Backpropagation Through Time}
An {2:**extension**} of the standard backpropagation used on {2:[[Recurrent Neural Networks|RNNs]] and **neural networks** that process **sequential data**}.
<!--ID: 1741576238555-->


In BPPT:
1. {1:**Unfold** (copy)} the [[Recurrent Neural Networks|RNN]] **through** the {1:**time steps**}
2. Run a {1:**forward pass**} through the entire unfolded network
3. Calculate the {1:**error at the output**}
4. {1:**Propagate**} this error **backward** though all time steps to {1:**update** the **weights and biases**}
<!--ID: 1741576238559-->


BPPT has the [[vanishing gradient]] problem.
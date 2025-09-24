{1:Tensor Processing Unit}
abbr. {1:**TPU**}
Custom-developed hardware by {2:**Google**} specifically designed ({2:application-specific integrated circuits}) to {2:**accelerate [[machine learning]] workloads**},
providing superior performance for {2:**deep learning models**}.
<!--ID: 1741574730473-->


## Compared to [[Central Processing Unit|CPU]] and [[Graphical Processing Unit|GPU]]
+ Feature {1:**matrix multiplication units** (**MXU**)}
	+ Large matrix calculations form the {2:**foundation** of deep learning algorithms}
	+ Uses a **[[Systolic Array|systolic array]] architecture**, where data flows through a grid of processing elements in a wave-like pattern
	+ {2:**Faster and more efficient**}
- {1:**Extremely fast data transfer**} between memory units
	- Deep learning workloads often **memory-bound**
	- 8GB-32GB **High-bandwidth memory** (HBM)
	- **Near-linear scaling** of performance per TPU
- {1:**Superior interconnect**} architecture
	- Allow multiple TPUs to be networked together in **pods**
	- Supports **distributed training**
- {1:**Energy efficient**}
	- Achieved by specializing in the specific computations needed for neural networks rather than general-purpose processing.
	- This lead to lower operating costs and reduced environmental impact for large-scale AI operations.
<!--ID: 1741655885454-->


Studies have shown that TPUs can be 30-80 times more energy-efficient than contemporary CPUs and GPUs for certain deep learning workloads, making them particularly valuable for data centers and cloud computing environments.
and low precision
<!--ID: 1741574730474-->

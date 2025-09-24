Main feature: [[Parallels processing]].

{1:Transformer neural networks}
A neural network architecture that relies entirely on {2:**self-attention mechanisms**} and {2:**[[Feedforward Neural Network|FFNNs]]**}, eliminating recurrence and convolutions.
Introduced in the {3:seminal "Attention Is All You Need" paper} ({3:Vaswani et al., 2017}) for **Google Translate**.
<!--ID: 1741570833309-->


## Self-attention Mechanism

{1:Self-attention mechanism (SAM)} **simultaneously** adds {2:**weight**} to {2:each word **based on importance and relationship**}, disregarding the distance.
<!--ID: 1745077033762-->


## Multi-head Attention

{1:Multi-head attention} applies different {1:self-attentions}, resulting in different {2:perspectives on word relationship/combination}, which is then {2:combined}.
<!--ID: 1741570833311-->


TNNs architecture example:
1. Input embeddings: turn each word to meaningful vector.
2. Positional encodings: generate mathematical value through mathematical functions to indicate position of words.
3. [[Encoder Architecture|Encoder layers]]: using SAM, trained FFNNs, and output normalization, accurately represent text.
4. Decoder layers: using SAM, trained FFNNs, and output normalization, produce next token.
5. Output layer: generates next worn in output sentence.

## TNNs Compared to RNNs
+ {1:**Parallelization**}
	- [[Recurrent Neural Networks#RNNs Cons|RNN]] is impossible to {1:parallelize} effectively.
	- TNNs {2:self-attention mechanisms **process tokens independently** of each others}, enabling parallel processing of the entire sequence.
	- TNNs can leverage {2:**hardware optimizations** like [[Graphical Processing Unit|GPUs]] and [[Tensor Processing Unit|TPUs]]}.
	- {2:**Reduced training time**}, crucial for training large models on large datasets.
- {1:**Long-term Dependencies**}: improve capability to learn relationship with long distances e.g. [[T5]].
	- RNNs {2:struggle} with long-term dependencies.
	- TNNs {2:self-attention mechanisms **directly connect**} any two tokens in the sequence, regardless of {2:distance}.
	- TNNs can better **capture {2:context}**.
- {1:**Scalability**}: tackle {2:**large datasets**} and {2:**complex tasks**} more effectively.
	- TNNs architecture allows for {2:more straightforward} parallelization and optimization.
	- They can handle increased data and model sizes by {2:leveraging distributed computing resources} efficiently.
- Require {1:larger **datasets**} and {1:**computational resources**}
	- RNNs is useful for {2:**low-resource**} application or devices and {2:**real-time** processing}.
<!--ID: 1741570833312-->

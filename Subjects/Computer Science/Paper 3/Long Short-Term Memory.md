---
composes:
  - "[[LSTM Layers]]"
---
![[SMA/Subjects/Computer Science/Paper 3/LSTM.png]]

{1:Long Short-Term Memory}
abbr. {1:LSTM}
Introduced by {2:Hochreiter and Schmidhuber} in {2:1997}, it's a type of **{2:[[Recurrent Neural Networks|RNN]]}**, addressing **{2:[[Vanishing Gradient|vanishing gradient]]}** problem by using {2:**targeted updating**}, therefore more stable gradient and less prone to rapid changes.
<!--ID: 1741572407915-->

## LSTM Layers
LSTM also contains input and output layer, but **replace** {1:**hidden layer** found} in RNNs and [[Feedforward Neural Network|FFNNs]] with {1:**[[LSTM Layers|LSTM layers]]** made up of [[LSTM Cells|LSTM cells]]}.
Each cell contains {1:a series of "gates"}, which {1:are mathematical functions} to process information,
and their {1:**output update**} the {1:**hidden state**}, and **only** influence next layer cells by doing so.
![[LSTM Cell.png]]
<!--ID: 1741573055408-->


### LSTM Cell State
($s$) Like a conveyor belt, it flow {1:gate-modified} {1:**relevant**} information throughout the {1:**sequence**} and acts as {1:the network's **long-term memory**}.
It's updated after output gate and input gate:
$$s_{t} = f_{t} (s_{t-1}) + i_{t}(s_{t})$$
where $s$ is the cell state.
<!--ID: 1741572407926-->

### LSTM Forget Gate
Decides what information is {1:**discarded**} from the cell.
Usually uses {1:[[Sigmoid Function|sigmoid function]]} as the activation function, passing $x_{i}$ to it:
$$f_{t} = \sigma(W_{f} \times (h_{t-1}, x_{t}) + b_{f}), \text{ where } 1 \text{ means keep and } 0 \text{  forget}$$
$$\sigma(x_{i}) \times f_{t} = s, \text{ where } f_{t} \text{ is the forget gate and } s \text{ the cell state.}$$
<!--ID: 1741572407927-->


### LSTM Input Gate
Decides which values are {1:**updated/stored**} in the [[Long Short-Term Memory#LSTM Cell State|cell state]].
It has two layer:
- A {2:**sigmoid**} layer that decide {2:which values to **update**}
$$i_{t} = \sigma(W_{i} \times (h_{t-1}, x_{t}) + b_{i})$$
- A {1:**tanh**} function that creates {2:**addable candidate values**} for cell state.
$$s_{t} = \tanh(W_{s} \times (h_{t-1}, x_{t}) + b_{s})$$
<!--ID: 1741572407929-->


### Output Gate
Decides what information from the cell state is used to {1:**generate the output**}
$$o_{t} = \sigma(W_{o} \times (h_{t-1}, x_{t} + b_{o}))SS$$
$$h_{t} = o_{t} \times \tanh s_{t}$$
where output is passed as {1:the **updated** value for the **hidden state**}.
<!--ID: 1741572407932-->

## Advantages of LSTM
- Capture {1:**long-range dependencies**} for many time-steps
- Select information to be {1:**remembered**} or {1:**forgotten**}
- Naturally handle {1:**real-time**} and {1:**differing length inputs**}
<!--ID: 1741573055414-->

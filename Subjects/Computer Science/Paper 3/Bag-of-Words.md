A simple text representation technique in [[natural language processing|NLP]] that treats a document as an **unordered collection of words frequency**, ignoring word order and grammar.
It's primarily used to convert text into a vector suitable for [[Machine Learning|ML]] algorithms.

Limitations:
- **Ignores Context and Semantics**: The model doesn't capture the meaning or relationships between words in a sentence. 
- **High Dimensionality**: The resulting vectors can be very large, especially with large vocabularies, potentially leading to computational challenges. 
- Doesn't Capture Word Relationships: It **doesn't account for synonyms or phrases**, which can be crucial for certain tasks. 

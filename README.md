# VectorBridge: A Robust Technique for Efficient Cross-Model Embeddings Translation

#### See (Arxiv Link Here) for more information

VectorBridge is aimed at creating an interoperability layer between different sentence embeddings models, thereby promoting vendor neutrality and enabling users to swap models freely based on their specific needs and preferences, without the need for re-embedding a sample corpus. _VectorBridge thereby enables the querying vector databases/stores encoded in closed-source models, using only open-source tools._

## Overview

`/models` Contains pretrained .h5 models that can be loaded to translate embeddings.

`/benchmarking` Contains benchmarks relating to translational models using the MTEB evaluation metrics.

`/datasets` Is an incomplete repository of data we used to train the models. Any datasets not present in this folder (by nature of their size) will be mentioned in the _Methodology_ section.

## Methodology 

VectorBridge is a proof-of-concept demonstrating how a small sample of input:output pairs of embeddings models can be used to deduce an appropriate mapping between differing embeddings models, allowing for the "translation" of vector spaces.

VectorBridge is aimed at creating an interoperability layer between different sentence embeddings models, thereby promoting vendor neutrality and enabling users to swap models freely based on their specific needs and preferences.

```markdown
## Code Example 

```

## Discussion



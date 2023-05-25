# Translatooor

## Overview

1) loadparquet.py: loads parquet (see: https://huggingface.co/datasets/nomic-ai/cohere-wiki-sbert ), generates wikidownload.csv
2) OSEmbeddingsV2.ipynb: takes wikidownload.csv, adds the mpnet embeddings, saves as a new csv: CompositeEmbeddings.csv
3) NN.ipynb: Neural Net training, prediction, and eval.

Translatooor is a novel methodology designed to alleviate platform lock-in associated with hosted APIs, particularly those responsible for generating word embeddings. This model enables the transformation of one embeddings model's output into the representation space of another embeddings model. 

This unique approach to creating a mapping between different embeddings models fosters versatility and adaptability. Specifically, it provides a framework to map between open and closed-source models or between two closed-source models. Consequently, it prevents any single vendor from monopolizing embeddings output within an opaque, black-box model.

## Methodology 

Translatooor leverages a small sample of input:output pairs to deduce an appropriate mapping between differing embeddings models. These pairs provide the necessary cross-references to inform the conversion process. The end goal is to create interoperability between different word embeddings models, thereby promoting vendor neutrality and enabling users to swap models freely based on their specific needs and preferences.

```markdown
## Code Example 

```

## Benefits and Implications

This innovative approach paves the way for a more diverse and open ecosystem in the field of natural language processing. By offering an alternative to proprietary, black-box models, it reduces vendor lock-in and promotes user autonomy. Users can now effectively transition between different embedding models without losing the semantic and syntactic richness of their data. 

Furthermore, the ability to convert embeddings across various models fuels research collaboration and resource-sharing, further accelerating progress in the AI and machine learning domain.

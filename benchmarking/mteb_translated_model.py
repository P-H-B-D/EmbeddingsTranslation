import numpy as np

class TranslatedModel:

    def __init__(self, model_from, model_to, input_shape):
        self.model_from = model_from
        self.model_to = model_to
        self.input_shape = input_shape
    
    def encode(self, sentences, batch_size=32, **kwargs):
        embeddings = []
        for i in range(0, len(sentences), batch_size):
            batch = sentences[i:i+batch_size]
            curr_batch_size = len(batch)
            from_embedding = self.model_from.encode(batch)
            print(len(from_embedding))
            from_embedding_array = np.array(from_embedding).reshape(curr_batch_size, self.input_shape)
            to_embedding = self.model_to.predict(from_embedding_array)
            embeddings.extend(to_embedding)
        return embeddings

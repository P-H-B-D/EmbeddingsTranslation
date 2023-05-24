from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

print("Model Loaded")
embeddings = model.encode(sentences)
print("Embedding Created: ", embeddings)

print("Model Loaded")
embeddings = model.encode(sentences[0])
print("Embedding Created: ", embeddings)
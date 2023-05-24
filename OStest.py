from sentence_transformers import SentenceTransformer
sentences = ["YouTube is a global online video sharing and social media platform headquartered in San Bruno, California. It was launched on February 14, 2005, by Steve Chen, Chad Hurley, and Jawed Karim. It is owned by Google, and is the second most visited website, after Google Search. YouTube has more than 2.5 billion monthly users who collectively watch more than one billion hours of videos each day. , videos were being uploaded at a rate of more than 500 hours of content per minute."]

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

print("Model Loaded")
embeddings = model.encode(sentences)
print("Embedding Created: ", embeddings)


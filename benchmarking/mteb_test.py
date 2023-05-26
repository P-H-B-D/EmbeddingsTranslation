from mteb import MTEB
from sentence_transformers import SentenceTransformer
from mteb_translated_model import TranslatedModel
from keras.models import load_model

model_name = "translated_models/mpnet_to_sbert"

trained_model = load_model("bigsmall.h5", compile=False)
from_model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")
model = TranslatedModel(from_model, trained_model, 768)

evaluation = MTEB(tasks=["Banking77Classification"])
results = evaluation.run(model, output_folder=f"benchmarking/results/{model_name}")
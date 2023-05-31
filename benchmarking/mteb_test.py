from mteb import MTEB
from sentence_transformers import SentenceTransformer
from mteb_translated_model import TranslatedModel
from keras.models import load_model

model_names = {
    "sbert": "sentence-transformers/all-MiniLM-L6-v2",
    "mpnet": "sentence-transformers/all-mpnet-base-v2"
}

from_model_name = "mpnet"
from_model = SentenceTransformer(model_names[from_model_name])

to_model_name = "sbert"
# to_model = SentenceTransformer(model_names[to_model_name])

trained_model = load_model("../models/bigsmallnew.h5", compile=False)
translation_model = TranslatedModel(from_model, trained_model, 768)

model_name = f"{from_model_name}_to_{to_model_name}"

evaluation = MTEB()
evaluation.run(translation_model, output_folder=f"benchmarking/results/{model_name}")

# # evaluation = MTEB(tasks=["EmotionClassification"])
# # evaluation.run(to_model, output_folder=f"benchmarking/results/{to_model_name}")

# evaluation = MTEB(tasks=["SciFact"])
# evaluation.run(from_model, output_folder=f"benchmarking/results/{from_model_name}")
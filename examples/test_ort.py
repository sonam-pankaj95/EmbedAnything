import embed_anything
from embed_anything import EmbedData, EmbeddingModel, TextEmbedConfig, WhichModel, embed_query
from embed_anything.vectordb import Adapter
import os
from time import time
<<<<<<< HEAD
from fastembed import TextEmbedding
=======
>>>>>>> c65096182fc3ba0fd2f86b070944ee50bcce5989
import numpy as np



model = EmbeddingModel.from_pretrained_onnx(
    WhichModel.Bert, "BGESmallENV15Q"
)

sentences = [
    "The quick brown fox jumps over the lazy dog",
    "The cat is sleeping on the mat",
    "The dog is barking at the moon",
    "I love pizza",
    "I like to have pasta",
    "The dog is sitting in the park",
]

embedddings = embed_query(sentences, embeder=model)

embed_vector = np.array([e.embedding for e in embedddings])

print("shape of embed_vector", embed_vector.shape)
similarities = np.matmul(embed_vector, embed_vector.T)

print(similarities)

<<<<<<< HEAD
model = TextEmbedding(model_name = "BAAI/bge-small-en-v1.5",
                      providers=["CUDAExecutionProvider", "CPUExecutionProvider"])

embeddings = np.array(list(model.embed(sentences)))

print(embeddings.shape)

similarities = np.matmul(embeddings, embeddings.T)

print(similarities)

=======
>>>>>>> c65096182fc3ba0fd2f86b070944ee50bcce5989

from embed_anything import EmbeddingModel, WhichModel, embed_query, TextEmbedConfig
import time
import os
import pymupdf
from semantic_text_splitter import TextSplitter
import time
import os

model = EmbeddingModel.from_pretrained_onnx(
    WhichModel.Bert, "BGESmallENV15Q"
)
splitter = TextSplitter(1000)
config = TextEmbedConfig(batch_size=128)

def embed_anything():
# get all pdfs from test_files

  for file in os.listdir("bench"):
    text = []
    doc = pymupdf.open("bench/" + file)

    for page in doc:
        text.append(page.get_text())
    
    text = " ".join(text)
    chunks = splitter.chunks(text)
    embeddings = embed_query(chunks, model, config)

start = time.time()
embed_anything()

print(time.time() - start)
<<<<<<< HEAD


# from fastembed import TextEmbedding
# import pymupdf
# from semantic_text_splitter import TextSplitter
# import time
# import os
# import numpy as np
# splitter = TextSplitter(1000)
# files = []
# model = TextEmbedding(model_name = "BAAI/bge-small-en-v1.5",
#                       providers=["CUDAExecutionProvider", "CPUExecutionProvider"])

# def fastembed():
# # get all pdfs from test_files

#   for file in os.listdir("bench"):

#     text = []
#     doc = pymupdf.open("bench/" + file)

#     for page in doc:
#         text.append(page.get_text())

#     text = " ".join(text)
#     chunks = splitter.chunks(text)
#     embeddings = list(model.embed(chunks))

# start = time.time()
# fastembed()
# print(time.time() - start)
=======
>>>>>>> c65096182fc3ba0fd2f86b070944ee50bcce5989

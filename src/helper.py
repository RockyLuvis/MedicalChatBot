from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone

from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec, PodSpec
import time

from langchain_pinecone import PineconeVectorStore


def load_pdf(data):
  loader = DirectoryLoader(
              data,
              glob="*.pdf",
              loader_cls=PyPDFLoader
            )
  doc = loader.load()
  return doc

#Perform Chunking
def text_split(extracted_data):
   chunker = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
   chunks = chunker.split_documents(extracted_data)
   return chunks

def download_hf_embeddings():
  embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
  return embeddings
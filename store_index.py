# Use to store data in Pinecone

from src.helper import load_pdf, text_split, download_hf_embeddings
from langchain.vectorstores import Pinecone
import pinecone

from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec, PodSpec  
import time

from dotenv import load_dotenv
import os
load_dotenv()

HF_TOKEN_PATH = os.environ.get('HF_TOKEN_PATH')
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

  
use_serverless = True  

# configure client  
pc = Pinecone(api_key=PINECONE_API_KEY)  
if use_serverless:  
    spec = ServerlessSpec(cloud='aws', region='us-east-1')  
else:  
    # if not using a starter index, you should specify a pod_type too  
    spec = PodSpec()  
# check for and delete index if already exists  
index_name = 'langchain-rag-medicalbot'  
if index_name in pc.list_indexes().names():  
    pc.delete_index(index_name)  
# create a new index  
pc.create_index(  
    index_name,  
    dimension=1536,  # dimensionality of text-embedding-ada-002  
    metric='dotproduct',  
    spec=spec  
)  
# wait for index to be initialized  
while not pc.describe_index(index_name).status['ready']:  
    time.sleep(1)  

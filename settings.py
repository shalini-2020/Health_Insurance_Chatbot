import os

os.environ['REPLICATE_API_TOKEN'] = "Your REplicate Key here"
os.environ['PINECONE_API_KEY'] = "Your Pinecone API Key here"

REPLICATE_API_TOKEN = os.environ['REPLICATE_API_TOKEN']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']

index_name = "health"

data_path = 'data/'
db_vector_path = 'vector_data'
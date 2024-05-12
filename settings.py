import os

os.environ['REPLICATE_API_TOKEN'] = "r8_HEPtv2COBH9ulBrjYMKwhMW3Mc6uJ4Q0GnfBp"
os.environ['PINECONE_API_KEY'] = "41a546af-cd2f-4bfd-91d8-44e56b65aa51"

REPLICATE_API_TOKEN = os.environ['REPLICATE_API_TOKEN']
PINECONE_API_KEY = os.environ['PINECONE_API_KEY']

index_name = "health"

data_path = 'data/'
db_vector_path = 'vector_data'
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import settings

def loaddata():
    loader = DirectoryLoader(settings.data_path,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    files = loader.load()
    return files


def docsplit(extracted_data):
    
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=2000,
        chunk_overlap=200,
        length_function=len
    )
    text_chunks = text_splitter.split_documents(extracted_data)
    return text_chunks 

#download embedding model
def  hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    return embeddings

def create_vectordb():
    docs = loaddata()
    doc_chunk = docsplit(docs)
    doc_embeddings = hugging_face_embeddings()
    vectors = FAISS.from_documents(doc_chunk, doc_embeddings)
    vectors.save_local(settings.db_vector_path)


if __name__ == "__main__":
    create_vectordb()

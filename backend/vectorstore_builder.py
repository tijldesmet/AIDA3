from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def create_vectorstore(doc_texts):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = [Document(page_content=t, metadata={"source": f"doc_{i}"}) for i, t in enumerate(doc_texts)]
    texts = text_splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(texts, embeddings)

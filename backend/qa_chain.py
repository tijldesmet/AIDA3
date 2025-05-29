from dotenv import load_dotenv
load_dotenv()
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

def create_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever(search_type="similarity", k=5)
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)

def answer_question(chain, vraag):
    result = chain(vraag)
    antwoord = result['result']
    bronnen = [str(doc.metadata) for doc in result['source_documents']]
    return antwoord, bronnen

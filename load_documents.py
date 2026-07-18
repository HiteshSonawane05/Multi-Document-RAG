from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

def get_vectordb(file_name):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200,chunk_overlap=20)

    documents = []
    metadatas = []

    for name in file_name:

        file_obj = PdfReader(name)

        for page_num, p in enumerate(file_obj.pages):

            text = p.extract_text()

            chunks = text_splitter.split_text(text)

            for chunk in chunks:

                documents.append(chunk)

                metadatas.append({
                    "pdf_name": name,
                    "page": page_num + 1
                })

    client = chromadb.Client()

    vectordb = client.get_or_create_collection(name='multi_pdf_vdb')

    vectordb.add(
        ids=['id_' + str(i) for i in range(len(documents))],
        documents=documents,
        metadatas=metadatas
    )

    return vectordb
















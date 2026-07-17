import streamlit as st
from generator import generate_answer
from load_documents import get_vectordb
st.title('PDF Question Answering System')

# PDF Upload
uploaded_files = st.file_uploader(
    "Upload PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    file_names = []

    for uploaded_file in uploaded_files:

        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        file_names.append(uploaded_file.name)

    st.session_state.vectordb = get_vectordb(file_names)

    st.success(f"{len(uploaded_files)} PDFs Uploaded Successfully")

if 'history' not in st.session_state:
    st.session_state.history = []
# history = st.session_state['history']
# Display previous chat
print(st.session_state.history)
for msg in st.session_state.history:
    with st.chat_message(msg['role']):
        st.markdown(msg['message'])

question = st.chat_input("Ask")   # Waiting
if question:
    with st.chat_message("user"):
        st.markdown(question)
    st.session_state.history.append({'role':'user','message':question})

    with st.chat_message("assistant"):
        with st.spinner('AI is thinking....'):
            answer,context,metadata = generate_answer(question, st.session_state.history[-2:],st.session_state.vectordb)
            if answer:
                st.markdown(answer)
                with st.expander("See Source"):
                    st.write("PDF :", metadata[0]["pdf_name"])
                    st.write("Page :", metadata[0]["page"])
                    st.write(context[0])
                st.session_state.history.append({'role': 'assistant', 'message': answer})
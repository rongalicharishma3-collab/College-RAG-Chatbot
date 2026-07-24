import streamlit as st

from utils.pdf_loader import load_documents
from utils.text_splitter import split_documents
from utils.vector_store import create_vector_store
from utils.rag_chain import get_rag_chain

st.set_page_config(
    page_title="College Information Chatbot",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 College Information Chatbot")

# -----------------------
# Conversation History
# -----------------------
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------
# Create Vector Database
# -----------------------
if st.button("Create Vector Database"):

    with st.spinner("Creating Vector Database..."):

        docs = load_documents()
        chunks = split_documents(docs)
        create_vector_store(chunks)

    st.success("✅ Vector Database Created Successfully!")

st.divider()

# -----------------------
# Ask Question
# -----------------------
question = st.text_input("Ask your question")

if st.button("Get Answer"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    try:

        with st.spinner("Searching documents..."):

            # -----------------------
            # Load RAG
            # -----------------------
            st.write("🔹 Loading RAG...")
            retriever, chain = get_rag_chain()
            st.write("✅ RAG Loaded")

            # -----------------------
            # Retrieve Documents
            # -----------------------
            st.write("🔹 Retrieving documents...")
            docs = retriever.invoke(question)
            st.write(f"✅ Retrieved {len(docs)} documents")

            # -----------------------
            # Remove Duplicate Chunks
            # -----------------------
            unique_chunks = []
            seen = set()

            for doc in docs:
                if doc.page_content not in seen:
                    unique_chunks.append(doc.page_content)
                    seen.add(doc.page_content)

            context = "\n\n".join(unique_chunks[:3])

            st.write("🔹 Sending context to Groq...")

            # -----------------------
            # Generate Answer
            # -----------------------
            answer = chain.invoke(
                {
                    "context": context,
                    "question": question
                }
            )

            st.write("✅ Groq Response Received")

        # -----------------------
        # Save Chat History
        # -----------------------
        st.session_state.history.append(
            {
                "question": question,
                "answer": answer
            }
        )

        # -----------------------
        # Display Answer
        # -----------------------
        st.subheader("Answer")
        st.write(answer)

        # -----------------------
        # Display Sources
        # -----------------------
        st.subheader("Source Documents")

        shown = set()

        for doc in docs:

            source = f"{doc.metadata['source']} (Page {doc.metadata['page'] + 1})"

            if source not in shown:
                st.write("📄", source)
                shown.add(source)

    except Exception as e:

        st.error("❌ Something went wrong.")
        st.exception(e)

# -----------------------
# Conversation History
# -----------------------
if st.session_state.history:

    st.divider()
    st.subheader("💬 Conversation History")

    for chat in reversed(st.session_state.history):

        st.markdown(f"**🙋 Question:** {chat['question']}")
        st.markdown(f"**🤖 Answer:** {chat['answer']}")
        st.markdown("---")
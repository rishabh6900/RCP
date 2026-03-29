from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

def run_rag(llm, retriever, prompt, query):
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)

    rag_chain = create_retrieval_chain(
        retriever,
        combine_docs_chain
    )

    result = rag_chain.invoke({
        "input": query,
        "query": query
    })

    return result["answer"] 
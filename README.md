# Intelligent PDF Queries with RAG(Retrieval Augmented Generation)

About RAG-Powered PDF Query System: An intelligent tool for querying and retrieving insights from multiple PDF documents using Retrieval-Augmented Generation (RAG) technology.

![RAG](https://github.com/user-attachments/assets/d6bc2d11-3f86-47fd-be5b-45e3c976cc6e)

## Retrieval-Augmented Generation (RAG) process

Here's a breakdown of the process:

- **Document Retrieval:** The process begins with a user query. This query is then used to retrieve relevant documents from a knowledge base. In the image, the documents are represented by a series of file icons.

- **Document Processing:** The retrieved documents are loaded, transformed, and embedded into a vector representation. This allows for efficient comparison and search based on semantic similarity.

- **Vector Database:** The embedded document vectors are stored in a vector database. This database facilitates efficient semantic search, allowing the model to find the most relevant information based on the user's query.

- **Semantic Search:** The system performs a semantic search on the vector database using the user's query. This means that the search is based on the meaning of the query, rather than just matching keywords. The most relevant documents are retrieved.

- **Retrieved Insights:** The relevant documents from the database are used to generate insights or context relevant to the query.

- **Prompt Generation:** Based on the retrieved insights and the original query, a prompt is generated. This prompt is designed to guide the LLM's response generation, incorporating the relevant knowledge from the retrieved documents.

- **LLM Model:** The generated prompt is fed to an LLM model. This model is trained to generate human-like text based on the provided context.

- **Processed Output:** The LLM model processes the prompt and generates a response. This response is then presented to the user, incorporating both the LLM's knowledge and the relevant information retrieved from the documents.

Overall, RAG enhances LLM capabilities by enabling them to access a wider range of knowledge through external document retrieval and semantic search. This allows LLMs to generate more accurate, informative, and relevant responses to user queries.

### Setting up the Machine

- Clone the repository to the folder.
- Create virtual environment using `python -m venv .venv`
- Activate the Virtual environment using `source venv/bin/activate`
- Install all the required libraries `google-generativeai`, `streamlit` and `google-generativeai`
- create local environment by the name of `.env`.

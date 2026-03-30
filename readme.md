# Prerequisite & Course Planning Assistant 
An Agentic Retrieval-Augmented Generation (RAG) system that helps students plan their academic courses using catalog-grounded reasoning. 

# Objective 
1. Answer prerequisite queries with citations
2. Generate term-wise course plans
3. Ask clarifying questions
4. Refuse when data is not in catalog

# Dataset  
```bash 
https://drive.google.com/file/d/1rozSDc1IB3-51kOL7N47ZRCQ85ClGZKG/view?usp=sharing
```

# Key Catalog Rules

1. Students must complete prerequisites before enrolling
2. Instructor consent may override prerequisites
3. Co-requisites require concurrent enrollment
4. Course levels:
    -> 0–99 → Intro
    -> 100–199 → Undergraduate
    -> 200+ → Graduate

# Tech stack 
Gemini API, LangChain, bge-small-en-v1.5(Embeddings), FAISS, Streamlit ,python 

# Rag Pipeline 
```bash 
Document Ingestion
        |
        |
Chunking strategy 
        |
        |
Embeddings 
        |
        |
Retrieval 
        |
        |
Prompt Design
```

# Test case  
```bash 
https://drive.google.com/file/d/1wGl4gbrN_b7sx-cE120WuztFmE-qnQVP/view?usp=sharing
```

# Live Link 
```bash  
https://ggvmtgdqra33sjuot7mcnc.streamlit.app/
```

# Installation 
Step -1 
```bash 
git clone https://github.com/rishabh6900/RCP

cd DDR
```
Step -2 Create virtual environment 
``` bash
conda create --name RagR python=3.11 
```
```bash 
conda activate RagR
```

Step -3 Install dependencies
``` bash 
pip install -r requirements.txt
``` 
Step-4  Environment Variables 
Create a .env file in the project root.
```bash
GOOGLE_API_KEY = "your_api_key_here"
```
step-5 Run the Application 
```bash 
python -m streamlit run app.py 
```

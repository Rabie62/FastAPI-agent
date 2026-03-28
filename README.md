FastAPI Expert: Documentation-Aware AI Agent

This project is a specialized AI Agent designed to act as a technical expert for the FastAPI framework. It leverages Hybrid Search (combining lexical and vector retrieval) to provide accurate, context-aware answers and code examples directly from the official FastAPI documentation.
Built as part of the AI Hero: AI Agents Crash Course, it demonstrates how to transform a standard LLM into an "agentic" system by providing it with custom tools.

🚀 Key Features

- Data Ingestion: Automatically downloads and processes the latest English documentation from the official FastAPI GitHub repository.

- Advanced Chunking: Implements a dual-chunking strategy:

* Sliding Window: Context-preserving overlapping chunks.

* Section-Based: Markdown-aware splitting by headers (##) to maintain structural relevance.

- Hybrid Search Engine:

* Lexical Search: Powered by minsearch for precise keyword matching.

* Vector Search: Uses SentenceTransformer (multi-qa-distilbert-cos-v1) to capture semantic meaning.

- Agentic Framework: Uses LangChain to create an agent that can autonomously decide when to use the search_fastapi_docs tool.

- High-Performance LLM: Integrated with Nvidia Nemotron-3 (120B) via OpenRouter for sophisticated reasoning and code generation.

🛠️ Tech Stack

- Language: Python 3.14+

- Orchestration: LangChain

- Embeddings: Sentence-Transformers (HuggingFace)

- LLM: Nvidia Nemotron-3-super-120b (via OpenRouter)

- Search: MinSearch (Lexical) & VectorSearch (Dense)

- Data Handling: requests, python-frontmatter, zipfile, numpy

📋 Prerequisites

- You will need an API key from OpenRouter to run the agent.
  
- Install dependencies: pip install requests python-frontmatter numpy tqdm sentence-transformers langchain-openai langchain-core minsearch


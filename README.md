# FastAPI AI Documentation Agent

**7-Day AI Agents Email Crash-Course Final Project**  
Built following Alexey Grigorev's 7-Day AI Agents Crash Course.

## ✨ What it does

- Answers any question about **FastAPI** using the **official documentation**
- Hybrid search (lexical + semantic) over all `.md` files
- Full agent with tool calling (Pydantic AI)
- Live web UI with Streamlit

## 🛠️ Tech Stack

- **Data Ingestion**: GitHub zip + frontmatter (Day 1)
- **Chunking**: Intelligent section-based splitting (Day 2)
- **Search**: minsearch + SentenceTransformers hybrid (Day 3)
- **Agent**: Pydantic AI + function calling (Day 4)
- **Evaluation**: LLM-as-a-Judge with automated test generation (Day 5)
- **Deployment**: Streamlit (Day 6)

## 🚀 Live Demo

**→ [Open the live agent](https://your-streamlit-url.streamlit.app)** (replace after deployment)

## 📊 Evaluation Results (Day 5)

- See full metrics in the evaluation notebook

## How to run locally

```bash
git clone <your-repo>
cd <your-repo>
pip install -r requirements.txt
streamlit run app.py

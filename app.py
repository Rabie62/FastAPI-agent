import streamlit as st
import pickle
import asyncio
from pathlib import Path
import os
from typing import List
from pydantic_ai import Agent
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIChatModel
from openai import AsyncOpenAI

st.set_page_config(page_title="FastAPI AI Expert", page_icon="⚡", layout="wide")

# Custom CSS for a premium look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: -webkit-linear-gradient(45deg, #059669, #10B981);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .sub-header {
        font-size: 1.1rem;
        color: #6B7280;
        margin-bottom: 2rem;
    }
    
    /* Style Chat messages */
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    /* Gradient Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">⚡ FastAPI AI Expert</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Ask anything about <b>FastAPI</b> — powered by hybrid search + kimi k2.5</p>', unsafe_allow_html=True)

# Layout: Info Row
col1, col2, col3 = st.columns(3)
with col1:
    st.info("📚 Trained on Official Docs")
with col2:
    st.success("⚡ Async & Fast Responses")
with col3:
    st.warning("🔍 Hybrid Lexical+Vector Search")
st.divider()

# Load the saved agent (one-time)
@st.cache_resource
def load_agent():
    with open("agent_package/fastapi_agent.pkl", "rb") as f:
        pkg = pickle.load(f)
        
    text_index = pkg["text_index"]
    vector_index = pkg["vector_index"]
    embedding_model = pkg["embedding_model"]
    system_prompt = pkg["system_prompt"]
    model_name = pkg["model_name"]
    
    def search_fastapi_docs(query: str) -> List[dict]:
        """
        Search the FastAPI documentation using hybrid search.
        Returns relevant sections with title, filename and content.
        """
        t_results = text_index.search(query, num_results=5)
        v_query = embedding_model.encode(query)
        v_results = vector_index.search(v_query, num_results=5)
        
        seen = set()
        combined = []
        for res in t_results + v_results:
            uid = res['filename'] + res['section_content'][:80]
            if uid not in seen:
                seen.add(uid)
                combined.append(res)
        return combined[:5]

    api_key = st.secrets.get("OPENROUTER_API_KEY", os.environ.get("OPENROUTER_API_KEY"))
    openai_client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )
    provider = OpenAIProvider(openai_client=openai_client)
    model = OpenAIChatModel(
        model_name,
        provider=provider
    )
    
    agent = Agent(
        name="fastapi_agent",
        model=model,
        system_prompt=system_prompt,
        tools=[search_fastapi_docs],
    )
    return agent

agent = load_agent()

# Chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("How do I implement OAuth2 password flow?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("🧠 Synthesizing answer..."):
            result = asyncio.run(agent.run(user_prompt=prompt))
            response = result.output
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar info
with st.sidebar:
    st.image("https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png", width=200)
    st.header("About this Agent")
    st.markdown("""
    - **Architecture**: Hybrid lexical + vector search
    - **LLM**: kimi k2.5 via OpenRouter
    - **Knowledge Base**: Official FastAPI documentation
    """)
    
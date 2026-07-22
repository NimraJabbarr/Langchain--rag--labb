from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate,load_prompt

from dotenv import load_dotenv
import streamlit as st

# Load environment variables (OPENAI_API_KEY from .env)
load_dotenv()

# Define the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Streamlit UI
st.header("Research Tool")

# Dropdowns for paper, style, and length
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Select...",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# PromptTemplate with placeholders
template = load_prompt("template.json")

# Action button
if st.button("Summarize"):
    if paper_input != "Select...":
        # Fill placeholders
        prompt = template.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })

        # Send to model
        result = model.invoke(prompt)
        st.write(result.content)
    else:
        st.warning("Please select a research paper first.")

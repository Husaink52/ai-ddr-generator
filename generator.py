from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_ddr(merged_data):

    prompt = f"""
You are a STRICT building inspection analyst.

You MUST follow ALL rules:
- Do NOT invent information
- Use ONLY provided data
- If data is missing → write "Not Available"
- If conflict exists → explicitly mention "Conflict detected"
- Use simple, client-friendly language

INPUT DATA:
{merged_data}

Generate a structured DDR:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing Information
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content

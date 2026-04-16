from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def generate_ddr(merged_data):

    prompt = f"""
You are a STRICT building inspection analyst.

Generate a DDR report using the following rules:

- Do NOT invent information
- Use ONLY provided data
- If information is missing → write "Not Available"
- If conflict exists → clearly mention "Conflict detected"
- Avoid repeating similar observations
- Group similar issues logically
- Keep observations specific and actionable
- Use simple client-friendly language
- Include thermal reasoning where relevant

INPUT DATA:
{merged_data}

Generate a structured DDR:

1. Property Issue Summary
2. Area-wise Observations
3. Root Cause
4. Severity (grouped logically)
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

from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ddr(merged_data):
    prompt = f"""
You are a building inspection expert.

Based ONLY on the following observations, generate a structured DDR report.

Observations:
{merged_data}

Rules:
- Do NOT invent data
- Mention "Not Available" where needed
- Keep it client-friendly

Output format:
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
        temperature=0.3,
    )

    return response.choices[0].message.content
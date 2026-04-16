# 🏗️ AI DDR Generator – Applied AI Builder Assignment

## 📌 Overview

This project is an AI-powered system that converts **raw inspection reports and thermal scan data** into a structured, client-ready **Detailed Diagnostic Report (DDR)**.

The system is designed to handle **real-world imperfect data**, including:

* Missing information
* Conflicting observations
* Unstructured inputs

It follows a **hybrid AI architecture (rule-based + LLM reasoning)** to ensure accuracy, reliability, and generalization.

---

## 🎯 Objective

To build an AI workflow that:

* Extracts insights from inspection and thermal reports
* Merges multi-source data logically
* Handles missing and conflicting information explicitly
* Produces a clear, client-friendly DDR

---

## 🧠 System Design

The solution is built as a **multi-stage pipeline**:

### 1. Data Extraction Layer

* Extracts **text and images** from PDFs using `PyMuPDF`
* Works for both:

  * Inspection reports
  * Thermal reports

---

### 2. Structuring Layer

* Converts unstructured text into structured observations
* Detects:

  * Areas (Hall, Bedroom, Kitchen, etc.)
  * Issues (dampness, leakage, cracks, etc.)

---

### 3. Validation Layer (Critical for Reliability)

* Ensures:

  * Missing fields → explicitly marked as `"Not Available"`
  * Prevents empty or invalid entries

---

### 4. Merging Layer (Core Logic)

Combines inspection + thermal data using rule-based logic:

* Thermal cold spots (< 23°C) → indicate possible moisture
* Links thermal anomalies with inspection observations
* Detects **conflicts**:

  * Example: Inspection says "no issue" but thermal shows anomaly

---

### 5. Reasoning Layer (LLM)

Uses **LLaMA 3 (70B) via Groq API** to generate the final DDR.

The LLM is **strictly controlled via prompt design**:

* No hallucination allowed
* Must not invent data
* Must explicitly mention:

  * Missing information
  * Conflicts

---

### 6. Output Layer

Generates a structured DDR with:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing Information

---

## ⚙️ Tech Stack

* **Python**
* **Streamlit** (UI & deployment)
* **Groq API (LLaMA 3 - 70B)** (LLM reasoning)
* **PyMuPDF** (PDF parsing)
* **Pillow** (image handling)

---

## 🔍 Key Features

### ✅ Hybrid AI System

Combines:

* Rule-based validation (deterministic)
* LLM reasoning (flexible)

---

### ✅ Conflict Detection

Explicitly identifies contradictions between:

* Inspection data
* Thermal readings

---

### ✅ Missing Data Handling

* Any missing information is labeled as:

  ```
  Not Available
  ```

---

### ✅ Generalization

* Not hardcoded for specific files
* Works on similar inspection reports

---

### ✅ Image Extraction

* Extracts images from reports
* Displays them alongside output (basic implementation)

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

---

## 🌐 Live Demo

👉 [Add your Streamlit link here]

---

## 📂 Project Structure

```
ai-ddr-generator/
│
├── app.py              # Streamlit app
├── extractor.py        # PDF text + image extraction
├── processor.py        # Structuring + merging logic
├── generator.py        # LLM-based DDR generation
├── requirements.txt
└── README.md
```

---

## ⚠️ Limitations

* Image-to-area mapping is basic (page-based)
* Area detection is keyword-based (can be improved with NLP models)
* Thermal-to-specific-area mapping is approximate
* No persistent storage (stateless app)

---

## 🔮 Future Improvements

* Advanced NLP for better area classification
* Stronger conflict reasoning using structured knowledge graphs
* Precise image-to-observation mapping
* Export DDR as downloadable PDF
* Add severity scoring model

---

## 🧪 Evaluation Alignment

This solution directly addresses evaluation criteria:

| Criteria          | Approach                                            |
| ----------------- | --------------------------------------------------- |
| Accuracy          | Structured extraction + keyword filtering           |
| Logical merging   | Rule-based integration of thermal + inspection data |
| Conflict handling | Explicit detection and reporting                    |
| Missing data      | Enforced "Not Available" logic                      |
| Clarity           | LLM generates client-friendly structured output     |
| System thinking   | Hybrid pipeline (rules + AI)                        |

---

## 🎥 Loom Video

👉 [Add Loom video link here]

---

## 📌 Key Insight

> This system prioritizes **reliability over blind AI generation** by combining deterministic validation with controlled LLM reasoning.

---

## 👤 Author

Husain K
AI Generalist Assignment Submission

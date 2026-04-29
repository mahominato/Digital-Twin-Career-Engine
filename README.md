# 🚀 Digital Twin: AI Career Command Center

## 📝 Overview
This project is an advanced "Digital Twin" system designed to manage professional growth. It analyzes a user's digital footprint (skills, academic background, and interests) to predict optimal career paths using Machine Learning and provides an autonomous AI Agent to bridge skill gaps.

---

## 🏗 The 5-Layer Gen AI Architecture

### 1. Platform Layer (Data & Context)
* **MCP Integration:** The system is engineered to bridge **NotebookLM** and **Antigravity**. 
* **Data Source:** Personal data (CV, LinkedIn, Academic Transcripts, and YouTube History) was synthesized in NotebookLM to create a structured skill profile.
* **Implementation:** Using the Model Context Protocol (MCP), the application queries the synthesized knowledge base to extract a high-fidelity "Skill Vector" for the user.

### 2. Model Layer (Reasoning & Prediction)
* **Algorithm:** A classical Machine Learning script using **Scikit-Learn**.
* **Logic:** The system applies **Cosine Similarity** to compare the user's current skill vector against a curated dataset of tech job requirements (`JOBS`).
* **Output:** The model generates a `results.json` file containing the top 3 job matches, a mathematical "Match Score", and identifies specific "Missing Skills" required to reach the goal.

### 3. Agent Layer (Autonomous Execution)
* **Function:** An autonomous workflow that takes the "Missing Skills" from the Model Layer and interacts with the live internet.
* **Prompt Injection:** A dynamic system prompt instructs the Agent to find real-world resources (GitHub repos, Hackathons, Documentation) to close the identified skill gaps.
* **Tool Calling:** The agent autonomously executes web searches and parses results to provide actionable learning paths.

### 4. Application Layer (Vibe-Coded UI)
An interactive dashboard built with **Streamlit**, featuring four specialized modules:
* **📊 Analytics (Balance Wheel):** A dynamic radar chart comparing Hard vs. Soft skills.
* **🎮 Tech Tree:** A video-game-style map showing the "levels" needed to unlock the dream job.
* **💬 Twin Coach (Agent Mode):** A chatbot with a **"Roast My Stack"** toggle that critiques the user's progress using a high-pressure tech-lead persona.
* **🎓 Semester Wrapped:** A functional tool that generates a shareable graphic summarizing the user's achievements and growth.

### 5. Infrastructure Layer (Hardware & Hosting)
* **Local Compute:** The Streamlit UI, Data Processing, and the Scikit-Learn ML Engine run locally on the user's CPU to ensure data privacy and speed.
* **Cloud Compute:** High-level reasoning and autonomous web browsing are handled by LLM APIs (Gemini/Antigravity) via secure cloud calls.

---

## 🛠 Tech Stack
* **Frontend:** Streamlit, Plotly
* **ML Engine:** Scikit-Learn, NumPy
* **Logic:** Python (JSON, PIL)
* **AI:** Gemini API / Antigravity Agent Platform

---

## 🚀 How to Run
1. Install dependencies: `pip install streamlit scikit-learn plotly pillow`
2. Run the application: `streamlit run app.py`
3. Navigate to the **Infra** tab and click **"Run Career Prediction Engine"** to initialize the ML Model.
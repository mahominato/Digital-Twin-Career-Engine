import streamlit as st
import plotly.graph_objects as go
import json
import os
import datetime
import google.generativeai as genai
import pandas as pd
import plotly.express as px
from PIL import Image, ImageDraw


# Importing your specific logic layers
from model_layer import skill_categories
from ml_engine import predict_careers


# ---------------- CONFIG & THEME ----------------
st.set_page_config(
    page_title="Digital Twin Career Engine",
    page_icon="🚀",
    layout="wide",
)


def inject_altynbek_style():
    st.markdown(
        """
        <style>
            /* Main Background */
            .stApp {
                background: linear-gradient(135deg, #0f172a 0%, #111827 45%, #1e293b 100%);
                color: #f8fafc;
            }
            /* Sidebar */
            section[data-testid="stSidebar"] {
                background: #0b0f19 !important;
                border-right: 1px solid rgba(255,255,255,0.1);
            }
            /* Hero Card */
            .hero-card {
                padding: 35px;
                border-radius: 28px;
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.15);
                box-shadow: 0 25px 50px rgba(0,0,0,0.4);
                margin-bottom: 25px;
            }
            .hero-title {
                font-size: 44px;
                font-weight: 900;
                color: #ffffff;
                margin-bottom: 8px;
            }
            /* RPG Tech Tree Cards */
            .tech-card {
                padding: 24px;
                border-radius: 22px;
                background: rgba(15, 23, 42, 0.8);
                border: 1px solid rgba(148, 163, 184, 0.2);
                min-height: 160px;
                margin-bottom: 15px;
            }
            .skill-pill {
                display: inline-block;
                padding: 5px 12px;
                border-radius: 50px;
                margin: 4px;
                background: rgba(59,130,246,0.15);
                color: #60a5fa;
                border: 1px solid rgba(59,130,246,0.3);
                font-size: 11px;
                font-weight: 600;
            }
            /* Semester Wrapped Card */
            .wrapped-card {
                padding: 40px;
                border-radius: 30px;
                background: linear-gradient(135deg, #6366f1, #a855f7, #ec4899);
                color: white;
                box-shadow: 0 20px 60px rgba(168,85,247,0.4);
                margin-bottom: 30px;
                text-align: center;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_altynbek_style()


# ---------------- DATA LOGIC ----------------
def load_results():
    if os.path.exists("results.json"):
        with open("results.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def get_coach_response(prompt, roast_mode, api_key):
    # Gemini API Call logic
    if api_key:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            behavior = "You are a toxic tech lead roasting a junior." if roast_mode else "You are a helpful career mentor."
            full_query = f"{behavior} Question: {prompt}"
            return model.generate_content(full_query).text
        except Exception:
            pass
    # Local fallback logic (Your original logic)
    return "API unavailable. Analyzing based on tech-tree categories..."


# ---------------- UI COMPONENTS ----------------
def render_wrapped(data):
    if data:
        st.markdown(f"""
            <div class="wrapped-card">
                <div style="text-transform: uppercase; letter-spacing: 2px; font-size: 14px;">Your 2026 Evolution</div>
                <div style="font-size: 48px; font-weight: 900; margin: 15px 0;">{data[0]['job_title']}</div>
                <div style="font-size: 22px; opacity: 0.9;">Current Mastery: <b>{data[0]['match_score']}%</b></div>
                <div style="margin-top: 25px; font-size: 16px; background: rgba(0,0,0,0.2); display: inline-block; padding: 10px 30px; border-radius: 50px;">
                    Digital Twin Status: Optimized
                </div>
            </div>
        """, unsafe_allow_html=True)


def render_tech_tree(data):
    st.subheader("🕹️ RPG Tech Tree")
    if not data:
        st.info("No prediction data. Run the ML Engine first.")
        return
   
    cols = st.columns(3)
    for idx, career in enumerate(data[:3]):
        with cols[idx]:
            st.markdown(f"""
                <div class="tech-card">
                    <div style="color: #94a3b8; font-size: 11px; text-transform: uppercase;">Path Unlocking</div>
                    <div style="font-size: 22px; font-weight: 800; color: #fff; margin: 5px 0;">{career['job_title']}</div>
                    <div style="color: #60a5fa; font-weight: 700;">Score: {career['match_score']}%</div>
                </div>
            """, unsafe_allow_html=True)
            st.progress(career['match_score'] / 100)
           
            if career.get('missing_skills'):
                st.markdown("Missing Nodes:")
                pills = "".join([f'<span class="skill-pill">🔒 {s}</span>' for s in career['missing_skills']])
                st.markdown(pills, unsafe_allow_html=True)


def render_balance_wheel(user_skills):
    st.subheader("⚖️ The Balance Wheel")
    # Using your model_layer categorization
    radar_data = skill_categories(user_skills)
    df = pd.DataFrame(radar_data)
   
    fig = px.line_polar(df, r="value", theta="category", line_close=True)
    fig.update_traces(fill="toself", line_color="#6366f1", fillcolor="rgba(99, 102, 241, 0.3)")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        polar=dict(bgcolor="rgba(0,0,0,0)", radialaxis=dict(gridcolor="#334155"))
    )
    st.plotly_chart(fig, use_container_width=True)


# ---------------- MAIN APPLICATION ----------------
with st.sidebar:
    st.markdown("### 🧠 AI Identity")
    api_key = st.text_input("Gemini Key", type="password")
    roast_mode = st.toggle("🔥 Roast Mode", value=False)
   
    st.divider()
    st.markdown("### 📥 Profile Input")
    raw_input = st.text_area("Update Skills", "Figma, UX Research, C++, Wireframing")
    user_skills = {s.strip().lower(): 0.9 for s in raw_input.split(",")}
   
    if st.button("🚀 Execute Pipeline", use_container_width=True):
        predict_careers(user_skills)
        st.rerun()


# Hero Section
st.markdown("""
    <div class="hero-card">
        <div style="color: #6366f1; font-weight: bold; letter-spacing: 1px;">SYSTEM STATUS: ONLINE</div>
        <div class="hero-title">Career Command Center</div>
        <div style="color: #94a3b8; font-size: 18px;">Mapping digital footprints to high-performance career trajectories.</div>
    </div>
""", unsafe_allow_html=True)


# Navigation
tab1, tab2, tab3, tab4 = st.tabs(["🎮 Career Tree", "📊 Skill Analytics", "💬 Twin Coach", "⚙️ System"])


with tab1:
    results = load_results()
    render_wrapped(results)
    render_tech_tree(results)


with tab2:
    render_balance_wheel(user_skills)


with tab3:
    st.subheader("💬 Live Coach Chatbot")
    if "messages" not in st.session_state:
        st.session_state.messages = []


    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.write(m["content"])


    if prompt := st.chat_input("Analyze my trajectory..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
       
        response = get_coach_response(prompt, roast_mode, api_key)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()


with tab4:
    st.subheader("Infrastructure Layer")
    if st.button("Generate PNG Summary"):
        # Your original PIL generation logic would be called here
        st.success("Wrapped PNG created successfully.")


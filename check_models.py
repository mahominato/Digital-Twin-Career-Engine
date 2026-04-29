import google.generativeai as genai
import streamlit as st

try:
    # Загружаем ключ
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    print("Список доступных моделей:")
    # В новых версиях свойство называется supported_generation_methods
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Ошибка: {e}")
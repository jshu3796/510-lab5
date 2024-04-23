import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# 加载环境变量
load_dotenv()

# 配置 API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# 设定提示模板
prompt_template = """
You are an expert chef.

Please take the ingredients provided by the user and suggest a dish along with detailed cooking steps.

The ingredients are:
{ingredients}
"""

def generate_content(ingredients):
    prompt = prompt_template.format(ingredients=ingredients)
    response = model.generate_content(prompt)
    return response.text

# 设置 Streamlit 页面
st.title("🍽️ AI Cooking Assistant")

# 创建文本区域让用户输入食材
ingredients = st.text_area("Enter the ingredients you have (separated by commas):")
if st.button("Suggest a dish!"):
    reply = generate_content(ingredients)
    st.write(reply)

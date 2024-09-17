import streamlit as st
import google.generativeai as genai

# Configure the generative AI model
genai.configure(api_key='Your API Key')

# Custom CSS for dark theme styling
st.markdown("""
    <style>
    .main {
        background-color: #1e1e1e;
        color: #ffffff;
        padding: 20px;
        border-radius: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #1e1e1e;
        color: #ffffff;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        background-color: #333333;
        color: #ffffff;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #4CAF50;
    }
    .stMarkdown {
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

st.title('💬 Chat with Generative AI')

model = genai.GenerativeModel('gemini-1.5-pro-latest')
chat = model.start_chat(history=[])

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

# Sidebar for history
st.sidebar.title('📜 Chat History')
for i, (q, _) in enumerate(st.session_state.history):
    if st.sidebar.button(f"Q{i+1}: {q}"):
        question = q
        response = chat.send_message(question)
        st.write('Your AI Agent (from history):', response.text)
        st.session_state.history.append((question, response.text))

# Main chat interface
st.markdown("### Ask your question:")
question = st.text_input('You: ')
if st.button('Send'):
    response = chat.send_message(question)
    st.write('Your AI Agent:', response.text)
    
    # Update history
    st.session_state.history.append((question, response.text))

# Add a separator
st.markdown("---")

# Footer
st.markdown("""
    <div style="text-align: center; color: #ffffff;">
        <small>Powered by Generative AI</small>
    </div>
""", unsafe_allow_html=True)
import streamlit as st

# 初始化 session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Say something")  # 注意：streamlit并没有提供`chat_input`函数

if prompt:
    # 当用户输入了新的消息时，添加到session state中
    st.session_state.messages.extend([
        {
            "role": "user",
            "content": prompt
        },
        {
            "role": "assistant",
            "content": f"response: {prompt}"
        }
    ])

# 循环遍历 session state 中的消息并显示
for i in st.session_state.messages:
    with st.chat_message(i["role"]):  # 注意：streamlit并没有提供`chat_message`函数
        st.write(i["content"])

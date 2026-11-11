import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Local Lingo Lite",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Local Lingo Lite")
st.caption("IA 100% local • Privacidade total")

# Verificar servidor
def check_server():
    try:
        r = requests.get("http://localhost:8080/health", timeout=2)
        return r.status_code == 200
    except:
        return False

if not check_server():
    st.error("❌ Servidor offline. Inicie o `llama-server` primeiro.")
    st.stop()

st.success("✅ Servidor local online")

# Inicializar histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input do usuário
if prompt := st.chat_input("Digite sua mensagem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Preparar prompt
    system_prompt = "You are a helpful English tutor."
    full_prompt = f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
    
    for msg in st.session_state.messages[-6:]:
        role = "user" if msg["role"] == "user" else "assistant"
        full_prompt += f"<|im_start|>{role}\n{msg['content']}<|im_end|>\n"
    
    full_prompt += "<|im_start|>assistant\n"

    # Requisição com streaming
    with st.chat_message("assistant"):
        try:
            payload = {
                "prompt": full_prompt,
                "n_predict": 512,
                "temperature": 0.7,
                "stop": ["<|im_end|>"],
                "stream": True
            }
            
            with requests.post("http://localhost:8080/completion", json=payload, stream=True, timeout=120) as response:
                response.raise_for_status()
                
                full_response = ""
                message_placeholder = st.empty()
                
                for line in response.iter_lines():
                    if line:
                        if line.startswith(b"data: "):
                            data = json.loads(line[6:])
                            if "content" in data:
                                chunk = data["content"]
                                full_response += chunk
                                message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Erro: {str(e)}")

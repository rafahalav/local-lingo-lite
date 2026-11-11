import requests
import json

print("🔍 Testando conexão com o servidor local...")

try:
    response = requests.get("http://localhost:8080/health")
    if response.status_code == 200:
        print("✅ Servidor está online e saudável!")
        print(f" Status: {response.json()}")
    else:
        print("❌ Servidor respondeu com status diferente de 200")
except requests.exceptions.ConnectionError:
    print(" Erro: Não foi possível conectar ao servidor.")
    print("💡 Verifique se o llama-server está rodando no terminal 1.")
    exit()

# Teste de inferência rápida
print("\n🧠 Enviando pergunta de teste...")
payload = {
    "prompt": "<|im_start|>system\nVocê é um assistente útil.<|im_end|>\n<|im_start|>user\nQuanto é 2+2?<|im_end|>\n<|im_start|>assistant\n",
    "n_predict": 50,
    "temperature": 0.7,
    "stop": ["<|im_end|>"]
}

response = requests.post("http://localhost:8080/completion", json=payload, timeout=60)
data = response.json()

print("\n💬 Resposta do modelo:")
print(f"   {data['content'].strip()}")
print("\n✅ Teste concluído! Agora vamos para a interface Streamlit.")

# 🇧🇷🇺🇸 Local Lingo Lite

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![llama.cpp](https://img.shields.io/badge/Backend-llama.cpp-000000.svg)](https://github.com/ggml-org/llama.cpp)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Uma aplicação web de tutor de inglês **100% local, privada e ultraleve**, projetada para rodar eficientemente em hardware modesto (CPUs sem GPU dedicada e RAM limitada). 

Este projeto demonstra como integrar um backend de inferência em C++ (`llama.cpp`) com um frontend moderno em Python (`Streamlit`), eliminando a dependência de APIs em nuvem, custos por token e riscos de privacidade.

---

## ✨ Funcionalidades

- 🚫 **Zero Dependência de Nuvem**: Toda a inferência ocorre localmente na sua máquina.
- ⚡ **Streaming em Tempo Real**: Respostas geradas token por token para uma experiência fluida.
- 🛡️ **Privacidade Total**: Suas conversas nunca saem do seu dispositivo.
- 🪶 **Otimizado para Hardware Modesto**: Configurado para rodar em CPUs antigas (ex: Intel Core i5 1ª Ger.) com 8GB de RAM, utilizando quantização GGUF (Q4_K_M) e flags de compilação nativa.
- 🧩 **Arquitetura Modular**: Separação clara entre o motor de inferência (C++) e a interface de usuário (Python).

---

## 🛠️ Stack Tecnológica

| Camada | Tecnologia | Justificativa |
|--------|------------|---------------|
| **Backend de IA** | `llama.cpp` (C++) | Inferência de LLMs com eficiência máxima em CPU. |
| **Frontend** | `Streamlit` | Prototipagem rápida de interfaces de dados e chat. |
| **Comunicação** | `requests` (Python) | Requisições HTTP leves para a API local do `llama-server`. |
| **Modelo** | Qwen2.5 1.5B / SmolLM2 360M (GGUF) | Modelos quantizados (Q4_K_M) que equilibram inteligência e baixo consumo de RAM. |
| **Ambiente** | Python `venv` | Isolamento de dependências do sistema operacional. |

---

## 📋 Pré-requisitos

- Sistema Operacional: **Linux** (recomendado, ex: MX Linux, Linux Mint, Ubuntu) ou Windows com WSL2.
- Python 3.8 ou superior.
- Ferramentas de compilação: `build-essential`, `cmake`, `git`.

---

## 🚀 Instalação e Configuração

Siga os passos abaixo para configurar o projeto do zero:

### 1. Clonar o Repositório e Criar Ambiente Virtual
```bash
git clone https://github.com/SEU_USUARIO/local-lingo-lite.git
cd local-lingo-lite
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Compilar o `llama.cpp` (Otimizado para seu CPU)
```bash
git clone https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
mkdir build && cd build
cmake -DGGML_NATIVE=ON ..  # Habilita otimizações específicas do seu processador (ex: AVX2)
make -j2                   # Compila usando 2 núcleos
cd ../..
```

### 3. Baixar o Modelo Quantizado (GGUF)
Baixe um modelo compatível e coloque-o na raiz do projeto `local-lingo-lite`. Exemplo com Qwen2.5 1.5B:
```bash
wget -O model.gguf https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF/resolve/main/qwen2.5-1.5b-instruct-q4_k_m.gguf
```
*(Alternativa ultraleve: [SmolLM2 360M](https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct-GGUF))*

---

## 💻 Como Usar

O projeto opera em dois terminais separados para garantir estabilidade:

**Terminal 1: Iniciar o Motor de IA**
```bash
cd ~/local-lingo-lite/llama.cpp/build
# Otimizado para hardware com limitação térmica/de RAM:
./bin/llama-server -m ../../model.gguf -c 512 --port 8080 -ngl 0 -t 2 -b 256
```
*Aguarde a mensagem: `llama server listening at http://127.0.0.1:8080`*

**Terminal 2: Iniciar a Interface Web**
```bash
cd ~/local-lingo-lite
source venv/bin/activate
streamlit run app.py
```
O navegador abrirá automaticamente em `http://localhost:8501`.

---

## ⚙️ Notas de Hardware e Otimização

Este projeto foi testado e validado em um **Intel Core i5-520M (1ª Geração) com 8GB de RAM**. Para garantir estabilidade em hardware similar, as seguintes otimizações foram aplicadas:

- `-t 2`: Limita o uso a 2 threads, evitando sobrecarga em CPUs dual-core.
- `-c 512`: Reduz a janela de contexto para 512 tokens, diminuindo drasticamente o uso de RAM e a carga de processamento, sem perder a coerência em conversas curtas.
- `-ngl 0`: Força a execução na CPU (ideal para GPUs integradas muito básicas ou inexistentes).
- **Compilação Nativa**: A flag `-DGGML_NATIVE=ON` garante que o compilador utilize instruções vetoriais (como AVX2) disponíveis no processador, acelerando a inferência.

> **⚠️ Aviso Térmico:** Notebooks antigos podem sofrer *thermal throttling*. Monitore a temperatura (ex: com `htop` ou `sensors`). Se ultrapassar 90°C, considere limpeza física do hardware ou a troca para um modelo ainda menor (ex: 360M).

---

## 📂 Estrutura do Projeto

```text
local-lingo-lite/
├── app.py                  # Interface Streamlit (Frontend)
├── requirements.txt        # Dependências Python
├── model.gguf              # Modelo de IA quantizado (não versionado no Git)
├── venv/                   # Ambiente virtual Python (não versionado)
└── llama.cpp/              # Submódulo do motor de inferência (não versionado)
```

---

## 🤝 Contribuindo e Licença

Sinta-se à vontade para abrir *Issues* ou *Pull Requests* com melhorias de performance ou novos recursos.

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
*Desenvolvido com foco em acessibilidade, privacidade e engenharia de software eficiente.*
```

---
# local-lingo-lite

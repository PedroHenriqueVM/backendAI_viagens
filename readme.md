# 🌎 API Roteiros de Viagem

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-API-black)
![Google Gemini](https://img.shields.io/badge/IA-Gemini-blueviolet)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

API REST desenvolvida em **Python com Flask** para geração automática de roteiros de viagem personalizados usando inteligência artificial (Google Gemini).

O sistema permite:

* Gerar roteiros completos para qualquer destino
* Personalizar por quantidade de dias e perfil de orçamento (Alto, Médio, Baixo)
* Sugestão de atrações, restaurantes, valores e dicas úteis
* Resposta estruturada em JSON

---


# 🚀 Deploy da API

🔗 **API online na Vercel**

https://backend-ai-viagens.vercel.app/

---

# 🌐 Front-end do Projeto

🔗 Link do front-end:

https://frontend-ai-viagens.vercel.app/

---

# 💻 Repositório do Projeto

🔗 GitHub

https://github.com/PedroHenriqueVM/backendAI_viagens.git

---

# 📖 Documentação da API

Endpoint principal:

```text
POST /generate
```

---

# 📚 Funcionalidades

✔ Geração de roteiros personalizados por destino, dias e orçamento
✔ Sugestão de atrações turísticas reais
✔ Sugestão de restaurantes e valores estimados
✔ Conversão automática de moedas para viagens internacionais
✔ Dicas úteis sobre o destino
✔ Resposta 100% em português e formato JSON

---

# 🛠 Tecnologias utilizadas

* Python
* Flask
* Flask-CORS
* Google Gemini (google-genai)
* Python Dotenv
* Vercel

---

# 📂 Estrutura do Projeto

```
backendAI_viagens
│
├── app.py
├── config.py
├── requirements.txt
├── .env
├── vercel.json
└── readme.md
```

---

# ⚙️ Instalação do Projeto

## 1️⃣ Clonar repositório

```
git clone https://github.com/SeuUsuario/backendAI_viagens.git
```

```
cd backendAI_viagens
```

---

## 2️⃣ Criar ambiente virtual

```
python -m venv venv
```

Ativar ambiente virtual

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

---

## 3️⃣ Instalar dependências

```
pip install -r requirements.txt
```

---

# 🔑 Configuração do .env

Crie um arquivo `.env` na raiz do projeto com sua chave da API Gemini:

```
GEMINI_API_KEY=SEU_TOKEN_GEMINI
```

---

# ▶️ Executar a API

```
python app.py
```

Servidor rodará em:

```
http://localhost:5000
```

---

# 📡 Exemplo de requisição

## Gerar roteiro de viagem

```
POST /generate
```

Body:

```json
{
	"destino": "Curitiba, Brasil",
	"dias": 3,
	"orcamento": "Médio"
}
```

Resposta:

```json
{
	"status": "success",
	"parametros_busca": {
		"destino": "Curitiba, Brasil",
		"dias": 3,
		"orcamento": "Médio"
	},
	"dados_roteiro": {
		"nome_do_roteiro": "...",
		"destino": "...",
		"duracao": "...",
		"perfil_orcamento": "...",
		"estimativa_custo_total": "...",
		"roteiro_diario": [ ... ],
		"dicas_uteis": [ ... ]
	}
}
```

---

# 🧪 Testes da API

A API pode ser testada utilizando:

* Thunder Client
* Postman
* Insomnia

---

# 👨‍💻 Autor

Pedro Vasconcelos

Projeto desenvolvido para fins educacionais no curso de **Desenvolvimento de Sistemas**.

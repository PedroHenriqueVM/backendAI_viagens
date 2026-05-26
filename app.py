import os
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import ROTEIRO_SCHEMA, SYSTEM_INSTRUCTION

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app)

def generate_travel_itinerary(destino, dias, orcamento):
    # Prompt otimizado para gerar roteiros estruturados por tempo e custo
    conteudo_prompt = (
        conteudo_prompt = (
            f"Gere um plano de viagem completo para o destino {destino}. "
            f"O roteiro DEVE conter EXATAMENTE {dias} dias diferentes. "
            f"Crie obrigatoriamente todos os dias do Dia 1 até o Dia {dias}, "
            f"sem resumir, sem agrupar e sem pular dias. "
            f"O orçamento obrigatório é {orcamento}. "
            f"Cada dia deve possuir atividades diferentes distribuídas em manhã, tarde e noite. "
            f"As descrições devem ser curtas e objetivas para evitar cortes na resposta."
        )
    )
    
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=conteudo_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema=ROTEIRO_SCHEMA,
        )
    )
    return response.text

@app.route("/")
def root():
    return jsonify({
        "status": "success",
        "message": "API Gerador de Roteiros de Viagem funcionando!",
        "version": "3.0"
    }), 200

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    
    # Validação básica dos dados recebidos do frontend
    if not data or not all(k in data for k in ("destino", "dias", "orcamento")):
        return jsonify({
            "status": "error",
            "message": "Por favor, envie 'destino', 'dias' e 'orcamento' no formato JSON."
        }), 400
        
    destino = data.get("destino")
    dias = data.get("dias")
    orcamento = str(data.get("orcamento")).capitalize() # Padroniza para 'Alto', 'Médio' ou 'Baixo'
    
    if orcamento not in ["Alto", "Médio", "Baixo"]:
        return jsonify({
            "status": "error",
            "message": "O orçamento deve ser exclusivamente 'Alto', 'Médio' ou 'Baixo'."
        }), 400
        
    try:
        # Envia os parâmetros para a API do Gemini
        roteiro_json_string = generate_travel_itinerary(destino, dias, orcamento)
        
        # Transforma a resposta em um formato que o Flask consegue enviar
        roteiro_estruturado = json.loads(roteiro_json_string)
        
        return jsonify({
            "status": "success",
            "parametros_busca": {
                "destino": destino,
                "dias": dias,
                "orcamento": orcamento
            },
            "dados_roteiro": roteiro_estruturado
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Erro interno ao gerar o roteiro de viagem: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(debug=True)
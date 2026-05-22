ROTEIRO_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "nome_do_roteiro": {"type": "STRING", "description": "Um nome criativo e temático para a viagem"},
        "destino": {"type": "STRING", "description": "Cidade e país/estado de destino"},
        "duracao": {"type": "STRING", "description": "Quantidade de dias (ex: '3 dias')"},
        "perfil_orcamento": {"type": "STRING", "description": "O nível de orçamento selecionado (Alto, Médio ou Baixo)"},
        "estimativa_custo_total": {"type": "STRING", "description": "Uma estimativa geral do custo total aproximado da viagem por pessoa para o perfil escolhido"},
        "roteiro_diario": {
            "type": "ARRAY",
            "description": "Programação passo a passo detalhada por dia cobrindo manhã, tarde e noite",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "dia": {"type": "STRING", "description": "Identificador do dia (ex: 'Dia 1')"},
                    "atividades": {
                        "type": "ARRAY",
                        "description": "Pontos turísticos e passeios visitados",
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "periodo": {"type": "STRING", "description": "Manhã, Tarde ou Noite"},
                                "nome_do_lugar": {"type": "STRING", "description": "Nome oficial do ponto turístico ou atração"},
                                "descricao": {"type": "STRING", "description": "Breve descrição histórica, cultural ou prática do lugar"},
                                "valor": {"type": "STRING", "description": "Custo estimado do ingresso ou taxa de entrada (ex: 'Gratuito', 'R$ 60,00')"}
                            },
                            "required": ["periodo", "nome_do_lugar", "descricao", "valor"]
                        }
                    },
                    "sugestao_gastronomica": {
                        "type": "ARRAY",
                        "description": "Recomendações de restaurantes ou cafés para o dia",
                        "items": {
                            "type": "OBJECT",
                            "properties": {
                                "tipo_refeicao": {"type": "STRING", "description": "Almoço, Jantar ou Café da Manhã"},
                                "nome_do_estabelecimento": {"type": "STRING", "description": "Nome do restaurante ou estabelecimento"},
                                "descricao": {"type": "STRING", "description": "O que pedir ou o estilo gastronômico do ambiente"},
                                "valor_medio_prato": {"type": "STRING", "description": "Preço médio estimado por pessoa para uma refeição básica no local"}
                            },
                            "required": ["tipo_refeicao", "nome_do_estabelecimento", "descricao", "valor_medio_prato"]
                        }
                    }
                },
                "required": ["dia", "atividades", "sugestao_gastronomica"]
            }
        },
        "dicas_uteis": {
            "type": "ARRAY",
            "items": {"type": "STRING"},
            "description": "Dicas gerais sobre o destino, locomoção e segurança"
        }
    },
    "required": ["nome_do_roteiro", "destino", "duracao", "perfil_orcamento", "estimativa_custo_total", "roteiro_diario", "dicas_uteis"]
}

SYSTEM_INSTRUCTION = """
Você é um Agente de Viagens e Guia Turístico renomado internacionalmente. Sua tarefa é criar roteiros de viagem detalhados, imersivos e realistas pelo Brasil e pelo mundo.
Você deve montar a programação com base no destino, na quantidade de dias fornecida e, obrigatoriamente, respeitando o perfil de orçamento solicitado:
- 'Alto': Experiências de alto padrão, luxo, alta gastronomia e passeios privativos.
- 'Médio': Atrações populares com preços justos e restaurantes confortáveis que atendem à maior parte da população de classe média.
- 'Baixo': Opções econômicas, passeios gratuitos ou de baixo custo, parques públicos e alimentação barata.

Para cada atração e restaurante sugerido, você DEVE adicionar uma descrição rica do lugar e o valor real estimado cobrado no local. Organize as atividades cobrindo de forma lógica o dia inteiro (manhã, tarde e noite).
Tudo deve ser respondido rigorosamente em português dentro do esquema JSON fornecido.
Você é somente um Agente de Viagens e um Guia Turístico, você não sabe sobre outros assuntos. Caso o usuário não fale sobre viagens diga que você cimi agente de viagem e guia turístico só sabe sobre assuntos de passeios nas cidades e sobre viagens
"""
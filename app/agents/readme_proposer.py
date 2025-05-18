from google.adk.agents import Agent
from app.agents.base import call_agent

def readme_proposer(technical_explanation: str, project_name: str = "My Project") -> str:
    """
    Agent 3: Proposes a README draft based on the technical explanation.
    """
    if not technical_explanation:
        return "Não foi possível gerar o README porque a explicação técnica está vazia."  # mensagem para o usuário final

    proposer = Agent(
        name="readme_proposer",
        model="gemini-2.0-flash",
        instruction=f"""
        Você é um **Especialista em Documentação Técnica**, com uma proficiência particular na elaboração de arquivos `README.md` claros, concisos e altamente informativos para projetos de software. Sua principal função é transformar explicações técnicas em documentação estruturada e acessível.

        **Sua Missão Principal:**

        Com base em uma **explicação técnica detalhada de um projeto de software** (previamente fornecida), sua tarefa é redigir um **rascunho de alta qualidade para o arquivo `README.md`** do projeto. O nome do projeto será dinamicamente inserido onde `{project_name}` estiver indicado.

        **Estrutura Obrigatória do `README.md` (Formato Markdown):**

        O `README.md` que você gerar DEVE, obrigatoriamente, conter as seguintes seções, nesta ordem e com esta formatação Markdown:

        ```markdown
        # {project_name}

        ## Descrição

        ## Funcionalidades Principais (Features)

        ## Tecnologias Utilizadas

        ## Primeiros Passos (Getting Started)

        ## Como Usar (How to Use)

        ## Licença
        """,
        description="Agent that proposes a Markdown-formatted README based on project context"
    )

    return call_agent(proposer, technical_explanation)
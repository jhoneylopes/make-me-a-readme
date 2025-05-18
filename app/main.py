import os
import json

from app.project_crawler import get_project_path
from app.project_crawler import read_project_files

# --- Funções dos Agentes de IA (Placeholders) ---

def agente_revisor_codigo(arquivos_projeto: dict[str, str]) -> dict:
    """
    Agente 1: Acessa e revisa a base de código.
    (Placeholder: Simula uma análise e retorna uma estrutura de dados)
    """
    print("\n🤖 Agente 1: Revisando a base de código...")
    if not arquivos_projeto:
        return {"sumario": "Nenhum código para revisar.", "arquivos_analisados": []}

    # Em um cenário real, aqui você enviaria 'arquivos_projeto' para um LLM
    # com um prompt para analisar o código.
    # Exemplo de prompt: "Analise os seguintes arquivos de código e forneça um resumo
    # das principais funcionalidades, tecnologias usadas e estrutura geral."

    sumario_analise = f"Análise simulada de {len(arquivos_projeto)} arquivo(s). "
    sumario_analise += "Principais tecnologias detectadas (simulado): Python, JavaScript. "
    sumario_analise += "Estrutura parece ser um aplicativo web com backend e frontend."

    # Simulação de uma saída mais estruturada que o LLM poderia retornar
    analise_simulada = {
        "sumario_geral": sumario_analise,
        "arquivos_analisados": list(arquivos_projeto.keys()),
        "tecnologias_identificadas": ["Python", "JavaScript", "Flask (simulado)"],
        "principais_modulos": {
            "app.py (simulado)": "Ponto de entrada principal, rotas da API.",
            "utils.js (simulado)": "Funções utilitárias para o frontend."
        },
        "pontos_chave": [
            "O projeto parece seguir uma arquitetura MVC (simulado).",
            "Há uso de funções assíncronas no código JavaScript (simulado)."
        ]
    }
    print("   Análise do Agente 1 concluída (simulada).")
    return analise_simulada

def agente_explicador_tecnico(analise_codigo: dict) -> str:
    """
    Agente 2: Explica tecnicamente o que está sendo feito.
    (Placeholder: Simula uma explicação baseada na análise)
    """
    print("\n🤖 Agente 2: Gerando explicação técnica...")
    if not analise_codigo or "sumario_geral" not in analise_codigo:
        return "Não foi possível gerar uma explicação técnica devido à falta de análise do código."

    # Em um cenário real, aqui você enviaria 'analise_codigo' (ou partes dela) para um LLM.
    # Exemplo de prompt: "Com base na seguinte análise de código: [dados da analise_codigo],
    # explique tecnicamente o que o projeto faz, seus principais componentes,
    # como eles interagem e quais algoritmos ou padrões de design são importantes."

    explicacao = f"**Explicação Técnica (Simulada)**\n\n"
    explicacao += f"{analise_codigo.get('sumario_geral', 'O projeto não pôde ser sumarizado.')}\n\n"
    explicacao += "**Componentes Principais (Simulado):**\n"
    for modulo, desc in analise_codigo.get('principais_modulos', {}).items():
        explicacao += f"- **{modulo}**: {desc}\n"
    
    explicacao += "\n**Tecnologias (Simulado):**\n"
    explicacao += ", ".join(analise_codigo.get('tecnologias_identificadas', ["N/A"])) + "\n"

    explicacao += "\n**Observações Adicionais (Simulado):**\n"
    for ponto in analise_codigo.get('pontos_chave', []):
        explicacao += f"- {ponto}\n"

    print("   Explicação técnica do Agente 2 gerada (simulada).")
    return explicacao

def agente_propositor_readme(explicacao_tecnica: str, nome_projeto: str = "Meu Projeto Incrível") -> str:
    """
    Agente 3: Propõe um README para o projeto.
    (Placeholder: Simula a criação de um rascunho de README)
    """
    print("\n🤖 Agente 3: Propondo estrutura do README...")
    if not explicacao_tecnica:
        return "# README\n\nNão foi possível gerar o conteúdo do README."

    # Em um cenário real, aqui você enviaria 'explicacao_tecnica' para um LLM.
    # Exemplo de prompt: "Com base na seguinte explicação técnica: [explicacao_tecnica],
    # gere um rascunho de README.md para um projeto chamado '{nome_projeto}'.
    # Inclua seções como: Descrição, Funcionalidades, Tecnologias Utilizadas,
    # Como Começar (Instalação, Configuração), Como Usar."

    readme_rascunho = f"# {nome_projeto}\n\n"
    readme_rascunho += "## Descrição (Gerado por IA - Simulado)\n"
    readme_rascunho += "Este projeto é uma aplicação X que faz Y, utilizando Z.\n"
    readme_rascunho += "A análise técnica indica o seguinte:\n"
    readme_rascunho += explicacao_tecnica.replace("**Explicação Técnica (Simulada)**\n\n", "") # Remove título redundante
    readme_rascunho += "\n## Funcionalidades (Simulado)\n"
    readme_rascunho += "- Funcionalidade A\n- Funcionalidade B\n- Funcionalidade C\n"
    readme_rascunho += "\n## Tecnologias Utilizadas (Simulado)\n"
    readme_rascunho += "- Python\n- JavaScript\n- Flask\n" # Exemplo, poderia vir da análise
    readme_rascunho += "\n## Como Começar (Simulado)\n"
    readme_rascunho += "### Pré-requisitos\n"
    readme_rascunho += "- Python 3.x\n- Node.js (se aplicável)\n"
    readme_rascunho += "### Instalação\n"
    readme_rascunho += "```bash\n"
    readme_rascunho += "git clone [https://exemplo.com/seu-projeto.git](https://exemplo.com/seu-projeto.git)\n"
    readme_rascunho += "cd seu-projeto\n"
    readme_rascunho += "pip install -r requirements.txt # Exemplo\n"
    readme_rascunho += "```\n"
    readme_rascunho += "\n## Como Usar (Simulado)\n"
    readme_rascunho += "Execute o comando:\n"
    readme_rascunho += "```bash\n"
    readme_rascunho += "python app.py # Exemplo\n"
    readme_rascunho += "```\n"

    print("   Rascunho do README proposto pelo Agente 3 (simulado).")
    return readme_rascunho

def agente_redator(rascunho_readme: str) -> str:
    """
    Agente 4: Redator que irá melhorar o texto do README.
    (Placeholder: Simula uma revisão e melhoria do texto)
    """
    print("\n🤖 Agente 4: Refinando o README (Redação)...")
    if not rascunho_readme:
        return "# README (Erro na Redação)\n\nTexto base para revisão não fornecido."

    # Em um cenário real, aqui você enviaria 'rascunho_readme' para um LLM.
    # Exemplo de prompt: "Revise e melhore o seguinte rascunho de README.md.
    # Torne-o mais claro, conciso, profissional e envolvente.
    # Corrija erros gramaticais e de estilo. Mantenha o formato Markdown."
    # Adicione uma introdução mais cativante e uma conclusão, se apropriado."

    readme_refinado = rascunho_readme # Simplesmente repassa por enquanto
    # Poderia adicionar:
    readme_refinado = readme_refinado.replace(
        "Este projeto é uma aplicação X que faz Y, utilizando Z.",
        "Este é um projeto inovador que visa solucionar o problema X através de uma abordagem Y, construído com as tecnologias Z. (Texto melhorado por IA - Simulado)"
    )
    readme_refinado += "\n## Contribuição (Simulado)\n"
    readme_refinado += "Contribuições são bem-vindas! Por favor, leia nossas diretrizes de contribuição (se houver) antes de enviar um pull request.\n"
    readme_refinado += "\n## Licença (Simulado)\n"
    readme_refinado += "Este projeto é licenciado sob a Licença MIT (Exemplo).\n"

    print("   README refinado pelo Agente 4 (simulado).")
    return readme_refinado

# --- Fluxo Principal ---
def main():
    """
    Função principal para orquestrar a geração do README.
    """
    print("🚀 Iniciando o Gerador de README com IA!")

    # 1. Obter caminho do projeto
    caminho_do_projeto = get_project_path()
    nome_base_projeto = os.path.basename(caminho_do_projeto) # Pega o nome da pasta como nome do projeto

    # 2. Agente 1: Ler e revisar a base de código
    arquivos_lidos = read_project_files(caminho_do_projeto)
    if not arquivos_lidos:
        print("\nNenhum arquivo relevante foi lido. Encerrando o processo.")
        return

    analise_do_codigo = agente_revisor_codigo(arquivos_lidos)
    # print("\n--- Saída Agente 1 (Análise do Código - Simulado) ---")
    # print(json.dumps(analise_do_codigo, indent=2, ensure_ascii=False)) # Para visualização

    # 3. Agente 2: Explicar tecnicamente
    explicacao_tecnica_gerada = agente_explicador_tecnico(analise_do_codigo)
    # print("\n--- Saída Agente 2 (Explicação Técnica - Simulado) ---")
    # print(explicacao_tecnica_gerada)

    # 4. Agente 3: Propor README
    readme_proposto = agente_propositor_readme(explicacao_tecnica_gerada, nome_projeto=nome_base_projeto)
    # print("\n--- Saída Agente 3 (Rascunho README - Simulado) ---")
    # print(readme_proposto)

    # 5. Agente 4: Redator para melhorar o texto
    readme_final = agente_redator(readme_proposto)
    print("\n--- ✅ README Final Gerado (Simulado) ---")
    print(readme_final)

    # 6. Salvar o README gerado
    caminho_readme_gerado = os.path.join(caminho_do_projeto, "README_gerado_ia.md")
    try:
        with open(caminho_readme_gerado, 'w', encoding='utf-8') as f:
            f.write(readme_final)
        print(f"\n💾 README salvo em: {caminho_readme_gerado}")
    except Exception as e:
        print(f"\n⚠️ Erro ao salvar o README: {e}")

    print("\n🎉 Processo concluído!")

if __name__ == "__main__":
    main()

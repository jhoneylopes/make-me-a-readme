import os

from app.project_crawler import get_project_path, read_project_files
from app.agents.agent_reviewer import agente_revisor_codigo
from app.agents.tech_explainer import tech_explainer
from app.agents.readme_proposer import readme_proposer
from app.agents.readme_refiner import readme_refiner

def main():
    """
    Função principal para orquestrar a geração do README com IA (simulado).
    """
    print("🚀 Iniciando o Gerador de README com IA!")

    # 1. Obter caminho do projeto
    caminho_do_projeto = get_project_path()
    nome_base_projeto = os.path.basename(caminho_do_projeto)

    # 2. Agente 1: Ler e revisar a base de código
    print("====== Agente 1: Ler e revisar a base de código ======")
    arquivos_lidos = read_project_files(caminho_do_projeto)
    if not arquivos_lidos:
        print("\nNenhum arquivo relevante foi lido. Encerrando o processo.")
        return        
    analise = agente_revisor_codigo(arquivos_lidos)
    print("Resumo da análise:\n", analise)
    print("\n")

    # 3. Agente 2: Explicar tecnicamente
    print("====== Agente 2: Explicar tecnicamente ======")
    explicacao_tecnica_gerada = tech_explainer(analise)
    print("Resumo da explicação técnica:\n", explicacao_tecnica_gerada)

    # # 4. Agente 3: Propor README
    print("====== Agente 3: Propor README ======")
    project_name = os.path.basename(caminho_do_projeto.rstrip("/"))
    readme_draft = readme_proposer(explicacao_tecnica_gerada, project_name=project_name)
    print("\nRascunho do README:\n", readme_draft)

    # # 5. Agente 4: Refinar README
    print("====== Agente 4: Refinar README ======")
    readme_final = readme_refiner(readme_draft)
    print("\n--- ✅ README Final Gerado ---\n")
    print(readme_final)    

    # 6. Salvar o README gerado
    print("====== Salvar o README gerado ======")
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
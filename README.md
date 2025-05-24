# make-me-a-readme

## Descrição

Este projeto automatiza a criação de arquivos README para projetos de software, utilizando inteligência artificial para analisar o código-fonte e gerar um ponto de partida para a documentação. O objetivo é economizar tempo, promover a consistência e melhorar a visibilidade dos projetos.

## Funcionalidades Principais

*   **Geração Automatizada de README:** Gera automaticamente um arquivo README básico com base no código do projeto.
*   **Análise Impulsionada por IA:** Utiliza agentes de IA para entender o código e criar documentação relevante.
*   **Pipeline Modular:** Emprega uma arquitetura de pipeline onde diferentes agentes de IA lidam com tarefas específicas no processo de criação do README.
*   **Agentes Configuráveis:** Permite a fácil modificação do comportamento dos agentes de IA através de arquivos de configuração.

## Tecnologias Utilizadas

*   **Python:** Linguagem de programação principal.
*   **Google AI (Gemini API) e Google AI Agent Development Kit (ADK):** Utilizados para integração de modelos de IA e desenvolvimento de agentes.
*   **`dotenv`:** Para gerenciar chaves de API e outras informações confidenciais.
*   **`unittest`:** Framework de testes integrado do Python.

## Primeiros Passos

1.  **Clone o repositório:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
2.  **Instale as dependências:** (Certifique-se de ter o Python e o pip instalados)
    ```bash
    pip install -r requirements.txt
    ```
    *Nota:* Pode ser necessário criar o arquivo `requirements.txt` listando todas as dependências do projeto.
3.  **Configure as chaves de API:** Configure as chaves de API necessárias (por exemplo, a chave da Google Gemini API) usando a biblioteca `dotenv`. Crie um arquivo `.env` no diretório raiz e adicione suas chaves:
    ```
    GOOGLE_API_KEY=your_api_key
    ```
4.  **Execute a aplicação:**
    ```bash
    python app/readme_generator.py
    ```
    O script solicitará que você especifique o diretório do projeto para o qual deseja gerar um README.

## Como Usar

1.  Execute o script `readme_generator.py`.
2.  Forneça o caminho para o diretório do projeto quando solicitado.
3.  O script executará o pipeline de IA, gerando um rascunho do arquivo README.
4.  Revise e refine o arquivo README gerado para garantir a precisão e a integridade das informações.

## Próximos Passos

*   **Implementar o Agente de Refinamento de README:** Desenvolver o Agente de Refinamento de README para aprimorar o rascunho inicial do README.
*   **Aprimorar o Tratamento de Erros:** Aprimorar o tratamento de erros em toda a aplicação para lidar com possíveis problemas, como erros de leitura de arquivos ou falhas em chamadas de API.
*   **Escrever Mais Testes:** Aumentar a cobertura de testes, com foco particular em testes unitários para componentes principais.
*   **Lidar com Arquivos Grandes de Forma Eficiente:** Abordar as limitações de tamanho de entrada, implementando métodos para lidar com arquivos maiores de forma mais eficiente.
*   **Gerenciar Limitações de Contexto:** Esteja atento às limitações de contexto do modelo de IA e explore estratégias para gerenciar a quantidade de informações fornecidas aos agentes de uma só vez.

## Licença

Este projeto está licenciado sob a licença MIT – consulte o arquivo LICENSE para obter detalhes.
from pathlib import Path
from app.readme_generator import main

def test_readme_generator_with_valid_mock(tmp_path, monkeypatch):
    # Criar estrutura de arquivos reais
    project_path = tmp_path / "project_alpha"
    project_path.mkdir()

    # Criar arquivos relevantes
    (project_path / "main.py").write_text("print('hello')")
    helpers_dir = project_path / "helpers"
    helpers_dir.mkdir()
    (helpers_dir / "utils.js").write_text("function test() {}")

    # Simular input() para retornar o caminho do projeto
    monkeypatch.setattr("builtins.input", lambda _: str(project_path))

    # Rodar a main()
    main()

    # Verificar se o README foi criado
    readme_path = project_path / "README_gerado_ia.md"
    assert readme_path.exists(), "README não foi gerado"
    content = readme_path.read_text()
    assert "Descrição" in content
    assert "Tecnologias" in content
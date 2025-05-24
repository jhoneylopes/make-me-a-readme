import os
import tempfile
from app.project_crawler import get_project_path, read_project_files
from app.agents.create_agent import create_agent

def generate_codebase_input(project_files: dict[str, str]) -> str:
    input_text = "### Project files:\n"
    for path, content in project_files.items():
        input_text += f"\n\n#### {path}\n```\n{content[:3000]}\n```"
    return input_text

def main():
    print("🚀 Starting AI README Generator!")

    # 1. Get project path
    project_path = get_project_path()
    project_basename = os.path.basename(project_path)

    # 2. Agent 1: Read and review the codebase
    print("====== Agent 1: Read and review the codebase ======")
    read_files = read_project_files(project_path)
    if not read_files:
        print("\nNo relevant files were read. Exiting process.")
        return

    input_text = generate_codebase_input(read_files)
    analysis = create_agent(
        name="code_reviewer_agent",
        model="gemini-2.0-flash",
        instruction_path="./instructions/reviewer.txt",
        textual_input=input_text,
        description="Agent that reviews the codebase and provides a technical overview"
    )
    print("Analysis summary:\n", analysis)
    print("\n")

    # 3. Agent 2: Technical explainer
    print("====== Agent 2: Technical explainer ======")
    technical_explanation = create_agent(
        name="tech_explainer_agent",
        model="gemini-2.0-flash",
        instruction_path="./instructions/explainer.txt",
        textual_input=analysis,
        description="Agent that explains the codebase in technical terms"
    )
    print("Technical explanation summary:\n", technical_explanation)

    
    # 4. Agent 3: Propose README
    print("====== Agent 3: Propose README ======")

    # Read and customize the instruction file
    with open("./instructions/readme_proposer.txt", encoding="utf-8") as f:
        instruction_content = f.read()

    # Replace the placeholder with the actual project name
    instruction_content = instruction_content.replace("{+project_name+}", project_basename).replace("{project_name}", project_basename)

    # Create a temporary file for the customized instruction
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode="w", encoding="utf-8") as temp_instruction_file:
        temp_instruction_file.write(instruction_content)
        temp_instruction_path = temp_instruction_file.name

    # Use the temp file path in create_agent (no need to pass context anymore)
    readme_draft = create_agent(
        name="readme_proposer_agent",
        model="gemini-2.0-flash",
        instruction_path=temp_instruction_path,
        textual_input=technical_explanation,
        description="Agent that drafts a README for the project"
    )

    # Clean up the temp file after use
    os.remove(temp_instruction_path)

    print("\nREADME draft:\n", readme_draft)

    # 5. Agent 4: Refine README
    print("====== Agent 4: Refine README ======")
    readme_final = create_agent(
        name="readme_refiner_agent",
        model="gemini-2.0-flash",
        instruction_path="./instructions/readme_refiner.txt",
        textual_input=readme_draft,
        description="Agent that refines the README draft"
    )
    print("\n--- ✅ Final README generated ---\n")
    print(readme_final)

    # 6. Save the generated README
    print("====== Saving generated README ======")
    readme_output_path = os.path.join(project_path, "README_generated_ai.md")
    try:
        with open(readme_output_path, 'w', encoding='utf-8') as f:
            f.write(readme_final)
        print(f"\n💾 README saved to: {readme_output_path}")
    except Exception as e:
        print(f"\n⚠️ Error while saving the README: {e}")

    print("\n🎉 Process completed!")


if __name__ == "__main__":
    main()
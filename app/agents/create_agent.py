from google.adk.agents import Agent
from app.agents.call_agent import call_agent

def create_agent(
    name: str,
    model: str,
    instruction_path: str,
    textual_input: str,
    description: str = "",
) -> str:
    """
    Generic function to run any agent based on instructions from a file.
    The input can be any text you want to provide to the agent.
    
    Args:
        name (str): Name of the agent.
        model (str): Model name to be used by the agent.
        instruction_path (str): Path to the instruction file (in English).
        textual_input (str): The input text to be processed by the agent.
        description (str, optional): Description of the agent.

    Returns:
        str: Agent's output or an error message if no input is provided.
    """
    if not textual_input:
        return "No input provided for the agent."

    # Load instruction from file
    with open(instruction_path, encoding="utf-8") as f:
        instruction = f.read()

    agent = Agent(
        name=name,
        model=model,
        instruction=instruction,
        description=description,
    )

    return call_agent(agent, textual_input)
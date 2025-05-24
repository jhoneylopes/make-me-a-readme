import os
import textwrap
import warnings
from datetime import date
from IPython.display import Markdown
from google import genai
from google.genai import types
from google.adk.agents import Agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

# Ignora warnings
warnings.filterwarnings("ignore")

# Configuração da API
client = genai.Client()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def call_agent(agent: Agent, message_text: str, context: dict = None) -> str:
    session_service = InMemorySessionService()
    session = session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    content = types.Content(role="user", parts=[types.Part(text=message_text)])

    final_response = ""
    run_args = {
        "user_id": "user1",
        "session_id": "session1",
        "new_message": content
    }
    if context is not None:
        run_args["context"] = context

    for event in runner.run(**run_args):
        if event.is_final_response():
            for part in event.content.parts:
                if part.text is not None:
                    final_response += part.text + "\n"
    return final_response

def to_markdown(text: str) -> Markdown:
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))

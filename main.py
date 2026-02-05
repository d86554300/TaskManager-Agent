import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from todoist_api_python.api import TodoistAPI


# Load .env file to be able to read the entries on it.
load_dotenv()
todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Init the todoist API
todoist = TodoistAPI(todoist_api_key)

@tool
def add_task(task, description=None):
    """
    Add a new task to the users task list. Use this when the user wants to add or create a task.
    """
    todoist.add_task(content=task,
                     description=description)

tools = [add_task]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=gemini_api_key, temperature=0.3
)

# Construct the prompt
system_prompt = "You are a helpful assistant. You will help the user add tasks."
user_input = "add task to buy some milk from a local shop with the description, the description was added by llm"

prompt_template = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("user", user_input),
        MessagesPlaceholder("agent_scratchpad")
    ]
)

agent = create_openai_tools_agent(llm, tools, prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
response = agent_executor.invoke({"input": user_input})

print(response["output"])
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
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

@tool
def show_tasks():
    """Show all tasks from todoist. Use this when the user wants to show all tasks."""
    all_tasks = todoist.get_tasks()
    tasks = []
    for task in all_tasks:
        tasks.append(task.content)
    
    return tasks

tools = [add_task, show_tasks]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=gemini_api_key,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    temperature=0.3
)

# Construct the prompt
system_prompt = """
    You are a helpful assistant. 
    You will help the user add tasks.
    You will help the user show existing tasks.
    """

prompt_template = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("user", "{input}"), # placeholder handled dynamically by lanchain,
        MessagesPlaceholder("agent_scratchpad"),
        MessagesPlaceholder("history")
    ]
)

agent = create_openai_tools_agent(llm, tools, prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

history = []
while True:
    user_input = input("What the task name you want to build? ")
    response = agent_executor.invoke({"input": user_input, "history": history})
    print(response["output"])
    history.append(HumanMessage(content=response["output"]))
    history.append(AIMessage(content=response["output"]))
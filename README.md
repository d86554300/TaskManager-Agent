# TaskManager-Agent

An intelligent AI Agent designed to streamline task management by integrating LLM capabilities with [Todoist](https://todoist.com/). This agent helps you automate the creation, organization, and tracking of your items using natural language.

## 🚀 Overview

TaskManager-Agent acts as a bridge between your personal productivity workflow and AI. Instead of manually sorting through tasks, you can interact with the agent to handle the heavy lifting of organizing your Todoist projects, labels, and deadlines.

## ✨ Features

* **AI-Powered Task Creation**: Generate tasks from natural language descriptions.
* **Todoist Integration**: Direct sync with your Todoist account via API.
* **Automated Management**: Efficiently categorize and prioritize items based on your preferences.
* **Python-Based**: Lightweight and easily extensible for custom workflows.

## 🛠️ Tech Stack

* **Language**: Python 3.x
* **API**: Todoist REST API
* **Intelligence**: Powered by LLM (OpenAI) for agentic decision-making.

## 📋 Prerequisites

Before running the agent, ensure you have:

1.  A **Todoist API Token** (Found in your Todoist Settings > Integrations > Developer).
2.  An **OpenAI API Key** (or your preferred LLM provider).
3.  Python installed (refer to `.python-version`).

## ⚙️ Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/d86554300/TaskManager-Agent.git](https://github.com/d86554300/TaskManager-Agent.git)
    cd TaskManager-Agent
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Variables**:
    Create a `.env` file in the root directory (you can use `.env_local` as a template) and add your credentials:
    ```env
    TODOIST_API_KEY=your_api_key_here
    OPENAI_API_KEY=your_openai_key_here
    ```

## 🚀 Usage

Run the main agent script to start managing your tasks:

```bash
python main.py

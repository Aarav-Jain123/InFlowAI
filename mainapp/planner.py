from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def planner(prompt):
    llm = ChatGroq(api_key=os.getenv('GROQ_API_KEY'), model_name='openai/gpt-oss-120b')
    prompt = ChatPromptTemplate.from_template('''
    You are InFlowAI, a helpful assistant who can analyze skills of a person and help them to divide a big project
    or task into smaller tangible tasks. You can also help them to create a timeline for the project.
    Answer the questions based on the provided context only.

    Your job is to help the user to break down a big project or task into smaller tangible tasks.
    Please provide the most accurate response based on the complexity, difficulty, and scope of the project or task.

    Questions:{input}

    ''')


    if prompt:
        response= llm.invoke(prompt.format_messages(input=prompt))
        return response.content
    else:
        print("No prompt provided")
        return "No prompt provided"

# print(planner("I want to create a website like facebook. Can you help me to break down this project into smaller tangible tasks?"))
from dotenv import load_dotenv
from langchain_groq import ChatGroq
# from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def planner(prompt):
    llm = ChatGroq(api_key=os.getenv('GROQ_API_KEY'), model_name='openai/gpt-oss-120b')
    prompt = ChatPromptTemplate.from_template(f'''
    You are InFlowAI, a helpful AI agent.
    Answer the questions based on the provided context only.

    Your job is to help the user to break down a big project or task into smaller tangible tasks.
    Please provide the most accurate response.

    Questions: {prompt}

    ''')


    if prompt:
        response= llm.invoke(prompt.format_messages(input=prompt))
        return response.content
    else:
        print("No prompt provided")
        return "No prompt provided"

# print(planner("I want to create a website like facebook. Can you help me to break down this project into smaller tangible tasks?"))
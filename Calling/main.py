from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import requests
load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""
    return a * b


llm = ChatGroq(model="openai/gpt-oss-20b")

llm_with_tools = llm.bind_tools([multiply]) # binding the tools with llm so that it can access these tools when needed

# print(llm_with_tools.invoke('Hi how are you!')) --> normal response

print(llm_with_tools.invoke('can you multiply 3 with 10').tool_calls[0])
# Output - {'name': 'multiply', 'args': {'a': 3, 'b': 10}, 'id': 'fc_97c23796-f45b-4677-b61f-4c74381ccf5a', 'type': 'tool_call'}

# The LLM doesn't actually run the tool - it just suggests the tool and the input arguments . The actual execution is handled by Langchain or you.
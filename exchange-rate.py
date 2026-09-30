from langchain_groq import ChatGroq
from langchain_core.tools import tool,InjectedToolArg
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import requests
import json
from typing import Annotated

load_dotenv()

@tool
def get_conversion_factor(base_currency:str,target_currency:str)->float:
    """
    This function fetches the current conversion factor between a given base currency and a target currency
    """
    url=f'https://v6.exchangerate-api.com/v6/e58a3805090f6132e7806fd3/pair/{base_currency}/{target_currency}'
    response = requests.get(url)
    return response.json()

@tool
def convert(base_currency_value:int,conversion_rate:Annotated[float,InjectedToolArg])->float:
    """
    given a currency conversion rate this function calculates the target currency value from a given base currency value
    """
    return base_currency_value*conversion_rate


# print(get_conversion_factor.invoke({'base_currency':'USD','target_currency':'INR'}))
# print(convert.invoke({'base_currency_value':10,'conversion_rate':96.0579}))
llm = ChatGroq(model="openai/gpt-oss-20b")

llm_with_tools = llm.bind_tools([get_conversion_factor,convert])

messages = [HumanMessage('What is the conversion factor between USD and INR , and based on that can you convert 10 usd to inr')]

ai_message=llm_with_tools.invoke(messages)

for tool_call in ai_message.tool_calls:
    if(tool_call['name']=='get_conversion_factor'):
        tool_message1 = get_conversion_factor.invoke(tool_call)
        conversion_rate = json.loads(tool_message1.content)['conversion_rate']
        messages.append(tool_message1)



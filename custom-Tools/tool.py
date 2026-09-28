from langchain_core.tools import tool
# steps to create a custom tool

# Step 1 - create a function
def multiply(a,b):
    """Multiply two numbers"""   #<-- it is recomended to provide a doc string here so that llm can understand what does this tool do 
    return a*b

# Step 2 - add type hints
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""   
    return a*b

# Step 2 - add tool decorator

@tool
def multiply(a:int,b:int)->int:
    """Multiply two numbers"""   
    return a*b


result = multiply.invoke({"a":3,"b":5}) # passing a dict here
print(result) # --> 15

print(multiply.name) #--> multiply
print(multiply.description) #--> Multiply two numbers
print(multiply.args) #--> {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}

# A tool always have these properties -> name ,description, args
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of Peru?"})
print(result)

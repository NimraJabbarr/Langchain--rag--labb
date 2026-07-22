from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage
chat_template=ChatPromptTemplate([

                    ("System","You are a helpful {domain} expert"),
                    ("Human","Explain in simple terms What is{topic}")
                     

])
prompt=chat_template.invoke({"domain":"cricket"},{"topic:""Consistency"})
print(prompt)
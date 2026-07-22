from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful customer"),
        MessagesPlaceholder(variable_name="chat_history"),  # ✅ spelling fixed
        ("human", "{query}")
    ]
)

chat_history = []

# load chat history
with open("chat_history.txt") as f:
    # ✅ flatten lines instead of nested list
    lines = f.readlines()
    chat_history.extend(lines)

# create prompt
prompt = chat_template.invoke({
    "chat_history": chat_history,
    "query": "Where is my refund"
})

print(prompt)

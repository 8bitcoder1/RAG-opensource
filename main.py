import chainlit as cl
from localrag import get_relevant_context, generate_response

@cl.on_message
def chat_interface(message):
    context = get_relevant_context(message.content)
    answer = generate_response(message.content, context)
    cl.Message(content=answer).send()

if __name__ == "__main__":
    cl.run()

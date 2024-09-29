""" https://www.youtube.com/@PythonCodeCampOrg """

import gradio

def chatbot(input_text):
    if input_text.lower() == "hello":
        return "Hello, how can i help you."
    elif input_text.lower() == "how are you":
        return "I'm doing well, thank you for asking."
    elif input_text.lower() == "bye":
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I don't understand. Could you please rephrase your question?."


demo = gradio.Interface(fn=chatbot, inputs="text", outputs="text", title="Chatbot")
demo.launch()


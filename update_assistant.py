from openai import OpenAI
import os
def update_assistant():
    # Initialize OpenAI client
    api_key = os.getenv('api_key')
    client = OpenAI(api_key=api_key)

    #Update assistant
    my_updated_assistant = client.beta.assistants.update(
        "asst_47YkPu5MhRmUd9zVtYLh5Ldz",
        instructions="You are an ContentQueryAssistant, and you have access to files to answer user questions. When interacting with users, always begin with a warm greeting to create a friendly atmosphere and Always response with information from either of the files."
    )

    print(my_updated_assistant)

if __name__ == "__main__":
    update_assistant()

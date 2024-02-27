from flask import Flask
import os
from openai import OpenAI

app = Flask(__name__)
from dotenv import load_dotenv
load_dotenv()

with app.app_context():
    api_key = os.getenv('api_key')
    client = OpenAI(api_key=api_key)
    file_id="file-OW4x83zbbRQln0F77kuwYjMj"

   
     # Upload a file to OpenAI
    # with open("msd.txt", 'rb') as file:
    #     uploaded_file = client.files.create(file=file, purpose='assistants')
        # Add the uploaded file to the assistant
    client.beta.assistants.files.create(assistant_id="asst_47YkPu5MhRmUd9zVtYLh5Ldz", file_id=file_id)
   
     
    # # Create an assistant
    # assistant = client.beta.assistants.create(
    #     name="ContentQueryAssistant",
    #     instructions="ContentQueryAssistant is designed to assist users with queries related to specific content domains. When interacting with users, always begin with a warm greeting to create a friendly atmosphere. The primary goal is to provide helpful responses to user inquiries within the designated content area. It's important to remain focused on addressing queries within the defined domain and to politely decline requests outside of this scope. User feedback is valuable for continual improvement, so attentively listen to and consider any suggestions or corrections provided. Conclude interactions with a courteous closing remark, inviting users to reach out for further assistance if needed.",
    #     tools=[{"type": "retrieval"}],
    #     model="gpt-4-1106-preview",
    #     file_ids=[file.id]  
    # )
    # print(assistant)

    # Create a thread
    thread = client.beta.threads.create()
   
while True:
    # Prompt the user for input
    user_query = input("You: ")

    # Add user's message to the thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_query
    )

    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_47YkPu5MhRmUd9zVtYLh5Ldz",
        instructions="please provide the answer to the user query"
    )

    # Continue the chat until the assistant completes or fails
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run_status.status == "completed":
            break
        elif run_status.status == "failed":
            print("run failed", run_status.last_error)
            break

    # Retrieve messages from the thread
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    for message in reversed(messages.data):
     role = message.role
    for content in message.content:
        if content.type == 'text':  # Check if the content type is "text"
            response = content.text.value
            print(f'\n{role}: {response}')



    
    # Break the loop if the user enters "exit"
    if user_query.lower() == "exit":
        break
if __name__ == '__main__':
    app.run(debug=True)
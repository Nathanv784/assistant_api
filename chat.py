from openai import OpenAI
import os
def start_chat():
    # Initialize OpenAI client
    api_key = os.getenv('api_key')
    client = OpenAI(api_key=api_key)

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
            assistant_id="asst_m0VkDhWQQ2x7SB08i5aYXCwv",
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
                if content.type == 'text':  
                    response = content.text.value
                    print(f'\n{role}: {response}')

if __name__ == "__main__":
    start_chat()

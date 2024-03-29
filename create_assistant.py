from openai import OpenAI
import os

def create_assistant():
    try:
        # Initialize OpenAI client
        api_key = os.getenv('api_key')
        client = OpenAI(api_key=api_key)

        # List of filenames to upload
        file_names = ["state_of_the_union.txt", "sachin.txt"]

        uploaded_file_ids = []

        # Loop through each file name and upload it to OpenAI
        for file_name in file_names:
            with open(file_name, 'rb') as file:
                uploaded_file = client.files.create(file=file, purpose='assistants')
                uploaded_file_ids.append(uploaded_file.id)

        # Create an assistant
        assistant = client.beta.assistants.create(
            name="ContentQueryAssistant",
            instructions="ContentQueryAssistant is designed to assist users with queries related to specific content domains. When interacting with users, always begin with a warm greeting to create a friendly atmosphere. The primary goal is to provide helpful responses to user inquiries within the designated content area. It's important to remain focused on addressing queries within the defined domain and to politely decline requests outside of this scope. User feedback is valuable for continual improvement, so attentively listen to and consider any suggestions or corrections provided. Conclude interactions with a courteous closing remark, inviting users to reach out for further assistance if needed.",
            tools=[{"type": "retrieval"}],
            model="gpt-4-1106-preview",
            file_ids=uploaded_file_ids
        )

        print(assistant)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    create_assistant()

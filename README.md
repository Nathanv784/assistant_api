#   Building a Chat Conversation using LangChain and OpenAI 



## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Download and install Python from [here](https://www.python.org/downloads/).

- **OpenAI API Key**: Create an OpenAI API Key from [here](https://openai.com/blog/openai-api).

## Getting Started

To get a local copy up and running, follow these simple steps:

1. **Clone the repository:**

    ```bash
    git clone [repository_url]
    ```

2. **Setting up Virtual Environment:**

    - **Install Virtual Environment:**

        For Linux/Mac:

        ```bash
        sudo apt install python3.8-venv
        ```

    - **Create a Virtual Environment:**

        For Linux/Mac:

        ```bash
        python3 -m venv envname
        ```

        For Windows:

        ```bash
        python -m venv envname
        ```

        Example:

        ```bash
        python3 -m venv env1
        ```

    - **Activate the Virtual Environment:**

        For Linux/Mac:

        ```bash
        source envname/bin/activate
        ```

        For Windows:

        ```bash
        .\envname\Scripts\activate
        ```

3.  **Install Dependencies:**

        ```bash
        pip install -r requirements.txt
        
4. **Create .env file:**

     -It is responsible for storing environment-specific configuration values, such as database credentials, API keys, and other sensitive data.

    ```bash
    touch sample.env
    ```

5. **Run the Application:**

    ```bash
    python3 app.py
    ```

6. **Deactivate the Virtual Environment:**

    ```bash
    deactivate
    ```
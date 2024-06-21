# Sample AI assistant

You need an `OPENAI_API_KEY` and a `GOOGLE_API_KEY` to run this code. Store them in a `.env` file in the root directory of the project, or set them as environment variables.

![image](https://github.com/olimiemma/alloy-voice-assistant-/assets/98601170/7607aeac-2c40-4049-a021-239e2aa70748)

![image](https://github.com/olimiemma/alloy-voice-assistant-/assets/98601170/e85b4703-ff26-4505-ac40-7c01c26fd247)


If you are running the code on Apple Silicon, run the following command:

```
$ brew install portaudio
```

Create a virtual environment, update pip, and install the required packages:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -U pip
$ pip install -r requirements.txt
```

Run the assistant:

```
$ python3 assistant.py
```

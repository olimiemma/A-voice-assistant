# AI assistant
# I've added and edited alot from Santiago's original code,so go to his git for the original code.
# You might need to install a few things so get ready for that. But I tried this myself, it runs.

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
To run the provided Python script and use the assistant, follow these steps:

1. Install the required dependencies by running the following command in your terminal or command prompt:

   ```
   pip install opencv-python openai python-dotenv langchain langchain-community langchain-openai langchain-google-genai pyaudio SpeechRecognition
   ```

2. Set up your API credentials:
   - Create a `.env` file in the same directory as the script.
   - Add your OpenAI API key to the `.env` file like this: `OPENAI_API_KEY=your_api_key_here`
   - If you're using Google's Gemini Flash model, add your Google API key to the `.env` file like this: `GOOGLE_API_KEY=your_api_key_here`

3. Make sure you have a webcam connected to your computer.

4. Run the script by executing the following command in your terminal or command prompt:

   ```
   python assistant.py
   ```

5. The script will start the webcam stream and display it in a window titled "webcam".

6. Speak your prompt or question clearly into the microphone. The assistant will process your audio using speech recognition.

7. The assistant will analyze the audio prompt and the current webcam frame to generate a response.

8. The generated response will be displayed in the console and also played back as audio using text-to-speech.

9. You can continue asking questions or providing prompts, and the assistant will respond accordingly.

10. To stop the program, press the 'q' key or the 'Esc' key while the webcam window is active.

Note: The script uses Whisper for speech recognition and OpenAI's API for text-to-speech. Make sure you have a stable internet connection and valid API credentials for these services to work properly.

Also, the script is set up to use Google's Gemini Flash model by default. If you want to use OpenAI's GPT-4o model instead, uncomment the line `# model = ChatOpenAI(model="gpt-4o")` and comment out the line `model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")`.





# Running the Assistant

To run the provided Python script and use the assistant, follow these steps:

1. Install the required dependencies by running the following command in your terminal or command prompt:

   ```
   pip install opencv-python openai python-dotenv langchain langchain-community langchain-openai langchain-google-genai pyaudio SpeechRecognition
   ```

2. Set up your API credentials:
   - Create a `.env` file in the same directory as the script.
   - Add your OpenAI API key to the `.env` file like this: `OPENAI_API_KEY=your_api_key_here`
   - If you're using Google's Gemini Flash model, add your Google API key to the `.env` file like this: `GOOGLE_API_KEY=your_api_key_here`

3. Make sure you have a webcam connected to your computer.

4. Run the script by executing the following command in your terminal or command prompt:

   ```
   python assistant.py
   ```

5. The script will start the webcam stream and display it in a window titled "webcam".

6. Speak your prompt or question clearly into the microphone. The assistant will process your audio using speech recognition.

7. The assistant will analyze the audio prompt and the current webcam frame to generate a response.

8. The generated response will be displayed in the console and also played back as audio using text-to-speech.

9. You can continue asking questions or providing prompts, and the assistant will respond accordingly.

10. To stop the program, press the 'q' key or the 'Esc' key while the webcam window is active.

Note: The script uses Whisper for speech recognition and OpenAI's API for text-to-speech. Make sure you have a stable internet connection and valid API credentials for these services to work properly.

Also, the script is set up to use Google's Gemini Flash model by default. If you want to use OpenAI's GPT-4o model instead, uncomment the line `# model = ChatOpenAI(model="gpt-4o")` and comment out the line `model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")`.


https://www.linkedin.com/in/olimiemma/

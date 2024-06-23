import base64
from threading import Lock, Thread
import os

import cv2
import openai
from cv2 import VideoCapture, imencode
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema.messages import SystemMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from pyaudio import PyAudio, paInt16
from speech_recognition import Microphone, Recognizer, UnknownValueError

load_dotenv()


class WebcamStream:
    # ... (WebcamStream class remains unchanged)


class Assistant:
    def __init__(self, model_name):
        self.chain = self._create_inference_chain(model_name)

    def answer(self, prompt, image):
        if not prompt:
            return

        print("Prompt:", prompt)

        response = self.chain.invoke(
            {"prompt": prompt, "image_base64": image.decode()},
            config={"configurable": {"session_id": "unused"}},
        ).strip()

        print("Response:", response)

        if response:
            self._tts(response)

    def _tts(self, response):
        player = PyAudio().open(format=paInt16, channels=1, rate=24000, output=True)

        with openai.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice="alloy",
            response_format="pcm",
            input=response,
        ) as stream:
            for chunk in stream.iter_bytes(chunk_size=1024):
                player.write(chunk)

    def _create_inference_chain(self, model_name):
        SYSTEM_PROMPT = """
        You are a witty assistant that will use the chat history and the image 
        provided by the user to answer its questions.

        Use few words on your answers. Go straight to the point. Do not use any
        emoticons or emojis. Do not ask the user any questions.

        Be friendly and helpful. Show some personality. Do not be too formal.
        """

        prompt_template = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=SYSTEM_PROMPT),
                MessagesPlaceholder(variable_name="chat_history"),
                (
                    "human",
                    [
                        {"type": "text", "text": "{prompt}"},
                        {
                            "type": "image_url",
                            "image_url": "data:image/jpeg;base64,{image_base64}",
                        },
                    ],
                ),
            ]
        )

        if model_name == "gemini":
            model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")
        elif model_name == "gpt4v":
            model = ChatOpenAI(model="gpt-4-vision-preview")
        elif model_name == "claude":
            model = ChatAnthropic(model="claude-3-opus-20240229")
        else:
            raise ValueError(f"Unsupported model: {model_name}")

        chain = prompt_template | model | StrOutputParser()

        chat_message_history = ChatMessageHistory()
        return RunnableWithMessageHistory(
            chain,
            lambda _: chat_message_history,
            input_messages_key="prompt",
            history_messages_key="chat_history",
        )


def main():
    webcam_stream = WebcamStream().start()

    # Choose the model to use
    model_name = os.getenv("MODEL_NAME", "gemini")  # Default to Gemini if not specified
    assistant = Assistant(model_name)

    def audio_callback(recognizer, audio):
        try:
            prompt = recognizer.recognize_whisper(audio, model="base", language="english")
            assistant.answer(prompt, webcam_stream.read(encode=True))

        except UnknownValueError:
            print("There was an error processing the audio.")

    recognizer = Recognizer()
    microphone = Microphone()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)

    stop_listening = recognizer.listen_in_background(microphone, audio_callback)

    try:
        while True:
            cv2.imshow("webcam", webcam_stream.read())
            if cv2.waitKey(1) in [27, ord("q")]:
                break
    finally:
        webcam_stream.stop()
        cv2.destroyAllWindows()
        stop_listening(wait_for_stop=False)


if __name__ == "__main__":
    main()

# Voice-to-Voice Assistant Components
This repository contains elements that can be integrated as a voice-to-voice assistant.

The functions are redundant to an extent.

Livekit Cloud and Open-AI Realtime both allow voice to voice. Livekit can be run locally, but i'm not sure if the GUI is avalible for local use. We will see.

Pointer is a querey function, which allows models to determine the appropriate resource to access based on the user querey.

Streamlit is just a basic script to generate a streamlit app, which may not be the best endpoint. I just included it here because it has proved helpful in the past. 

## LiveKit Cloud Voice Assistant
LiveKit offers backend support for Large Language Model (LLM) interactions. Its main function is a voice chat interface, which can be accessed at https://agents-playground.livekit.io/

Workflow: Converts voice input to text, processes it through an LLM, and then converts the response back to speech.
Latency: While there is noticeable latency, integrating the OpenAI Realtime API can mitigate this issue.
Monitoring: Features an open-source console for auditing conversations, ensuring quality and appropriateness—ideal for personal LLMs where unsupervised user monitoring is crucial.
To run the application:

create an account at https://agents-playground.livekit.io/

create a playground, get the url, api, and secret

put them in your .env

cd VoiceAssistant

python Talk.py start



## Pointer
Pointer enforces selection among predefined options.

Functionality: Utilizes a Weaviate database containing a list of databases, descriptive paragraphs, and few-shot examples to guide selection.
Purpose: Enables querying across multiple databases with differing data headers, preserving the integrity and format of publicly available datasets.
Use Case: For instance, when a user in Sacramento seeks shelter, Pointer directs the query to the appropriate database containing social service information.


## OpenAI-Realtime-py
This module is a cloned GitHub repository implementing OpenAI Realtime.

It should work out of the box, in console. I use Pycharm, but anything should be fine

Interface: Operates via the console without requiring a graphical user interface, making it suitable for deployments without a display.
Logging: Integration of logging functionality is recommended.

## Streamlit Deploy

I dont know if this will be needed in this project, but it is a quick way to spin up an app to test functionality. The livekit cloud console is very good.
Integration: Compatible with the LiveKit script, enhancing its utility.
A straightforward deployment script for Streamlit applications.

Future development should incorporate audio i/o.

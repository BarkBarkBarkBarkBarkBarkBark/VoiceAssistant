This package contains several elements that can eventually be combined into a voice to voice assistant. The elements are as follows

########Pointer########

Pointer forces a choice among pre-specified options.

A weaviate database contains a list of databases, a paragraph description, and few shot examples to guide selection.

The purpose is to enable queries of many different databases, where the data headers don't match and cannot be combined. This example uses databases containing information about social services in sacramento. A user requests assistance with something, for example they are seeking shelter, and pointer directs the query to the appropriate database. This allows us to preserve the integrity and format of publicly available databases.


#######Livekit Cloud Voice Assistant#######

Livekit provides backend support for LLM calls. This instance uses a voice to text to LLM, and then a text to speech to user format. There is a noticeable latency, but it is possible to use the OpenAI realtime api to reduce the latency. This is an excellent option for a single user, as there is a bundled and open source console. This can be used to audit conversations for quality and appropriateness. 

I think it will be an excellent tool for personal LLMs, where monitoring is important where the user is unsupervised.


To run the application, run from the terminal.
    cd VoiceAssistant
    python Talk.py start

#######OpenAI-Realtime-py#######

This is a cloned GitHub repo instantiating OpenAI Realtime. It works in console, without the need for any UI, so this will be excellent for any deployment where a screen is not necessary. Logging will need to be implemented. Best yet, this script will work when integrated into the Livekit script.

#######Streamlit Deploy#######

This is simple deploy script for streamlit. It would be good to get it to work with audio i/o




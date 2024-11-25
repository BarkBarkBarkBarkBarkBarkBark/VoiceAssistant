import asyncio
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.multimodal import MultimodalAgent
from livekit.plugins import openai

load_dotenv()  # Load environment variables (e.g., OpenAI API key)

# Define AssistantFnc to add AI callable functions
class AssistantFnc:
    async def get_weather(self, location: str) -> str:
        """Retrieve the current weather for a given location."""
        # Simulated weather response
        return f"The weather in {location} is sunny and 75°F."

async def entrypoint(ctx: JobContext):
    # Initial system prompt for the assistant
    system_prompt = (
        "You are a voice assistant created by LiveKit using OpenAI Realtime API. "
        "Your responses should be short and clear, suitable for a spoken interaction. "
        "Avoid complex punctuation or overly detailed responses."
    )

    # Initialize the MultimodalAgent with OpenAI Realtime API
    assistant = MultimodalAgent(
        openai_realtime=openai.RealtimeAPI(),  # Connect to OpenAI Realtime API
        system_prompt=system_prompt,          # Set the assistant's behavior
        ai_functions=AssistantFnc()           # Add AI callable functions
    )

    await ctx.connect()  # Connect to the room
    assistant.start(ctx.room)  # Start the assistant in the room

    # Initial greeting
    await assistant.say("Hey, how can I help you today!", allow_interruptions=True)

    # Keep the agent running
    await asyncio.Event().wait()

if __name__ == "__main__":
    # Run the LiveKit application
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))

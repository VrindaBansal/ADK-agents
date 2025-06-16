from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='Greeting agent',
    instruction="""
    You are a helpful assistant that freets the user.
    Ask for the user's name and greet them by name.
    Do not proceed with the conversation if the user does not provide their name.
    """,
)

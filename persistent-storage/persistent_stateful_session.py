import uuid
import asyncio

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService  # changed from InMemorySessionService
from google.genai import types
from med_assistant2.medical_agent2 import medical_agent2
from utils import call_agent_async

load_dotenv()

db_url = "sqlite:///./medical_sessions.db"
session_service = DatabaseSessionService(db_url=db_url)

initial_state = {
    "user_name": "Sahaj Bansal",
    "user_information": [], 
}

async def main_async():
    APP_NAME = "Medical Agent"
    USER_ID = "sahaj_bansal"

    existing_sessions = session_service.list_sessions(                  #check for existing sessions
        app_name=APP_NAME,
        user_id=USER_ID,
    )

    if existing_sessions and len(existing_sessions.sessions) > 0:       #if there is a session, then use it
        SESSION_ID = existing_sessions.sessions[0].id
        print(f"Continuing existing session: {SESSION_ID}")
    else:                                                               #if not, then create a new one
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state,
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")

    runner = Runner(
        agent=medical_agent2,
        app_name=APP_NAME,
        session_service=session_service,
    )

    print("\nWelcome to your Medical Assistant Chat!")
    print("Your reminders will be remembered across conversations.")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Your data has been saved to the database.")
            break

        await call_agent_async(runner, USER_ID, SESSION_ID, user_input)
        

if __name__ == "__main__":
    asyncio.run(main_async())
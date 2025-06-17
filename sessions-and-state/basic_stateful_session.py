import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService  # changed from InMemorySessionService
from google.genai import types
from med_assistant.medical_agent import medical_agent

load_dotenv()

session_service_stateful = DatabaseSessionService(db_url="sqlite:///./medical_sessions.db")

initial_state = {
    "user_name": "Sahaj Bansal",
    "user_information": """
        I am a 12 year old boy.
        I live a mildly active lifestyle. 
        I don't eat too many vegetables but I prefer to eat fruits.
        I sometimes worry about my skin as it gets dry sometimes. 
        My family has a history of diabetes and heart diseases. 
        I have a sweet tooth and I love to eat ice cream.
        I play a lot of video games.
        I am a big fan of the sport of badminton.
    """, 
}

APP_NAME = "Medical Assistant"
USER_ID = "sahaj_bansal"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)

print("CREATED NEW SESSION:")
print(f"\tSession ID: {SESSION_ID}")

runner = Runner(
    agent=medical_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

new_message = types.Content(
    role="user", parts=[types.Part(text="How can Sahaj proactively take care of his health?")]
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final Response: {event.content.parts[0].text}")

print("==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
)

# Log final Session state
print("=== Final Session State ===")
for key, value in session.state.items():
    print(f"{key}: {value}")

print("Session saved to database: medical_sessions.db")
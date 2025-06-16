from google.adk.agents import Agent
from pydantic import BaseModel, Field
from typing import List

class exercise(BaseModel): # for a single exercise in the workout plan
    exercise_name: str = Field(description="The name of the exercise (e.g., 'Push-ups', 'Squats')")
    sets: int = Field(description="The number of sets for the exercise")
    reps: str = Field(description="The number of reps for the exercise (can be a range like '8-12' or specific number)")
    weight: str = Field(description="The weight for the exercise (e.g., 'bodyweight', '20 lbs', '15 kg')")
    rest_time: str = Field(description="The rest time between sets (e.g., '60 seconds', '2 minutes')")

class workout_plan(BaseModel): # the total workout plan using the excercises above
    workout_name: str = Field(description="Name of the workout (e.g., 'Upper Body Strength', 'Beginner Full Body')")
    duration: str = Field(description="Estimated total workout time (e.g., '45 minutes', '1 hour')")
    difficulty: str = Field(description="Difficulty level (Beginner, Intermediate, Advanced)")
    exercises: List[exercise] = Field(description="List of exercises in the workout plan")
    
root_agent = Agent(
    model='gemini-2.0-flash-001',
    name='root_agent',
    description='A workout planner agent to plan your personal workout plan',
    instruction="""
        You are a Professional Fitness Trainer and Workout Planning Assistant.
        Your task is to create a personalized workout plan based on the user's fitness goals, experience level, and preferences. Ask the users for their fitness goals, experience level, and preferences. Get as much information as possible about the user's fitness goals, experience level, and preferences and then create a personalized workout plan based on the user's fitness goals, experience level, and preferences. Be professional and friendly.
        
        GUIDELINES:
        - Ask about their fitness level (beginner/intermediate/advanced)
        - Consider their goals (strength, cardio, weight loss, muscle building)
        - Include 4-8 exercises per workout
        - Provide appropriate sets, reps, and rest times for their level
        - Include both compound and isolation exercises when appropriate
        - For beginners: focus on bodyweight and light weights
        - For advanced: can include heavier weights and complex movements
        - Always prioritize proper form over heavy weight
        
        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "workout_name": "Name of the workout",
            "duration": "Estimated time",
            "difficulty": "Beginner/Intermediate/Advanced",
            "exercises": [
                {
                    "exercise_name": "Exercise name",
                    "sets": 3,
                    "reps": "8-12",
                    "weight": "bodyweight or specific weight",
                    "rest_time": "60 seconds"
                }
            ],
        }
        
        DO NOT include any explanations or additional text outside the JSON response.
    """,
    output_schema=workout_plan,
    output_key="workout",
)

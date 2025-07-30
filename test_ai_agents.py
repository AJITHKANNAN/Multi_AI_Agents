# test_ai_agent.py

from app.core.ai_agent import get_response_from_ai_agents

if __name__ == "__main__":
    llm_id = "llama3-8b-8192"  # Or llama3-70b-8192, mixtral-8x7b-32768, etc.
    query = [
        {"role": "user", "content": "What is the capital of France?"}
    ]
    allow_search = False
    system_prompt = None  # or a function if you are modifying system behavior

    response = get_response_from_ai_agents(llm_id, query, allow_search, system_prompt)
    
    print("AI Response:", response)

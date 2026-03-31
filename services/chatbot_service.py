# services/chatbot_service.py

from rag.chain import build_rag_chain

rag_chain = build_rag_chain()

# Store history in memory: { session_id: [messages] }
sessions = {}

def format_history(messages):
    formatted = ""
    for msg in messages:
        role = msg["role"].upper()
        content = msg["content"]
        formatted += f"{role}: {content}\n"
    return formatted

def ask_question(question: str, session_id: str = "default"):
    if session_id not in sessions:
        sessions[session_id] = []
    
    history_str = format_history(sessions[session_id])
    try:
        # response is now a ChatResponse object
        resp_obj = rag_chain.invoke({
            "question": question,
            "chat_history": history_str
        })
    except Exception as e:
        print(f"Error during chain invocation: {e}")
        # Fallback to a default response if the LLM/parser fails completely
        resp_obj = {
            "message": "I'm sorry, I'm having trouble processing that right now. Could you rephrase your question?",
            "product_list": []
        }
    # Convert Pydantic object to dictionary
    if hasattr(resp_obj, 'model_dump'):
        resp_dict = resp_obj.model_dump()
    elif hasattr(resp_obj, 'dict'):
        resp_dict = resp_obj.dict()
    else:
        # Fallback if it's already a dict or something else
        resp_dict = resp_obj

    # Save to history
    sessions[session_id].append({"role": "user", "content": question})
    sessions[session_id].append({"role": "bot", "content": resp_dict.get("message", "")})
    
    # Limit history
    if len(sessions[session_id]) > 10:
        sessions[session_id] = sessions[session_id][-10:]
        
    return resp_dict

def clear_session(session_id: str):
    if session_id in sessions:
        del sessions[session_id]

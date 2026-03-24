import requests
url = "http://127.0.0.1:5000/chat"
payload = {
    "message": "We often receive a high volume of applications, but many are not relevant to our requirements. Interview coordination also takes too much time. How can your solution help us solve these hiring challenges?",
    "session_id": "debug_session"
}
response = requests.post(url, json=payload)
print(response.json())




'''
curl -X POST http://127.0.0.1:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "What is SmartScore?", "session_id": "test_user_123"}'


     '''
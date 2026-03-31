import requests
url = "https://consultant-api-dev.cadient.ai/chat"
payload = {
    "message": "I'm preparing a personalized landing page for In-N-Out Burger. Recommended product: smart-tenure.md. Their top hiring problems: Catastrophic Employee Retention Crisis; Massive Candidate Experience Failure and Drop-offs; Zero Assessment Usage Creating Quality-of-Hire Problems. Recommended angle: \"We helped you process 17.5 million applicants before, but the 87% turnover and 1.6M+ candidate dropoffs showed there were gaps in the foundation. Our predictive retention technology has evolved significantly since 2022 - we can now predict which candidates will stay beyond 90 days before you make the offer. Given your massive hiring volumes, even small improvements in retention and candidate experience could save millions in costs. Worth exploring what's changed in our platform since you left?\". Please provide the most compelling value propositions, key capabilities, and outcome-focused language to highlight for this company specifically.",
    "session_id": "debug_angle_test_001"
}
response = requests.post(url, json=payload)
print(response.json())




'''
curl -X POST https://consultant-api-dev.cadient.ai/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "What is SmartScore?", "session_id": "test_user_123"}'


     '''
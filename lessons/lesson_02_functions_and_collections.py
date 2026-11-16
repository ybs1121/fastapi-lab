def make_answer(question: str, topic: str = "general") -> str:
    return f"[{topic}] {question}"


requests = [
    {"question": "FastAPI가 뭐야?", "topic": "python"},
    {"question": "이벤트 루프가 뭐야?"},
]

for request in requests:
    question = request["question"]
    if "topic" in request:
        print(make_answer(question, topic=request["topic"]))
    else:
        print(make_answer(question))

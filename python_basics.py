requests = [
    {"question": "FastAPI가 뭐야?", "topic": "python"},
    {"question": "이벤트 루프가 뭐야?"},
]


def make_answer(request: dict[str, str]) -> str:
    question = request["question"]
    topic = request.get("topic", "general")
    return f"[{topic}] {question}"


for request in requests:
    print(make_answer(request))




class AssistRequest:
    def __init__(self, question: str, topic: str | None = None):
        self.question = question
        self.topic = topic

    def describe(self) -> str:
        topic = self.topic if self.topic is not None else "general"
        return f"[{topic}] {self.question}"


first = AssistRequest("FastAPI가 뭐야?", topic="python")
second = AssistRequest("이벤트 루프가 뭐야?")

print(first.question)
print(first.describe())
print(second.describe())
class AssistRequest:
    def __init__(self, question: str, topic: str | None = None):
        self.question = question
        self.topic = topic

    def describe(self) -> str:
        topic = self.topic if self.topic is not None else "general"
        return f"[{topic}] {self.question}"

    def set_topic(self, topic: str):
        self.topic = topic


first = AssistRequest("FastAPI가 뭐야?", topic="python")
second = AssistRequest("이벤트 루프가 뭐야?")


print(first.describe())
print(second.describe())

second.set_topic("python")
print(first.describe())
print(second.describe())
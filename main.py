import asyncio
from time import perf_counter

import time

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()



class AssistRequest(BaseModel):
    question: str = Field(min_length=1)
    topic: str | None = None


@app.post("/assist")
def assist(request: AssistRequest) -> dict[str, str | None]:
    print("assist 함수에 들어옴")
    return {
        "answer": f"받은 질문: {request.question}",
        "topic": request.topic,
    }



async def fetch_context() -> str:
    await asyncio.sleep(1)
    return "DB 조회 완료"


async def call_llm() -> str:
    await asyncio.sleep(2)
    return "LLM 응답 완료"


@app.get("/async-demo")
async def async_demo(concurrent: bool = False):
    started_at = perf_counter()

    if concurrent:
        context, answer = await asyncio.gather(fetch_context(), call_llm())
    else:
        context = await fetch_context()
        answer = await call_llm()

    return {
        "context": context,
        "answer": answer,
        "elapsed_seconds": round(perf_counter() - started_at, 2),
    }



@app.get("/wait-demo")
async def wait_demo(blocking: bool = False):
    if blocking:
        time.sleep(8)
    else:
        await asyncio.sleep(8)

    return {"done": True}


@app.get("/ping")
async def ping():
    return {"pong": True}
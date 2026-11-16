from time import perf_counter  # 표준 라이브러리

from pydantic import BaseModel  # 외부 패키지: 프로젝트의 .venv에 설치돼 있어야 해


print(f"표준 라이브러리에서 가져온 함수: {perf_counter.__name__}")
print(f"외부 패키지에서 가져온 클래스: {BaseModel.__name__}")

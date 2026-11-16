# Python / FastAPI 실습 기록

목표는 이 프로젝트의 코드를 읽고 작은 변경을 할 수 있는 거야. 값이 어디서 오고, 어떤 코드가 실행되고, 결과가 어떻게 달라지는지 설명할 수 있으면 다음으로 넘어가.

한 번에 한 개념을 봐. 실제 코드에 나온 문법은 짧은 예제와 Java/Spring 비교로 풀어보고, 그중 핵심 몇 줄을 직접 작성해. 실행하기 전에 결과를 예상하고, 실행한 뒤에는 예상과 맞았는지 확인해. 내부 구현은 현재 코드를 이해하거나 고치는 데 필요할 때 살펴봐. 기록에는 실행해 본 것과 직접 작성한 것을 구분해서 남겨.

## 다음 실습

FastAPI 3교시는 `Depends`부터 시작해. 요청을 처리할 때 FastAPI가 어떤 함수를 호출하고, 그 반환값이 엔드포인트의 어느 인자로 들어가는지 확인해.

## 2026-11-16까지 한 것

| 주제 | 확인한 내용 | 직접 작성 |
| --- | --- | --- |
| FastAPI 1교시 | `POST /assist`, Pydantic 검증, 200과 422, 필드 생략과 `null`을 실습했어. | |
| FastAPI 2교시 | 순차 `await`와 `gather`의 시간 차이, `asyncio.sleep()`과 `time.sleep()`이 `/ping`에 주는 영향을 실습했어. | |
| [import](lesson_01_imports.py), [함수와 컬렉션](lesson_02_functions_and_collections.py) | 기초 문법을 훑었고, 딕셔너리에서 키로 값을 꺼내는 코드가 익숙하다고 확인했어. | |
| [class와 self](lesson_03_class.py) | 변경 전후를 출력해 `second`의 표시가 `[general]`에서 `[python]`으로 바뀌고 `first`는 그대로인 걸 확인했어. | `set_topic` 정의와 `second.set_topic("python")` 호출 완료 |
| [with](lesson_04_with.py) | 블록 밖에서도 `stream`을 참조할 수 있고, 닫힌 스트림에서 `read()`를 호출하면 `ValueError`가 나는 걸 확인했어. | 읽는 줄을 블록 밖으로 옮겨 실행 완료 |
| [async with](lesson_05_async_with.py) | 정상일 때는 빌리기 → 조회 → 반납 순서야. 블록 안에서 예외가 나면 반납을 마친 뒤 예외가 블록 밖으로 전파돼. | 조회하는 줄을 `raise RuntimeError("조회 실패")`로 바꿔 반납이 실행되는 걸 확인했어. |

FastAPI 3교시는 `Depends` → 요청 컨텍스트 → asyncpg 연결 빌리기와 반납 → 트랜잭션 순서로 진행하고, 이후 SSE와 테스트로 이어가.

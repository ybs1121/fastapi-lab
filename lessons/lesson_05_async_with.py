import asyncio


class DemoConnection:
    # 실제 DB 없이 비동기로 빌리고 돌려주는 흐름을 흉내 내.
    async def __aenter__(self):
        await asyncio.sleep(0.3)
        print("커넥션을 빌렸어")
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await asyncio.sleep(0.3)
        print("커넥션을 돌려줬어")

    async def fetch(self) -> str:
        await asyncio.sleep(0.3)
        return "조회 결과"


async def main() -> None:
    async with DemoConnection() as connection:
        print(await connection.fetch())

    print("블록을 나왔어")


asyncio.run(main())

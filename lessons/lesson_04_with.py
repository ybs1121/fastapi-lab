from io import StringIO


# 디스크에 파일을 만들지 않고 닫히는 동작을 볼 수 있어.
with StringIO("FastAPI 실습") as stream:
    print(f"읽은 값: {stream.read()}")
    print(f"블록 안에서 닫혔나? {stream.closed}")

print(f"블록 밖에서 닫혔나? {stream.closed}")

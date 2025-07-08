from fastapi import FastAPI


app = FastAPI(
    title="openbudget",
)


@app.get("/")
async def hello():
    return "hello"

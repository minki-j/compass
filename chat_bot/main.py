from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
a = {}


def template_response(text):
    return JSONResponse(
        {
            "version": "2.0",
            "template": {"outputs": [{"simpleText": {"text": text}}]},
        }
    )


@app.get("/")
async def root():
    print("root route called")
    return template_response("Hello World")


@app.post("/")
async def post(data: dict):
    print("data", data)
    return template_response("Return Messages")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)

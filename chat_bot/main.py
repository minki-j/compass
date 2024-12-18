from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import json

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



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)

import uvicorn
from fastapi import FastAPI
import gradio as gr


def echo(message, history):
    return message


model_match_io = gr.ChatInterface(fn=echo, examples=["hello", "hola", "merhaba"], title="Echo Bot")

app_conf = [
    {
        "name": "model",
        "io": model_match_io,
        "description": "知我AI模型测试工具",
    }
]
app = FastAPI()


@app.get("/")
def read_tools():
    return {
        'message': 'server is running'
    }


@app.get("/tools")
def read_tools():
    return {
        "tools": [{
            "name": i["name"],
            "description": i["description"],
            "path": "/tools/" + i["name"],
        } for i in app_conf]
    }


if __name__ == '__main__':
    for i in app_conf:
        app = gr.mount_gradio_app(app, i["io"], path=f"/tools/{i['name']}")

    uvicorn.run(app, host="0.0.0.0", port=7860)

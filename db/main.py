from pymongo import MongoClient
import gradio as gr
import pandas as pd

client = MongoClient(
    host='10.0.0.142',
    port=27017,
)

db = client['test']
collection = db['test']

main_io = gr.Blocks()


def get_data():
    res = [{
        "id": str(i.get("_id")),
        "name": i.get("name"),
        "age": i.get("age"),
        "sex": i.get("sex")
    } for i in list(collection.find())]
    return pd.DataFrame(res)


with main_io:
    main_io.title = 'DB测试'

    output = gr.DataFrame(get_data())

    main_io.load(get_data, inputs=[], outputs=[output])

main_io.launch()

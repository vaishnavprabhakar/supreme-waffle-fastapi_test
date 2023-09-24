from fastapi import FastAPI


app = FastAPI()







@app.get('/')
async def index():
    data = {
        'msg': 'This is just fast...'
    }
    print(type(data))
    return data
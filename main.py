from fastapi import FastAPI


app = FastAPI()







@app.get('/')
async def index():
    data = {
        'msg': 'This is just fast...'
    }
    return data
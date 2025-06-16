import uvicorn
from api._init_ import routes
from fastapi import FastAPI, HTTPException, status

app = FastAPI(
    title='YoutubeApi',
    description='vamooooooooo',
    version='1.0.0'
)

@app.get('/', status_code=200)
def xd():
    return {"message": "Bem vindo"}

app.include_router(routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
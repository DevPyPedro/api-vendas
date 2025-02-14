from fastapi import FastAPI,Response

from src.adapters.controllers.client.client_controller import router as client_router

app = FastAPI()

@app.get("/", tags=['API Service'])
def read_root():
    headers = {"Custom-Header": "API APP VENDAS"}
    return Response(content="SERVICE ONLINE", status_code=200, headers=headers)

app.include_router(client_router)
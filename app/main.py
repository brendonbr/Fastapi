from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests



app=FastAPI()



templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Minha página", "content": "Bem-vindo à minha página!"})

@app.post("/cv2")
async def opencv():
    pass

@app.post("/meuendpoint")
async def meu_endpoint(campo1: int, campo2: int):
    # código para processar os dados aqui
    resultado = {"mensagem": "Dados recebidos com sucesso!"}
    url = f"http://0.0.0.0:7010/meuendpoint"
    dados = {f"campo1": {campo1}, "campo2": {campo2}}
    response = requests.post(url, data=dados)
    if response.status_code == 200:
        resultado = response.json()
        # código para atualizar o front-end com o resultado aqui
        print(campo1,campo2)
    else:
        print("Erro ao enviar dados para o back-end.")
    return resultado
    
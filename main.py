from fastapi import FastAPI
from app.routes import router
from app.crud import criar_tabela

app = FastAPI()

criar_tabela()
app.include_router(router)




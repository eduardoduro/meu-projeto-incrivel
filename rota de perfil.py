from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Modelo de dados para a meta
class ProfileUpdate(BaseModel):
    meta: Optional[str] = None

@app.put("/profile")
async def update_profile(
    meta: str = Form(None), 
    foto: UploadFile = File(None)
):
    # Aqui entraria a lógica para salvar no Banco de Dados
    resultado = {
        "status": "Perfil atualizado com sucesso",
        "dados_recebidos": {
            "nova_meta": meta,
            "arquivo_foto": foto.filename if foto else "Nenhuma foto enviada"
        }
    }
    return resultado
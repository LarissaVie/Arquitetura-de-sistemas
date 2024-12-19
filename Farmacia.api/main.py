from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo para os medicamentos
class Medication(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

# Armazenamento em memória
medications: List[dict] = []

# Endpoint para listar todos os medicamentos
@app.get("/medications")
async def list_medications():
    """Retorna a lista de todos os medicamentos disponíveis"""
    return {
        "status": "success",
        "message": "Medicamentos recuperados com sucesso.",
        "data": medications
    }

# Endpoint para cadastrar um novo medicamento
@app.post("/medications")
async def create_medication(medication: Medication):
    """Adiciona um novo medicamento à farmácia"""
    new_medication = {
        "id": len(medications) + 1,  # Gera um ID simples
        **medication.dict()
    }
    medications.append(new_medication)
    return {
        "status": "success",
        "message": "Medicamento adicionado com sucesso.",
        "data": new_medication
    }

# Endpoint para atualizar os dados de um medicamento
@app.put("/medications/{medication_id}")
async def update_medication(medication_id: int, medication: Medication):
    """Atualiza os detalhes de um medicamento existente"""
    for existing_medication in medications:
        if existing_medication["id"] == medication_id:
            existing_medication.update(medication.dict())
            return {
                "status": "success",
                "message": "Medicamento atualizado com sucesso.",
                "data": existing_medication
            }
    raise HTTPException(status_code=404, detail="Medicamento não encontrado.")

# Endpoint para deletar um medicamento
@app.delete("/medications/{medication_id}")
async def delete_medication(medication_id: int):
    """Remove um medicamento da farmácia"""
    for index, medication in enumerate(medications):
        if medication["id"] == medication_id:
            deleted_medication = medications.pop(index)
            return {
                "status": "success",
                "message": "Medicamento removido com sucesso.",
                "data": deleted_medication
            }
    raise HTTPException(status_code=404, detail="Medicamento não encontrado.")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.Controller import HealthController
from app.database import Base, engine
from app.Model.Ateneo import Ateneo
from app.Model.Dipartimento import Dipartimento
from app.Model.Corso import Corso

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Identico al tuo @CrossOrigin di Spring!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Includiamo la rotta di test
app.include_router(HealthController.router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Backend Python Segreteria avviato"}
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import face_recognition
import os

app = FastAPI()

# Permitir la conexión desde tu web de Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cambia esto por la URL real de tu página en Vercel
URL_VERCEL_FOTOS = "https://serial-atletico-ensenada-victormktplus.vercel.app"

@app.get("/")
def home():
    return {"status": "IA Cerebro Activo - Demo Cross Country"}

@app.post("/buscar")
async def buscar(file: UploadFile = File(...)):
    # 1. Recibir la selfie y verificar que haya un rostro
    img = face_recognition.load_image_file(file.file)
    encodings = face_recognition.face_encodings(img)
    
    # 2. Si no hay rostro, devolvemos error (validación real)
    if not encodings:
        return {"success": False, "error": "No se detectó ningún rostro en la selfie."}
    
    # 3. Mágia de la Demo (Simulación exitosa)
    # Devolvemos las URLs completas de tus 8 fotos alojadas en Vercel
    fotos_encontradas = [
        f"{URL_VERCEL_FOTOS}/victor1.jpg",
        f"{URL_VERCEL_FOTOS}/victor2.jpg",
        f"{URL_VERCEL_FOTOS}/victor3.jpg",
        f"{URL_VERCEL_FOTOS}/victor4.jpg",
        f"{URL_VERCEL_FOTOS}/victor5.jpg",
        f"{URL_VERCEL_FOTOS}/victor6.jpg",
        f"{URL_VERCEL_FOTOS}/victor7.jpg",
        f"{URL_VERCEL_FOTOS}/victor8.jpg"
    ]
    
    return {
        "success": True, 
        "fotos": fotos_encontradas
    }

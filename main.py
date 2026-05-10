from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import face_recognition
import pickle

app = FastAPI()

# Esto permite que tu web en Vercel pueda hablar con este servidor
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Cerebro de IA funcionando"}

@app.post("/buscar")
async def buscar(file: UploadFile = File(...)):
    # 1. Recibir la foto
    img = face_recognition.load_image_file(file.file)
    encodings = face_recognition.face_encodings(img)
    
    if not encodings:
        return {"error": "No se detectó rostro en la selfie"}
    
    # 2. Por ahora, para tu demo, devolveremos un éxito simulado
    # En el siguiente paso meteremos la base de datos real
    return {
        "success": True, 
        "fotos": ["serial1.jpg", "serial2.jpg"] 
    }

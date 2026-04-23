from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import face_recognition
import pickle

app = FastAPI()

# Esto permite que tu sitio de Vercel hable con Replit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simulamos una base de datos de fotos para la demo
# En tu PC de la maestría generarás el .pkl real con miles de fotos
try:
    with open('base_fotos.pkl', 'rb') as f:
        BASE_FOTOS = pickle.load(f)
except:
    BASE_FOTOS = [] # Si no hay base, enviamos lista vacía

@app.post("/buscar")
async def buscar(file: UploadFile = File(...)):
    img = face_recognition.load_image_file(file.file)
    encodings = face_recognition.face_encodings(img)
    
    if not encodings:
        return {"error": "No se detectó rostro"}
    
    # Aquí iría la lógica de comparación que vimos antes
    # Por ahora, devolvemos un éxito simulado para la demo visual
    return {
        "success": True, 
        "fotos": [
            "serial1.jpg", "serial2.jpg" # Fotos donde "aparece" el corredor
        ]
    }
# main.py

from fastapi import FastAPI
from dotenv import load_dotenv
from config.settings import get_settings
from db.connection import connection
from api.routers import studentrouter
load_dotenv()
import uvicorn
app = FastAPI()






print(get_settings().mongodb_uri)
print("coming at main aftering hitting middleware")
app.include_router(studentrouter)

@app.get("/info")
async def get_info():
    return {"message": "Student API is running"}

if __name__=='__main__':
    uvicorn.run("main:app", port=5000, log_level="info")




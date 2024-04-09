from fastapi import APIRouter, HTTPException
from models.student_models import StudentCreate, StudentInDB, StudentOut, listStudentData
from services.student_services import create_student, list_students, get_student, update_student, delete_student

studentrouter = APIRouter()

@studentrouter.post("/students", response_model=StudentOut, status_code=201)
async def create_student_api(student: StudentCreate):
    try:
        return await create_student(student)
    except HTTPException as e:
        raise e

@studentrouter.get("/students", response_model=listStudentData)
async def list_students_api(country: str = None, age: int = None):
    try:
        return await list_students(country, age)
    except HTTPException as e:
        raise e

@studentrouter.get("/students/{student_id}", response_model=StudentCreate)
async def get_student_api(student_id: str):
    try:
        return await get_student(student_id)
    except HTTPException as e:  
        raise e

@studentrouter.patch("/students/{student_id}")
async def update_student_api(student_id: str, student: StudentInDB):
    try:
        return await update_student(student_id, student)
    except HTTPException as e:
        raise e

@studentrouter.delete("/students/{student_id}")
async def delete_student_api(student_id: str):
    try:
        return await delete_student(student_id)
    except HTTPException as e:
        raise e

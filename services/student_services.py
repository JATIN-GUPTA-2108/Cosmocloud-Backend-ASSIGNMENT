# app/services.py


from typing import Optional
from fastapi import HTTPException
from models.student_models import StudentCreate, StudentInDB, StudentOut, listStudentData, listStudentModel
from repository.student_repository import create_student_repo, delete_student_repo, get_student_repo, list_students_repo, update_student_repo


async def create_student(student: StudentCreate) -> StudentOut:
    try:
        return await create_student_repo(student)
    except HTTPException as e:
        raise e

async def list_students(country: Optional[str] = None, age: Optional[int] = None) -> listStudentData:
    try:
        studentsWithAdress = await list_students_repo(country, age)
        print(type(studentsWithAdress))
        data = []
        for i in studentsWithAdress:
            data.append(listStudentModel(name=i.name, age=i.age))
        return listStudentData(data=data)
        # return None
    except HTTPException as e:
        raise e

async def get_student(student_id: str) -> StudentCreate:
    try:
        return await get_student_repo(student_id)
    except HTTPException as e:
        raise e

async def update_student(student_id: str, student: StudentInDB):
    try:
        return await update_student_repo(student_id, student)
    except HTTPException as e:
        raise e

async def delete_student(student_id: str):
    try:
        return await delete_student_repo(student_id)
    except HTTPException as e:
        raise e

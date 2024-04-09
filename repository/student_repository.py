

from typing import Optional
from bson import ObjectId
from fastapi import HTTPException, Response
from db import connection
from models.student_models import StudentCreate, StudentInDB, StudentOut


async def create_student_repo(student: StudentCreate) -> StudentOut:
    try:
        print("come here at  create_student_repo")
        collection = connection.students
        student_dict = student.model_dump()
        new_user = await collection.insert_one(student_dict)
        return StudentOut(id=str(new_user.inserted_id))
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")


async def list_students_repo(country: Optional[str] = None, age: Optional[int] = None) -> list[StudentCreate]:
    try:
        collection = connection.students
        query = {}
        if country:
            query["address.country"] = country
        if age:
            query["age"] = {"$gte": age}
        students = await collection.find(query).to_list(length=None)
        print(students)
        students = [{k: v for k, v in student.items() if k != '_id'} for student in students]
        print(students)
        return [StudentCreate(**student) for student in students]
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")


async def get_student_repo(student_id: str) -> StudentCreate:
    try:
        collection = connection.students
        student:Optional[dict] = await collection.find_one({"_id": ObjectId(student_id)})
        if student:
            student.pop('_id')
            return StudentCreate(**student)
        else:
            raise HTTPException(status_code=404, detail="Student not found")
    except HTTPException as he:
        raise he
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")


async def update_student_repo(student_id: str, student: StudentInDB):
    try:
        collection = connection.students
        updated_student_data = student.model_dump(exclude_unset=True)  # Exclude unset fields
        if student.address:
            updated_student_data["address"] = student.address.model_dump(exclude_unset=True)
            if(student.address.city):
                updated_student_data['address.city'] = student.address.city
            if(student.address.country):
                updated_student_data['address.country'] = student.address.country
            updated_student_data.pop('address')

        
        updated_student = await collection.find_one_and_update(
            {"_id": ObjectId(student_id)},
            {"$set": updated_student_data},
            return_document=True
        )
        if updated_student:
            response = Response(status_code=204)
            return response
        else:
            raise HTTPException(status_code=404, detail="Student not found")
    except HTTPException as he:
        raise he
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")


async def delete_student_repo(student_id: str):
    try:
        collection = connection.students
        result = await collection.delete_one({"_id": ObjectId(student_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Student not found")
    except HTTPException as he:
        raise he
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal server error")
          
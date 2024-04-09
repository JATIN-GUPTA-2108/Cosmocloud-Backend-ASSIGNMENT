# app/models.py

from pydantic import BaseModel, validator, StrictStr, StrictInt
from typing import Optional

class AddressModel(BaseModel):
    city: StrictStr
    country: StrictStr
    class Config:
        extra = "forbid"

class StudentBase(BaseModel):
    name: StrictStr
    age: StrictInt 
    address: AddressModel
    class Config:
        extra = "forbid"

class StudentCreate(StudentBase):
    pass

class AddressForPatch(BaseModel):
    city: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    class Config:
        orm_mode = True
        extra = "forbid"

class StudentInDB(StudentBase):
    name:Optional[StrictStr] = None
    age:Optional[StrictInt] = None
    address:Optional[AddressForPatch] = None
    class Config:
        orm_mode = True
        extra = "forbid"


class StudentOut(BaseModel):
    id: str
    class Config:
        extra = "forbid"

class StudentOut(BaseModel):
    id:str
    class Config:
        extra = "forbid"


class listStudentModel(BaseModel):
    name:StrictStr
    age:StrictInt
    class Config:
        extra = "forbid"

class listStudentData(BaseModel):
    data:list[listStudentModel]
    class Config:
        extra = "forbid"
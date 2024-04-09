import json
from fastapi import Request, HTTPException
from app.models.student_models import StudentCreate
from pydantic import ValidationError
from starlette.middleware.base import BaseHTTPMiddleware

class RequestValidatorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            if request.method in ["POST", "PUT", "PATCH"]:
                request_body = await request.body()
                request_body_str = request_body.decode()  # Decode the request body
                student_data = json.loads(request_body_str)
                # Validate the request body against the StudentCreate model
                StudentCreate(**student_data)
        except ValidationError as e:
            error_details = []
            for error in e.errors():
                field = ".".join(error["loc"]) if error["loc"] else "body"
                error_details.append({
                    "field": field,
                    "msg": error["msg"],
                    "type": error["type"]
                })
            raise HTTPException(status_code=422, detail=error_details)
        
        response = await call_next(request)
        return response

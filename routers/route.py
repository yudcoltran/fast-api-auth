from fastapi import APIRouter, Request, Body, Response, status
from typing import List
from models.user import UpdateUser, User
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("/users", response_model=List[User])
async def getUsers(request: Request):
    users = request.app.database["users"].find(limit=100)
    return users

@router.post("/user", response_model=User)
async def createUser(request: Request, user: User = Body(...)):
    user = jsonable_encoder(user)
    new_user = request.app.database["users"].insert_one(user)
    create_user = request.app.database["users"].find_one(
        {"_id": new_user.inserted_id}
    )
    return create_user

@router.put("/user/{id}", response_model=UpdateUser)
async def updateUser(request: Request, user: UpdateUser = Body(...)):
    user = {k:v for k, v in user.model_dump().items() if v is not None}
    
    if len(user) >= 1:
        update_result = request.app.database['users'].update_one(
            {"_id": id}, {"$set": user}
        )
        
        if update_result.modified_count == 0:
            return "User is not found"

        exit_user = request.app.database['users'].find_one(
            {"_id": id}
        )

        return exit_user
    
    return "User not found"

@router.delete("user/{id}")
async def delete(request: Request, id: str, response: Response):
    delete_result = request.app.database["users"].delete_one(
        {"_id": id}
    )
    
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    
    return "user not found"
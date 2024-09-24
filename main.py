from fastapi import FastAPI, HTTPException
from models import Todo
app = FastAPI()



todos:list[Todo] = []

@app.get("/")
async def root():
    return {"message": "Hello World"}


#Get all todos
@app.get("/todos")
def all_todos() -> dict:
    return {"todos": todos}

#get single todo
@app.get("/todos/{todo_id}")
def get_todo( todo_id:int )->dict:
    for todo in todos:
        if todo.id == todo_id:
            return {"todo":todo}
    raise HTTPException(status_code=404,detail=f"No todo is found with id {todo_id}")


#Create a todo
@app.post("/todos")
def add_todo(todo:Todo)->dict:
    todos.append(todo)
    return {"message": f"{todo.title} has been added to the list"}


#delete single todo
@app.delete("/todos/{todo_id}")
def delete_todo( todo_id:int )->dict:
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": f"The {todo.title} has been deleted"}
    raise HTTPException(status_code=404,detail=f"No todo is found with id {todo_id}")

#update single todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int , updated_todo: Todo)->dict:
    for todo in todos:
        if todo.id == todo_id:
            todo.title = updated_todo.title
            return {"todo":todo}
    raise HTTPException(status_code=404,detail=f"No todo is found with id {todo_id}")

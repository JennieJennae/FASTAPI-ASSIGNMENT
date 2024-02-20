from fastapi import FastAPI

app = FastAPI()

students_db = {}
student_id_counter = 0


student_resource_template = {
    "id": "",
    "name": "",
    "age": "",
    "sex": "",
    "height": ""
}


@app.get("/students")  
def get_all_students():
    return students_db


@app.get("/students/{id}")
def get_individual_student(id: int):
    if id in students_db:
        return students_db[id]
    else:
        return {"error": "Student not found"}


@app.post("/students/")
def add_student(name: str, age: int, gender: str, height: float):
    global student_id_counter
    student_id_counter += 1
    
    new_student_data = student_resource_template.copy()
    new_student_data["id"] = student_id_counter
    new_student_data["name"] = name
    new_student_data["age"] = age
    new_student_data["gender"] = gender
    new_student_data["height"] = height
    
    students_db[new_student_data["id"]] = new_student_data
    return {"msg": "New student added successfully"}


@app.put("/students/{id}")   
def update_student(id: int, name: str, age: int, gender: str, height: float):
    if id in students_db:
        student_data = students_db[id]
        student_data["name"] = name
        student_data["age"] = age
        student_data["gender"] = gender
        student_data["height"] = height
        return {"msg": "Student details updated successfully"}
    else:
        return {"error": "Student not found"}


@app.delete("/students/{id}")
def delete_student(id: int):
    if id in students_db:
        del students_db[id]
        return {"msg": "Student deleted successfully"}
    else:
        return {"error": "Student not found"}

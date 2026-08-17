from fastapi import FastAPI, Path, HTTPException, Query
import json

# Create a FastAPI application instance.
# This object is the main entry point for defining API routes and handling requests.
app = FastAPI()

def load_data():
    with open('patient.json', 'r') as f:
        data = json.load(f)

        return data


# Define a route for the root URL '/'.
# When a user visits http://localhost:8000/ this function runs.
@app.get('/')
def hello():
    # Return a simple JSON response with a greeting message.
    return {"Message": "Patient Management System API"}


# Define a second route for '/about'.
# When a user visits http://localhost:8000/about this function runs.
@app.get('/about')
def about():
    # Return a JSON response with a message in Telugu meaning "let's study".
    return {"message": "A fully functional API to manage your patient's records"}


@app.get('/view')
def view():
    data = load_data()

    return data

# Creating the routes with path parameters
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="id of the patient in the DB", example="P001")):
    # load data
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="Patient not found")



@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, width or BMI"), order: str = Query("asc", description="Sort in ascending order or in descending order") ):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=404, detail=f"Invalid field is selected from {valid_fields}")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=404, detail="Invalid field selected between asc and desc")

    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x:x.get(sort_by, 0), reverse=sort_order)

    return sorted_data
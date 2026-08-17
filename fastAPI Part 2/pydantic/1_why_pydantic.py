# Type validation failure 

# Imagine if a programmer wants to insert the data into the database then 
def insert_patient_data(name: str, age: int):
    print(name)
    print(age)
    print("Inserted into database")

insert_patient_data("raghav", "twenty")



# If just we use parameter explanation

def insert_patient_data2(name: str, age: int):
    print(name)
    print(age)
    print("Inserted into database")

insert_patient_data2("abhi", "40")  # It still inserts this data into database


# Successful code but even this isn't the scalable one 

def insert_patient_data3(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("Inserted into database")

    else:
        raise TypeError("Incorrect datatype")

insert_patient_data2("abhi", "40")  # The code logic is correct but it fails in the scaling


# Data validation failure

def insert_patient_data3(name: str, age: int):
    
    if type(name) == str and type(age) == int:
        if age >= 0:
            print(name)
            print(age)
            print("Inserted into database")

        else:
            raise ValueError('Age cannot be negative')

    else:
        raise TypeError("Incorrect datatype")


# In order to make sure our function is working properly we need to write the maximum number of lines of code to reduce the logical errors exactly the pydantic is going to take care of this, it is mainly used for validations in python.
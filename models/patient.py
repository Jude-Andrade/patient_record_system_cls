from models.person import Person

class Patient(Person):
    def __init__(self, blood_type=None, medical_history=None,):
        if blood_type: self.set_blood_type(blood_type) 
        if medical_history: self.set_medical_history(medical_history)
        
    def get_blood_type(self): return self.__blood_type
    def get_medical_history(self): return self.__medical_history
    
    def set_blood_type(self, blood_type):
        blood_validation = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
        
        if blood_type not in blood_validation:
            raise ValueError("Invalid Blood Type!")
        
        self.__blood_type = blood_type

    def set_medical_history(self, medical_history):
        self.__medical_history = medical_history
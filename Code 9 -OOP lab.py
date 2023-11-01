#!/usr/bin/env python
# coding: utf-8

# In[36]:


class Patients:
    def __init__(self, name, age, gender, blood_pressure, temperature):
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_pressure = blood_pressure
        self.temperature = temperature
    
    def display_patient_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nBlood Pressure: {self.blood_pressure[0]} / {self.blood_pressure[1]}\nTemperature: {self.temperature}")
              
    def is_hypertensive(self):
              systolic, diastolic = self.blood_pressure
              return systolic >= 140 or diastolic >=90
    def is_feverish(self):
        return self.temperature >=37.5


# In[37]:


#defining data
patient1 = Patients("John Doe", 45, "Male", (140,85), 36.8)
patient2 = Patients("Jane Smith", 32, "Female", (130,88), 37.6)


# In[38]:


#Display patient information
patient1.display_patient_info()


# In[39]:


patient2.display_patient_info()


# In[30]:


#Checking for hypertension
patient1.is_hypertensive()


# In[42]:


patient2.is_hypertensive()


# In[43]:


# Checking for fever
patient1.is_feverish()


# In[44]:


patient2.is_feverish()


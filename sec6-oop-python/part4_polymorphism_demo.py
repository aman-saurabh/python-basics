"""
The word polymorphism means 'having many forms'.Polymorphism let us define methods with same name in different classes.
Polymorphism can exist in between inherited classes a well as non-inherited classes.
In previous part we have already seen example of 'polymorphism with inheritance'.
In this part we will see details about polymorphism in between non-inherited classes.
"""

# Example - Polymorphism in between non-inherited classes :-
class Doctor:
    def duty(self):
        print("Doctor's duty is to treat people and make them cure.")

class Army:
    def duty(self):
        print("Army's duty is to protect country from enemies.")

doctor_obj = Doctor()
army_obj = Army()

# Polymorphism with for loop:
for professions in (doctor_obj, army_obj):
    professions.duty()

# Polymorphism with functions and objects:
def get_duty(obj):
    obj.duty()

get_duty(doctor_obj)
get_duty(army_obj)

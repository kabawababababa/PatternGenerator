measurements = {
        'neck':None,
        'armLength':None, #hold arms out straight, measure from wrist to armpit
        'wristCircumference':None,
        'upperArmCircumference':None,

        'underArmBody':None, #around the body, under the armpits
        'bust':None, #thickest point of bust 
        'hip':None, #widest part of hip area, or widest part of torso 
        'units':"cm"
    }

# class measurements():
#     neck=None;
#     #hold arms out straight, measure from wrist to armpit
#     armLength=None;
#     wristCircumference=None;
#     upperArmCircumference=None;

#     underArmBody=None; #around the body, under the armpits
#     bust=None;
#     hip=None;
#     units="cm";
#     permittedUnits=["in", "cm"]
    
#     #array of measurements
#     def __init__(self, measurements):

#         neck, armLength, wristCircumference, upperArmCircumference = measurements[0:3]
#         upperArmBody, bust, hip, units = measurements[4:7]
        
#         if units not in self.permittedUnits: 
#             raise ValueError("invalid units, choose either: " + self.permittedUnits[0] + " or " + self.permittedUnits[1])

#     def set_measurements(self, measurements):

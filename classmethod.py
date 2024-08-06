class student:
    gradutaion='Be'
    def draduation_in(cls):
        print("gradtuatiuon",cls.gradutaion)
        
student.gradutaion_in=classmethod(student.gradutaion_in)
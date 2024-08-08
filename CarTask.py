
from abc import ABC , abstractmethod
class car(ABC):
    @abstractmethod
    def start_egine():
        pass
    @abstractmethod
    def stop_engine():
        pass
    
    def drive(self):
        print("vehicle is moving smoothly...")
class electricar(car):
    def start_egine(self):
        print("electric car is stated....")  
    def stop_engine(self):
        print("electric car stoped...")  
        
class gasolinecar(car):
    def start_egine(self):
        print("electric car is stated....")  
    def stop_engine(self):
        print("electric car stoped...")  
        
tata=electricar()
tata.start_egine()
tata.stop_engine()
tata.drive()

bmw=gasolinecar()
bmw.start_egine()
bmw.stop_engine()
bmw.drive()

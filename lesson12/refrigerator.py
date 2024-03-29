
from shipping import ShippingContainer

import iso6346

class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS=4.0
    FRIDGE_VOLUME_FT3 = 100


    def __init__(self, owner_code, length_ft,contents,celsius):
        super().__init__(owner_code,length_ft,contents)
        self.celsius=celsius
    
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self,value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self,value):
        self.contents=RefrigeratedShippingContainer._f_to_c(value)
    
    @property
    def volume_ft3(self):
        return super().volume_ft3-RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9


    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32



    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(owner_code=owner_code,serial=str(serial).zfill(6),category='R')



class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20.0
    @RefrigeratedShippingContainer.celsius.setter
    def celsius(self,value):
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too cold!")
        RefrigeratedShippingContainer.celsius.fset(self,value)

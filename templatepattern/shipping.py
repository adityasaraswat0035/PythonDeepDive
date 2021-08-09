import iso6346
class ShippingContainer:
    next_serial=1337
    HEIGHT_FT=8.5
    WIDTH_FT=8.0
    def __init__(self,owner_code,length_ft,contents):
        self.owner_code=owner_code
        self.contents=contents
        self.length_ft=length_ft
        # self.serial=ShippingContainer._get_next_serial_v1()
        # self.next_serial += 1
        # self.bic=ShippingContainer._make_bic_code(owner_code=owner_code,serial=ShippingContainer._get_next_serial_v1())
        #Polymorphic behiavior of static method
        self.bic=self._make_bic_code(owner_code=owner_code,serial=ShippingContainer._get_next_serial_v1())


    @staticmethod #internal to the class so static method
    def _make_bic_code(owner_code,serial):
        return iso6346.create(owner_code=owner_code,serial=str(serial).zfill(6))

    @staticmethod
    def _get_next_serial():
        result=ShippingContainer.next_serial
        ShippingContainer.next_serial+=1
        return result


    @classmethod
    def _get_next_serial_v1(cls):
        result=cls.next_serial
        cls.next_serial+=1
        return result

    @classmethod
    def create_empty(cls,owner_code,length_ft,*args,**kwargs):
        return cls(owner_code,length_ft,contents=None,*args,**kwargs)


    @classmethod
    def create_with_items(cls,owner_code,length_ft,items,*args,**kwargs):
        return cls(owner_code,length_ft,contents=list(items),*args,**kwargs)    

    @property
    def volume_ft3(self):
        return self._calc_volume(self)
    def _calc_volume(self):
         return ShippingContainer.HEIGHT_FT*ShippingContainer.WIDTH_FT*self.length_ft

import enum


class DataType(enum.Enum):
    GEO = "GEOLOCATION"
    DVS = "DISPLAYEDVEHICLESPEED"
    ENT = "ENGINETORQUE"
    BOP = "BOOSTPRESSURE"
    BRP = "BRAKINGPRESSURE"
    LAA = "LATERALACCELERATION"
    LOA = "LONGITUDINALACCELERATION"
    PEF = "PEDALFORCE"


class TableEntry:
    def __init__(self):
        self.geolocation = "N/A"
        self.displayedvehiclespeed = "N/A"
        self.enginetorque = "N/A"
        self.boostpressure = "N/A"
        self.brakingpressure = "N/A"
        self.lateralacceleration = "N/A"
        self.longitudinalacceleration = "N/A"
        self.pedalforce = "N/A"

    def add_from_line_array(self, line_array):
        data_type = line_array[1]
        if data_type == DataType.GEO.value:
            self.geolocation = Geolocation(line_array)
        if data_type == DataType.DVS.value:
            self.displayedvehiclespeed = Displayedvehiclespeed(line_array)
        if data_type == DataType.ENT.value:
            self.enginetorque = Enginetorque(line_array)
        if data_type == DataType.BOP.value:
            self.boostpressure = Boostpressure(line_array)
        if data_type == DataType.BRP.value:
            self.brakingpressure = Brakingpreasure(line_array)
        if data_type == DataType.LAA.value:
            self.lateralacceleration = Lateralacceleration(line_array)
        if data_type == DataType.LOA.value:
            self.longitudinalacceleration = Longitudinalacceleration(line_array)
        if data_type == DataType.PEF.value:
            self.pedalforce = Pedalforce(line_array)

    def __str__(self):
        return ""


class Geolocation:
    def __init__(self, line_array):
        pass


class Displayedvehiclespeed:
    def __init__(self, line_array):
        pass


class Enginetorque:
    def __init__(self, line_array):
        pass


class Boostpressure:
    def __init__(self, line_array):
        pass


class Brakingpreasure:
    def __init__(self, line_array):
        pass


class Lateralacceleration:
    def __init__(self, line_array):
        pass


class Longitudinalacceleration:
    def __init__(self, line_array):
        pass


class Pedalforce:
    def __init__(self, line_array):
        pass
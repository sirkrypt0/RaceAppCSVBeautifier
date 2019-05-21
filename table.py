import enum


class DataType(enum.Enum):
    GEO = "GEOLOCATION"
    TSP = "TIMESTAMP"
    GX1 = "GEOLOC1.1"
    GY1 = "GEOLOC1.2"
    GX2 = "GEOLOC2.1"
    GY2 = "GEOLOC2.2"
    DVS = "DISPLAYEDVEHICLESPEED"
    ENT = "ENGINETORQUE"
    BOP = "BOOSTPRESSURE"
    BRP = "BRAKINGPRESSURE"
    LAA = "LATERALACCELERATION"
    LOA = "LONGITUDINALACCELERATION"
    PEF = "PEDALFORCE"


class TableEntry:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.geolocation = ["N/A", "N/A", "N/A", "N/A"]
        self.displayedvehiclespeed = "N/A"
        self.enginetorque = "N/A"
        self.boostpressure = "N/A"
        self.brakingpressure = "N/A"
        self.lateralacceleration = "N/A"
        self.longitudinalacceleration = "N/A"
        self.pedalforce = "N/A"
        self.changed = False

    def get_entry(self):
        return [self.timestamp, self.geolocation[0], self.geolocation[1], self.geolocation[2], self.geolocation[3],
                self.displayedvehiclespeed, self.enginetorque, self.boostpressure, self.brakingpressure,
                self.lateralacceleration, self.longitudinalacceleration, self.pedalforce]

    def add_from_line_array(self, line_array):
        data_type = line_array[1]
        self.changed = True
        if data_type == DataType.GEO.value:
            self.geolocation = self.parse_geolocation(line_array)

        elif data_type == DataType.DVS.value:
            self.displayedvehiclespeed = self.parse_displayedvehiclespeed(line_array)

        elif data_type == DataType.ENT.value:
            self.enginetorque = self.parse_enginetorque(line_array)

        elif data_type == DataType.BOP.value:
            self.boostpressure = self.parse_boostpressure(line_array)

        elif data_type == DataType.BRP.value:
            self.brakingpressure = self.parse_brakingpreasure(line_array)

        elif data_type == DataType.LAA.value:
            self.lateralacceleration = self.parse_lateralacceleration(line_array)

        elif data_type == DataType.LOA.value:
            self.longitudinalacceleration = self.parse_longitudinalacceleration(line_array)

        elif data_type == DataType.PEF.value:
            self.pedalforce = self.parse_pedalforce(line_array)

        else:
            print(data_type, "was not a DataType")

            self.changed = False

    def parse_geolocation(self, line_array):
        # Split at | and ignore the first value as this is the timestamp
        geoloc = line_array[4].split("|")
        return [geoloc[1], geoloc[2], geoloc[4], geoloc[5]]

    def parse_displayedvehiclespeed(self, line_array):
        return line_array[4]

    def parse_enginetorque(self, line_array):
        return line_array[4]

    def parse_boostpressure(self, line_array):
        return line_array[4]

    def parse_brakingpreasure(self, line_array):
        return line_array[4]

    def parse_lateralacceleration(self, line_array):
        return line_array[4]

    def parse_longitudinalacceleration(self, line_array):
        return line_array[4]

    def parse_pedalforce(self, line_array):
        return line_array[4]


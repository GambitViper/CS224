class Mountain(object):
    num_mountains = 0

    def __init__(self, name, elevation, prominence, latitude, longitude, climbed):
        self.name = name
        self.elevation = elevation
        self.prominence = prominence
        self.latitude = latitude
        self.longitude = longitude
        self.climbed = climbed
        Mountain.num_mountains += 1

    def __del__(self):
        Mountain.num_mountains -= 1

    def __repr__(self):
        printstr =  "Name:       {:<15s}\n".format(self.name)
        printstr += "Elevation:  {:<15d}\n".format(self.elevation)
        printstr += "Prominence: {:<15d}\n".format(self.prominence)
        printstr += "Latitude:   {:<15s}\n".format(str(self.latitude))
        printstr += "Longitude:  {:<15s}\n".format(str(self.longitude))
        printstr += "Climbed:    {:<15s}\n".format(str(self.climbed))
        return printstr
    
    def is_higher(self, mountain):
        return self.elevation > mountain.elevation

    def climb(self):
        self.climbed = True
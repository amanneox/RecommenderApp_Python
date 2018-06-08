from geopy.distance import great_circle

class Distace(object):

    def distance(self,start,end,range):
        dist= great_circle(start, end).kilometers
        if float(dist) <= range:
            return dist
        else:
            return False




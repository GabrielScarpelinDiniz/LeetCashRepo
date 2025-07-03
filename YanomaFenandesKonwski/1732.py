class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        lista = []
        lista.append(altitude)
        for i in range(len(gain)):
            altitude += gain[i]
            lista.append(altitude)
        return(max(lista))
            

        
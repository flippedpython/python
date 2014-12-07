import math

def main():

    airports = {'LAX':(33.9425, -118.408056),
                'LHR':(51.4775, -0.461389),
               'DXB':(25.252778, 55.364444),
                'IST':(40.976111, 28.814167)}

    choice = input('enter airport code ').upper()

    print(choice in airports)
    print(airportExists(choice,airports))
    
    print(getAirportData(choice, airports))

    x = distanceKM(getAirportData('LHR', airports),getAirportData('IST',airports))
    print('%.2f km' % x)

#define d2r (M_PI / 180.0)

#calculate haversine distance for linear distance
def distanceKM(portA, portB):
#(double lat1, double long1, double lat2, double long2)
    print(portA,'\t',portB)
    lat1 = portA[0]
    long1 = portA[1]
    lat2 = portB[0]
    long2 = portB[1] 
    dlong = (long2 - long1) * (math.pi / 180.0)
    dlat = (lat2 - lat1) * (math.pi / 180.0);
    a = pow(math.sin(dlat/2.0), 2) + math.cos(lat1*(math.pi / 180.0)) * math.cos(lat2*math.pi / 180.0) * pow(math.sin(dlong/2.0), 2);
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
    d = 6367 * c;

    return d;

def airportExists(code, d):
    return code in d

def getAirportData(code,d):
    if airportExists(code,d):
        return d[code]

main()

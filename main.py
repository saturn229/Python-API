import requests
import json
from datetime import datetime
from my_objects import ISS

# Grand Rapids latitude 42 longitude 85
# http://api.open-notify.org/iss-pass.json?lat=LAT&lon=LON
def getDate(risetime):
    return datetime.utcfromtimestamp(risetime).strftime('%H:%M:%S')

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


    #enter city risetime and duration to text file

if __name__ == '__main__':
    city = input("Enter City: ")
    lat = float(input("Enter latitude: "))
    long = float(input("Enter longitude: "))
    list_of_passovers = []
    response = requests.get("http://api.open-notify.org/iss-pass.json", params={"lat": lat, "lon": long})
    jprint(response.json())
    passovers_list = response.json()['response']
    duration = ''
    risetime = ''

    for passover in passovers_list:
        for key, item in passover.items():
            if key == 'duration':
                duration = item // 60
            elif key == 'risetime':
                risetime = getDate(item)
                object1 = ISS(risetime, duration, city)
                list_of_passovers.append(object1)

        # print("The ISS will pass over ", city, " today at ", risetime, " for about ", duration, "minute(s)")
    with open("passoverData.txt", "w") as file:
        file.write("The next 5 passovers of the ISS in {} \n".format(city))
        for passover in list_of_passovers:
            file.write(passover.__str__())




'''
Name: Andrea Napoli-Wilson
Class: CIS 250
Date: 9/25/2020
Project name: Final Project
'''

import requests

def fer(k):
    """return Kelvin to Fahrenheit"""
    f = (9/5) * (k - 273) + 32
    return f


def get_data(url, zip=None, city=None):

  if zip is not None:
    url += "&zip="+str(zip)+",us"
  else:
    url += "&q="+city
    
  r = requests.get(url)

  return r

def itworks(resp):
    if resp.status_code == 200:
        data = resp.json()
        
        my_str="""
{name} Weather Forecast:
There will be {description} with wind speed of {windspeed}.
Visibility will be {visibility}.
Min. Temp will be {temp_min:.2f} and max will be {temp_max:.2f}.""".format(name=data['name'],description=data['weather'][0]['description'], windspeed=data['wind']['speed'], visibility=data['visibility'], temp_min=fer(data['main']['temp_min']), temp_max=fer(data['main']['temp_max']))
        print(my_str)
    else:
        print("Request not valid, try again: ",resp)

def main():

    apiid = "cba7fee375a53b5fde82e6dda8ce69a1"
    apiurl = "http://api.openweathermap.org/data/2.5/weather?appid=" + apiid

    while (True):
        inp =int(input("Please select one :\n1. Zip Code\n2. City Name\n3. Exit\n"))

        if inp == 1:
            dataZip=input("Please enter the zip code: ")
            dataZip = dataZip.strip()
            if len(dataZip) != 5:
                print("Please enter a 5-digit zip code")
                continue
            try:
                
                test = int(dataZip)
                resp= get_data(apiurl,dataZip,None)
                itworks(resp)
            except Exception as ex:
                print("Error : ",ex)
        elif inp == 2:

            dataZip = input("Please enter city name :")
        
            try:    
                resp= get_data(apiurl,None,dataZip)
                itworks(resp)
            except Exception as ex:
                print("Error :",ex)
        elif inp==3:
            break
        else:
            print("Invalid, please try again..\n")


if __name__ =="__main__":
    main()

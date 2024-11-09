import requests, json
api_key="1735fec0ffc5adea93fcbe29dfa8a6c4"

#base url variable to store url
base_url="https://api.openweathermap.org/data/2.5/weather?"

#to get the city name
city_name =input ("Enter city name:")

#complete url address to store
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

#get method of request module
#return response object
print(complete_url)
response =requests.get(complete_url)

data= response.json()
print("---------------")
print("Json Data")
print(data)
print("---------------")

if data["cod"] !="404":
    record=data["main"]
    current_pressure=record["pressure"]
    current_humidity=record["humidity"]
    current_temperature =record["temp"]
    record1=data["weather"]
    weather_description = record1[0]["description"]
    print("Temperature (in kelvin unit)=",current_temperature)
    print("Temperature (in kelvin unit)="+str(current_temperature)+"\n atmospheric pressure(in nPa unit)="+str(current_pressure)+"\n humidity (in percentage)= "+str(current_humidity)+"\n description="+str(weather_description))
else:
    print("City not found")

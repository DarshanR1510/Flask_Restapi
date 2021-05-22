import requests

base = "http://127.0.0.1:5000/"

response = requests.put(base + "video/5", {"name":"How to make restapi", "views":5555555, "likes":98765})
print(response.json())
print("Press any key")
input()

response = requests.patch(base + "video/2", {"views":99, "likes":161386})
print(response.json())
print("Press any key")
input()

response = requests.get(base + "video/1")
print(response.json())
print("Press any key")
input()

response = requests.delete(base + "video/4")
print(response)



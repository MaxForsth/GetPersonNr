import requests
import random

looping = True


print("\n hämta personNr från skatteverket \n")

while looping:
    randomtal = random.randint(1, 100)

    url = f"https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763/json?_offset={randomtal}&_limit=100"

    req = requests.get(url)


    jsondata = req.json()
    print(req)
    list = jsondata['results']
    print(list)

    EnTill = input("\n vill du slumpa ett personNr till? j/n \n")

    if (EnTill == "n" or EnTill == "n"):
        break
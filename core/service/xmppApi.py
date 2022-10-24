import requests
import config


cfg = config.Config('res/configs/config.cfg')

headers = {
        'accept': '*/*',
        'Authorization': cfg.of_secret,
        'Content-Type': 'application/json'
    }

user_api = 'http://im.ydns.eu:9090/plugins/restapi/v1/users'
def addAccount(user, password):
    data = {
  "username": user,
  "name": "string",
  "email": "string",
  "password": password,
  "properties": [
    {
      "key": "string",
      "value": "string"
    }
  ]
}
    response = requests.post(user_api, headers=headers, json=data)
    print(response)

    return #result


def changePassword(user, password):

    data = {
        "username": user,
        "name": "string",
        "email": "string",
        "password": password,
        "properties": [
            {
                "key": "string",
                "value": "string"
            }
        ]
    }

    url = f'http://im.ydns.eu:9090/plugins/restapi/v1/users/{user}'
    respons = requests.put(url, headers=headers, json=data)
    print (respons)


def delAccount(user):
    H = {

        'accept': '*/*',
        'Authorization': cfg.of_secret
    }
    print(user)
    url_del = f'http://im.ydns.eu:9090/plugins/restapi/v1/users/{user}'
    response = requests.delete(url_del,headers=H)
    print(response)
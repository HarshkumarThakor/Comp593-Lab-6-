import requests
from sys import argv 

def main():
    name = argv[1]
    dict = get_user_info(name)
    if dict:
        user_strings = get_user_strings(dict)
        pastebin_url = post_to_pastebin(user_strings[0], user_strings[1])
        print(pastebin_url)

def get_user_info(name):
    print("getting pokemon info..", end='')
    url = 'https://pokeapi.co/api/v2/pokemon/' 
    response = requests.get(url + str(name))

    if response.status_code == 200:
        print('success')
        return response.json()
    else:
        print('failed.Response code:',response.status_code)
        return None
    
def get_user_strings(user_dict):
    title = user_dict['name'] + "Pokemon abiltites"
    body_text = "Abilties: " + user_dict['abilities'][0]['ability']['name'] + "\n"
    body_text += "Abilties: " + user_dict['abilities'][1]['ability']['name'] + "\n" 
    body_text += "Abilties: " + user_dict['abilities'][2]['ability']['name']
    return (title, body_text)
    

def post_to_pastebin(title, body):
    print("Posting to PasteBin..", end='')
    
    parameter = {
       'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
       'api_option': 'paste',
       'api_paste_code':body,
       'api_paste_name':title
    }
    
    response = requests.post( "https://pastebin.com/api/api_post.php", data=parameter)

    if response.status_code == 200:
        print('success')
        return response.text # Converts response body to a string
    else:
        print('failed.Response code:', response.status_code)
        return response.status_code

main()
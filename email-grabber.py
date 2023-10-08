import requests

url = "https://joaopessoa.ifpb.edu.br/horario/api/professor"

response = requests.get(url)

data = response.json()

gmail_prof = []
hotmail_prof = []

for dict in data:
        if 'gmail' in dict['email']:
                gmail_prof.append(dict)
        if 'hotmail' in dict['email']:
                hotmail_prof.append(dict)

print("\nGMAIL")

for gmail in gmail_prof:
        print(gmail['email'])

print("\nHOTMAIL\n")

for hotmail in hotmail_prof:
        print(hotmail['email'])

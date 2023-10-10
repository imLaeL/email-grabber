import requests

url = "https://joaopessoa.ifpb.edu.br/horario/api/professor"

response = requests.get(url)

data = response.json()

prof_gmail = {}
prof_hotmail = {}

for dict in data:
        if 'gmail'  in dict['email']:
                prof_gmail[dict['nome']] = dict['email']
        elif 'hotmail' in dict['email']:
                prof_hotmail[dict['nome']] = dict['email']


print("\nGMAIL---------------------------\n")

for i, j in prof_gmail.items():
        
        print(i, "=>", j)

print("\nHOTMAIL---------------------------\n")

for i, j in prof_hotmail.items():
        
        print(i, "=>", j)
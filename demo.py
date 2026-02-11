import requests

r = requests.get("https://api.smith.langchain.com/health")
print(r.status_code, r.text)

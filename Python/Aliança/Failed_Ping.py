import requests

def get_new_meet_link():
    session = requests.Session()
    response = session.get("https://meet.google.com/new", allow_redirects=True)
    return response.url

link = get_new_meet_link()
print("Fresh Meet link:", link)
import json

import requests


def user_pass_f():

    url = "http://localhost:8000"
    headers = {
        "username": "user1",
        "password": "p"
    }

    t = requests.post(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def user_pass_post_c():

    url = "http://localhost:8000"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.post(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def user_pass_get_c():

    url = "http://localhost:8000"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def user_pass_get_c():

    url = "http://localhost:8000"
    headers = {
        "username": "mirko",
        "password": "mirko"
    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def user_pass_get_f():

    url = "http://localhost:8000"
    headers = {
        "username": "a",
        "password": "a"
    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def token_get_f():

    url = "http://localhost:8000"
    headers = {
        "access-token": "a.f.v",
        "refresh-token": "a",
    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def token_get_c():

    url = "http://localhost:8000"
    # headers = {
    #     "access-token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRRExzQXA1YmhYbklPOThWOTBqd3hjS01XeU9hcVlWX1ZlZkJHdkFGWlY0In0.eyJleHAiOjE2NTg4MzMzNDIsImlhdCI6MTY1ODgzMzI4MiwianRpIjoiOWI4NjU0ZmMtZmNlOS00ZTkxLWE2ZGQtNmE4OTE0OWMxMWE1IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJzdWIiOiJkNzRkYTllMi01ZWMzLTRjMDYtYTI0Yy05OWVjNGU0OGNkZjQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImIyZGJmNzU1LTQxOTEtNDRmOC1hNDU0LWY3ODU1ZGM0MmNjMSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZXNvdXJjZV9hY2Nlc3MiOnsiYmV5b25kX2NsaSI6eyJyb2xlcyI6WyJ1c2VyX3JvbGVfMiJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiMmRiZjc1NS00MTkxLTQ0ZjgtYTQ1NC1mNzg1NWRjNDJjYzEiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6Im1pcmtvIn0.Di2e_1NANMz7xAjqqWn3YVL2kWXz7h6a2HIsNpa6md2I3c8LJCGCAjEY2SnqF_EhAcZC_zgQNAjlLBZWnTbpzS71b2_Y3MxeLecTNx4Q_lqVUNskpItTUuhh1LFXqYdUMnr9eQ5nIJvgkwzHHbc364OMGQospsUf4xMgyoKTBTruXjjFbXHWdfZ520LkhmeG3vSZYbN9SDafpIpkiyE632CqJUdXN1J6PElklGUXJrVm9QKw3Lb3zsW-uMihwRXpEv6N0mynxb4ViYoCvzqnJ3My26fWNgPoXvBV7M3zqlL8dQzHgdFw7HLqpgzl_rBeTKdd3Ud2uvp34cz1eZEhyQ",
    #     "refresh-token": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhNzYyZmYyYi04NjdiLTRjZTUtYTQxNy0xOGVmOWJkNTU0YjYifQ.eyJleHAiOjE2NTg4MzUwODIsImlhdCI6MTY1ODgzMzI4MiwianRpIjoiMjdlNDg0NGMtNDA5NC00YzNhLWFkOWYtMjFhMmI3MGNiNTQ1IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2JleW9uZCIsInN1YiI6ImQ3NGRhOWUyLTVlYzMtNGMwNi1hMjRjLTk5ZWM0ZTQ4Y2RmNCIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImIyZGJmNzU1LTQxOTEtNDRmOC1hNDU0LWY3ODU1ZGM0MmNjMSIsInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiMmRiZjc1NS00MTkxLTQ0ZjgtYTQ1NC1mNzg1NWRjNDJjYzEifQ.PsPEZM4FqisIZ2ouhOyasOD4RCf_sHEHujkSdntaHyw",
    #
    # }

    headers = {
    "access-token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRRExzQXA1YmhYbklPOThWOTBqd3hjS01XeU9hcVlWX1ZlZkJHdkFGWlY0In0.eyJleHAiOjE2NTg4NDM3OTYsImlhdCI6MTY1ODg0MzczNiwianRpIjoiOGU3ZGNiYzUtZTNjNC00NGM0LThkNjQtZTQ0MmJlM2Q0ODQwIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJzdWIiOiJkNzRkYTllMi01ZWMzLTRjMDYtYTI0Yy05OWVjNGU0OGNkZjQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImRlOTMzNGY0LTE4ZDktNDRlMS04MmFjLTY1NzJmOTE0ODcwMSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZXNvdXJjZV9hY2Nlc3MiOnsiYmV5b25kX2NsaSI6eyJyb2xlcyI6WyJ1c2VyX3JvbGVfMiJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJkZTkzMzRmNC0xOGQ5LTQ0ZTEtODJhYy02NTcyZjkxNDg3MDEiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6Im1pcmtvIn0.Z7Svv7YhojxTSmi3P202FYTKBFiGdE6pw6mMbhMYtWD71OhtMMeVg8QAY5feWkusb1W8RG1Pg2G8umt5h07LnD7s4dXZrvClouytuSbiRgC_6G2WqocCOPS_QTfx2pKOF1iPu5_WyCsHPXNxLVTabkKzogKaEqbbN9_na-Ux6AbnTaluE5FrEyPnIGm7WoCSwBUyxMC6pklO4JgDxswnIx_iNCK-J8z2icf871nHCXubsygSL70N7SrfHHqzP-5lc6XcY6wX-tOwVn4HL89QNczfm5LchI3AvhPHmNvCCRhbtPzwu6Hd9fc746VVMtSjmCuQUN_ubyWc3l1ovv3Qqw",
    "expires_in": 60,
    "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRRExzQXA1YmhYbklPOThWOTBqd3hjS01XeU9hcVlWX1ZlZkJHdkFGWlY0In0.eyJleHAiOjE2NTg4NDM3OTYsImlhdCI6MTY1ODg0MzczNiwiYXV0aF90aW1lIjowLCJqdGkiOiJjOWJjZDE2Yy0zZDk5LTQyZmItYTA2NS1hNTk4NjVkZGMwY2UiLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2JleW9uZCIsImF1ZCI6ImJleW9uZF9jbGkiLCJzdWIiOiJkNzRkYTllMi01ZWMzLTRjMDYtYTI0Yy05OWVjNGU0OGNkZjQiLCJ0eXAiOiJJRCIsImF6cCI6ImJleW9uZF9jbGkiLCJzZXNzaW9uX3N0YXRlIjoiZGU5MzM0ZjQtMThkOS00NGUxLTgyYWMtNjU3MmY5MTQ4NzAxIiwiYXRfaGFzaCI6IjNELVd0amtGOTFZckNJN0Nfc29hMkEiLCJhY3IiOiIxIiwic2lkIjoiZGU5MzM0ZjQtMThkOS00NGUxLTgyYWMtNjU3MmY5MTQ4NzAxIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJtaXJrbyJ9.izD04OkOJIwQGTx5KYBk0--y2XscRM67znGFDnY59EM6lQYtXV1N8Y2MyQiisNvQ3Vnw0f1MyYxLCe0yuFKigf8PJgC4LpQsv95wm7XiailGXFHSHy34-48IyVv1oGWAIdgJX8NHYfvE8Fow9ey1bKsWor6EaPhra9pjIoyYiuH5vXV_iV6qRAziCs18mH9RqSwo7_xORX6BZdRbYb345r7vtgAzKxqUC0eUjZOU6b60rQCkH9X6WOXGIcPlsOGPxGujTnT3ZRa9nXErkzeimlFukgCbHEGx7sDuzjVjdVUNOW4EgAVL0LR5P8QcoxN5F4bwy-0u2QALu2Xmtm8HLg",
    "not-before-policy": 0,
    "refresh_expires_in": 1800,
    "refresh-token": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhNzYyZmYyYi04NjdiLTRjZTUtYTQxNy0xOGVmOWJkNTU0YjYifQ.eyJleHAiOjE2NTg4NDU1MzYsImlhdCI6MTY1ODg0MzczNiwianRpIjoiYTY2ODBhYTYtZGNkNS00MjkwLTgxMDQtY2M1YjhkN2FkNzFiIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2JleW9uZCIsInN1YiI6ImQ3NGRhOWUyLTVlYzMtNGMwNi1hMjRjLTk5ZWM0ZTQ4Y2RmNCIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImRlOTMzNGY0LTE4ZDktNDRlMS04MmFjLTY1NzJmOTE0ODcwMSIsInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJkZTkzMzRmNC0xOGQ5LTQ0ZTEtODJhYy02NTcyZjkxNDg3MDEifQ.rWaYZqjb1HHgB_8vUtmGoomgfsd9cRrzix0t_QY6djI",


    }


    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


def main():
    # user_pass_f()
    # user_pass_get_f()

    # user_pass_post_c()
    # user_pass_get_c()

    token_get_f()
    token_get_c()

if __name__ == '__main__':
    main()

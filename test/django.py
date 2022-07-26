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
        "access-token": "a",
        "refresh-token": "a",
    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))

def token_get_c():

    url = "http://localhost:8000"
    headers = {
        "access-token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRRExzQXA1YmhYbklPOThWOTBqd3hjS01XeU9hcVlWX1ZlZkJHdkFGWlY0In0.eyJleHAiOjE2NTg4MzMzNDIsImlhdCI6MTY1ODgzMzI4MiwianRpIjoiOWI4NjU0ZmMtZmNlOS00ZTkxLWE2ZGQtNmE4OTE0OWMxMWE1IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJzdWIiOiJkNzRkYTllMi01ZWMzLTRjMDYtYTI0Yy05OWVjNGU0OGNkZjQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImIyZGJmNzU1LTQxOTEtNDRmOC1hNDU0LWY3ODU1ZGM0MmNjMSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZXNvdXJjZV9hY2Nlc3MiOnsiYmV5b25kX2NsaSI6eyJyb2xlcyI6WyJ1c2VyX3JvbGVfMiJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiMmRiZjc1NS00MTkxLTQ0ZjgtYTQ1NC1mNzg1NWRjNDJjYzEiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6Im1pcmtvIn0.Di2e_1NANMz7xAjqqWn3YVL2kWXz7h6a2HIsNpa6md2I3c8LJCGCAjEY2SnqF_EhAcZC_zgQNAjlLBZWnTbpzS71b2_Y3MxeLecTNx4Q_lqVUNskpItTUuhh1LFXqYdUMnr9eQ5nIJvgkwzHHbc364OMGQospsUf4xMgyoKTBTruXjjFbXHWdfZ520LkhmeG3vSZYbN9SDafpIpkiyE632CqJUdXN1J6PElklGUXJrVm9QKw3Lb3zsW-uMihwRXpEv6N0mynxb4ViYoCvzqnJ3My26fWNgPoXvBV7M3zqlL8dQzHgdFw7HLqpgzl_rBeTKdd3Ud2uvp34cz1eZEhyQ",
        "refresh-token": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhNzYyZmYyYi04NjdiLTRjZTUtYTQxNy0xOGVmOWJkNTU0YjYifQ.eyJleHAiOjE2NTg4MzUwODIsImlhdCI6MTY1ODgzMzI4MiwianRpIjoiMjdlNDg0NGMtNDA5NC00YzNhLWFkOWYtMjFhMmI3MGNiNTQ1IiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2JleW9uZCIsInN1YiI6ImQ3NGRhOWUyLTVlYzMtNGMwNi1hMjRjLTk5ZWM0ZTQ4Y2RmNCIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImIyZGJmNzU1LTQxOTEtNDRmOC1hNDU0LWY3ODU1ZGM0MmNjMSIsInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiMmRiZjc1NS00MTkxLTQ0ZjgtYTQ1NC1mNzg1NWRjNDJjYzEifQ.PsPEZM4FqisIZ2ouhOyasOD4RCf_sHEHujkSdntaHyw",

    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


def main():
    # user_pass_f()
    # user_pass_get_f()

    user_pass_post_c()
    user_pass_get_c()

    # token_get_f()
    # token_get_c()

if __name__ == '__main__':
    main()

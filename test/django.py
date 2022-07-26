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


    headers = {
        "access-token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRRExzQXA1YmhYbklPOThWOTBqd3hjS01XeU9hcVlWX1ZlZkJHdkFGWlY0In0.eyJleHAiOjE2NTg4NDM3OTYsImlhdCI6MTY1ODg0MzczNiwianRpIjoiOGU3ZGNiYzUtZTNjNC00NGM0LThkNjQtZTQ0MmJlM2Q0ODQwIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJzdWIiOiJkNzRkYTllMi01ZWMzLTRjMDYtYTI0Yy05OWVjNGU0OGNkZjQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImRlOTMzNGY0LTE4ZDktNDRlMS04MmFjLTY1NzJmOTE0ODcwMSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZXNvdXJjZV9hY2Nlc3MiOnsiYmV5b25kX2NsaSI6eyJyb2xlcyI6WyJ1c2VyX3JvbGVfMiJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJkZTkzMzRmNC0xOGQ5LTQ0ZTEtODJhYy02NTcyZjkxNDg3MDEiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6Im1pcmtvIn0.Z7Svv7YhojxTSmi3P202FYTKBFiGdE6pw6mMbhMYtWD71OhtMMeVg8QAY5feWkusb1W8RG1Pg2G8umt5h07LnD7s4dXZrvClouytuSbiRgC_6G2WqocCOPS_QTfx2pKOF1iPu5_WyCsHPXNxLVTabkKzogKaEqbbN9_na-Ux6AbnTaluE5FrEyPnIGm7WoCSwBUyxMC6pklO4JgDxswnIx_iNCK-J8z2icf871nHCXubsygSL70N7SrfHHqzP-5lc6XcY6wX-tOwVn4HL89QNczfm5LchI3AvhPHmNvCCRhbtPzwu6Hd9fc746VVMtSjmCuQUN_ubyWc3l1ovv3Qqw",

        "refresh-token": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhNzYyZmYyYi04NjdiLTRjZTUtYTQxNy0xOGVmOWJkNTU0YjYifQ.eyJleHAiOjE2NTg4NDU1MzYsImlhdCI6MTY1ODg0MzczNiwianRpIjoiYTY2ODBhYTYtZGNkNS00MjkwLTgxMDQtY2M1YjhkN2FkNzFiIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2JleW9uZCIsInN1YiI6ImQ3NGRhOWUyLTVlYzMtNGMwNi1hMjRjLTk5ZWM0ZTQ4Y2RmNCIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImRlOTMzNGY0LTE4ZDktNDRlMS04MmFjLTY1NzJmOTE0ODcwMSIsInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJkZTkzMzRmNC0xOGQ5LTQ0ZTEtODJhYy02NTcyZjkxNDg3MDEifQ.rWaYZqjb1HHgB_8vUtmGoomgfsd9cRrzix0t_QY6djI",

    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


def main():
    # user_pass_f()
    # user_pass_get_f()

    # user_pass_post_c()
    user_pass_get_c()

    token_get_f()
    token_get_c()

if __name__ == '__main__':
    main()

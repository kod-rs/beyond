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
        "access-token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRRExzQXA1YmhYbklPOThWOTBqd3hjS01XeU9hcVlWX1ZlZkJHdkFGWlY0In0.eyJleHAiOjE2NTg4NDg1MjEsImlhdCI6MTY1ODg0ODQ2MSwianRpIjoiOTkwMzJmY2ItMzM0OS00ZWM3LTlmYjQtOWRlMjM1MmMyZThiIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJzdWIiOiJkNzRkYTllMi01ZWMzLTRjMDYtYTI0Yy05OWVjNGU0OGNkZjQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImJiMDQ1NTA5LTQ0ZDctNGRmMy04ZDE5LTRmZTZlNzRhZDM2NSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiKiJdLCJyZXNvdXJjZV9hY2Nlc3MiOnsiYmV5b25kX2NsaSI6eyJyb2xlcyI6WyJ1c2VyX3JvbGVfMiJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiYjA0NTUwOS00NGQ3LTRkZjMtOGQxOS00ZmU2ZTc0YWQzNjUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByZWZlcnJlZF91c2VybmFtZSI6Im1pcmtvIn0.fK-Zcdkc2MyxZP5RfwIO5z7c0qJi0fIankrY3M63l3HyjnJ8luCGmWJiwIpCEeVyrdX3iPVsvlGcbuzO5-1Nm4TaKIfq8or4CgKjqi2se7Qmo9Mkq1L9rue2vhkai0Xz3aGqENWW2ixE2AbyKic9mAEFFcYxk6SVib5xVah_g2L1jusSB2MTivL60cejTKTczKGFayE3223yHVnaOmB7zTqTfSSviIX35N1BrezxvOtlmol8plOd0KP0nOc9wdYJ09lgMmsHg4p8k3B9pNiIk5uHlHrRwnW47AACJS3oo4iLSTrkV-dgE45uFJDsfP4seIrwqaOEMp6Q4p0Bqw6_dQ",
        "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJRRExzQXA1YmhYbklPOThWOTBqd3hjS01XeU9hcVlWX1ZlZkJHdkFGWlY0In0.eyJleHAiOjE2NTg4NDg1MjEsImlhdCI6MTY1ODg0ODQ2MSwiYXV0aF90aW1lIjowLCJqdGkiOiJkZGZkMDY1MC1jYWFlLTRlMmUtYTc2Yi1lOTk4NjNiZTUwZWYiLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2JleW9uZCIsImF1ZCI6ImJleW9uZF9jbGkiLCJzdWIiOiJkNzRkYTllMi01ZWMzLTRjMDYtYTI0Yy05OWVjNGU0OGNkZjQiLCJ0eXAiOiJJRCIsImF6cCI6ImJleW9uZF9jbGkiLCJzZXNzaW9uX3N0YXRlIjoiYmIwNDU1MDktNDRkNy00ZGYzLThkMTktNGZlNmU3NGFkMzY1IiwiYXRfaGFzaCI6ImtVeW9sR0JRRlJxaktEZThYMXdpNnciLCJhY3IiOiIxIiwic2lkIjoiYmIwNDU1MDktNDRkNy00ZGYzLThkMTktNGZlNmU3NGFkMzY1IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJtaXJrbyJ9.NyoGkbF-ZEebEeJ76FuDt-yj8IFIA8upjl_ys06xz3_ncrqlTpGiU2K2Ok9_5g77dywdWXK0vWw023cBM__fJqYlpdcQ94CUeTNCBIUAoOmo7auZD-MwCyulroAwkYwan1aMIa2mi4rHw5JtQ_Jf1XzLt60S_9RR2XR1KNRe3nVRwbhkEc7LXsfuS3p5uCFWlvdkR1Z1xhlrijFbHbY77aDulZyKU3shz3q-wwyQ50Fp1i9VZFYLUDvXbZ-d2D5xlUsdnLFCBpEemnumJPW2uZw5FQXyNPtpdlKT7WDBLVg85fSvu53xGsj_05mRvbkJzryVSXMpkgWq3l7hvKuDuA",
        "refresh-token": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJhNzYyZmYyYi04NjdiLTRjZTUtYTQxNy0xOGVmOWJkNTU0YjYifQ.eyJleHAiOjE2NTg4NTAyNjEsImlhdCI6MTY1ODg0ODQ2MSwianRpIjoiZjEwMzFjYzMtYzVjOS00YTUyLThhMWItMWEzZThlMzY0YmRmIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy9iZXlvbmQiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAvcmVhbG1zL2JleW9uZCIsInN1YiI6ImQ3NGRhOWUyLTVlYzMtNGMwNi1hMjRjLTk5ZWM0ZTQ4Y2RmNCIsInR5cCI6IlJlZnJlc2giLCJhenAiOiJiZXlvbmRfY2xpIiwic2Vzc2lvbl9zdGF0ZSI6ImJiMDQ1NTA5LTQ0ZDctNGRmMy04ZDE5LTRmZTZlNzRhZDM2NSIsInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJzaWQiOiJiYjA0NTUwOS00NGQ3LTRkZjMtOGQxOS00ZmU2ZTc0YWQzNjUifQ.p17JVJRHrR6-ORkWE5cSOf7JcEELY40Bgm-3bkCF1Ss",
        "scope": "openid email profile",
        "session_state": "bb045509-44d7-4df3-8d19-4fe6e74ad365",
        "token_type": "Bearer"

    }

    t = requests.get(url, headers=headers, verify=False)
    print(json.dumps(json.loads(t.text), indent=4, sort_keys=True))


def main():
    # user_pass_f()
    # user_pass_get_f()

    # user_pass_post_c()
    user_pass_get_c()

    # token_get_f()
    # token_get_c()

if __name__ == '__main__':
    main()

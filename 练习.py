# import requests
#
#
# url = "https://dev-auth.sprintray.com/activate?user_code=SVKLRXTJ"
# response = requests.get(url, allow_redirects=False, verify=False)
# print(response)
# if 'Location' in response.headers:
#     location_value = response.headers['Location']
#     two = f"https://dev-auth.sprintray.com{location_value}"
#     print(two)
#     responsetwo = requests.post(two, allow_redirects=False, verify=False)
#     print(responsetwo)
#     if response.status_code == 302 and 'Location' in responsetwo.headers:
#         redirect_url = responsetwo.headers['Location']
#         response_redirect = requests.post(redirect_url)
#         print("==========")
#         print(response_redirect.text)
#     else:
#         print("----")
#         print(response.text)


import lackey
i = 1
while True:

    try:
        lackey.click("1.jpg")
        i = i+1
        print(i)
    except lackey.FindFailed:
        i = i + 1
        print(i)
        pass


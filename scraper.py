import requests
from lxml import html

USERNAME = "lhuang1@fandm.edu"
PASSWORD = "NLP123456"

LOGIN_URL = "https://sso.accounts.dowjones.com/login?state=g6Fo2SA5NVUzVXByTzZtZTh0YWM0dEh5VndHa1ZjT2EyOG52WaN0aWTZIDlicjNlSWRyUi1NT2YyQ3c2SFQ1M1ozejdwbGVIOFF2o2NpZNkgNWhzc0VBZE15MG1KVElDbkpOdkM5VFhFdzNWYTdqZk8&client=5hssEAdMy0mJTICnJNvC9TXEw3Va7jfO&protocol=oauth2&prompt=login&scope=openid%20idp_id%20roles%20email%20given_name%20family_name%20djid%20djUsername%20djStatus%20trackid%20tags%20prts&response_type=code&redirect_uri=https%3A%2F%2Faccounts.wsj.com%2Fauth%2Fsso%2Flogin&nonce=d532442b-0026-4759-aaf5-60f97febc6ee&connection=DJldap&ui_locales=en-us-x-wsj-0&mg=ss-ngx&savelogin=on#!/signin"
URL = 

def main():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers = dict(referer = URL))
    tree = html.fromstring(result.content)
    bucket_names = tree.xpath("//div[@class='repo-list--repo']/a/text()")

    print(bucket_names)

if __name__ == '__main__':
    main()
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
    'Cookie':'anonymid=jozr6a3d-h5z2ge; _de=67B57ED212200CFEE773B49343C73032; depovince=HUB; _r01_=1; ick_login=d3b902f4-91af-4c1f-863f-a7dd336fe34d; jebecookies=d94828ab-c47e-45c5-a978-dae313606ca3|||||; JSESSIONID=abcwmHt1ZRNwn6jihfZKw; p=8ab5526104597d8ff266c483257fb0175; first_login_flag=1; ln_uact=15313299416; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=cf7c3eb25853cc0542f0ef398d5df3915; societyguester=cf7c3eb25853cc0542f0ef398d5df3915; id=968910325; xnsid=cceb207f; ver=7.0; loginfrom=null; wp_fold=0'
}
r = requests.get(url,headers=headers)
print('Status_code:',r.status_code)

print(r.json())
response_dict = r.json()
print('Total respositories:',response_dict['total_count'])

repo_dicts = response_dict['items']
print(len(repo_dicts))

repo_dict = repo_dicts[0]
#遍历字典的键key
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)


print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
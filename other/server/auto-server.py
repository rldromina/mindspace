
# coding: utf-8

# In[1]:


import subprocess
import requests
import json
import os
import re
from time import sleep


# In[2]:


def start_server():
    os.chdir(r"C:\Users\mgrinberg\Desktop\disc c\Psico\Neurocomp\other")
    os.system(r"call C:\Users\mgrinberg\AppData\Local\Continuum\anaconda3\Scripts\activate.bat")
    os.system("set FLASK_APP=srv.py")
    os.system("start python srv.py")
    return None


# In[3]:


def get_tunnel():
    localhost_url = "http://localhost:4040/api/tunnels" #Url with tunnel details
    tunnel_url = requests.get(localhost_url).text #Get the tunnel information
    j = json.loads(tunnel_url)
    tunnel_url = j['tunnels'][0]['public_url']
    return tunnel_url

def replace_ngrok(tunnel_url):
    path = r"C:\Users\mgrinberg\Desktop\disc c\Psico\Neurocomp"
    path_idx = '\index.html'

    with open(path + path_idx, 'r+') as file:
        html = file.read()
        html = re.sub('(https://.+ngrok.+)/postdata', tunnel_url + '/postdata', html)
        file.seek(0)
        file.write(html)


# In[4]:


def commit_git(usr='cerebrock', repo = 'mindspace'):
    passw = input('Ingresar password: \n')
    os.chdir(path)
    os.system(f"git remote set-url origin https://{usr}:{passw}@github.com/cerebrock/{repo}.git")
    os.system("git add *")
    os.system("git commit -m 'auto'")
    os.system("git push origin master")
    return None


# In[ ]:


if __name__ == '__main__':
    while True:
        start_server()
        url = get_tunnel()
        replace_ngrok(url)
        commit_git()
        sleep(28000)
        os.system(r'taskkill /f /im ngrok.exe')


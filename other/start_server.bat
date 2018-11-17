call C:\Users\mgrinberg\AppData\Local\Continuum\anaconda3\Scripts\activate.bat
set FLASK_APP=srv.py
start flask run
start ngrok http 5000

::curl --silent --show-error http://127.0.0.1:4040/api/tunnels | sed -nE 's/.*public_url":"https:..([^"]*).*/\1/p'
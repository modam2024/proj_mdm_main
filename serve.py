from waitress import serve
from mdmproj1.wsgi import application

print("Django Server Started")

try:
    serve(application, host='0.0.0.0', port=8000)
except Exception as e:
    print("Server Error : ", e)

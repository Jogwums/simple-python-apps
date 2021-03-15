import requests
from win10toast import ToastNotifier
import json
import time

def update():
    r = requests.get('')
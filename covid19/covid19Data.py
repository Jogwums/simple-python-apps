import time
import COVID19Py
import matplotlib.pyplot as plt
from win10toast import ToastNotifier


def update():
    covid19 = COVID19Py.COVID19()
    data=covid19.getAll(timelines=True)
    virusdetails=dict(data["latest"])
    names=list(virusdetails.keys())
    values=list(virusdetails.values())
    # plt.bar(range(len(virusdetails)),values, tick_label=names)
    # plt.show()
    print(virusdetails)

    text = f'Confirmed : {values[0]} \nDeaths: {values[1]} \nRecovered: {values[2]}'

    while True:
        toast = ToastNotifier()
        toast.show_toast("Covid19 Stats", text, duration=20)
        time.sleep(20)

update()
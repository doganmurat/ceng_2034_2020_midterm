import os,requests,threading


cpuc = os.cpu_count()
print("Cpu core count value is: ", cpuc)

liste = list(os.getloadavg())


print("5 minute loadavg is ", liste[1])


if (cpuc - liste[1] < 1):
	exit()
else:
	print("5 minute loadavg is not near to cpu core count value")
"""


def check(url):
    r = request.get(url)
    if (r.status_code/200 < 1.495):
        print(url, " is working")
    else:
        print(url, " is not working")

thread1 = threading.Thread(target=check, args=("https://api.github.com",))
thread2 = threading.Thread(target=check, args=(​"http://bilgisayar.mu.edu.tr​",))
thread3 = threading.Thread(target=check, args=("https://www.python.org/​",))
thread4 = threading.Thread(target=check, args=("http://akrepnalan.com/ceng2034​",))
thread5 = threading.Thread(target=check, args=("​https://github.com/caesarsalad/wow​",))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

"""


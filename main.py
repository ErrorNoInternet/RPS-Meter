import time
import logging
import threading
from flask import Flask

rps = 0
rpsCounter = 0
requests = 0
highestRPS = 0
app = Flask('app')
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def clearRPS():
    while True:
        time.sleep(1)
        global rps
        global rpsCounter
        rps = rpsCounter
        rpsCounter = 0

@app.route('/')
def main():
    startTime = time.time()

    global requests
    requests += 1
    global rpsCounter
    rpsCounter += 1
    global highestRPS
    highestRPS = highestRPS

    if rps > highestRPS:
        highestRPS = rps

    html = """
    <body style="background-color: rgb(51, 51, 51);">
    <meta property="og:title" content="RPS Meter">
    <meta property="og:description" content="A simple requests per second meter">
    <title>RPS Meter</title>
    <font size="20">
    <div><p class="center" style="color:#ffffff;">""" + str(rps) + """ RPS</p></div>
    </font>
    <font size="2">
    <div><p class="center" style="color:#ffffff;"><b>""" + str(requests) + """</b> total requests<br>Highest RPS: <b>""" + str(highestRPS) + """</b><br><b>""" + str(round((time.time() - startTime) * 1000, 4)) + """</b> ms latency</p></div>
    </font>
    <style>
    .center {
            text-align: center
    }
    </style>
    """
    return html

threading.Thread(target=clearRPS).start()
app.run(host='0.0.0.0', port=8080)


from datetime import datetime
import psutil
from flask import Flask,request, render_template
from gpiozero import LED
from time import sleep
app = Flask(__name__)
led = LED(1)
led2 = LED(2)
@app.route("/")
def home():
    date_time = datetime.now()
    #CPU
    cpu_time = psutil.cpu_times()
    cpu_freq = psutil.cpu_freq()
    #Disks
    disk_usage = psutil.disk_usage('/')
    disk = psutil.disk_partitions()
    #Memory
    swap_memory = psutil.swap_memory()
    vitural_memory = psutil.virtual_memory()
    #Sensors
    sensors_temperature = psutil.sensors_temperatures()
    sensors_fans = psutil.sensors_fans()
    sensors_battery = psutil.sensors_battery()
    
    pc_users = psutil.users()
    return render_template('index.html',date_time=date_time,cpu_time=cpu_time,cpu_freq=cpu_freq,disk_usage=disk_usage,disk=disk
                           ,swap_memory=swap_memory,vitural_memory=vitural_memory,sensors_temperature=sensors_temperature
                           ,sensors_fans=sensors_fans,sensors_battery=sensors_battery,pc_users=pc_users)
if __name__ == "__main__":
    app.run(host = '0.0.0.0')
    led.on()
    led2.on()
    sleep(10)
    led.off()
    led2.off()
    sleep(10)

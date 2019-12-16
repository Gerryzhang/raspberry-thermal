import time
while True:
    #每间隔2s执行一次
    time.sleep(2)
    with open('/sys/class/thermal/thermal_zone0/temp','r') as f:
        #打印当前温度
        print(int(f.read()) / 1000)

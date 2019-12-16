import time

while True:
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        # 打印当前温度
        print("当前温度%.2f" % (int(f.read()) / 1000))
    # 每间隔2s执行一次
    time.sleep(2)

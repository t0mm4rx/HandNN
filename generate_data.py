import subprocess

def take_snapshot(n):
    subprocess.call('fswebcam -d /dev/video1 -S 10 --no-banner -r 640x480 data/right2/' + str(n) + '.png', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

last_index = 0
while True:
    take_snapshot(last_index)
    print(last_index)
    last_index += 1

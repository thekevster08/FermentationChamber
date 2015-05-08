import time
import subprocess

def read_temp_raw(device_file):
    catdata = subprocess.Popen(['cat',device_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out,err = catdata.communicate()
    out_decode = out.decode('utf-8')
    lines = out_decode.split('\n')
    return lines

def read_temp(device_file):
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:]!='YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equal_pos = lines[1].find('t=')
    if equal_pos != -1:
        temp_string = lines[1][equal_pos+2:]
        temp_c = float(temp_string)/1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f
from django.http import HttpResponse
from django.shortcuts import  render
import  struct
import socket
import time
def search_form(request):
    return render(request,'search_form.html')

def search(request,mac='1E-29-66-8F-67-0E'):
    request.encoding='utf-8'
    print("mac="+request.GET['q'])
    MAC = request.GET['q']
    BROADCAST = "59.44.20.194"   #ip地址
    if len(MAC) != 17:
        raise ValueError("MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")
    mac_address = MAC.replace("-",'')
    data = ''.join(['FFFFFFFFFFFF',mac_address * 20])
    print("data="+data)
    send_data = b''
    for i in range(0,len(data),2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])
    print("send_data="+send_data)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        return HttpResponse("关机成功")
    except Exception as e:
        return HttpResponse("关机失败"+e)

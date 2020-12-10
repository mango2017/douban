from django.http import HttpResponse
from django.shortcuts import  render
import  struct
import socket
import time
def search_form(request):
    return render(request,'search_form.html')


def search(request,mac='DC-4A-3E-78-3E-0A'):
    request.encoding='utf-8'
    print(request.GET['q'])
    MAC = request.GET['q']
    BROADCAST = "192.168.0.255"
    if len(MAC) != 17:
        raise ValueError("MAC address should be set as form 'XX-XX-XX-XX-XX-XX'")
    mac_address = MAC.replace("-",'')
    data = ''.join(['FFFFFFFFFFFF',mac_address * 20])
    send_data = b''

    for i in range(0,len(data),2):
        send_data = b''.join([send_data, struct.pack('B', int(data[i: i + 2], 16))])
    print(send_data)
    # if 'q' in request.GET   and request.GET['q']:
    #     message = '你搜索的内容为:'+ request.GET['q']
    # else:
    #     message = '你提交了空表单'
    # return HttpResponse(message)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        time.sleep(1)
        sock.sendto(send_data, (BROADCAST, 7))
        # return HttpResponse()
        return HttpResponse("关机成功")
    except Exception as e:
        return HttpResponse("关机失败"+e)
        # print(e)
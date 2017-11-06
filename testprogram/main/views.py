import json
from django.contrib.auth.decorators import login_required
from operator import methodcaller
import re
# from netmiko import ConnectHandler
# import sys
from ciscoconfparse import CiscoConfParse
from django.shortcuts import render
@login_required
def index(request):
    # net_connect = ConnectHandler(device_type='cisco_ios', ip='ip_address', username='usernamecisco', password='passwordcisco')
    # net_connect.find_prompt()
    # output = net_connect.send_command("show run")
    # tidak bisa tes koneksi langsung karena ssh cisco tidak bisa di open "connection refused"

    # contoh config langsung
    parse = CiscoConfParse("media/contoh.txt") #open file di folder media

    # contoh output parse interfaces
    active_intfs = parse.find_parents_wo_child("^interf", "shutdown")
    jso= json.dumps([dict(interfaces=inter) for inter in active_intfs])
    with open('media/output.json', 'w') as f:
        f.write(json.dumps(jso, indent=4)) #membuat nama file di folder media namanya output.json
    return render(request,"index.html",{"parse":active_intfs,"json":jso})


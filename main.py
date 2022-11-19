import requests
import pull
import json
from datetime import datetime as dt
from time import sleep

proxies = dict(
    http="socks5://172.27.144.1:7890",
    https="socks5://172.27.144.1:7890"
    )

bearer_token = "rMQ91DrZFRfDHoP5GbmjG3dQ8iMZk/XnPq4couGYACKMf5AoCSwAr/D9NcFvnHpZ-adnan"
URL = "https://api.kirimwa.id/v1/"
WEBHOOK_URL = "https://webhook.site/8536b5b8-b964-4e34-827d-33495874aeff"

GROUP_ID = "120363028252064433"

KAMAR = ["tahfidz", "kamar1", "kamar2", "kamar3", "kamar4", "kamar5", "kamar6", "kamar7", "kamar8", "kamar9"]
USTD = ["hendra", "mahmud", "mahmud", "iman", "aris", "anshar", "syukron", "adnan", "anshar", "iman"]

def deleteDatainWebhook():
    print(dt.strftime(dt.now(),'[%Y/%m/%d %H:%M]')+" Procces delete data in webhooks")
    r = requests.delete(url=WEBHOOK_URL+"/request", proxies=proxies)
    if r.status_code != 200:
        print(dt.strftime(dt.now(),'[%Y/%m/%d %H:%M]')+" Delete data in webhooks FAILURE")
        sleep(5)
        deleteDatainWebhook()
    else:
        print(dt.strftime(dt.now(),'[%Y/%m/%d %H:%M]')+" Delete data in webhooks SUCCESS")
    

def getMessagesinWebhook():
    data_js = []
    print(dt.strftime(dt.now(),'[%Y/%m/%d %H:%M]')+" Load to Get message from GROUP_ID")
    # r = requests.get(url=WEBHOOK_URL+"/requests", proxies=proxies)
    r = requests.get(url=WEBHOOK_URL+"/requests")
    if r.status_code != 200:
        print(dt.strftime(dt.now(),'[%Y/%m/%d %H:%M]')+" Load to Get message FAILURE, STATUS_CODE : " + str11(r.status_code))
        sleep(5)
        getMessagesinWebhook()
    else:
        print(dt.strftime(dt.now(),'[%Y/%m/%d %H:%M]')+" Load to Get message SUCCESS")
        for data in r.json()['data']:
            data_js.append(json.loads(data['content']))
        return data_js

def change_name_(form):
    """form is dictonary
    {
        "kamar": "kamar1-tahfidz",
        "pulang": [],
        "sakit": []
    }
    """
    if form["kamar"] != "tahfidz":
        form["kamar"] = form["kamar"].replace("kamar","")
    list_sp = pull.list_with_specific("kamar",form["kamar"])
    nama = [k[1] for k in list_sp]
    print("Data santri sebelum di-edit: ", form)
    if len(form["pulang"]):
        for pul in form["pulang"]:
            pass

def msg_to_dict(msg):
    global status
    for mes in msg:
        text_message = mes['payload']['text']
        id_message = mes['payload']['id']
        arr_txt_line = text_message.replace('\t', '').split('\n')
        pulang_start = 0
        pulang_stop = 0
        sakit_start = 0
        sakit_stop = len(arr_txt_line)
        status = False
        # ==== Loop kamar untuk mendapatkan status kamar ====
        for kam in KAMAR:
            # ==== penyaringan per-tama untuk status kamar ====
            kamr = ""
            if kam in text_message.rsplit():
                # ==== looping untuk number line dari arr_txt_line (pesan dalam array pemisah new line) ====
                stat_sp = None
                for num in range(len(arr_txt_line)):
                    if arr_txt_line[num] == "pulang" or arr_txt_line[num] == "pulang:":
                        pulang_start = num+1
                        status = True
                    if arr_txt_line[num] == "sakit" or arr_txt_line[num] == "sakit:":
                        pulang_stop = num
                        sakit_start = num+1
                        status = True
            else: continue
        return [status, pulang_start, pulang_stop, sakit_start, sakit_stop, arr_txt_line, text_message]
            # break

def start():
    while True:
        # msg = getMessagesinWebhook()
        msg = [
            {"payload": {
                "text": "kamar7\npulang\n1. andika (sakit)\n2. aldi van reza (acara keluarga)\nsakit\n1. amar (demam)",
                "id": 123
                }
            },
            {"payload": {
                "text": "kamar8\npulang\n1. adhitya\n2. zidane (acara keluarga)\nsakit\n1. makmur (demam)",
                "id": 122
                }
            },
            {"payload": {
                "text": "tahfidz\npulang\n1. rafael (acara keluarga)\n2. faisal (sakit)\nsakit\n1. yazid (demam)",
                "id": 121
                }
            }
            ]
        if len(msg) != 0:
            # jika ada data maka mendelete data di webhook
            # deleteDatainWebhook()
            pass
        hass = msg_to_dict(msg)
        if hass[0]:
            print("\n\n")
            print("="*10+"\nIni data Pulang\n"+"="*10)
            print(hass[5][hass[1]:hass[2]])
            print("="*10+"\nIni data sakit\n"+"="*10)
            print(hass[5][hass[3]:hass[4]])
        else:
            print("Input message salah")
            print("="*10)
            print("Format Text: "+hass[6])
            print("="*10)
            print("Format Array/List: ")
            print(hass[5])
            print("="*10)
        sleep(5)



if __name__ == "__main__":
    start()

import requests
import json
from datetime import datetime as dt
from time import sleep

proxies = dict(
    http="socks5://172.27.144.1:7890",
    https="socks5://172.27.144.1:7890"
    )

bearer_token = "rMQ91DrZFRfDHoP5GbmjG3dQ8iMZk/XnPq4couGYACKMf5AoCSwAr/D9NcFvnHpZ-adnan"
URL = "https://api.kirimwa.id/v1/"
WEBHOOK_URL = "https://webhook.site/token/67cba561-639e-48e4-87e0-0dab27133097"

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
    r = requests.get(url=WEBHOOK_URL+"/requests", proxies=proxies)
    if r.status_code != 200:
        print(dt.strftime(dt.now(),'[%Y/%m/%d %H:%M]')+" Load to Get message FAILURE")
        sleep(5)
        getMessagesinWebhook()
    else:
        print(dt.strftime(dt.now(),'[%Y/%m/%d %H:%M]')+" Load to Get message SUCCESS")
        for data in r.json()['data']:
            data_js.append(json.loads(data['content']))
        return data_js

def start():
    while True:
        msg = getMessagesinWebhook()
        if len(msg) != 0:
            # jika ada data maka mendelete data di webhook
            deleteDatainWebhook()
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
                if kam in text_message.rsplit():
                    # ==== looping untuk number line dari arr_txt_line (pesan dalam array pemisah new line) ====
                    stat_sp = None
                    for num in range(len(arr_txt_line)):
                        if arr_txt_line[num] == "pulang" or arr_txt_line[num] == "pulang:":
                            stat_sp = "pulang"
                            pulang_start = num+1
                            status = True
                        if arr_txt_line[num] == "sakit" or arr_txt_line[num] == "sakit:":
                            stat_sp = "sakit"
                            pulang_stop = num
                            sakit_start = num+1
                            status = True
                else: continue
            # ==== jika ada data ====
            print("pul_start: "+str(pulang_start), end=', ')
            print("pul_stop: "+str(pulang_stop))
            print("sakit_start: "+str(sakit_start), end=', ')
            print("sakit_stop: "+str(sakit_stop))
            if status:
                print("\n\n")
                print("="*10+"\nIni data Pulang\n"+"="*10)
                print(arr_txt_line[pulang_start:pulang_stop])
                print("="*10+"\nIni data sakit\n"+"="*10)
                print(arr_txt_line[sakit_start:sakit_stop])
            else:
                print("Input message salah")
                print("="*10)
                print("Format Text: "+text_message)
                print("="*10)
                print("Format Array/List: ")
                print(arr_txt_line)
                print("="*10)
        break
        # sleep(5)



if __name__ == "__main__":
    start()

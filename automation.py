import os
import time
from ccq_api import ccq_stat
from twilio.rest import Client

account_sid = "AC4d1c5954d9228371bcd3fce922093c26"
auth_token = "071302b5888b57adbd7ac8bb3c482941"

#account_sid = os.environ.get('TWILIO_ACC_SID')
#auth_token = os.environ.get('TWILIO_AUTH_TOK')
#if not account_sid or not auth_token:
#    raise ValueError('TWILIO_ACC_SID and TWILIO_AUTH_TOK envvars must be set')
client = Client(account_sid, auth_token)


def ccq_stat_auto(phone, jid):
    running_chk = False

    while True:
        status_update = ccq_stat(phone, jid)[jid]
        
        print(f"{jid}: {status_update['status']}")
        if status_update['status'] == "Running" and not running_chk:
            send_text(f"Job {jid} is Running", phone)
            running_chk = True

        elif status_update['status'] == "Completed":
            send_text(f"Job {jid} is Completed", phone)
            break
        
        elif status_update['status'] == "Deleting":
            break

        time.sleep(6)

def send_text(text_2_send, phone):
    sent_data = client.messages.create(
        body=text_2_send[:1500],
        from_='+12055462249', to=phone)
    return sent_data

import os
from threading import Thread
from ccq_api import ccq_del, ccq_stat, ccq_sub
from twilio.rest import Client
from automation import ccq_stat_auto
import emoji

#account_sid = os.environ.get('TWILIO_ACC_SID')
#auth_token = os.environ.get('TWILIO_AUTH_TOK')
#if not account_sid or not auth_token:
#    raise ValueError('TWILIO_ACC_SID and TWILIO_AUTH_TOK envvars must be set')

account_sid = "TWILIO_SID"
auth_token = "TWILIO_AUTH_TOKEN"

client = Client(account_sid, auth_token)

def process_msg():
    msg_data = client.messages.list(limit=1)[0]
    user_msg = msg_data.body
    phone = msg_data.from_
    print(f'Processing: "{user_msg}" from "{phone}".')

    text_2_send = parse_msg(user_msg, phone)
    sent_data = send_text(text_2_send, phone)

    print(f'Sending: "{sent_data.body}" to "{sent_data.to}".')


def parse_msg(user_msg, phone):
    split_msg = user_msg.split()

    if len(split_msg) == 1:
        cmd = split_msg[0]
    elif len(split_msg) == 2:
        if split_msg[1].isdecimal():
            cmd, jid = split_msg
            if len(jid) != 4:
                return "Error"
        cmd, script_loc = split_msg

    elif len(split_msg) > 2:
        return "Error"

    if cmd.lower() == "submit":
        res = ccq_sub(phone, script_loc)
        Thread(target=ccq_stat_auto, args=[phone, res]).start()
        return f"Submission in Progress - {res}"

    elif cmd.lower() == "status":
        if 'jid' in locals():
            return f"Status: {ccq_stat(phone, jid)}"
        else:
            return f"Statuses: {ccq_stat(phone, None)}"

    elif cmd.lower() == "delete":
        return f"Deleted - {ccq_del(phone, jid)}"

    elif cmd.lower() == "helpme":
        return ("Commands: \n To Submit Filepath ------- submit filepath\
                \n To\nView Job Status ------- status JOB-ID \n To Delete\
                Job ------- delete JOB-ID")
    
    elif cmd.lower() == "demo-time":
        #return f"IT'S TIME EVERYONE!"
        return emoji.emojize("IT'S DEMO TIME!!! :partying_face: :partying_face: :partying_face: :partying_face: :partying_face: :partying_face: :party_popper: :party_popper: :party_popper:")

    else:
        return "Error"


def send_text(text_2_send, phone):
    sent_data = client.messages.create(
        body=text_2_send[:1500],
        from_='+12055462249', to=phone)
    return sent_data

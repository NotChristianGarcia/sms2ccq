import os
from ccq_api import ccq_del, ccq_stat, ccq_sub
from twilio.rest import Client

account_sid = "AC4d1c5954d9228371bcd3fce922093c26"
auth_token = "071302b5888b57adbd7ac8bb3c482941"

#account_sid = os.environ.get('TWILIO_ACC_SID')
#auth_token = os.environ.get('TWILIO_AUTH_TOK')
#if not account_sid or not auth_token:
#    raise ValueError('TWILIO_ACC_SID and TWILIO_AUTH_TOK envvars must be set')
client = Client(account_sid, auth_token)


def process_msg():
    msg_data = client.messages.list(limit=1)[0]
    user_msg = msg_data.body
    phone = msg_data.from_
    print(f'Processing: "{user_msg}" from "{phone}".')

    text_2_send = parse_msg(user_msg, phone)
    sent_data = send_msg(text_2_send, phone)

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
        return f"Submission in Progress - {ccq_sub(phone, script_loc)}"

    elif cmd.lower() == "status":
        if 'jid' in locals():
            return f"Status: {ccq_stat(phone, jid)}"
        else:
            return f"Statuses: {ccq_stat(phone, None)}"

    elif cmd.lower() == "delete":
        return f"Deleted - {jid}"

    elif cmd.lower() == "helpme":
        return ("Commands: \n To Submit Filepath ------- submit filepath\
                \n To\nView Job Status ------- status JOB-ID \n To Delete\
                Job ------- delete JOB-ID")

    else:
        return "Error"


def send_msg(text_2_send, phone):
    sent_data = client.messages.create(
        body=text_2_send,
        from_='+12055462249', to=phone)
    return sent_data
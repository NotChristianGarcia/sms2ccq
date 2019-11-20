from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from ccq_api import ccq_del, ccq_stat, ccq_sub

account_sid="AC4d1c5954d9228371bcd3fce922093c26"
auth_token="02bc72aad5788a27f84db756e124291a"
client = Client(account_sid, auth_token)



app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
	user_msg = client.messages.list(limit=1)[0].body


	# Start our response
	resp = MessagingResponse()


	split_msg = user_msg.split()


	if len(split_msg) == 1:
		cmd = split_msg[0]
	elif len(split_msg) == 2:
		if split_msg[1].isdecimal():
			cmd, jid = split_msg
			if len(jid) != 4:
				resp.message("Error")
				return str(resp)
		else:
			cmd, script_loc = split_msg

	elif len(split_text) > 2:
		resp.message("Error")
		return str(resp)


	if cmd.lower() == "submit":
		resp.message(f"Submission in Progress - {jid}")

	elif cmd.lower() == "status":
		resp.message(f"Status: {ccq_stat('16507999956', jid)}")

	elif cmd.lower() == "delete":
		resp.message(f"Deleted - {jid}")

	elif cmd.lower() == "helpme":
		resp.message("Commands: \n To Submit Filepath ------- submit filepath \n To View Job Status ------- status JOB-ID \n To Delete Job ------- delete JOB-ID")

	else:
		resp.message("Error")

	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)

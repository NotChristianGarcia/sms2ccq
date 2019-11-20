import os
import time
from messaging import send_msg
   
def ccq_stat_auto(phone, jid):
	running_chk = False

	status_update = ccq_stat(phone,jid)

	while True:  
		if status_update['status'] == "Running" and not running_chk:
			send_msg(f"Job {jid} is Running", phone)
			running_chk = True

		elif status_update['status'] == "Completed":
        		send_msg(f"Job {jid} is Completed", phone)
			break
	
		time.sleep(6)

   
	def ccq_stat_auto(phone, jid):

   'jid' in locals():
         return f"Status: {ccq_stat(phone, jid)}"
     else:
         return f"Statuses: {ccq_stat(phone, None)}"



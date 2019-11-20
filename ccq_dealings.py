import ccqclient as cc
import json
import re

# default ccq instance
hostname = 'crappieshrimpcitrine.cloudycluster.net'
username = 'sms2ccq'
password = 'Sms2ccqsms2ccq'
cloud = cc.CCQCloud.GCP
scheduler = cc.CCQScheduler.Slurm

client = cc.CCQClient(hostname, username, password, cloud, scheduler)


def ccq_stat(phone, jid):
    if jid:
        stat_res = client.ccqstat(jid)
    else:
        stat_res = client.ccqstat()

    final_res = {}
    for res in stat_res:
        final_res[res.job_id] = {
            'name': res.job_name,
            'scheduler': res.scheduler_name,
            'status': res.job_status}
    return final_res

def ccq_del(phone, jid):
    del_res = client.ccqdel(jid)
    if json.loads(del_res)['status'] == 'success':
        return 'success'
    return 'no_success'

def ccq_sub(phone, script_loc):
    split_loc = script_loc.split('/')
    job_path = '/'.join(split_loc[:-1])
    job_name = split_loc[-1]
    sub_res = client.ccqsub(job_path, job_name, '')
    jid = re.findall(r"[0-9]{4}", sub_res)
    return jid

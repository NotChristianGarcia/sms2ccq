import enum
import hashlib
import json
import os
import tempfile
import urllib.request
import webdav3.client

def raw_ccqdel(hostname, username, password, jobId):
    encodedUserName = username
    encodedPassword = password
    jobForceDelete = ""
    valKey = "unpw"
    dateExpires = ""
    certLength = 0
    ccAccessKey = ""
    remoteUserName = username
    databaseDelete = ""
    data = {"jobId": str(jobId), "userName": str(encodedUserName), "instanceId": None, "jobNameInScheduler": None, "password": str(encodedPassword), "jobForceDelete": jobForceDelete, 'schedulerType': None, 'schedulerInstanceId': None, 'schedulerInstanceName': None, 'schedulerInstanceIp': None, "valKey": str(valKey), "dateExpires": str(dateExpires), "certLength": str(certLength), "ccAccessKey": str(ccAccessKey), "remoteUserName": str(remoteUserName), "databaseDelete": str(databaseDelete)}
    url = "https://%s/srv/ccqdel" % hostname
    data = json.dumps(data).encode()
    headers = {"Content-Type": "application/json"}
    request = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(request).read().decode()
    #response = json.loads(response)
    return response#["payload"]["message"]

def raw_ccqstat(hostname, username, password, jobId="all", printErrors="", printOutputLocation="",
    printInstancesForJob="", databaseInfo=""):
    encodedUserName = username
    encodedPassword = password
    verbose = False
    instanceId = None
    schedulerName = "default"
    valKey = "unpw"
    dateExpires = ""
    certLength = 0
    ccAccessKey = ""
    remoteUserName = username
    printNumberOfInstancesRegistered = ""
    data = {"jobId": str(jobId), "userName": str(encodedUserName), "password": str(encodedPassword), "verbose": verbose, "instanceId": None, "jobNameInScheduler": None, "schedulerName": str(schedulerName), "schedulerType": None, "schedulerInstanceId": None, "schedulerInstanceName": None, "schedulerInstanceIp": None, "printErrors": str(printErrors), "valKey": str(valKey), "dateExpires": str(dateExpires), "certLength": str(certLength), "jobInfoRequest": False, "ccAccessKey": str(ccAccessKey), "printOutputLocation": str(printOutputLocation), "printInstancesForJob": str(printInstancesForJob), "remoteUserName": str(remoteUserName), "databaseInfo": str(databaseInfo), "printNumberOfInstancesRegistered": str(printNumberOfInstancesRegistered)}
    url = "https://%s/srv/ccqstat" % hostname
    data = json.dumps(data).encode()
    headers = {"Content-Type": "application/json"}
    request = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(request).read().decode()
    response = json.loads(response)
    return response["payload"]["message"]

def raw_ccqsub(hostname, username, password, path, name, jobScript, volumeType, schedType):
    numberOfInstancesRequested = 1
    numCpusRequested = 1
    stdoutFileLocation = "default"
    stderrFileLocation = "default"
    memoryRequested = "1000"
    useSpot = "no"
    spotPrice = None
    requestedInstanceType = "default"
    networkTypeRequested = "default"
    optimizationChoice = "cost"
    criteriaPriority = "mcn"
    schedulerToUse = "default"
    certLength = 0
    output = "/home/%s" % username
    justPrice = ""
    useSpotFleet = "False"
    spotFleetWeights = None
    spotFleetTotalSize = None
    spotFleetType = "lowestPrice"
    terminateInstantly = "False"
    skipProvisioning = "False"
    submitInstantly = "False"
    timeLimit = "None"
    createPInstances = "False"
    image = "None"
    maxIdle = 5
    placementGroupName = None
    useGpu = "False"
    gpuType = None
    usePreemptible = "False"
    cpuPlatform = None
    maintain = "False"

    jobScriptLocation = path
    jobScriptText = jobScript
    jobName = name
    ccOptionsParsed = {"numberOfInstancesRequested": str(numberOfInstancesRequested),  "numCpusRequested": str(numCpusRequested), "wallTimeRequested": "None", "stdoutFileLocation": str(stdoutFileLocation), "stderrFileLocation": str(stderrFileLocation), "combineStderrAndStdout": "None", "copyEnvironment": "None", "eventNotification": "None", "mailingAddress": "None", "jobRerunable": "None", "memoryRequested": str(memoryRequested), "accountToCharge": "None", "jobBeginTime": "None", "jobArrays": "None", "useSpot": str(useSpot), "spotPrice": str(spotPrice), "requestedInstanceType": str(requestedInstanceType), "networkTypeRequested": str(networkTypeRequested), "optimizationChoice": str(optimizationChoice),  "pathToExecutable": "None", "criteriaPriority": str(criteriaPriority), "schedulerToUse": str(schedulerToUse), "schedType": str(schedType), "volumeType": str(volumeType), "certLength": str(certLength), "jobWorkDir": str(output), "justPrice": str(justPrice), "ccqHubSubmission": "False", "useSpotFleet": str(useSpotFleet), "spotFleetWeights": str(spotFleetWeights), "spotFleetTotalSize": spotFleetTotalSize, "spotFleetType": str(spotFleetType), "terminateInstantly": str(terminateInstantly), "skipProvisioning": str(skipProvisioning), "submitInstantly": str(submitInstantly), "timeLimit": str(timeLimit), "createPInstances": str(createPInstances), "image": str(image), "maxIdle": str(maxIdle), "placementGroupName": str(placementGroupName), "useGpu": str(useGpu), "gpuType": str(gpuType), "usePreemptible": str(usePreemptible), "cpuPlatform": str(cpuPlatform), "maintain": str(maintain)}
    jobMD5Hash = hashlib.md5("".join(jobScript.split()).encode()).hexdigest()
    encodedUserName = username
    encodedPassword = password
    valKey = "unpw"
    dateExpires = ""
    certLength = 0
    ccAccessKey = ""
    remoteUserName = username
    data = {"jobScriptLocation": str(jobScriptLocation), "jobScriptFile": str(jobScriptText), "jobName": str(jobName), "ccOptionsCommandLine": ccOptionsParsed, "jobMD5Hash": jobMD5Hash, "userName": str(encodedUserName), "password": str(encodedPassword), "valKey": str(valKey), "dateExpires": str(dateExpires), "certLength": str(certLength), "ccAccessKey": str(ccAccessKey), "remoteUserName": str(remoteUserName)}

    data["ccOptionsCommandLine"]["userSpecifiedInstanceType"] = "false"

    url = "https://%s/srv/ccqsub" % hostname
    data = json.dumps(data).encode()
    headers = {"Content-Type": "application/json"}
    request = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(request).read().decode()
    response = json.loads(response)
    return response["payload"]["message"]

class CCQJob:
    def __init__(self, client, job_id, job_name, scheduler_name, job_status):
        self.client = client
        self.job_id = job_id
        self.job_name = job_name
        self.scheduler_name = scheduler_name
        self.job_status = job_status

    def __repr__(self):
        return "CCQJob(%s, %s, %s, %s)" % (self.job_id, self.job_name, self.scheduler_name, self.job_status)

    def info(self):
        return raw_ccqstat(self.client.hostname, self.client.username, self.client.password, jobId=self.job_id, databaseInfo="True")

    def errors(self):
        return raw_ccqstat(self.client.hostname, self.client.username, self.client.password, jobId=self.job_id, printErrors="True")

    def output(self):
        return raw_ccqstat(self.client.hostname, self.client.username, self.client.password, jobId=self.job_id, printOutputLocation="True")

    def instances(self):
        return raw_ccqstat(self.client.hostname, self.client.username, self.client.password, jobId=self.job_id, printInstancesForJob="True")

class CCQCloud(enum.Enum):
    AWS = enum.auto()
    GCP = enum.auto()

class CCQScheduler(enum.Enum):
    Slurm = enum.auto()
    Torque = enum.auto()

class CCQClient:
    def __init__(self, hostname, username, password, cloud, scheduler):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.cloud = cloud
        self.scheduler = scheduler

    def ccqstat(self, jobId='all'):
        data = raw_ccqstat(self.hostname, self.username, self.password, jobId)

        jobs = []
        for item in data.split("\n")[2:]:
            if len(item) == 0:
                break
            x = item.split()
            jobs.append(CCQJob(self, x[0], x[1], x[2], x[3]))

        return jobs

    def ccqsub(self, job_path, job_name, job_body, vol_type=None):
        if not vol_type:
            if self.cloud == CCQCloud.AWS:
                vol_type = "ssd"
            elif self.cloud == CCQCloud.GCP:
                vol_type = "pd-ssd"

        if self.scheduler == CCQScheduler.Slurm:
            scheduler = "SLURM"
        elif self.scheduler == CCQScheduler.Torque:
            scheduler = "Torque"

        f = tempfile.NamedTemporaryFile(delete=False)
        f.write(job_body.encode())
        f.close()

        client = webdav3.client.Client({"webdav_hostname": "https://%s" % self.hostname, "webdav_login": self.username, "webdav_password": self.password})
        client.download(job_path + job_name, job_name)

        job_body = ""
        with open(job_name, 'r') as script:
            for line in script.readlines():
                job_body += line

        return raw_ccqsub(self.hostname, self.username, self.password, job_path, job_name, job_body, vol_type, scheduler)

    def ccqdel(self, jobId):
        return raw_ccqdel(self.hostname, self.username, self.password, jobId)

# SMS2CCQ Hackathon Project
#### The Team:                                                                      
 Christian R. Garcia - github.com/notchristiangarcia
 Cindy Yongoueth - github.com/cyyongoueth
 Avery Giles - github.com/averyrgiles

#### The Event:
The event page is hackhpc.org. The event supplied mentorship from employees at Omnibond to help facilitate learning of the CloudyCluster platform along with additional help from some TACC employees and volunteers.

#### Project Description:
This project allows users to take control of their HPC jobs via text. This project interfaces with Omnibond's CloudyCluster platform which makes of the Google Cloud Platform and job management to scale up HPC job resources. The project also relies on Twilio, a communication API for SMS that allows developers to receive and send SMS.

This project gives users access to the status, delete, and submit commands for CloudyCluster. The project also gives automated text messages when important state changes happen on your CloudyCluster job when you submit the job with our script. This automation is done in parallel to our script, so it is non-blocking and runs in the background.

#### Examples:
Texting your setup Twilio number with ```submit sample_job.sh``` would result in a CloudyCluster job starting with the script located on your CloudyCluster server at ~/sample_job.sh and a text containing your CloudyCluster jobId. The submit command also results in automation text to be sent, once a job is submitted another parallel script begins and will text when your CloudyCluster job reaches the "Running" and "Completed" states.

Texting your setup Twilio number with ```status``` or ```status $(jobId)``` would result in a receiving status messages for all or a particular job. The status consists of jobId, script, scheduler, and, state.

Texting your setup Twilio number with ```delete $(jobId)``` would result in the deletion of the particular job and a text mentioning success or not.

Texting your setup Twilio number with ```helpme``` results in a text containing a list of possible commands.

Texting your setup Twilio number with ```demo-time``` results in a easter egg of emojis.

#### Issues:
Due to the nature of a hackathon, our issues will stay forever unfixed.
An attempt was made to dockerize our project to allow for easy deployment, however network ports on the twilio tunnel were not able to be ported to the host computer. This resulted in non-communication.
	Potential fix: Put all containers in the docker-compose on one network so they talk to each other as they don't need to be exposed to the outside world.

An attempt was also made to allow for linked authentication of phone number and CloudyCluster instance with a Redis database. Time constraints ruined this.

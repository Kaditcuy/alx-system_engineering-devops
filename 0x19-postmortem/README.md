# Apache Server Failure

## Date of Incident: 
[Fri, 3 Mar 2023 07:32:16 WAT]

## Summary:
[A 500 Internal server error was returned when trying to reach the Apache server making the rsources requested from the server unavailable for endusers.]

## Timeline of events:
* 7:32 AM - Our monitoring system detected a 500 Internal Server was reached from our server logs

* 7:40 AM - Upon receiving an alert, our on-call engineer initiated an investigation into the issue.

* 7:45 AM - The engineer noticed when trying to reach the server locally that a 500 Internal Server error was reached verifying the alert

* 7:50 AM - The engineer checked the apache configuration file to check which port it was configured to listen on and used netstat to check if its actually listening on that port, the access and error log files where also checked, check to make sure the apache serviice is running.

* 8:20 AM - The enginner finally used strace to trace the open,read and write requests made by apache, where a wrong misspelt php file was discovered in the wordpress settings file and was fixed.

* 8:25 AM - A puppet script was written to automate the fixing process

## Resolution:
[The enginner finally used strace to trace the open,read and write requests made by apache, where a wrong misspelt php file was discovered in the wordpress settings file and was fixed and a puppet script was written to automate the fixing process].

## Lessons Learned:
[To always be syntathically careful when naming files]

Recommendations:
* Have someone to regularly check through all the files hosted on the server for any synthax error.

* Provide webstack debuuging training for junior engineers.

## Conclusion:
The outage on 3 March caused by a syntax error in the maning of one of the files in the wordpress settings that caused a denial of our server to endusers. The issue was resolved using strace and automated using puppet. Going forward, we will be implementing several corrective and preventative measures to prevent similar issues and improve our overall web stack reliability.

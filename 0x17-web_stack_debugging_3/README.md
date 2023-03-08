#  Web stack debugging #3

## Commands to run to help when debugging webservers

* Check if the web server has started
	`service <webserver> status`

* Check the process list
	`ps aux`

* Check your webserver configuration, to verify what port it should listen to and to ensure its listening on said port (port 80 and 443 are the ideal ports for http and https traffic respectively).
	`/etc/ directory is your friend :)` common webservers and their corresponding configuration locations:
	```
	apache2 -> /etc/apache2/apache2.conf
	nginx -> /etc/nginx/nginx.conf
	lighttpd -> /etc/lighttpd/lighttpd.conf
	```
But its best to just check with the documentation of the web server you're using to know where its configuration files are kept.

* Check if its listening on the port specified in its config file, in our case either 80 or 443
	`netstat -lpdn`

* Check if a firewall is enabled
	`sudo ufw status`

* Check the log files
	```
	tail -f /var/log/<webserver>/error.log
	tail -f /var/log/<webserver>/access.log
	```
will display the last 10lines of the files and keep updating the entries as new logs ae added

* Can I connect to the HTTP port from the location I am browsing from?
	`curl 127.0.0.1:80/443<port for http traffic>

* Check if the process is running
	`pgrep and ps`
	```
	pgrep -lf <name of the process> -> gives process pid
	```

Used strace -p (pid of process to attach to strace) -e trace=open,read,write  to attach the aapache service process for monitoring for all read open and write system calls apache will make, then i curled my loopback which is being hosted by apache to see exactly what the error is with apache that was given a 500 Internal server error, it was an open system call to a wordpress file that had a misspelling of phpp instead of php, the script 0-strace_is_your_friend.pp is a puppet script that fixes the above error

## Side notes and more:
REcently encountered something that i woud like to note here, so flask by default listens on port 5000, so i started the flask server with a python script and i noticed that port 5000 was in use, this was how i solved it

* sudo lsof -i | grep :5000 -> To see the process id and name associated with it
* ps -p <PID> -o comm -> to get more details about the process
* sudo kill <pid> -> to terminate it

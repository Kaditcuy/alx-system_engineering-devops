# Webstack monitoring
## `DevOPs` `SysAdmin` `monitoring`

* Installed datadog agent on server web-01, created an application key and updated user profile with both api key and application key.

```
For context: Datadog is a monitoring software
```

* gethost.sh -> Script to validate server/host running datadog agent

References: https://www.linkedin.com/pulse/error-forbidden-datadog-postmortem-andres-castaneda/?trk=public_profile_article_view

* 1) Set up a monitor to monitor read and write requests issued to the device per second
	System mertic for that is:
	```
	system.io.r_s --> read
	system.io.w_s --> write
	```

* 2) Set up a dashboard and fetched its id using datadogs api
	seen in `getDashID.sh` script.

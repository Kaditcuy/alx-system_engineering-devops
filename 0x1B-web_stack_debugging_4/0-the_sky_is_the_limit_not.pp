# Fixed number of max open files per process "ulimit" for nginx


exec { 'Nginx-max_file_dp-fix':
	command => "/bin/sed -i /etc/default/nginx -e 's/15/4096/'",
}

exec { 'restart nginx':
	command => '/usr/bin/service nginx restart',
	require => Exec['Nginx-max_file_dp-fix']
}

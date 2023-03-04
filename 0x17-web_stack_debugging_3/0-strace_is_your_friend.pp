#debugging today a Wordpress website running on a LAMP stack

# Using strace, find out why Apache is returning a 500 error
# found out issue is a mispelled resource, a fix is automated with Puppet

exec { 'fix-wordpress-mispelled-resource':
  command => "/bin/sed -i /var/www/html/wp-settings.php \
  -e 's/class-wp-locale.phpp/class-wp-locale.php/'"
}

# Using puppet to install flask from pip3
# Requirements flask must be of version 2.1.0

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

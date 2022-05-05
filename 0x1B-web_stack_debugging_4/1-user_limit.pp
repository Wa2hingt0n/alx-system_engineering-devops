# Enable the user holberton to login and open files without error.

exec { 'increase_hard_file_limit':
  command => 'sed -i "/holberton hard/s/5/10000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for Holberton user.
exec { 'increase_soft_file_limit':
  command => 'sed -i "/holberton soft/s/4/10000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
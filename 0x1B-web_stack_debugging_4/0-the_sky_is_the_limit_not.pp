# Allows Nginx to accept more requests

exec { 'fix':
  command => 'sed -i "s/15/4000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
} ->

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
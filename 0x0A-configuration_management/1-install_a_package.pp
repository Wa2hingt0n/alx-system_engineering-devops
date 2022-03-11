# Installs puppet-lint version 2.5.0

exec { 'gem install puppet-lint':
  command => '/usr/bin/gem install puppet-lint'
}

package { 'puppet-lint':
  ensure  => '2.5.0',
  require => Exec['gem install puppet-lint']
}
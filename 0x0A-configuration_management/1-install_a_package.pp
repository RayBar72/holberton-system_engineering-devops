#Installing Puppet-lint version 2.5.0
exec { 'puppet-lint':
  command => '/bin/gem install puppet-lint -v 2.5.0'
}

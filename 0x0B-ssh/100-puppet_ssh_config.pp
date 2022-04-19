# Setting up client ssh
file_line { 'Using ssh key school':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '  IdentityFile ~/.shh/school',
  replace =>  true,
}
file_line { 'Disable password authent':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '  PasswordAuthentication no',
  replace =>  true,
}

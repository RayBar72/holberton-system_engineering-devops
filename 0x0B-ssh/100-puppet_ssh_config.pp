# Setting up client ssh
file_line { 'Turn off passwd auth':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '  PasswordAuthentication no',
  replace =>  true,
}
file_line { 'Declare identity file':
  path    =>  '/etc/ssh/ssh_config',
  line    =>  '  IdentityFile ~/.shh/school',
  replace =>  true,
}


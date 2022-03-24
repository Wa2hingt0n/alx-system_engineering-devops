# Update the advanced package tool
exec { 'update software packages':
  command => 'apt-get update',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# Installing nginx
package { 'nginx':
  ensure => 'installed',
}

# Change access rights
exec { 'chmod www folder':
  command => 'chmod -R 755 /var/www',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}

# create index.html file
file { '/var/www/html/index.html':
  content => "Hello World!\n",
}

# Add a custom landing page
file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page\n",
}

# Configure server block to include redirection page and custom error message
file { 'Nginx default config file':
  ensure  => file,
  path    => '/etc/nginx/sites-enabled/default',
  content =>
  "server {
          listen 80;
          listen [::]:80;

          root /var/www/html;
          index index.html index.htm;

          location /redirect_me {
              return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
          }

          error_page 404 /404.html;
          location /404 {
              root /var/www/html;
              internal;
          }
  }",
}

# Restarting nginx
exec { 'restart service':
  command => 'service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin',
}
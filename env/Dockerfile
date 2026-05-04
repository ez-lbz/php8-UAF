FROM php:8.4-apache
# FROM php:8.5-apache

# Use prefork as in original
RUN a2dismod mpm_event 2>/dev/null; a2enmod mpm_prefork 2>/dev/null; true

# Set disable_functions
RUN echo "disable_functions = system,shell_exec,passthru,exec,popen,proc_open,pcntl_exec" > /usr/local/etc/php/conf.d/disable_functions.ini

COPY index.php /var/www/html/index.php
RUN chmod o+w /var/www/html

EXPOSE 80

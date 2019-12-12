# Ansible module development

This repo contains the demo for *Ansible module development* talk. It consists of a single module called line. To run the demo You need ansible installed.

For example to set ```Hello, world!``` as first line of ```/etc/motd``` run:

``` $ ansible -m line -a 'content="Hello, world!" path="/etc/motd"' localhost```

The module suports ```check``` mode:

``` $ ansible -m line -a 'content="Hello, world!" path="/etc/motd"' localhost --check```

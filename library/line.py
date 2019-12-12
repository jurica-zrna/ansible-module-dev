#!/usr/bin/python                                                                                                                                                                                                                            
# -*- coding: utf-8 -*-                                                                                                                                                                                                                      
                                                                                                                                                                                                                                             
# Copyright: (c) 2019, Jurica Zrna <jurica.zrna@ibm.com>                                                                                                                                                                                     
# All rights reserved.                                                                                                                                                                                                                       
                                                                                                                                                                                                                                             
ANSIBLE_METADATA = {'metadata_version': '1.1',                                                                                                                                                                                               
                    'status': ['preview'],                                                                                                                                                                                                   
                    'supported_by': 'community'}                                                                                                                                                                                             
                                                                                                                                                                                                                                             
DOCUMENTATION = r'''                                                                                                                                                                                                                         
---                                                                                                                                                                                                                                          
module: line                                                                                                                                                                                                                                 
version_added: 2.8                                                                                                                                                                                                                           
short_description: Set first line of file to desired string.                                                                                                                                                                                 
description:                                                                                                                                                                                                                                 
    - The C(line) module sets the first line of file to desired string.                                                                                                                                                                      
    - The file must exist and must be writeable by user.                                                                                                                                                                                     
options:                                                                                                                                                                                                                                     
  content:                                                                                                                                                                                                                                   
    description:                                                                                                                                                                                                                             
    - Desired content to be put in file.                                                                                                                                                                                                     
    type: str                                                                                                                                                                                                                                
    required: yes                                                                                                                                                                                                                            
  path:
    description:
    - Path to file to be changed.
    type: path
author:
- Jurica Zrna
'''

EXAMPLES = r'''
- name: Set motd
  line:
    content: "Hello, world!"
    path: "/etc/motd"
'''

RETURN = r'''
path:
    description: file path
    returned: success
    type: path
    sample:
      "gid": 0,
      "group": "root",
      "mode": "0644",
      "owner": "root",
      "path": "/etc/motd",
      "size": 286,
      "state": "file",
      "uid": 0
'''

from ansible.module_utils.basic import AnsibleModule

import fileinput
import sys

def main():
  module = AnsibleModule(
    argument_spec=dict(
      content = dict(type= 'str', required = True),
      path = dict(type = 'path', required = True),
    ),
    supports_check_mode = True
  )

  content = module.params['content']
  path = module.params['path']
  changed = False

  try:
    with open(path, 'r') as f:
      line = f.readline().strip("\r\n")
      if line != content:
        changed = True

    if changed and not module.check_mode:
      for n, line in enumerate(fileinput.input(path, inplace=True)):
        line = line.rstrip('\r\n')
        if n == 0:
          print(content)
        else:
          print(line)

  except:
    e = sys.exc_info()[1]
    module.fail_json(changed=changed, msg=str(e))

  module.exit_json(changed=changed, path=path)


if __name__ == '__main__':
    main()

#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
import hashlib
from operator import mod
from statistics import mode
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Create a file at the specified path with the specified file contents.

options:
    path:
        description: Full path to the file.
        required: true
        type: str
    content:
        description:
            - Content written to file.
        required: true
        type: str
        default: ''
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Emil Temerbulatov - студент курса DevOps Netology
'''

EXAMPLES = r'''
# Pass in a message
- name: Test module from a collections
  hosts: localhost
  collections:
    - netology.yandex_cloud_elk
  tasks:
    - name: Import role from a collections
      import_role:
        name: createfile_role
'''


from hashlib import md5
from os.path import exists
from ansible.module_utils.basic import AnsibleModule


def file_exist(file_path, new_content):
    ''' Check file already exist '''

    while exists(file_path): 
        with open(file_path, "rb") as f:
            file_content_hash = md5(bytes(f.read())).hexdigest()
        
        new_content_hash = md5(bytes(new_content, 'UTF-8')).hexdigest()
        if file_content_hash == new_content_hash:
            return True
        else:
            return False
    else:
        return False

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=False, default='')
    )


    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        result['changed'] = not file_exist(module.params['path'], module.params['content'])
        module.exit_json(**result)


    if file_exist(module.params['path'], module.params['content']):
        result['original_message'] = "File {path} already exist".format(path = module.params['path']) 
        result['message'] = 'File already exist'
    else:
        with open(module.params['path'], 'w') as new_file:
            new_file.write(module.params['content'])
        result['changed'] = True
        result['original_message'] = "File {path} succesfully created".format(path = module.params['path']) 
        result['message'] = 'File created'


    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
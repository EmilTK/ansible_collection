CreateFile
=========

Роль для создания, редактирования файла на файловой системе по указанному пути.

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

  variable | Description | Default
 --- | --- | ---
 filecreate_path | Путь до файла | /tmp/example.txt
 filecreate_content | Содержимое файла | "New content file"


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

- name: Test role and module from a collections
  hosts: localhost
  collections:
    - netology.yandex_cloud_elk
  tasks:
    - name: Import role from a collections
      import_role:
        name: createfile_role

License
-------

MIT

Author Information
------------------

Emil Temerbulatov - студент курса DevOps Netology
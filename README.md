# Ansible Collection - netology.yandex_cloud_elk

Modules
--------------

1. [my_own_module](plugins/modules/my_own_module.py)

> Данный модуль выполняет проверку наличия файла в файловой системе `path`  и сравнивает его содержимое с переданными параметрами `content`.
> Если файл отсутвует - создается файл `path` с сожержимым `content`
> Если файл содержимое файла отличается от `content` файл перезаписывается.

Roles
--------------

1. [createfile_role](roles/createfile_role/README.md)

> Данная роль использует модуль [my_own_module](plugins/modules/my_own_module.py) для проверки наличия, обновление содержимого и создания файла.

Role Variables
--------------

  variable | Description | Default
 --- | --- | ---
 filecreate_path | Путь до файла | /tmp/example.txt
 filecreate_content | Содержимое файла | "New content file"

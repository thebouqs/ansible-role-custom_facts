Ansible Custom Facts
=========
This role will allow for deploying custom facts to managed hosts.

Requirements
------------
This role has no external requirements

Role Variables
--------------

### custom_facts
The list all the custom facts to deploy, plus their state and dependencies if any.

**default**:
```yaml
custom_facts:
  users:
    state: 'present'
    dependencies: []
```

**type**: dictionary

**example**:
```yaml
custom_facts:
  users:
    state: 'absent'
    dependencies: []
  groups:
    state: 'present'
    dependencies:
      - { type: 'pip', packages: 'getent' }
```

### custom_facts_path
The directory where the custom facts should be deployed.

**default**: `''` Should be set to a distribution specific value

**type**: string

**example**:
```yaml
custom_facts_path: '/etc/ansible/facts.d'
```

### custom_facts_path_state
The state for the custom facts directory. Set this to absent to remove the custom facts, and ensure they aren't deployed.

**default**: `'directory'`

**type**: string

**example**:
```yaml
custom_facts_path_state: absent
```

### custom__facts_path_owner
The owner of the custom_ facts directory.

**default**: `''` should be set to a distribution specific value

**type**: string

**example**:
```yaml
custom__facts_path_owner: 'root'
```

### custom_facts_path_group
The group permission for the custom facts directory.

**default**: `''` should be set to a distribution specific value

**type**: string

**example**:
```yaml
custom_facts_path_group: 'root'
```

### custom_facts_mode
the mode (chmod) for the custom facts directory

**default**: `''` should be set to a distribution specific value

**type**: string

**example**:
```yaml
custom_facts_mode: 'ug=rwx,o-rwx'
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

```yaml
- hosts: all
  tasks:
    - include_role:
        name: custom_facts
```
License
-------

BSD

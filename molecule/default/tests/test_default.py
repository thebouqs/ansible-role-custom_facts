"""Molecule Default Intgration Test"""
import os
import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


@pytest.mark.parametrize("path,file_type", [
    ("/etc/ansible/facts.d", "directory"),
    ("/etc/ansible/facts.d/users.fact", "file")
    ]
)
def test_hosts_file(host, path, file_type):
    _file = host.file(path)
    assert _file.exists
    if file_type == "directory":
        assert _file.is_directory
        assert _file.mode == 0o755
    if file_type == "file":
        assert _file.is_file
        assert _file.mode == 0o550

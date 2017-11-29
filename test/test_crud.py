import pytest
from ansible.cli.playbook import PlaybookCLI


# MODULES = ['organization', 'product']
MODULES = ['organization']


def run_playbook(path, extra_vars=""):
    extra_vars += " ansible_python_interpreter=../vcr_python_wrapper.py"
    cli = PlaybookCLI([
        'ansible-playbook',
        "-vvv",
        "-i", "localhost,",
        "-c", "local",
        "-e", extra_vars,
        path
    ])
    cli.parse()
    return cli.run()


@pytest.mark.parametrize("module", MODULES)
def test_crud(module):
    assert run_playbook("test/test_playbooks/{}.yml".format(module)) == 0

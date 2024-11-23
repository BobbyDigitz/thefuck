ion
from thefuck.entrypoints.not_configured import main


@pytest.fixture(autouse=True)
def usage_tracker(mocker):
    return mocker.patch(
        'thefuck.entrypoints.not_configured._get_not_configured_usage_tracker_path',
        new_callable=MagicMock)


@pytest.fixture(autouse=True)
def usage_tracker_io(usage_tracker):
    io = StringIO()
    usage_tracker.return_value \
                 .open.return_value \
                 .__enter__.return_value = io
    return io


@pytest.fixture(autouse=True)
def usage_tracker_exists(usage_tracker):
    usage_tracker.return_value \
                 .exists.return_value = True
    return usage_tracker.return_value.exists


def _assert_tracker_updated(usage_tracker_io, pid):
    usage_tracker_io.seek(0)
    info = json.load(usage_tracker_io)
    assert info['pid'] == pid


def _change_tracker(usage_tracker_io, pid):
    usage_tracker_io.truncate(0)
    info = {'pid': pid, 'time': 0}
    json.dump(info, usage_tracker_io)
    usage_tracker_io.seek(0)


@pytest.fixture(autouse=True)
def shell_pid(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured._get_shell_pid',
                        new_callable=MagicMock)


@pytest.fixture(autouse=True)
def shell(mocker):
    shell = mocker.patch('thefuck.entrypoints.not_configured.shell',
                         new_callable=MagicMock)
    shell.get_history.return_value = []
    shell.how_to_configure.return_value = ShellConfiguration(
        content='eval $(thefuck --alias)',
         --alias)')
    logs.configured_successfully.assert_called_once()

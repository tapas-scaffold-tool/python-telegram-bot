from tempfile import TemporaryDirectory
from json import dumps

import nox


@nox.session()
@nox.parametrize("tapas_version", [
    "0.1.3",
    "0.1.4",
    "0.1.5",
    "0.1.6",
    "0.1.7",
    "0.1.8",
    "0.1.9",
    "0.1.10",
    # Add another supported tapas version
    "latest",  # Keep it if you want to always test latest version
])
def tests(session, tapas_version):
    if tapas_version == "latest":
        session.install(f"tapas")
    else:
        session.install(f"tapas=={tapas_version}")
    with TemporaryDirectory() as tmp:
        params = {
            # Fill tapa parameters for test
        }
        session.run("tapas", "dir:.", tmp, "-p", dumps(params))

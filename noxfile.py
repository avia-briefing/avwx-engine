import nox


@nox.session(python=["3.7", "3.8"])
def tests(session):
    session.install(".[scipy]")
    session.install(".[tests]")
    session.run("pytest", "--disable-warnings")

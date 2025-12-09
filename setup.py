from setuptools import setup, find_packages


HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str):
    """Return a list of requirements from the given file."""
    with open(file_path) as f:
        requirements = [line.strip() for line in f if line.strip()]

    # Remove "-e ." if present
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="MLProject",
    version="0.0.1",
    author="Junaid",
    author_email="junaid996.raja@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("Requirements.txt"),
)

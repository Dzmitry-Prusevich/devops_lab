from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    install_requires=['psutil'],
    scripts=['snapshot.py'],
    version="1",
    author="Prusevich Dzmitry",
    author_email="dzmitry_prusevich@epam.com",
    description="Application for taking snapshots of your system",
    license="free"
)
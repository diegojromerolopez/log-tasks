from setuptools import setup

setup(
    name='log-tasks',
    version='1.0',
    packages=['log_reader', 'log_reader.tasks','log_reader.tests'],
    scripts=['traffic_to_host', 'hourly_task'],
    install_requires=[
        "file-read-backwards==2.0.0",
        "pytest==4.4.2"
    ],
    url='https://github.com/diegojromerolopez/log-tasks',
    license='',
    author='diegoj',
    author_email='diegojromerolopez@gmail.com',
    description=''
)

from setuptools import setup

setup (
    name="ws09-modules",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "whatSticks09modules includes models and config for ws applications",
    packages=['ws09_config','ws09_models'],
    python_requires=">=3.6",
    )
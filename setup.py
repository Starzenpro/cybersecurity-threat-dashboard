from setuptools import setup, find_packages

setup(
    name="cybersecurity-threat-dashboard",
    version="0.1.0",
    description="A dashboard for cybersecurity threat detection and analysis",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
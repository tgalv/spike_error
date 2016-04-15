from setuptools import setup, find_packages

setup(
    name="error_spike",
    version = "0.1",
    author="Fix Me",
    author_email="fix.me@landregistry.gsi.gov.uk",
    packages=find_packages(),
    install_requires=["flask"],
    tests_require=["flask"],
    test_suite="error_spike.test_suite.suite",
    entry_points={'console_scripts':
                  ['error_spike = error_spike.main:main']}
)

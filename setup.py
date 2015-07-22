from setuptools import setup, find_packages

setup(
    name='GoDebian_api',
    version='1.1.0.dev1',
    url='https://github.com/ninjatrench/GoDebian_api',
    download_url="https://github.com/ninjatrench/GoDebian_api/tarball/master",
    license='MIT',
    author='Harsh Daftary',
    author_email='info@securitylabs.in',
    description='Python client for go.debian.net and deb.li URL shortening service',
    packages=find_packages(exclude=['tests*']),

    classifiers=[
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: API for go.debian.net :: API client',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    install_requires=['requests'],
    long_description=open("README.rst").read()
)
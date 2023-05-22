import setuptools

setuptools.setup(
    name="chompchange",
    version="0.1",
    packages=['chompchange'],
    include_package_data=True,
    description='Global blockchain supporting term-world.',
    long_description=open('README.md', 'r').read(),
    install_requires=[line.strip() for line in open('requirements.txt', 'r').readlines()]
 )

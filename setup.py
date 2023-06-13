import setuptools

setuptools.setup(
    name="chompchain",
    version="0.1",
    packages=['chompchain'],
    include_package_data=True,
    description='Global blockchain supporting term-world.',
    long_description=open('README.md', 'r').read(),
    install_requires=[line.strip() for line in open('requirements.txt', 'r').readlines()],
    entry_points = {
        'console_scripts': [
            'chompchain = chompchain.cli:main'
        ]
    }
)

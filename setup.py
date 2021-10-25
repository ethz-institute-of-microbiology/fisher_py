import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fisher_py',
    version='1.0.0',
    author='Dominik Werner',
    author_email='dominik.wenrer@live.com',
    description='This python module allows to extract data from the RAW-file-format produces by devices from Thermo Fisher Scientific.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'pythonnet>=2.5.1',
        'numpy>=1.17.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
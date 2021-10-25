import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fisher_py',
    version='0.0.1',
    author='ethz-institute-of-microbiology',
    author_email='dominik.werner@live.com',
    description='This python module allows to extract data from the RAW-file-format produces by devices from Thermo Fisher Scientific.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ethz-institute-of-microbiology/fisher_py',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'pythonnet>=2.5.1',
        'numpy>=1.17.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
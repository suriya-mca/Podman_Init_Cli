from setuptools import setup, find_packages

setup(
    name='podman-init',
    version='1.0.3',
    packages=find_packages(exclude=['tests']),
    package_data={'': ['templates/**/*.j2']},
    include_package_data=True,
    install_requires=[
        'click',
        'jinja2'
    ],
    entry_points={
        'console_scripts': [
            'podman-init = src:podman_init'
        ]
    },
    author='Suriya',
    description='Python command-line tool that automates the process of initializing Docker-related files for your projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/suriya-mca/Podman_Init_Cli',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    exclude_package_data={'': ['tests/*']}
)

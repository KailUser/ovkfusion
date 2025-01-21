from setuptools import setup, find_packages

setup(
    name='OVKFusion',
    version='0.1.0',  # Change this to match your versioning scheme
    author='Syirezz Cheese',
    author_email='syirezz@example.com',  # Update with your email
    description='A Python library for interacting with OVK.to platform',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KailUser/ovkfusion',  # Change this to your GitHub repo URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Change this if necessary
    install_requires=[
        'requests',
    ],
    test_suite='tests',  # Specifies the test folder
)
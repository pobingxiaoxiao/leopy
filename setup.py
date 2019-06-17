from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='leopy',
    version='0.11',
    description="Leo's python package and script collections.",
    long_description="I'm try to use python in my daily job and life.",
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
      ],
    keywords='electronics leo power motor',
    url='http://github.com/pobingxiaoxiao/leopy',
    author='Leo Zhang',
    author_email='zhangzhengnust@163.com',
    license='MIT',
    packages=['leopy'],
    install_requires=[
        'markdown',
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    entry_points = {
        'console_scripts': ['leo-slogon=leopy.command_line:main','leo-phone=leopy.command_line:phone'],
    },
)
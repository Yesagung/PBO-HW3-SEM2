from setuptools import setup, find_packages

setup(
    name='siwp2005_yesmannatanael_ht_sort',
    version='0.1.5',
    description='Package that includes multiple sorting method',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Yesagung/PBO-HW3-SEM2.git', 
    author='Yesman Natanael Agung Kristanto',
    author_email='yesman.422023030@civitas.ukrida.ac.id',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
)
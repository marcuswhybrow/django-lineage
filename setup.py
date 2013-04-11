from setuptools import setup, find_packages

setup(
    name='django-lineage',
    version='0.2.0',
    description='Lightweight template tags for neater hierarchical navigation',
    long_description=open('README.md').read(),
    author='Marcus Whybrow',
    author_email='pypi@marcuswhybrow.net',
    license='BSD',
    url='https://github.com/marcuswhybrow/django-lineage',
    download_url='https://github.com/marcuswhybrow/django-lineage/downloads',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
    ],
)

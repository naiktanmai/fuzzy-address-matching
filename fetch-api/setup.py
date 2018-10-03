from setuptools import setup

setup(
    name='fuzzy_address_matcher',
    version='1.0',
    long_description=__doc__,
    packages=['matcher'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=1.0.2'
    ]
)

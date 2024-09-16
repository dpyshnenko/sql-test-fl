import setuptools

setuptools.setup(
    name='sql_course',
    version='1.0.0',
    url='https://github.com/dpyshnenko/sql-test-fl',
    license='GPL3',
    packages=['sql_course'],
    package_dir={'sql_course': 'sql_course'},
    include_package_data=True,
    package_data={'': ['data/*.csv', "data/*.sql"]},
    install_requires=['pandas'],
)

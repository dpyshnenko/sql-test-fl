import setuptools

setuptools.setup(
    name='sql_test',
    version='1.0.0',
    url='https://github.com/uplimit/course-intermediate-sql',
    license='GPL3',
    packages=['sql_test'],
    package_dir={'sql_test': 'sql_test'},
    include_package_data=True,
    package_data={'': ['data/*.csv', "data/*.sql"]},
    install_requires=['pandas'],
)

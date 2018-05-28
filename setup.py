from setuptools import setup, find_packages

setup(
    name='twn_stock',
    description='Python Crawler Stock for TWN',
    version='0.01',
    author='Wayne Chiu',
    author_email='homeworker.wayne@gmail.com',
    packages=['twn_stock','twn_stock.code_crawler'],
    package_data={'twn_stock':['*.csv']},
    license='MIT'
)

from setuptools import setup, find_packages

setup(
    name='url2pdf-readable',
    version='0.1',
    scripts=['scripts/url2pdf-readable'],
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Covent an web article (URL) to a redable PDF, later to be printed or read on a e-reader',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/235/url2pdf-readable',
    author='Oleksandr Pryymak',
    author_email='235@inmind.org'
)

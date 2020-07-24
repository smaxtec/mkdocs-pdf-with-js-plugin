import subprocess

from os import path
from setuptools import setup, find_packages


def load_file(filename):

    working_directory = path.abspath(path.dirname(__file__))
    with open(path.join(working_directory, filename), encoding='utf-8') as f:
        long_description = f.read()

    return long_description


setup(
    name='mkdocs-pdf-with-js-plugin',
    version=subprocess.check_output(["git", "describe", "--tags"]).decode().strip(),
    description='A MkDocs plugin that exports your documentation as PDF with rendered JavaScript content.',
    long_description=load_file('README.md'),
    long_description_content_type="text/markdown",
    keywords='mkdocs pdf javascript selenium',
    url='https://github.com/smaxtec/mkdocs-pdf-with-js-plugin',
    author='Stefan Brandstaetter',
    author_email='stefan.brandstaetter@smaxtec.com',
    license='MIT',
    python_requires='>=3.4',
    install_requires=[
        'beautifulsoup4',
        'mkdocs>=1.0.4',
        'selenium',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Topic :: Documentation',
        'Topic :: Printing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.plugins': [
            'pdf-with-js = pdf_with_js.plugin:PdfWithJS'
        ]
    }
)

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Leonardo Gregianin, Gustavo Efeiche",
    author_email="leogregianin@gmail.com",
    name='ibge',
    license="MIT",
    description='Collection of APIs for the IBGE Data Services in Brazil',
    version='0.0.2',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/leogregianin/ibge/',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese (Brazilian)'
    ]
)
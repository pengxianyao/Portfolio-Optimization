from setuptools import setup, find_packages

with open(file="README.md", mode="r") as fh:
    long_description = fh.read()

setup(
    name='py-portfolio',
    author='Alex Reed',
    author_email='coding.sigma@gmail.com',
    version='0.0.1',
    description='A python application, that demonstrates optimizing a portfolio using machine learning.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/areed1192/portfolio-optimization',
    install_requires=[
        'requests',
        'matplotlib>=3.5.0',
        'numpy>=1.22.0',
        'pandas',
        'scipy',
        'fake_useragent',
        'python_dateutil',
        'scikit_learn'
    ],

    packages=find_packages(
        include=['pyopt']
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>3.7'
)

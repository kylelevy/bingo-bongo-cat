from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Cat that prints messages.'
LONG_DESCRIPTION = 'A package which makes troubleshooting code a little less painful by adding a cute cat to let you know where you went wrong.'

# Setting up
setup(
    name="bingo-bongo-cat",
    version=VERSION,
    author="Kyle Levy",
    author_email="",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'debugging', 'cat', 'funny'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
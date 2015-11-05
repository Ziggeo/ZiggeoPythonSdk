from setuptools import setup, find_packages


requirements = ['pycrypto>=2.6.1']


setup(
    name="ziggeo",
    version="1.0",
    description="Ziggeo SDK for python",
    url="http://github.com/Ziggeo/ZiggeoPythonSdk",
    license="Apache 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache 2.0 License",
        "Programming Language :: Python :: 2.7",
    ],
    keywords=("Ziggeo video-upload"),
    packages=find_packages(),
    install_requires=requirements,
)

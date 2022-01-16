from setuptools import setup, find_packages


requirements = ['pycryptodome>=3.7.0']


setup(
    name="ziggeo",
    version="2.27",
    description="Ziggeo SDK for python",
    long_description="Ziggeo API (https://ziggeo.com) allows you to integrate video recording and playback with only two lines of code in your site, service or app. This is the Python Server SDK repository.",
    url="http://github.com/Ziggeo/ZiggeoPythonSdk",
    license="Apache 2.0",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    keywords=("Ziggeo video-upload"),
    packages=["."],
    package_dir={'ziggeo': '.'},
    install_requires=requirements,
    author="Ziggeo",
    author_email="support@ziggeo.com"
)

import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccqclient",
    version="0.0.1",
    author="Omnibond Systems LLC",
    author_email="support@cloudycluster.com",
    description="Client for the CCQ meta-scheduler in CloudyCluster",
    long_description=long_description,
    long_description_content_type="text/plain",
    url="https://github.com/omnibond/ccqclient",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU LGPLv2.1",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

import setuptools

setuptools.setup(
    name="audible-activator",
    description="A script to retrieve your activation data (activation_bytes) from Audible servers.",
    url="https://github.com/aaschmid/audible-activator",

    packages=setuptools.find_packages(),
    package_dir={"": "."},
    package_data={"": ["AudibleGeneratePCPlayerID.c", "README.md", "LICENSE"]},
    include_package_data=True,
    python_requires=">=3.8",

    install_requires=[
        "requests>=2.6,<3",
        "selenium>=3,<5",
    ],
    scripts=["audible-activator.py"],
)

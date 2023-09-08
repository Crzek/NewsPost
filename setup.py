from setuptools import setup, find_packages

requirements = [
    "django==4.1",
    "pytest<7,>=5",
    "pytest-timeout",
    "pytest-django",
    "pylint",
    "setuptools-lint",
]

setup(
    name="django-basic-pytools",
    version="1.1.0",
    description="""Programming test task for django""",
    author="Devskiller",
    author_email="support@devskiller.com",
    packages=find_packages(),
    entry_points={"console_scripts": ["blog=blog.cli:main"]},
    include_package_data=True,
    exclude_package_data={
        "": ["test*.py", "tests/*.env", "**/tests.py"],
    },
    python_requires=">=3.8",
    install_requires=requirements,
    license="Proprietary",
    zip_safe=False,
    keywords="django-basic-pytools",
    tests_require=requirements,
    setup_requires=["pytest-runner"],
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-otp-provider",
    version="1.0.0",
    author="Andrei Koptev",
    author_email="akoptev1989@ya.ru",
    description="Django OTP (One Time Password)",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='django otp',
    url="https://github.com/a1k89/django_otp_provider",
    packages=setuptools.find_packages(exclude=["migrations"]),
    install_requires=['Django>=2.0',
                      'celery>=5.0',
                      'pyjwt'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    include_package_data=True
)
from setuptools import setup, find_packages

setup(
    name = "Django JsConnect",
    version = "0.2",
    packages = ['jsConnectDjango', 'jsConnectDjango.helpers'],
    include_package_data = True,

    author = "Aaron O'Mullane",
    author_email = "aaron.omullan@gmail.com",
    maintainer = "Kamil Burzynski",
    maintainer_email = "kamil@nopik.net",
    description = "Authentification bridge between a Django website and VanillaForums",
    license = "Apache",
    keywords = "python django authentication vanilla forums jsconnect",
    url = "https://github.com/Nopik/jsConnectDjango",
    install_requires = [],

    classifiers = [
        'Development Status :: 0.2 - Beta Testing',
        'Environment :: Unix-like Systems',
        'Intended Audience :: Developers, Project managers, Sys admins',
        'Programming Language :: Python',
        'Operating System :: Unix-like',
    ],
)

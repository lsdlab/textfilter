from setuptools import setup, find_packages

setup(
    name='textfilter',
    version='1.0.0',
    author="Chen Jian",
    author_email="lsdvincent@gmail.com",
    license='MIT',
    description="敏感关键词过滤输出",
    packages=find_packages(),
    # package_data={'': ['*.otf', 'fonts/*.otf']},
    # include_package_data=True,
    # install_requires=['pillow'],
    url='https://github.com/lsdlab/textfilter',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
)

from setuptools import setup,find_packages

setup(
    name='amqpymessenger',
    packages=find_packages(),

    description='AMQP library for python',
    long_description_content_type="text/markdown",
    long_description="AMQP library for python",
    url='https://github.com/yeranosyanvahan/amqpymessenger',
    author='Vahan Yeranosyan',
    author_email='vahan@yeranosyanvahan.com',
    maintainer='Vahan Yeranosyan',
    maintainer_email='vahan@yeranosyanvahan.com',
    license='MIT',
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'License :: MIT License',
    ],
    setuptools_git_versioning={
        "enabled": True,
    },
    setup_requires=["setuptools-git-versioning"],

)
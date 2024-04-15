from setuptools import setup, find_packages

setup(
    name='rxn_insight',
    version='0.1',
    description='A tool to analyze reaction data, name chemical reactions, and suggest reaction conditions based on this analysis.',
    long_description=open('README.md').read(),
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0',
        'numpy>=1.0',
        'rdkit>=2021.03.5',
        'click>=7.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.1, <4'
)

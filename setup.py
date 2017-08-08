from setuptools import setup, find_packages

version = '1.0.0'

setup(
    name='senaite.lims',
    version=version,
    description="SENAITE – A modern, mobile-first LIMS",
    long_description=open("README.md").read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Plone",
          "Framework :: Zope2",
      ],
    keywords='',
    author='SENAITE',
    author_email='senaite@ridingbytes.com',
    url='https://github.com/senaite/senaite.lims',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['liscon'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'bika.lims',
        'archetypes.schemaextender',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'unittest2',
        ]
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
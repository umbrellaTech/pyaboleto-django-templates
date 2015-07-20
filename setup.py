# -*- coding: utf-8 -*-
# http://peterdowns.com/posts/first-time-with-pypi.html
from distutils.core import setup
setup(
    name='pyaboleto_templates_django',
    packages=['pyaboleto_templates_django'], # this must be the same as the name above
    version='0.1',
    description='O pyaboleto (Python Yet Another Boleto Templates para Django) é um conjunto de templates no padrão'
                ' Django que utiliza os objetos de dados do pyaboleto para gerar os boletos.',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    url='https://github.com/umbrellaTech/pyaboleto_templates_django', # use the URL to the github repo
    download_url='https://github.com/umbrellaTech/pyaboleto_templates_django/tarball/0.1', # I'll explain this in a second
    keywords=['boleto', 'django', 'template'], # arbitrary keywords
    classifiers=[],
)

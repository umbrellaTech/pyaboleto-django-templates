# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright 2015 Umbrella Tech.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
__author__ = 'Kelson da Costa Medeiros <kelsoncm@gmail.com>'


from django.shortcuts import render_to_response
import pyaboleto.bb
from datetime import date


def boleto(request, *args, **kwargs):
    end = pyaboleto.bb.Endereco('12345-123', 'Logradouro', 'Nº', 'Complemento', 'Bairro', 'Cidade', 'UF', 'Brasil')
    ced = pyaboleto.bb.Cedente('Nome da empresa', '12.345.678/9012-34', end)
    sac = pyaboleto.bb.Sacado('Nome do cidadão', '123.456.789-01', end, '123465 SSP/UF')
    con = pyaboleto.bb.Convenio('050094', '31', pyaboleto.bb.banco_brasil, '1606-0', '06809350-0')
    bol = pyaboleto.bb.BBBoleto('01448-0', date(2016, 12, 31), 1.0, con, ced, sac)
    print bol.codigo_barras
    return render_to_response('custom_bb.html', {'boleto': bol})

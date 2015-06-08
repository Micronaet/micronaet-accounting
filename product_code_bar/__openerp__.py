# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011 Domsense srl (<http://www.domsense.com>)
#    Copyright (C) 2011-2013 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Product code Barcore",
    'version': '0.1',
    'category': 'Accounting & Finance',
    'summary': "Manages the product code",
    'description': "",
    'author': 'Micronaet Srl',
    'website': 'http://www.micronaet.it',
    "depends": [
        'product',
    ],
    "data": [
        'security/ir.model.access.csv',
        'product_code_view.xml'
    ],
    "active": False,
    "installable": True,
}

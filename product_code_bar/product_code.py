# -*- coding: utf-8 -*-
###############################################################################
#
# ODOO (ex OpenERP) 
# Open Source Management Solution
# Copyright (C) 2001-2015 Micronaet S.r.l. (<http://www.micronaet.it>)
# Developer: Nicola Riolini @thebrush (<https://it.linkedin.com/in/thebrush>)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import logging
import string
import time
import pdb
import openerp
import openerp.addons.decimal_precision as dp
from datetime import datetime
from dateutil.relativedelta import relativedelta
from operator import itemgetter
from openerp import SUPERUSER_ID
from openerp import pooler, tools
from openerp.osv import fields, osv, orm, expression
from openerp.tools.translate import _
from openerp.tools.float_utils import float_round


class field_product_code(orm.Model):

    _name = 'field.product.code'
    _description = 'Field product code'

    _columns = {
        'name': fields.char('Product', size=4),
        'note': fields.text('Note'),
        }

    def onchange_upper_product(self, cr, uid, ids, name, context=None):
        ''' Manages the capital of the fields in the form product
        '''
        res = {'value': {}}
        if name:
            res['value']['name'] = name.upper()
        return res

class field_brand_code(orm.Model):

    _name = 'field.brand.code'
    _description = 'Field brand code'

    _columns = {
        'name': fields.char('Brand', size=4),
        'note': fields.text('Note'),
        }

    def onchange_upper_brand(self, cr, uid, ids, name, context=None):
        ''' Manages the capital of the fields in the form brand
        '''
        res = {'value': {}}
        if name:
            res['value']['name'] = name.upper()
        return res

class field_material_code(orm.Model):

    _name = 'field.material.code'
    _description = 'Field material code'

    _columns = {
        'name': fields.char('Material', size=3),
        'note': fields.text('Note'),
        }

    def onchange_upper_material(self, cr, uid, ids, name, context=None):
        ''' Manages the capital of the fields in the form material
        '''
        res = {'value': {}}
        if name:
            res['value']['name'] = name.upper()
        return res

class product_code_bar(orm.Model):
    ''' Add extra field for manage product code
    '''
    _inherit = "product.product"

    _columns = {
        'product_code_id': fields.many2one('field.product.code', 'Product'),
        'brand_code_id': fields.many2one('field.brand.code', 'Brand', size=4),
        'material_code_id': fields.many2one(
            'field.material.code', 'Material', size=3),
        'size_code': fields.char('Size', size=7),
        'jolly_code': fields.char('Jolly', size=2),
        }

    #================#
    # Onchange event #
    #================#

    def onchange_upper_size(self, cr, uid, ids, size_code, context=None):
        ''' Manages the capital of the fields in the form size
        '''
        res = {'value': {}}
        if size_code:
            res['value']['size_code'] = size_code.upper()
        return res

    def onchange_upper_jolly(self, cr, uid, ids, jolly_code, context=None):
        ''' Manages the capital of the fields in the form jolly
        '''
        res = {'value': {}}
        if jolly_code:
            res['value']['jolly_code'] = jolly_code.upper()
        return res

    def onchange_product_code_id(self, cr, uid, ids, product_code_id, 
            brand_code_id, material_code_id, size_code, jolly_code, 
            context=None):
        ''' Read product code e write in ref code
        '''
        res = {}
        res['value'] = {}
        if product_code_id:
            product_code_pool = self.pool.get('field.product.code')
            product_code_proxy = product_code_pool.browse(
                cr, uid, product_code_id, context=context)
            res['value']['default_code'] = product_code_proxy.name
            
            if brand_code_id:
                brand_code_pool = self.pool.get('field.brand.code')
                brand_code_proxy = brand_code_pool.browse(
                    cr, uid, product_code_id, context=context)
                brand_code_proxy = brand_code_pool.browse(
                    cr, uid, brand_code_id, context=context)
                res['value']['default_code'] += brand_code_proxy.name
                
                if material_code_id:    
                    material_code_pool = self.pool.get('field.material.code')
                    material_code_proxy = material_code_pool.browse(
                        cr, uid, product_code_id, context=context)
                    material_code_proxy = material_code_pool.browse(
                        cr, uid, material_code_id, context=context)
                    res['value']['default_code'] += material_code_proxy.name
                    
                    if size_code:
                        size = size_code.upper() + "-" * (7 - len(size_code))
                        res['value']['default_code'] += size 
                        res['value']['size_code'] = size
                                                
                        if jolly_code:
                            jolly = jolly_code.upper() + "-" * (2 - len(jolly_code))
                            res['value']['default_code'] += jolly
                            res['value']['jolly_code'] = jolly
        return res
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

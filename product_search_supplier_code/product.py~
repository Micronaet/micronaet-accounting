# -*- coding: utf-8 -*-
###############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2001-2015 Micronaet S.r.l. (<http://www.micronaet.it>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import os
import sys
import logging
import openerp
import openerp.netsvc as netsvc
import openerp.addons.decimal_precision as dp
from openerp.osv import fields, osv, expression
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from openerp import SUPERUSER_ID, api
from openerp import tools
from openerp.tools.translate import _
from openerp.tools.float_utils import float_round as round
from openerp.tools import (DEFAULT_SERVER_DATE_FORMAT, 
    DEFAULT_SERVER_DATETIME_FORMAT, 
    DATETIME_FORMATS_MAP, 
    float_compare)


_logger = logging.getLogger(__name__)


class product_product_override_search(osv.osv):
    ''' Add extra field to product (for search in supplier code)
    ''' 
    _name='product.product'
    _inherit = 'product.product'

    # -------------------------------------------------------------------------
    # Override ORM
    # -------------------------------------------------------------------------
    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        """ 
        Search in supplier code and name for all products
        
        @param cr: cursor to database
        @param uid: id of current user
        @param args: list of conditions to be applied in search opertion
        @param offset: default from first record, you can start from n records
        @param limit: number of records to be comes in answer from search opertion
        @param order: ordering on any field(s)
        @param context: context arguments, like lang, time zone
        @param count: 
        
        @return: a list of integers based on search domain
        """
        new_args = []
        for search_item in args:
            if len(search_item) == 3 and search_item[0] == 'default_code':
                # Search i default supplier:
                query = """
                    SELECT product_tmpl_id from product_supplierinfo
                    WHERE product_name ilike '%s%s%s' OR product_code ilike '%s%s%s';""" % (
                        "%", search_item[2], "%", 
                        "%", search_item[2], "%", 
                        )
                cr.execute(query)        
                ids = [item[0] for item in cr.fetchall()]
                new_args.extend([
                    "|", "|", 
                    ('id', 'in', ids),
                    ('name', 'ilike', search_item[2]),
                    ('default_code', 'ilike', search_item[2]),
                    ])
            else: # add extra filters
                new_args.append(search_item)
        return super(product_product_override_search, self).search(
            cr, uid, new_args, offset, limit=limit, order=order, 
            context=context, 
            count=count)
    
    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=80):        
        ''' Foreign key search element 
            extend search to supplier name and code
        '''
        if args is None:
            args = []    
        if context is None:
            context = {}

        domain = [('default_code', 'ilike', name)]
        domain.extend(args)
        ids = self.search(cr, uid, domain, limit=limit, context=context)
        
        return super(product_product_override_search, self).name_get(
            cr, uid, ids, context=context)

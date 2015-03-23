#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2010-2012 Associazione OpenERP Italia
#    (<http://www.openerp-italia.org>).
#    Copyright(c)2008-2010 SIA "KN dati".(http://kndati.lv) All Rights Reserved.
#                    General contacts <info@kndati.lv>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields

class sale_order(osv.osv):
    ''' Override send invoice function 
    '''
    _name = 'sale.order'
    _inherit = 'sale.order'

    _columns = {
        'subject': fields.text(
            'Subject', required=False, readonly=False, 
            help='Subject for offer module'),
        'execution': fields.text(
            'Execution', required=False, readonly=False, 
            help='Execution note'),
        'exclusion': fields.text(
            'Exclusion', required=False, readonly=False, 
            help='Exclusion note'),
    }
    
    def print_quotation(self, cr, uid, ids, context=None):
        ''' Override sale order print function
        '''
        res = super(sale_order, self).print_quotation(
            cr, uid, ids, context=context)
        
        # replace report name:
        res['report_name'] = 'custom_sale_order_report'
        return res        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

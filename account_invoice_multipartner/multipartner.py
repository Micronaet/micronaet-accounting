# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP module
#    Copyright (C) 2010 Micronaet srl (<http://www.micronaet.it>) 
#    
#    Italian OpenERP Community (<http://www.openerp-italia.com>)
#
#############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields


class AccountInvoiceMultipartner(osv.osv):
    ''' Add more than one reference partner in account invoice
        (only in report document, not in journal entry)    
    '''
    _inherit = 'account.invoice'
    
    # on change function:
    def onchange_extra_address(self, cr, uid, ids, extra_address, partner_id, 
            context=None):
        ''' Set domain in partner_ids list when        
        '''
        res = {}
        if extra_address == 'contact' and partner_id:
            res['domain'] = {'partner_ids': [('parent_id', '=', partner_id)]}
        else:
            res['domain'] = {'partner_ids': []}
        res['value'] = {'partner_ids': False}
        return res
        
    _columns = {
        'extra_address': fields.selection([
            ('none', 'None'),
            ('contact', 'Contact'),
            ('partner', 'Partner'), ], 
                'Extra address', select=True, readonly=False, required=True),
        'partner_ids': fields.many2many(
            'res.partner', 'invoice_partner_rel', 'invoice_id', 'partner_id', 
            'Extra partner'),
    }
    
    _defaults = {
        'extra_address': lambda *a: 'none',
    }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

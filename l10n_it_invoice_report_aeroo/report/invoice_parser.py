#!/usr/bin/python
# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (C) 2010-2012 Associazione OpenERP Italia
#   (<http://www.openerp-italia.org>).
#   Copyright(c)2008-2010 SIA "KN dati".(http://kndati.lv) All Rights Reserved.
#                   General contacts <info@kndati.lv>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.report import report_sxw
from openerp.report.report_sxw import rml_parse


class Parser(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(Parser, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_address': self.get_address,
            'get_extra_data': self.get_extra_data,
            'get_partner_list': self.get_partner_list,
            'get_payment_list': self.get_payment_list,
        })

    def get_payment_list(self, move_id):
        ''' Return payment list from account move_id browse obj
        '''
        if not move_id:
            return []
            
        move_pool = self.pool.get('account.move.line')
        move_ids = move_pool.search(self.cr, self.uid, [('move_id','=',move_id),('date_maturity','!=',False)], order = 'date_maturity' )
        return move_pool.browse(self.cr, self.uid, move_ids)

    def get_partner_list(self, o):
        ''' Get list of partner address, depend on extra_field value
        '''
        res = [o.partner_id]
        if o.extra_address in ('contact', 'partner') and o.partner_ids:
            res.extend(o.partner_ids)
        return res

    def get_address(self, partner_proxy):
        ''' Get partner address with passed browse obj
        '''
        return "%s - %s - %s" % (
            partner_proxy.street or '',
            partner_proxy.zip or '',
            partner_proxy.city or '',
            )

    def get_extra_data(self, partner_proxy):
        ''' Get partner extra data with passed browse obj
            (no contact element for now)
        '''
        return "%s%s" % (
                "P.IVA: %s\n" % (
                    partner_proxy.vat if partner_proxy.vat else ""),
                "C.F.: %s" % (
                    partner_proxy.fiscalcode if partner_proxy.fiscalcode else ""), )            
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

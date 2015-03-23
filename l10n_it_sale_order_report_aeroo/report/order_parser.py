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
    counters = {}
    
    def __init__(self, cr, uid, name, context):
        
        super(Parser, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_address': self.get_address,
            'get_extra_data': self.get_extra_data,
            'get_partner_list': self.get_partner_list,
            'get_counter': self.get_counter,
            'set_counter': self.set_counter,
        })

    def get_counter(self, name):
        ''' Get counter with name passed (else create an empty)
        '''
        if name not in self.counters:
            self.counters[name] = False
        return self.counters[name]

    def set_counter(self, name, value):
        ''' Set counter with name with value passed
        '''
        self.counters[name] = value
        return "" # empty so no write in module

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
        '''
        return "Phone: %s\nFax: %s\nE-mail: %s\n%s" % (
            partner_proxy.phone or '',
            partner_proxy.fax or '',
            partner_proxy.email or '',
            "%s%s" % (
                "P.IVA: %s\n" % (
                    partner_proxy.vat if partner_proxy.vat else ""),
                "C.F.: %s" % (
                    partner_proxy.fiscalcode if partner_proxy.fiscalcode else \
                    ""), )
            )
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

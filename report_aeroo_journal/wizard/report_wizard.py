# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2001-2014 Micronaet SRL (<http://www.micronaet.it>).
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
###############################################################################
import os
import sys
import openerp.netsvc
import logging
from openerp.osv import osv, fields
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, DATETIME_FORMATS_MAP, float_compare
import openerp.addons.decimal_precision as dp
from openerp.tools.translate import _


_logger = logging.getLogger(__name__)

class account_move_journal_report_wizard(osv.osv_memory):
    ''' Wizard that let choose filter on journal report
    '''
    _name = "account.move.journal.report.wizard"

    # Wizard button:
    def action_print_journal(self, cr, uid, ids, context=None):
        ''' Print journal report
        '''
        if context is None: 
            context = {}        
        
        wizard_browse = self.browse(cr, uid, ids, context=context)[0]
        
        datas = {
            'from_date': wizard_browse.from_date or False,
            'to_date': wizard_browse.todate or False,
            'seq': wizard_browse.seq,
            'journal_id':  wizard_browse.journal_id.id,
        }

        return { # action report
                'type': 'ir.actions.report.xml',
                'report_name': "account_journal_move_report",
                'datas': datas,
            }            

    # default function:        
    def default_date_from_to(self, cr, uid, data_type, context=None):
        ''' Get default value for 4 type of data:
        '''        
        ref = datetime.now()

        if data_type == 'from_date':
            return ref.strftime("%Y-%m-01") # start month
        elif data_type == 'to_date':
            return (ref + relativedelta(months = 1)).strftime("%Y-%m-01") # start month
        else:
            return False # not possible

    _columns = {
        'from_date': fields.date('Date from >=', required=False),
        'to_date': fields.date('Date to <', required=False),
        'journal_id': fields.many2one('account.journal', 'Journal', required=True),
        'seq': fields.integer('Start sequence', help="Start number for progressive number of row in register"),
        }
        
    _defaults = {
        'from_date': lambda s, cr, uid, c: s.default_date_from_to(cr, uid, 'from_date', context=c),
        'to_date': lambda s, cr, uid, c: s.default_date_from_to(cr, uid, 'to_date', context=c),
        'seq': 1,
        }    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:


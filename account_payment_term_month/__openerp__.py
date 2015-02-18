# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Micronaet SRL (<http://www.micronaet.it>).
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


{
    "name": "Payment terms - Commercial month",
    "version": "1.0",
    "author": "Micronaet s.r.l.",
    "website": "http://www.micronaet.it",
    "category": "Account / Payments",
    "description": """
         This module manage commercial month for end of month deadline
    """,
    "depends": [
        "account",
    ],
    "init_xml": [],
    "demo_xml": [],
    "data": [
        "payment_view.xml",
    ],
    "active": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

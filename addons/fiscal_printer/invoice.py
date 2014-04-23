# -*- coding: utf-8 -*-
##############################################################################
#
#    fiscal_printer
#    Copyright (C) 2014 No author.
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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


import re
from openerp import netsvc
from openerp.osv import osv, fields

class invoice(osv.osv):
    """"""
    
    _name = 'account.invoice'
    _inherits = {  }
    _inherit = [ 'account.invoice' ]



    _columns = {
        'fiscal_printer_id': fields.many2one('fiscal_printer.fiscal_printer', string='Fiscal Printer'), 
    }

    _defaults = {
    }


    _constraints = [
    ]


    def onchange_journal_id(self, cr, uid, ids, journal_id, context=None):
        """"""
        result = super(invoice,self).onchange_journal_id(cr, uid, ids, journal_id, context=None)
        return result



invoice()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 Savoir-faire Linux. All Rights Reserved.
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

from openerp import api, fields, models
import openerp.addons.decimal_precision as dp


class HrPayslip(models.Model):

    _inherit = 'hr.payslip'

    # Fields required to compute benefits based on
    # a percentage of the gross salary for the pay period
    gross_salary = fields.Float(
        'Gross Salary',
        digits_compute=dp.get_precision('Payroll'),
        readonly=True,
        states={'draft': [('readonly', False)]},
        default=0,
    )

    @api.multi
    def set_gross_salary(self, gross):
        """
        Allow to set payslip fields directly from the salary rules.

        This is required to allow setting the gross_salary at a
        precise moment in the salary structure.

        Exemple
        -------
        payslip.set_gross_salary(GROSS)
        """
        self.write({'gross_salary': gross})

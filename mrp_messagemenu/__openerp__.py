# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2017- Vertel AB (<http://vertel.se>).
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
##############################################################################
{
<<<<<<< HEAD
'name': 'Event Message Menu',
'version': '0.1',
'summary': 'Menu for event calendar in message menu',
'category': 'event',
'description': """Menu for event calendar in message menu
=======
'name': 'Manufacturing Message Menu',
'version': '0.1',
'summary': 'Menu for event production orders in message menu',
'category': 'event',
'description': """Menu for production calendar in message menu
>>>>>>> 2fa84b6985c6e0c131c12a1e8050a58396716421

""",
'author': 'Vertel AB',
'website': 'http://www.vertel.se',
<<<<<<< HEAD
'depends': ['event',],
'data': ['event_messagemenu_view.xml', 'event_messagemenu_data.xml',],
=======
'depends': ['mrp',],
'data': ['mrp_messagemenu_view.xml'],
>>>>>>> 2fa84b6985c6e0c131c12a1e8050a58396716421
'installable': True,
}

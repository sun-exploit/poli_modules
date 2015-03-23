# Copyright (c) 2012 sun-exploit <a1@sun-exploit.com>
#
#  This file is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from component import xml_component

class pcs_component(xml_component):

    def __init__(self):
        print "hello_world from {0}".format(__name__)

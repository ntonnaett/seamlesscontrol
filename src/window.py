# window.py
#
# Copyright 2021 Nils Tonnätt
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk
from oscpy.client import OSCClient

@Gtk.Template(resource_path='/org/seamless/SeamlessControl/window.ui')
class SeamlesscontrolWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'SeamlesscontrolWindow'

    pause_button = Gtk.Template.Child()
    resume_button = Gtk.Template.Child()
    showcontrol = OSCClient('localhost', 9000)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pause_button.connect("clicked", self.on_pause_clicked, 'pause')
        self.resume_button.connect("clicked", self.on_resume_clicked, 'resume')

    def on_pause_clicked(self, button, name):
        print('Paused!')
        self.showcontrol.send_message(b'/pause', [1])

    def on_resume_clicked(self, button, name):
        print('Resumed!')
        self.showcontrol.send_message(b'/pause', [0])

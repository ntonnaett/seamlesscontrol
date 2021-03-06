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

    status_label = Gtk.Template.Child('status_label')

    showcontrol = OSCClient('localhost', 9000)
    cssProvider = Gtk.CssProvider()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cssProvider.load_from_resource(resource_path='/org/seamless/SeamlessControl/style.css')

    @Gtk.Template.Callback("pause_button_clicked")
    def on_pause_clicked(self, button):
        print('Paused!')
        self.showcontrol.send_message(b'/showcontrol/pause', [1])
        self.status_label.set_text('Status: Paused!')

    @Gtk.Template.Callback("resume_button_clicked")
    def on_resume_clicked(self, button):
        print('Resumed!')
        self.showcontrol.send_message(b'/showcontrol/pause', [0])
        self.status_label.set_text('Status: Playing!')

    @Gtk.Template.Callback("trailer_button_clicked")
    def on_trailer_clicked(self, button):
        print('Trailer!')
        self.showcontrol.send_message(b'/showcontrol/track', [0])

    @Gtk.Template.Callback("brunnen_button_clicked")
    def on_brunnen_clicked(self, button):
        self.showcontrol.send_message(b'/showcontrol/track', [1])

    @Gtk.Template.Callback("sufi_button_clicked")
    def on_sufi_clicked(self, button):
        self.showcontrol.send_message(b'/showcontrol/track', [2])

    @Gtk.Template.Callback("oksus_button_clicked")
    def on_oksus_clicked(self, button):
        self.showcontrol.send_message(b'/showcontrol/track', [3])

    @Gtk.Template.Callback("datenerhebung_button_clicked")
    def on_datenerhebung_clicked(self, button):
        self.showcontrol.send_message(b'/showcontrol/track', [4])


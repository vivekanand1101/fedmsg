# This file is part of fedmsg.
# Copyright (C) 2012 Red Hat, Inc.
#
# fedmsg is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Ralph Bean <rbean@redhat.com>
#
from fedmsg.meta.base import BaseProcessor


class AnnounceProcessor(BaseProcessor):
    __name__ = "announce"
    __description__ = "Official Fedora Announcements"
    __link__ = "https://fedoraproject.org/"
    __docs__ = "https://fedoraproject.org/"
    __obj__ = "Announcements"

    def subtitle(self, msg, **config):
        return msg['msg']['message']

    def link(self, msg, **config):
        return msg['msg']['link']

    def usernames(self, msg, **config):
        users = set()
        if 'username' in msg:
            users.update(set([msg['username']]))
        return users

    def agent(self, msg, **config):
        if 'username' in msg:
            return msg['username']
        return None

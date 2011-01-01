#!/usr/bin/env python

# Copyright (C) 2011  Braden Shepherdson 
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


import os
import sys
import time

from book import Book


if len(sys.argv) < 4:
    print ("Usage: %s <manga title> <export directory> <source directory...>" % sys.argv[0])
    sys.exit(1)

book = Book()
book.title = sys.argv[1]
book.directory = sys.argv[2]
directories = sys.argv[3:]

print('Sanity check:')
print('Manga title: %s' % book.title)
print('Export directory: %s' % os.path.join(unicode(book.directory), unicode(book.title)))
for dir in directories:
    print('Source directory: %s' % unicode(dir))

print('Press Ctrl-C to abort. Beginning conversion in 5 seconds...')
time.sleep(5)

# if we didn't get interrupted, begin conversion
print('Beginning conversion...')
book.addImageDirs(directories)
book.export()


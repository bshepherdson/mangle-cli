# Copyright (C) 2010  Alex Yatskov
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
import image

def convertPage(book, index):
    directory = os.path.join(unicode(book.directory), unicode(book.title))
    target = os.path.join(directory, '%05d.png' % index)
    source = unicode(book.images[index])

    if index == 0:
        try:
            if not os.path.isdir(directory):
                os.makedirs(directory)
        except OSError:
            print('Cannot create directory %s' % directory)
            sys.exit(1)
            return

        try:
            base = os.path.join(directory, unicode(book.title))

            mangaName = base + '.manga'
            if book.overwrite or not os.path.isfile(mangaName):
                manga = open(mangaName, 'w')
                manga.write('\x00')
                manga.close()

            mangaSaveName = base + '.manga_save'
            if book.overwrite or not os.path.isfile(mangaSaveName):
                mangaSave = open(base + '.manga_save', 'w')
                saveData = u'LAST=/mnt/us/pictures/%s/%s' % (book.title, os.path.split(target)[1])
                mangaSave.write(saveData.encode('utf-8'))
                mangaSave.close()

        except IOError:
            print('Cannot write mange file(s) to directory %s' % directory)
            sys.exit(1)
            return False

    print('Converting %d of %d: %s' % (index+1, len(book.images), source))

    try:
        if book.overwrite or not os.path.isfile(target):
            image.convertImage(source, target, str(book.device), book.imageFlags)
    except RuntimeError, error:
        print('Encountered an error: %s' % error)
        sys.exit(1)
        return


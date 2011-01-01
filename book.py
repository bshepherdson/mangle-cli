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

import image
from image import ImageFlags

from convert import convertPage

class Book:
    DefaultDevice = 'Kindle 3'
    DefaultOverwrite = True
    DefaultImageFlags = ImageFlags.Orient | ImageFlags.Resize | ImageFlags.Quantize


    def __init__(self):
        self.images = []
        self.title = None
        self.device = Book.DefaultDevice
        self.overwrite = Book.DefaultOverwrite
        self.imageFlags = Book.DefaultImageFlags
        self.directory = None

    def export(self):
        if len(self.images) == 0:
            print('No images found to export.')
            return

        for index in range(0,len(self.images)):
            convertPage(self, index)


    def addImageDirs(self, directories):
        filenames = []

        directories.sort()
        for directory in directories:
            for root, subdirs, subfiles in os.walk(unicode(directory)):
                subfiles.sort()
                subdirs.sort()
                for filename in subfiles:
                    path = os.path.join(root, filename)
                    if self.isImageFile(path):
                        filenames.append(path)

        print('Found %d image files.' % len(filenames))
        self.addImageFiles(filenames)


    def addImageFiles(self, filenames):
        for filename in filenames:
            self.images.append(filename)


    def isImageFile(self, filename):
        imageExts = ['.jpeg', '.jpg', '.gif', '.png']
        filename = unicode(filename)
        return (
            os.path.isfile(filename) and
            os.path.splitext(filename)[1].lower() in imageExts
        )


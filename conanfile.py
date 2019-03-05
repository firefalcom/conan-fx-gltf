# -*- coding: utf-8 -*-

import os
from conans import ConanFile, tools

class FxgltfConan(ConanFile):
    name = 'fx-gltf'
    version = '1.0.1'
    description = 'A C++14/C++17 header-only library for simple, efficient, and robust serialization/deserialization of glTF 2.0.'
    url = 'https://github.com/birsoyo/conan-fx-gltf'
    homepage = 'https://github.com/jessey-git/fx-gltf'
    author = 'Orhun Birsoy <orhunbirsoy@gmail.com>'

    license = 'MIT'

    no_copy_source = True

    # Packages the license for the conanfile.py
    exports = ["LICENSE.md"]

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"

    def requirements(self):
        self.requires('json/3.5.0@sesame/stable')

    def source(self):
        source_url = 'https://github.com/jessey-git/fx-gltf'
        tools.get(f'{source_url}/archive/v{self.version}.tar.gz')
        extracted_dir = self.name + '-' + self.version

        #Rename to "source_folder" is a convention to simplify later steps
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, 'include')
        self.copy(pattern='LICENSE', dst='license', src=self.source_subfolder)
        self.copy(pattern='*', dst='include', src=include_folder)

    def package_id(self):
        self.info.header_only()

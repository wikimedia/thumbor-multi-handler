# -*- coding: utf-8 -*-

# Copyright (c) 2016, thumbor-community, Wikimedia Foundation
# Use of this source code is governed by the MIT license that can be
# found in the LICENSE file.

from tc_core import Extension, Extensions
from wikimedia_thumbor_multi_handler.handlers.multi import MultiHandler


extension = Extension('wikimedia_thumbor_multi_handler')
extension.add_handler(MultiHandler.regex(), MultiHandler)

Extensions.register(extension)

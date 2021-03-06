# (C) Copyright 2005-2020 Enthought, Inc., Austin, TX
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in LICENSE.txt and may be redistributed only under
# the conditions described in the aforementioned license. The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
#
# Thanks for using Enthought open source!

import logging

logger = logging.getLogger(__name__)
logger.warning(
    "DEPRECATED: pyface.util.grid.api, use pyface.wx.grid.api instead. "
    "Will be removed in Pyface 7."
)

from pyface.wx.grid.api import *

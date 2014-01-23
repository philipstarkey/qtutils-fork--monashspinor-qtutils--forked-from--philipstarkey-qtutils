#####################################################################
#                                                                   #
# __init__.py                                                       #
#                                                                   #
# Copyright 2013, Christopher Billington, Philip Starkey            #
#                                                                   #
# This file is part of the qtutils project                          #
# (see https://bitbucket.org/philipstarkey/qtutils )                #
# and is licensed under the Simplified BSD License.                 #
# See the license.txt file in the root of the project               #
# for the full license.                                             #
#                                                                   #
#####################################################################

__version__ = '1.0.0'

from PySide.QtCore import qInstallMsgHandler 

def _message_handler(type, message):
    """Handle qt warnings etc with an exception, so they don't pass
    unnoticed"""
    print '%s: %s'%(type,message)
    #raise Exception('%s: %s'%(type,message))
        
qInstallMsgHandler(_message_handler)
del qInstallMsgHandler

from locking import qtlock
qtlock.enforce()

from invoke_in_main import inmain, inmain_later, inthread, inmain_decorator

from qsettings_wrapper import QSettingsWrapper
from UiLoader import UiLoader

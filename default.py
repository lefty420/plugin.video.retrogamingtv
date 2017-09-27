# -*- coding: utf-8 -*-
#------------------------------------------------------------
# 
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# 
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.retrotv'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_ID_1 = "UC_24jKIAWs4f3nk21CGgVRg"
YOUTUBE_CHANNEL_ID_2 = "PL3tf-8jUewlnWQ1cD5xaYjlmY8640BYVB"
YOUTUBE_CHANNEL_ID_3 = "PL3tf-8jUewll7lWLg23G7bhDq6lYEBKLH"
YOUTUBE_CHANNEL_ID_4 = "PL3tf-8jUewlmIFw7oZxpa_QVFWOelkyzf"
YOUTUBE_CHANNEL_ID_5 = "PL3tf-8jUewlkLQe9_NppdO7QI9VvgZ7cI"
YOUTUBE_CHANNEL_ID_6 = ""
YOUTUBE_CHANNEL_ID_7 = ""
YOUTUBE_CHANNEL_ID_8 = ""
YOUTUBE_CHANNEL_ID_9 = ""
YOUTUBE_CHANNEL_ID_10 = ""
YOUTUBE_CHANNEL_ID_11 = "PLE72EBEB8564D1357"
YOUTUBE_CHANNEL_ID_12 = "PLySo2SlSHPSODlQTwnsqEyP9CcTMQpYg_"
YOUTUBE_CHANNEL_ID_13 = "PLySo2SlSHPSPsMPvx3vXPmReAe05Vro9H"
YOUTUBE_CHANNEL_ID_14 = "PLySo2SlSHPSMTwqoNnjALvrxbyhP5sPQ0"
YOUTUBE_CHANNEL_ID_15 = "PL6fJmjt84zZhVlt_nTOeWQM8FCOEg4V4s"


# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="home",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/playlists/",
        thumbnail="http://www.ismokemag.co.uk/wp-content/uploads/2017/02/logo-retina.png",
        fanart="http://www.ismokemag.co.uk/wp-content/uploads/2017/09/gg4-organic-10.jpg",
        
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Stran Reviews",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://www.ismokemag.co.uk/wp-content/uploads/2017/09/gg4-organic-15.jpg",
        fanart="https://scontent-lhr3-1.xx.fbcdn.net/v/t31.0-8/20776410_1788082307874573_2176504166901003467_o.jpg?oh=f54807e7743da98b0e662c88a4c34b3e&oe=5A82340C",
        
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Wake and Bake With Tyler Green",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://scontent-lhr3-1.xx.fbcdn.net/v/t31.0-8/20776410_1788082307874573_2176504166901003467_o.jpg?oh=f54807e7743da98b0e662c88a4c34b3e&oe=5A82340C",
        fanart="https://scontent-lhr3-1.xx.fbcdn.net/v/t31.0-8/20776410_1788082307874573_2176504166901003467_o.jpg?oh=f54807e7743da98b0e662c88a4c34b3e&oe=5A82340C",
        folder=True )
  
    plugintools.add_item( 
        #action="", 
        title="Vlogs and Updates",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
       thumbnail="https://scontent-lhr3-1.xx.fbcdn.net/v/t31.0-8/20776410_1788082307874573_2176504166901003467_o.jpg?oh=f54807e7743da98b0e662c88a4c34b3e&oe=5A82340C",
        fanart="https://scontent-lhr3-1.xx.fbcdn.net/v/t31.0-8/20776410_1788082307874573_2176504166901003467_o.jpg?oh=f54807e7743da98b0e662c88a4c34b3e&oe=5A82340C",
        folder=True )
    
    plugintools.add_item( 
        #action="", 
        title="Uk Cannabis Clubs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://scontent-lhr3-1.xx.fbcdn.net/v/t31.0-8/20776410_1788082307874573_2176504166901003467_o.jpg?oh=f54807e7743da98b0e662c88a4c34b3e&oe=5A82340C",
        fanart="https://scontent-lhr3-1.xx.fbcdn.net/v/t31.0-8/20776410_1788082307874573_2176504166901003467_o.jpg?oh=f54807e7743da98b0e662c88a4c34b3e&oe=5A82340C",
        folder=True )
        
       
run()

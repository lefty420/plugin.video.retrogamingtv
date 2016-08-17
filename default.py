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

YOUTUBE_CHANNEL_ID_1 = "UCUVnfQaEmCIhFZC5d_JniyQ"
YOUTUBE_CHANNEL_ID_2 = "PLjnS472dZmYFlTGofe2Hzbsc9mAf5zEK9"
YOUTUBE_CHANNEL_ID_3 = "PLV4e_YFAA9T7topw7Hcny9gvI--KAUkBB"
YOUTUBE_CHANNEL_ID_4 = "PLV4e_YFAA9T4lz6DOTE4ZSd6gVcga6caf"
YOUTUBE_CHANNEL_ID_5 = "PL093A0D4B558C61E5"
YOUTUBE_CHANNEL_ID_6 = "PLB44A955104D61542"
YOUTUBE_CHANNEL_ID_7 = "PLCQyVJaPXQ7XzLLgaKEPUXctixKQPu73V"
YOUTUBE_CHANNEL_ID_8 = "PLbQ-gSLYQEc6IWgKJNOMUONgtNXdwVcDC"
YOUTUBE_CHANNEL_ID_9 = "PL8ByfLs8i7KT9Swtj0uQe1Wm98kkFIocH"
YOUTUBE_CHANNEL_ID_10 = "PLZQwwCu9Y8bduFA1jCUQwQKDGlCo68t8k"
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
        title="Classic Gaming Cartoons",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_ID_1+"/playlists/",
        thumbnail="http://www.superluigibros.com/images/super_mario_bros_super_show_releases/mario_bros_mix.jpg",
        fanart="https://i.ytimg.com/vi/_7mW3JM8dpE/maxresdefault.jpg",
        
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Games Master",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="http://vignette1.wikia.nocookie.net/magazinesfromthepast/images/5/5e/GamesMaster_Issue_8.jpg/revision/latest?cb=20130624082416",
        fanart="http://megagames.com/sites/default/files/game-content-images/gamesmaster.jpg",
        
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Bad Influence",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="http://vignette1.wikia.nocookie.net/magazinesfromthepast/images/3/3a/Bad_Influence_Issue_1.jpg/revision/latest?cb=20141128220822",
        fanart="http://vignette1.wikia.nocookie.net/magazinesfromthepast/images/3/3a/Bad_Influence_Issue_1.jpg/revision/latest?cb=20141128220822",
        folder=True )

   
   
    plugintools.add_item( 
        #action="", 
        title="Games Wolrd",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce619ce4b0d911b449a1d0/1333603993933/1000w/hitchcock4420121.jpeg",
        fanart="https://i.ytimg.com/vi/uRuzzzMODi8/maxresdefault.jpg",
        folder=True )  
    
    plugintools.add_item( 
        #action="", 
        title="Angry Video Game Nerd",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="http://ih1.redbubble.net/image.117727901.3187/raf,750x1000,075,t,101010:01c5ca27c6.jpg",
        fanart="https://i.ytimg.com/vi/1A5B8fXp0aU/maxresdefault.jpg",
        folder=True )
        
    plugintools.add_item( 
        #action="", 
        title="Classic Gaming commercials",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://static.squarespace.com/static/51b3dc8ee4b051b96ceb10de/51ce6099e4b0d911b4489b79/51ce61bae4b0d911b449ea22/1318437497002/1000w/nesclasicart8.jpeg",
        fanart="https://mpgs.scdn3.secure.raxcdn.com/images/kcfinder/upload/image/NesWall.jpg",
        folder=True )   
           
    plugintools.add_item( 
        #action="", 
        title="Video Game Nation",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/e6/52/3f/e6523f23e24a0764c987f4f9bb81c743.jpg",
        fanart="http://i.imgur.com/Gc4Xa.jpg",
        folder=True ) 
        
    plugintools.add_item( 
        #action="", 
        title="Screw Attack Top 10",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/9e/7e/24/9e7e244c357025bb57306b1b9bda88eb.jpg",
        fanart="http://orig13.deviantart.net/65ee/f/2009/213/b/4/screwattack_wallpaper_by_warman333.jpg",
        folder=True )   
        
    plugintools.add_item( 
        #action="", 
        title="RetroGame Music",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://pleated-jeans.com/wp-content/uploads/2011/02/Calvin-and-Hobbes-NES-Box-Art.jpg",
        fanart="http://cdn3.dualshockers.com/wp-content/uploads/2013/11/gmf.jpg",
        folder=True )    
        
    plugintools.add_item( 
        #action="", 
        title="Retro Hardware",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="http://pre10.deviantart.net/dd7f/th/pre/i/2012/347/d/2/assassin__s_creed_3__nes_style_by_ricgraydesign-d5nw7me.png",
        fanart="http://www.tokoretreat.co.uk/wp-content/uploads/2015/07/photo_game_console_icons_by_pixeloz-d28ry4i.jpg",
        folder=True )  
        
    plugintools.add_item( 
        #action="", 
        title="Speed Runs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="http://s3.media.squarespace.com/production/544173/6277734/wp-content/uploads/2009/05/half-life-2.jpg",
        fanart="https://s-media-cache-ak0.pinimg.com/originals/61/af/35/61af351b7f5ebf11a79f29ff5c59ea86.jpg",
        folder=True )               
run()

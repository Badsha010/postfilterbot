# Copyright (C) @CodeXBotz - All Rights Reserved
# Licensed under GNU General Public License as published by the Free Software Foundation
# Written by Shahsad Kolathur <shahsadkpklr@gmail.com>, June 2021

from pyrogram import __version__
from InlineBot import CUSTOM_START_MESSAGE

if CUSTOM_START_MESSAGE:
    START_MESSAGE = CUSTOM_START_MESSAGE
else:
    START_MESSAGE = """<b>Hello {mention},

I am an Inline Saver Bot, you can save inline filters and It can be use in any of your chats easily, Click help for more details</b> 
"""

HELP_MESSAGE = """<b><u>Main Available Commands</u></b>

○ <b>/add</b> <i>[keyword] [message or reply to message]</i>
    <i>Add an Inline filter, you can use MarkDown for formatting</i>
    
○ <b>/del</b> <i>[keyword]</i>
    <i>Delete existing Filter</i>
    
○ <b>/filters</b>
    <i>To view see your filters</i>
    
○ <b>/delall</b>
    <i>Delete all of your filters</i>
    
○ <b>/import</b> <i>[reply to an exported file]</i>
    <i>Import filters from Backup file</i>
    
○ <b>/export</b>
    <i>Export a Backup file of filters, this can be import by others</i>
"""

ABOUT_MESSAGE = f"""<b><u>ABOUT ME</u></b>

<b>○ Support : <a href='https://t.me/CodeXBotzSupport'>Code 𝕏 Botz Support</a>
○ Language : <a href='https://www.python.org/'>Python 3</a>
○ Library : <a href='https://github.com/pyrogram/pyrogram'>Pyrogram Asyncio {__version__}</a>
○ Channel : <a href='https://t.me/CodeXBotz'>Code 𝕏 Botz</a></b>"""

MARKDOWN_HELP = """<b><u>Markdown Formatting</u></b>

○ <b>Bold Words</b> :
    format: <code>*Bold Text*</code>
    show as: <b>Bold Text</b>
    
○ <b>Italic Text</b>
    format: <code>_Italic Text_</code>
    show as: <i>Italic Text</i>
    
○ <b>Code Words</b>
    format: <code>`Code Text`</code>
    show as: <code>Code Text</code>
    
○ <b>Under Line</b>
    format: <code>__UnderLine Text__</code>
    show as: <u>UnderLine Text</u>
    
○ <b>StrikeThrough</b>
    format: <code>~StrikeThrough Text~</code>
    show as: <s>StrikeThrough Text</s>
    
○ <b>Hyper Link</b>
    format: <code>[Text](https://t.me/CodeXBotz)</code>
    show as: <a href='https://t.me/CodeXBotz'>Text</a>
    
○ <b>Buttons</b>
    <u>Url Button</u>:
    <code>[Button Text](buttonurl:https://t.me/CoddeXBotz)</code>
    <u>Alert Button</u>:
    <code>[Button Text](buttonalert:Alert Text)</code>
    <u>In Sameline</u>:
    <code>[Button Text](buttonurl:https://t.me/CodeXBotz:same)</code></i>

○ <b>Notes:</b>
    <i>Keep every Buttons in Seperate line when formating</i>
    <i>Your alert message text must be less than 200 characters, otherwise bot will ignore that button</i>

○ <b>Tip:</b> <i>You can add buttons for sticker and video note in /add command</i>"""

#!/bin/sh

# Mouse cursor theme
xsetroot -cursor_name left_ptr

# Set keyboard layouts
setxkbmap -model pc105+inet -layout us,ru -option grp:caps_toggle &

# Keyboard per application daemon
kbdd &

# Nitrogen
nitrogen --restore &

# Xbindkeys
xbindkeys &

# Picom compositor
# picom &


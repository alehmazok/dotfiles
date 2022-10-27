#!/bin/sh

# Mouse cursor theme
xsetroot -cursor_name left_ptr

# Set keyboard layouts
setxkbmap -model pc105+inet -layout us,ru -option grp:caps_toggle &

# Keyboard per application daemon
kbdd &

# Keys remappgings
# No need to load it when using LightDM
# xmodmap $HOME/.Xmodmap

# Nitrogen
nitrogen --restore &

# Xbindkeys
xbindkeys &

# Picom compositor
# picom &

# Polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Network manager applet
nm-applet &

# Clipboard manager
# clipit &

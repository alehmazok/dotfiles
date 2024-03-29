# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "space", lazy.spawn('rofi -show drun'), desc="Spawn an application"),
    Key([mod, 'shift'], "space", lazy.spawn('rofi -show p -modi \
                        "p:rofi-power-menu --choices=lockscreen/logout/reboot/shutdown" \
                        -theme squared-everforest \
                        -font "JetBrains Mono 16" \
                        -width 20 \
                        -lines 6'
                        ), desc="Spawn an power menu"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], 'b', lazy.spawn('setxkbmap -model pc105+inet -layout us,by -option grp:caps_toggle'), desc="Set Belarus layout"),
    Key([mod, 'shift'], 'b', lazy.spawn('setxkbmap -model pc105+inet -layout us,ru -option grp:caps_toggle'), desc="Set Rus layout"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

colors = [
            '#111A2D',
            '#1D2E4E',
            '#2D112A',
            '#530030',
            '#7E0030',
            '#CA283D',
            '#FF583D',
            '#FF7E4A',
        ]

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Columns(
        border_focus=["#B9CA4A", "#B5BD68"], 
        border_focus_stack=["#ff8400", "#8f3d3d"], 
        border_width=3,
        margin=0,
        insert_position=1,
        ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=19,
    padding=0,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    padding=20,
                    ),
                widget.GroupBox(
                    margin_x=5,
                    padding_x=6,
                    padding_y=2,
                    # spacing=10,
                    ),
                widget.Prompt(),
                widget.WindowName(
                    padding=20,
                    ),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # widget.ThermalZone(),
                widget.Wttr(
                    location={
                        'Minsk': 'Minsk',
                        },
                    padding=20,
                    # background=colors[0],
                    ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    foreground=colors[1],
                    size_percent=100,
                    ),
                # widget.TextBox(
                #     text='',
                #     background=colors[2],
                #     foreground=colors[1],
                #     padding=0,
                #     fontsize=64,
                #     ),
                # widget.Bluetooth(),
                widget.ThermalSensor(
                        tag_sensor='edge',
                        padding=20,
                        # background=colors[1],
                        # fmt='GPU: {}',
                    ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    foreground=colors[1],
                    size_percent=100,
                    ),
                widget.Memory(
                        measure_mem='G',
                        format='{MemUsed:.1f}{mm} /{MemTotal: .1f}{mm}',
                        # background=colors[2],
                        # foreground=colors[1],
                        padding=20,
                        # fmt='RAM: {}',
                    ),
                # widget.PulseVolume(
                #     padding=20,
                #     ),
                # widget.Wlan(
                #     format='{essid} {percent:2.0%}',
                #     padding=20,
                #     background=colors[3],
                #     interface='wlan1',
                #     # fmt='Wifi: {}',
                #     ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    foreground=colors[1],
                    size_percent=100,
                    ),
                widget.KeyboardKbdd(
                    configured_keyboards=['us', 'ru', 'by'],
                    padding=20,
                    # background=colors[3],
                    ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    foreground=colors[1],
                    size_percent=100,
                    ),
                widget.Clock(
                    # format="%Y-%m-%d %a %H:%M",
                    format='%B %d, %H:%M',
                    padding=20,
                    # background=colors[4],
                    ),
                widget.Sep(
                    padding=10,
                    linewidth=2,
                    foreground=colors[1],
                    size_percent=100,
                    ),
                widget.Systray(
                    icon_size=24,
                    padding=20,
                    ),
                widget.Spacer(
                        length=30,
                        ),
                # widget.Sep(
                #     padding=10,
                #     linewidth=2,
                #     foreground=colors[1],
                #     size_percent=100,
                #     ),
                # widget.QuickExit(
                #     countdown_start=3,
                #     # default_text='🛑',
                #     padding=20,
                #     ),
            ],
            38,
            background='#111A2D',
            # border_color='#111A2D',
            # border_width=[0, 20, 0, 20],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=['#FF9B54'],
    border_width=3,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        # Match(wm_class="jetbrains-idea"),
        Match(title='Android Emulator'),
        Match(wm_class='lxappearance'),
        Match(wm_class='blueman-manager'),
        Match(wm_class='gpick'),        
        Match(wm_class='nomacs'),
        Match(wm_class='nm-connection-editor'),
        Match(wm_class='thunar'),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# Hooks
@hook.subscribe.startup_once
def autostart():
    autostart = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([autostart])


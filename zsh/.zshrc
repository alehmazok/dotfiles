# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=10000
SAVEHIST=10000
bindkey -e
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/aleh/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Profile
source $HOME/.profile

# Autosuggestions
# source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
# export ZSH_AUTOSUGGEST_STRATEGY=completion
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh

# Word movements
# Ctrl key
bindkey "^[[1;5C" forward-word
bindkey "^[[1;5D" backward-word
# Alt key
# bindkey "^[[1;3C" forward-word
# bindkey "^[[1;3D" backward-word
bindkey "^[[F" end-of-line  # Key End
bindkey "^[[H" beginning-of-line  # Key Beginning
# Ctrl + backspace
bindkey '^H' backward-kill-word
# Alt+Backspace
backward-kill-dir () {
    local WORDCHARS=${WORDCHARS/\/}
    zle backward-kill-word
    zle -f kill  # Ensures that after repeated backward-kill-dir, Ctrl+Y will restore all of them.
}
zle -N backward-kill-dir
bindkey '^[^?' backward-kill-dir
# Delete key
bindkey "^[[3~" delete-char

# Search history
autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search
zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search
bindkey "^[[A" up-line-or-beginning-search # Up
bindkey "^[[B" down-line-or-beginning-search # Down

# Neofetch perfomance
# cat .nf 2> /dev/null
# setsid neofetch >| .nf

# Aleh's aliases
# alias ll="ls -lha"
alias ll="exa -lha"
alias pacup="sudo pacman -Syy && sudo pacman -Syu"
alias yayup="yay -Syu && yay -Syu"
# alias google-chrome="chromium"

# Starship
eval "$(starship init zsh)"

# direnv
eval "$(direnv hook zsh)"

autoload zmv

## [Completion] 
## Completion scripts setup. Remove the following line to uninstall
[[ -f /home/aleh/.config/.dart-cli-completion/zsh-config.zsh ]] && . /home/aleh/.config/.dart-cli-completion/zsh-config.zsh || true
## [/Completion]


# Dotbot `paru` Plugin

A [Dotbot](https://github.com/anishathalye/dotbot) plugin to install packages on Arch Linux via [`paru`](https://github.com/Morganamilo/paru)

Based on [dotbot-yay](https://github.com/alexwh/dotbot-yay), which is based on [dotbot-pacaur](https://github.com/ajlende/dotbot-pacaur). This plugin will attempt to install `paru` if it is not present.

## Installation

Add this plugin to your dotfiles repository, for example by using a submodule:

```bash
git submodule add https://github.com/ConnorJC3/dotbot-paru.git
```

## Usage

Invoke dotbot with the `--plugin-dir` option, such as by modifying the default configuration like so:

```bash
"${BASEDIR}/${DOTBOT_DIR}/${DOTBOT_BIN}" -d "${BASEDIR}" -c "${CONFIG}" --plugin-dir "${BASEDIR}/dotbot-paru" "${@}"
```

## Configuration

Example configuration:

```yaml
- paru:
  - vim
  - zsh
  - firefox-nightly
```

For organization, you may also split packages between `pacman` and `paru` directives (they are functionally equivalent):

```yaml
- pacman:
  - vim
  - zsh
- paru:
  - firefox-nightly
```

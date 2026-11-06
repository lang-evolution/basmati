# Basmati Hyprland UI

## Install Elkowar's Eww and Python

NixOS: simply add:

```nix
eww
python3
wpctl
```

## Configure Hyprland

`~/config/hypr/hyprland.lua`

```lua
local basmati_root = "/PLACE/WHERE/YOU/CLONED/BASMATI"

<!-- You can use a hardcoded monitor like "e-DP1" instead of hl.get_monitors()[1] -->
local basmati_monitor = hl.get_monitors()[1]

hl.on("hyprland.start", function ()
  hl.exec_cmd("eww open --config " .. basmati_root .. " main_panel --arg 'basmati_monitor =" .. basmati_monitor .. "'")
end)
```

#!/usr/bin/env python3

import subprocess
import sys
import json

SOUND_BAR_COUNT = 5

shell = lambda args: subprocess.run(args, stdout=subprocess.PIPE).stdout.decode("utf-8")
hyprland = lambda cmd: ev(["hyprctl", "repl" f"'{cmd}'"])

volume = float(split(shell("wpctl get-volume @DEFAULT_AUDIO_SINK@"), " ")[1])
sound_bar_increment = 1.0 / SOUND_BAR_COUNT

def workspaces():
    return {
        "active": hyprland("hl.get_workspace(hl.get_active_workspace()).id"),
        "total": hyprland("getn(hl.get_workspaces())")
    }

def sound_bars():
    return {
        
    }

readings = {
    "workspaces": lambda: ,
    "sound_bars": map(lambda i: { "index": i, "active": volume <= sound_bar_increment * i}, 0..sound_bar_count),
    "warnings": {
        "network": shell("nm-online -t 4 && echo 1") == "1" ?
            { "attention": false, "state": "ONLINE" } :
            { "attention": true, "state": "OFFLINE" },
        "memory": { "": "", "": "" },
        "processor": { "": "" },
    }
    # TODO battery
}

workspaces_index_of_active = hyprland("hl.get_workspace(hl.get_active_workspace()).id")
workspaces_total_count = hyprland("getn(hl.get_workspaces())")

print(json.dumps(readings[sys.arv[1]]))


workspaces = {
    "active": 
    "total": 
}

num_of_current_workspaces = lambda: 
    return ev(["hyprctl", "repl" "''"])

def num_of_total_workspaces():
    return 

fn = sys.argv[0]
args = sys.argv[1:]

print(call(locals()[fn], args)

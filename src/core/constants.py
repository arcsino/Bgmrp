def get_blank_pack_mcmeta():
    return {
        "pack": {
            "min_format": 15,
            "max_format": 75,
            "pack_format": 75,
            "supported_formats": [15, 75],
            "description": "",
        }
    }


def get_blank_project_obj():
    return {
        "name": "",
        "description": "",
        "icon": "",
        "sounds": [],
        "volume": 20,
        "version": "1.21.11",
    }


def get_blank_sounds_obj():
    return {
        "music.creative": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.credits": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.dragon": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.end": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.game": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.menu": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.nether.basalt_deltas": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.nether.crimson_forest": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.nether.nether_wastes": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.nether.soul_sand_valley": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.nether.warped_forest": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.badlands": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.bamboo_jungle": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.cherry_grove": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.deep_dark": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.desert": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.dripstone_caves": {
            "sounds": [{"name": "bgm", "type": "event"}]
        },
        "music.overworld.flower_forest": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.forest": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.frozen_peaks": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.grove": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.jagged_peaks": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.jungle": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.lush_caves": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.meadow": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.old_growth_taiga": {
            "sounds": [{"name": "bgm", "type": "event"}]
        },
        "music.overworld.snowy_slopes": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.sparse_jungle": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.stony_peaks": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.overworld.swamp": {"sounds": [{"name": "bgm", "type": "event"}]},
        "music.under_water": {"sounds": [{"name": "bgm", "type": "event"}]},
        "bgm": {},
    }


def get_format_version():
    return {
        "1.21.11": 75,
        "1.21.9-1.21.10": 69,
        "1.21.7-1.21.8": 64,
        "1.21.6": 63,
        "1.21.5": 55,
        "1.21.4": 46,
        "1.21-1.21.3": 34,
        "1.20.5-1.20.6": 32,
        "1.20.3-1.20.4": 22,
        "1.20.2": 18,
        "1.20-1.20.1": 15,
    }

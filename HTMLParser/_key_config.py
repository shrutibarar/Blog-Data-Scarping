# base format for keys

base_key_format = {

    # main content to be scrapped from focus
    "focus": {
        "div": "ch bg et eu ev ew"
    },

    # tags and their respective titles and contents to be scrapped
    "contents": {
        "h1": {
            "pw-post-title": "Title",
            "Data-selectable-paragraph": "Key points"
        },
        "h2": {
            "Pw-subtitle-paragraph": "subtitle",
            "sub-sub-title": "major points",
        },

        "li": {
            "data-selectable-paragraph": None
        },
    },
    "paragraph": {
        "p": {
            " pw-post-body-paragraph": None,
            "em": None,
            "a": None,
            "af nc": None,
            "data-selectable-paragraph": None
        },
    },
    "figures": {
        "path": None    # if none then use a default path
    },
    "links": False      # either include links or not by default its false
 }




# keys for Medium website

# base format for keys

base_key_format = {

    # main content to be scrapped from focus
    "focus": "class_name",
    # tags and their respective titles and contents to be scrapped
    "contents": {
        "h1": {
            "class_name": "Title",
        },
        "h2": {
            "class_name": "subtitle",
        },
    },
    "figures": {
        "path": None  # if none then use a default path
    },
    "links": False  # either include links or not by default its false
}


# medium website content format keys
medium_key_format = {

    "focus": {
        "div": "ch bg et eu ev ew"
    },

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
        "p": {
            " pw-post-body-paragraph": None,
            "em": None,
            "a": None,
            "af nc": None,
            "data-selectable-paragraph": None
        },
    },
    "figures": {
        "path": None
    },
    "links": False
}

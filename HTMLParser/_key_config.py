# base format for keys

base_key_format = {

    # main content to be scrapped from focus
    "focus": {
        "div": "class_name"
    },

    # tags and their respective titles and contents to be scrapped
    "contents": {
        "h1": {
            "class_name": "what it does? e.g Title",
            "class_name_2": "Key points"
        },
        "h2": {
            "class_name": "subtitle",
            "class_name_2": "major points",
        }
    },
    "figures": {
        "path": None    # if none then use a default path
    },
    "links": False      # either include links or not by default its false
}

# keys for Medium website

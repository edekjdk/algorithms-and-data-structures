wi1 = {
    "name": "A Standup Cloud Team",
    "start_hour": 8,
    "prev": None,
    "next": None
}

wi2 = {
    "name": "B Architecture Board",
    "start_hour": 9,
    "prev": None,
    "next": None
}

wi3 = {
    "name": "C Cloud Training",
    "start_hour": 12,
    "prev": None,
    "next": None
}

wi1["next"] = wi2
wi2["prev"] = wi1
wi2["next"] = wi3
wi3["prev"] = wi2
work = wi1

# item = work
# while item:
#     print(item["name"])
#     item = item["next"]

def add_item_begin(my_collection, new_item):
    new_item["next"] = my_collection
    new_item["prev"] = None

    if my_collection:
        my_collection["prev"] = new_item
    my_collection = new_item
    return my_collection

wi4 = {
    "name": "_ Manager meeting",
    "start_hour": 12,
    "prev": None,
    "next": None
}


work = add_item_begin(work, wi4)

item = work
while item:
    print(item["name"])
    item = item["next"]

def add_item_end(my_collection, new_item):
    if my_collection == None:
        new_item["prev"] = None
        new_item["next"] = None
        return my_collection
    else:
        item = my_collection
        while item["next"]:
            item = item["next"]
        item["next"] = new_item
        new_item["next"] = None
        new_item["prev"] = item
        return my_collection

wi5 = {
    "name": "_ Compliance Check",
    "start_hour": 12,
    "prev": None,
    "next": None
}

work = add_item_end(work, wi5)

item = work
while item:
    print(item["name"])
    item = item["next"]
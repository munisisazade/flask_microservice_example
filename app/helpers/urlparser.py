from bson import ObjectId


def url_parse(url):
    url_list = url.split("/")
    base_id = url_list[-1]
    if url_list[-1]:
        try:
            ObjectId(base_id)
            return "".join(url.rsplit("/", 1)[0]) + "/{id}"
        except:
            return url

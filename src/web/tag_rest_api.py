"""Tag Rest API"""
from flask import Blueprint


blueprint = Blueprint("tags", __name__)


class TagRestAPI:
    """Tag Rest API"""

    @blueprint.route("/tags", methods=["GET"])
    def get_tag_list(self):
        """Get Tag List"""

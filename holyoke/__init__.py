# Copyright (c) Sunlight Foundation, 2014, under the terms of the BSD-3
# license, a copy of which is in the root level LICENSE file.
#
# This scraper was done at Hack for Western Mass, a huge shoutout
# to all the civic hackers and the Hack for Western Mass folks.

from pupa.utils import make_psuedo_id
from pupa.scrape import Jurisdiction, Post
from .people import HolyokePersonScraper

NAME = "Holyoke City"


class Holyoke(Jurisdiction):
    division_id = 'ocd-division/country:us/state:ma/place:holyoke'
    jurisdiction_id = 'ocd-jurisdiction/country:us/state:ma/place:holyoke/government'
    name = NAME
    url = 'http://www.holyoke.org/elected-officials/'

    scrapers = {
        "people": HolyokePersonScraper
    }

    # XXX: Add divison IDs
    posts = [Post(organization_id=make_psuedo_id(
        name=NAME,
        classification="legislature",
    ), **x) for x in [
        {"label": "Mayor", "role": "mayor",},
        {"label": "City Clerk", "role": "clerk",},
        {"label": "City Treasurer", "role": "treasurer",},
        {"label": "At Large", "role": "councilmember",},

        {"label": "Ward 1", "role": "councilmember"},
        {"label": "Ward 2", "role": "councilmember"},
        {"label": "Ward 3", "role": "councilmember"},
        {"label": "Ward 4", "role": "councilmember"},
        {"label": "Ward 5", "role": "councilmember"},
        {"label": "Ward 6", "role": "councilmember"},
        {"label": "Ward 7", "role": "councilmember"},
    ]]

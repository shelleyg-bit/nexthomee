
class SearchListings:
    def __init__(self, city='Portland, OR'):
        self.city = city
        return

    def payload(self, maximumListings):
        # TODO: currently city is fixed to portland,
        # make the bounding box change according to city
        # or zipcode
        return {
            "maximumListings": maximumListings,
            "maximumClusters": 26,
            "zoom": 10,
            "criteria": {
                "filters": {
                    "propertyType": 511,
                    "beds": {
                        "minimum": 0,
                        "maximum": 100
                    },
                    "baths": {
                        "minimum": 0,
                        "maximum": 50
                    },
                    "price": {
                        "minimum": 0,
                        "maximum": 100000000
                    },
                    "squareFeet": {
                        "minimum": 0,
                        "maximum": 1000000
                    },
                    "lotSize": {
                        "minimum": 0,
                        "maximum": 100
                    },
                    "yearBuilt": {
                        "minimum": 0,
                        "maximum": 3000
                    },
                    "date": 0,
                    "openHouseDate": 0,
                    "transactionType": 1,
                    "features": 268435546,
                    "shape": {},
                    "polygons": {},
                    "geography": {},
                    "geographies": [
                        {
                            "type": 1,
                            "id": 31342
                        }
                    ],
                    "priceReduction": {
                        "kind": 0,
                        "isRequired": 0
                    },
                    "floors": {
                        "range": {
                            "minimum": 0,
                            "maximum": 255
                        },
                        "mode": 0
                    },
                    "schoolRatings": {
                        "allSchools": {"value": 0},
                        "elementarySchool": {"value": 0},
                        "middleSchool": {"value": 0},
                        "highSchool": {"value": 0}
                    },
                    "association": {
                        "totalMonthlyFee": {"value": 0},
                        "restrictions": 0
                    },
                    "parking": {
                        "mustHaveGarage": 0,
                        "spaces": {"value": 0}
                    },
                    "waterfront": {"isRequired": 0},
                    "propertyView": {
                        "water": {
                            "kind": 0,
                            "isRequired": 0
                        },
                        "mountainHills": {"isRequired": 0},
                        "woods": {"isRequired": 0},
                        "city": {"isRequired": 0},
                        "other": {"isRequired": 0}
                    },
                    "basement": {
                        "kind": 0,
                        "isRequired": 0
                    },
                    "pool": 0,
                    "heating": {
                        "kind": 0,
                        "isRequired": False
                    },
                    "cooling": {
                        "kind": 0,
                        "isRequired": False
                    },
                    "petFriendly": {"isRequired": 0},
                    "pricePerSquareDimension": {
                        "minimum": 0,
                        "maximum": 100000,
                        "unit": 1
                    },
                    "style": 0,
                    "noBrokerFee": {"isRequired": 0},
                    "furnished": {"isRequired": 0},
                    "outdoorSpace": {"isRequired": 0},
                    "fireplace": {"isRequired": 0},
                    "hardwoodFloor": {"isRequired": 0},
                    "hasInLawSuite": {"isRequired": 0},
                    "accessibility": {"isRequired": 0},
                    "seniorCommunity": {"isRequired": 0},
                    "washerDryer": {
                        "kind": 0,
                        "isRequired": False
                    },
                    "dishwasher": {"isRequired": 0},
                    "gym": {"isRequired": 0},
                    "secondaryResidence": {"isRequired": 0},
                    "doorman": {"isRequired": 0},
                    "unitType": {
                        "kind": 0,
                        "isRequired": False
                    },
                    "elevator": {"isRequired": 0},
                    "storage": {"isRequired": 0},
                    "bikeStorage": {"isRequired": 0}
                },
                "active": 1,
                "comingSoon": 0,
                "contract": 0,
                "sold": 0,
                "offMarket": 0,
                "openHouse": 0,
                "brokerOpen": 0,
                "boundingBox": {
                    "latitude": {
                        "minimum": 45.183884,
                        "maximum": 45.899478
                    },
                    "longitude": {
                        "minimum": -123.013499,
                        "maximum": -122.295267
                    }
                },
                "orderBy": 1,
                "places": [],
                "mode": 1
            }
        }

    def url(self):
        return "https://www.homesnap.com/service/Listings/Search"

    def headers(self):
        return {
            "Connection": "keep-alive",
            "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/json; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36",
            "sec-ch-ua-platform": '"Windows"',
            "Origin": "https://www.homesnap.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://www.homesnap.com/homes/for_sale/OR/Portland/p_(21,31342)/c_45.541681,-122.654383/z_10",
            "Accept-Language": "en-US,en;q=0.9",
        }
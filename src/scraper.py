import requests
import pickle
import time
import pandas as pd
from api import SearchListings, ListingDetails

toplevel_props = ['ListingID', 'DefaultParentArea', 'Zip', 'Url', 'Building', 'BathsFull', 'BathsHalf', 'Beds', 'CurrentPrice',\
    'Days', 'FullStreetAddress', 'Latitude', 'Longitude', 'ListDate', 'LotSize', 'OriginalPrice', 'Ownership',\
    'PropertyStyle', 'PropertyType', 'Remarks', 'SqFt', 'TownhouseType', 'UnitCount', 'WalkScore', 'WalkScoreDescription', 'YearBuilt',\
    'Zip', 'Details', 'Amenities', 'BuildingAmenities']
secondlevel_props = {'DefaultParentArea': [['Name', 'Neighborhood']],\
    'Building': [['UnitCount', 'BuildingUnitCount'],['Name', 'BuildingName']]}
details_props = {
    'Interior Features': ['Accessibility Features', 'AllRoom Features', 'Elevator', 'Interior Features',\
        'Kitchen Appliances', 'Master Bedroom', 'Bedroom 2', 'Dining Room', 'Living Room'],\
    'Utilities': ['Fuel Description', 'Hot Water', 'Sewer', 'Water Description', 'Cooling Description',\
        'Heating Description'],\
    'Green Features': ['Green Energy Supplement', 'Green Verification HES Metric', 'Green Verification HES Year', "Green Verification HES "]
}

class HomeScraper():
    def __init__(self, city):
        self.city = city
        self.search_api = SearchListings(city)
        self.listings_api = ListingDetails()
        self.listing_detail_cookies = None
        self.total_listings = 0
        self.listings = None

    def download_listings(self):
        url = self.search_api.url()
        headers = self.search_api.headers()

        #use get to pull cookies
        get_response = requests.get(url, headers=headers)
        assert get_response.status_code == 200, f"failed get request with status code: {get_response.status_code}"


        #get the count of active listings
        time.sleep(1)
        payload = self.search_api.payload(maximumListings=10)
        post_response = requests.post(url, cookies=get_response.cookies, headers=headers, json=payload)
        assert post_response.status_code == 200, f'post request to search listings returned w/ status code: {post_response.status_code}'
        response_json = post_response.json()
        self.total_listings = response_json['d']['Count']

        # get all active listings
        time.sleep(1)
        payload = self.search_api.payload(maximumListings=self.total_listings)
        post_response = requests.post(url, cookies=get_response.cookies, headers=headers, json=payload)
        assert post_response.status_code == 200, f'post request to search listings returned w/ status code: {post_response.status_code}'
        response_json = post_response.json()
        self.listings = response_json['d']['Listings']
        return
    
    def download_listing_details(self, listing_id):
        # download detail of a single listing
        url = self.listings_api.url()
        headers = self.listings_api.headers()
        payload = self.listings_api.payload(listing_id)
        
        # TODO: use get to pull cookies
        # get_response = requests.get(url, headers=headers)
        # assert get_response.status_code == 200, f"failed get request with status code: {get_response.status_code}"

        # get details
        post_response = requests.post(url, cookies=self.listing_detail_cookies, headers=headers, json=payload)
        assert post_response.status_code == 200, f'post request to listing details returned w/ status code: {post_response.status_code}'
        if not self.listing_detail_cookies:
            self.listing_detail_cookies = post_response.cookies
        response_json = post_response.json()
        return response_json['d']
    
    def download_details(self, count=None):
        if not count:
            count = self.count
        # download details of all listings
        all_listings_details = []
        for listing in self.listings[:count]:
            details = self.download_listing_details(listing['Listing']['ID'])
            time.sleep(1)
            all_listings_details.append(details)
        return all_listings_details
    
    def to_pickle(self):
        # store as object to local filesystem
        filename = f'{self.city}_homesnap_scraper.pickle'
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        return



        

    
    

home_scraper = HomeScraper('Portland, OR')
home_scraper.download_listings()

home_scraper.to_pickle()

with open('Portland, OR_homesnap_scraper.pickle', 'rb') as f:
    portland_scraper = pickle.load(f) 

all_listings_details = portland_scraper.download_details(2)
all_listings_details

def clean_listing_details(listings_details):
    cleaned_listings_details = [] 
    for details in listings_details:
        details_dict = {}
        for prop in toplevel_props:
            inner_details = details[prop]
            if not inner_details:
                details_dict[prop] = None
            elif prop in secondlevel_props.keys():
                # for nested properties, extract the values
                # and store in a renamed property key
                for inner_prop in secondlevel_props[prop]:
                    details_dict[inner_prop[1]] = inner_details[inner_prop[0]]
            elif prop == 'Details':
                # extract more deeply nested values
                for inner_prop in inner_details:
                    inner_prop_name = inner_prop['Name']
                    if inner_prop_name in details_props.keys():
                        for innermost_prop in inner_prop['Fields']:
                            innermost_prop_name = innermost_prop['Name']
                            if innermost_prop_name in details_props[inner_prop_name]:
                                details_dict[innermost_prop_name] = innermost_prop['Value']
            else:
                details_dict[prop] = inner_details 
            
        cleaned_listings_details.append(details_dict)
    return pd.json_normalize(cleaned_listings_details)

cleaned_details = clean_listing_details(all_listings_details)

cleaned_details.head()

def store_all_listings(filename, data):
    # store to local system as pickle file
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
        return

store_all_listings('portland_or_listings_df.pickle', cleaned_details)

with open('portland_or_listings_df.pickle', 'rb') as f:
    portland_listings = pickle.load(f)

portland_listings





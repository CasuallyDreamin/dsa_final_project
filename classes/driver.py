class Driver:
    def __init__(self, nid, did, license_date):
        self.nid = nid
        self.did = did
        self.license_date = license_date

    def __repr__(self):
        return f"National ID: {self.nid} | Driver ID: {self.did} | License Date: {self.license_date}"
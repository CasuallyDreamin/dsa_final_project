from classes.db.data_structures.hashtable import hashtable

class Drivers:
    def __init__(self):
        self.drivers_nid = hashtable()
        self.drivers_did = hashtable()

    def add(self, driver):
        self.drivers_nid.insert(driver.nid)
        self.drivers_did.insert(driver.did)
        return True
    
    def get_by_nid(self, nid):
        return self.drivers_nid.get(nid)
    
    def get_by_did(self, did):
        return self.drivers_did.get(did)
    
    def get_all(self):
        return self.drivers_nid.get_all()
    
    def __repr__(self):
        return self.drivers_did.get_all()

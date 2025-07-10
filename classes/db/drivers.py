from classes.db.data_structures.hashtable import hashtable
from classes.driver import Driver

class Drivers:
    def __init__(self):
        self.drivers_nid = hashtable()
        self.drivers_did = hashtable()

    def add(self, driver):
        if not self.drivers_nid.insert(str(driver.nid), driver):
            return False
       
        if not self.drivers_did.insert(str(driver.did), driver):
            return False
        
        return True
    
    def get_by_nid(self, nid) -> Driver:
        return self.drivers_nid.get(str(nid))
    
    def get_by_did(self, did) -> Driver:
        return self.drivers_did.get(did)
    
    def get_all(self):
        return self.drivers_nid.get_all()
    
    def delete_nid(self, nid):
        driver = self.get_by_nid(nid)
        
        if not driver: return False

        self.drivers_nid.delete(nid)
        return self.drivers_did.delete(driver.did)

    def __repr__(self):
        return f"NationalID | DriverID | LicenseDate | Activity\n" + self.drivers_did.get_all()
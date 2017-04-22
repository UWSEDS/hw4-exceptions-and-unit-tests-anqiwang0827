# Import libraries
import unittest
import os
from manageData import get_data
from manageData import remove_data

class TestGetData(unittest.TestCase):
    # Test if file present locally
    def testLocalPresent(self):
        # Test variables
        filename = '4xy5-26gy.csv'
        url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        
        # Create empty file and overwrite if exists
        open(filename,'a').close()

        # Test function
        print("Test #1 - LocalPresent")
        result = get_data(url)
        output = 'FileExists'
        self.assertEqual(result,output)   

    # Test if file is not present locally and URL points to a file that exists
    def testLocalNotPresentThenDownloaded(self):
        # Test variables
        filename = '4xy5-26gy.csv'
        url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'

        # Delete file if exists
        if os.path.exists(filename):
            os.remove(filename)

        # Test function
        print("Test #2 - LocalNotPresentThenDownloaded")
        result = get_data(url)
        output = 'FileDownloaded'
        self.assertEqual(result,output)  

    # Test if file is not present locally and URL does not point to a file that exists
    def testLocalNotPresentNoUrl(self):
        # Test variables
        filename = '4xy5-26gy.csv'
        url = 'foo'

        # Delete file if exists
        if os.path.exists(filename):
            os.remove(filename)

        # Test function
        print("Test #3 - LocalNotPresentNoUrl")
        result = get_data(url)
        output = 'NoUrl'
        self.assertEqual(result,output) 

    # Test remove_data funcation when file present locally
    def testRemoveDataExisted(self):
        # Test variables
        filename = '4xy5-26gy.csv'
        
        # Create empty file and overwrite if exists
        open(filename,'a').close()

        # Test function
        print("Test #4 - RemoveDataExisted")
        result = remove_data(filename)
        output = 'FileDeleted'
        self.assertEqual(result,output) 

    # Test remove_data funcation when file not existed
    def testRemoveDataNotExist(self):
        # Test variables
        filename = '4xy5-26gy.csv'
        
        # Delete file if exists
        if os.path.exists(filename):
            os.remove(filename)

        # Test function
        print("Test #5 - RemoveDataNotExist")
        result = remove_data(filename)
        output = 'NoFile'
        self.assertEqual(result,output) 

if __name__ == '__main__':
    print('\n Running tests...\n')
    unittest.main(warnings='ignore')
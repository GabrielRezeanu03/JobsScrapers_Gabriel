import pytest
from sites.typingdna import typingdnaScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.typingdna.com/careers'
        URL_LOGO = 'https://www.typingdna.com/assets/images/typingdna-logo-blue.svg'
        company_name = 'typingdna'
        typingdna = typingdnaScrapper(company_name, URL, URL_LOGO)
        typingdna.get_response()
        typingdna.scrape_jobs()
        # typingdna.send_to_viitor()
        
        self.scraper_data = typingdna.return_data()

class Test_typingdna(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('typingdna', 'România')

    def test_typingdna(self, get_data):
        """
        Test the typingdna website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])
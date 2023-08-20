import pytest
from sites.saladbox import saladboxScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://saladbox.ro/ro/cariere'
        URL_LOGO = 'https://saladbox.ro/images/layout/logo.png'
        company_name = 'saladbox'
        saladbox = saladboxScrapper(company_name, URL, URL_LOGO)
        saladbox.get_response()
        saladbox.scrape_jobs()
        # saladbox.send_to_viitor()
        
        self.scraper_data = saladbox.return_data()

class Test_saladbox(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('saladbox', 'România')

    def test_saladbox(self, get_data):
        """
        Test the saladbox website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])
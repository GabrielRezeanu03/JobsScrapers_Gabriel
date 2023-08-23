import pytest
from sites.inova import inovagroupScrapper
from utils import TestUtils

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://www.inova-group.ro/cariere/'
        URL_LOGO = 'https://www.inova-group.ro/wp-content/uploads/2018/01/logo-mediu-1.png'
        company_name = 'inovagroup'
        inovagroup = inovagroupScrapper(company_name, URL, URL_LOGO)
        inovagroup.get_response()
        inovagroup.scrape_jobs()
        # inova.send_to_viitor()
        
        self.scraper_data = inovagroup.return_data()

class Test_inova(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        
        # You can now use the utility methods from TestUtils to avoid code duplication
        self.scraped_jobs_data = TestUtils.scrape_jobs(self.scraper_data)
        self.peviitor_jobs_data = TestUtils.scrape_peviitor('inovagroup', 'România')

    def test_inova(self, get_data):
        """
        Test the inova website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])
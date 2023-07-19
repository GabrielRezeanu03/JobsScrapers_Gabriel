import pytest
from sites.nokia import nokiaScrape
from sites.website_scraper_bs4 import BS4Scraper
import requests

class SetupTests:
    
    def get_jobs_careers(self):
        """
        Fixture for scraping process from career section.
        """
        URL = 'https://careers.nokia.com/ajax/content/job_results'
        URL_LOGO = 'https://www.nokia.com/nokia-ro/assets/images/layout_global/Forvianokia_Logo.svg'
        company_name = 'nokia'
        nokia = nokiaScrape(company_name, URL, URL_LOGO)
        nokia.set_headers()
        nokia.set_cookies()
        nokia.post_response()
        nokia.scrape_jobs()
        # nokia.send_to_viitor()
        
        self.scraper_data = nokia.return_data()
    
    def scrape_jobs(self):
        """
        Get the job details from the scrapped page
        """
        title = [title['job_title'] for title in self.scraper_data]
        job_city = [city['city'] for city in self.scraper_data]
        job_country = [country['country'] for country in self.scraper_data]
        job_link = [job_link['job_link'] for job_link in self.scraper_data]
        
        return title, job_city, job_country, job_link

    def _set_params(self, page):
        """
        Setting params for peviitor jobs request
        """
        self.params = {
            'q': 'nokia',
            'country': 'România',
            'page': page,
        }
    
    def _get_request(self):
        """
        Send a get request to get the jobs from future
        """
        response = requests.get('https://api.peviitor.ro/v3/search/', params=self.params).json()
        if 'response' in response and 'docs' in response['response']:
            self.response = response['response']['docs']
            return True
        else:
            return False
        
    def scrape_peviitor(self):
        """
        Get the job details from the peviitor
        """
        all_future_title, all_future_job_city, all_future_job_country, all_future_job_link = [], [], [], []

        page = 1
        self.response = []
        self._set_params(page)
        while self._get_request():
            if not self.response:  # If the response is empty, break the loop
                break

            all_future_title.extend([title['job_title'][0] for title in self.response])
            all_future_job_city.extend([city['city'][0] for city in self.response])
            all_future_job_country.extend([country['country'][0] for country in self.response])
            all_future_job_link.extend([job_link['job_link'][0] for job_link in self.response])

            page += 1
            self._set_params(page)

        return all_future_title, all_future_job_city, all_future_job_country, all_future_job_link

class Test_nokia(SetupTests):
    
    @pytest.fixture()
    def get_data(self):
        self.get_jobs_careers()
        self.scraped_jobs_data = self.scrape_jobs()
        self.peviitor_jobs_data = self.scrape_peviitor()

    def test_nokia(self, get_data):
        """
        Test the nokia website against the pe viitor data
        """
        # Test Title
        assert sorted(self.scraped_jobs_data[0]) == sorted(self.peviitor_jobs_data[0])
        # Test job city
        assert sorted(self.scraped_jobs_data[1]) == sorted(self.peviitor_jobs_data[1])
        # Test job country
        assert sorted(self.scraped_jobs_data[2]) == sorted(self.peviitor_jobs_data[2])
        # Test job link
        assert sorted(self.scraped_jobs_data[3]) == sorted(self.peviitor_jobs_data[3])
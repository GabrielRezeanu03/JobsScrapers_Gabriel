#
#
#
# elytishospital > https://elytis-hospital.ro/cariere/

from sites.website_scraper_bs4 import BS4Scraper

class elytishospitalScrapper(BS4Scraper):
    
    """
    A class for scraping job data from elytishospital website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.url)
    
    def scrape_jobs(self):
        """
        Scrape job data from elytishospital website.
        """

        job_elements = self.get_jobs_elements('css_', "h2 > a")
        job_cities_elements = self.get_jobs_elements('css_', "li.job-company-name > a")
        
        self.job_titles = self.get_jobs_details_text(job_elements)
        self.job_urls = self.get_jobs_details_href(job_elements)
        self.job_cities = self.get_jobs_details_text(job_cities_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title, job_url, job_city in zip(self.job_titles, self.job_urls, self.job_cities):
            if job_city == "@ ELYTIS Hospital":
                job_city = "Iasi"
            else:
                job_city = job_city.split()[-1]
            self.create_jobs_dict(job_title, job_url, "România", job_city)

if __name__ == "__main__":
    URL = 'https://elytis-hospital.ro/cariere/'
    URL_LOGO = 'https://elytis-hospital.ro/wp-content/uploads/2023/08/logo-1-scaled-2.png'
    company_name = 'elytishospital'
    elytishospital = elytishospitalScrapper(company_name, URL, URL_LOGO)
    elytishospital.get_response()
    elytishospital.scrape_jobs()
    elytishospital.sent_to_future()
    
    


#
#
#
# autosiena > https://autosiena.ro/cariera/


from sites.website_scraper_bs4 import BS4Scraper

class autosienaScrapper(BS4Scraper):
    
    """
    A class for scraping job data from autosiena website.
    """
    
    def __init__(self, company_name: str, url: str, company_logo_url: str):
        """
        Initialize the BS4Scraper class.
        """
        self.website_url = url
        super().__init__(company_name, company_logo_url)
        
    def get_response(self):
        self.get_content(self.website_url)
    
    def scrape_jobs(self):
        """
        Scrape job data from autosiena website.
        """

        job_titles_elements = self.get_jobs_elements('class_', "el-title uk-h3")
        
        self.job_titles = self.get_jobs_details_text(job_titles_elements)

        self.format_data()
        
    def sent_to_future(self):
        self.send_to_viitor()
    
    def return_data(self):
        return self.formatted_data

    def format_data(self):
        """
        Iterate over all job details and send to the create jobs dictionary.
        """
        for job_title in self.job_titles:
            self.create_jobs_dict(job_title, self.website_url, "România", "Satu Mare")

if __name__ == "__main__":
    URL = 'https://autosiena.ro/cariera/'
    URL_LOGO = 'https://autosiena.ro/wp-content/uploads/autosiena-300.svg'
    company_name = 'autosiena'
    autosiena = autosienaScrapper(company_name, URL, URL_LOGO)
    autosiena.get_response()
    autosiena.scrape_jobs()
    autosiena.sent_to_future()
    
    


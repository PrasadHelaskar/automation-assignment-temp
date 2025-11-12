from selenium.webdriver.common.by import By
from utils.baseMethods import BaseMethods
from utils.logger import Logger

log=Logger().get_logger()

class AutomationProjectTabs(BaseMethods):
    """
        Class Created for the elements Present in the brand page and home page to perform Action that needs to be done
    """
    __private_all_titles_logo=(By.ID, "brd-01fvc8gs4sa9kjs8wxs6gnsn76")
    __private_test_automation_project=(By.CSS_SELECTOR, "img[alt='Test automation project']")
    __private_details_section=(By.ID, "detailsSection")
    __private_video_section=(By.CSS_SELECTOR, "a[id='videosSection']")

    def click_all_title_logo(self):
        """
            Method created for to click on all titles button to contiune on next page.
        """
        self.click(self.__private_all_titles_logo)

    def click_test_automation_project(self):
        """
            Method created for to click on test automation project tile to contiune on next page.
        """
        self.click(self.__private_test_automation_project)

    def click_details_section(self):
        """
            Method created for to click on details scetion to contiune on next page.
        """
        self.click(self.__private_details_section)

    def click_video_section(self):
        """
            Method created for to click on details scetion to contiune on next page.
        """
        self.click(self.__private_video_section)
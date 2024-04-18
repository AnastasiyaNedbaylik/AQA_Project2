from selenium.webdriver.common.by import By


class RegisterPageLocators:
    REGISTER_FIRST_NAME = (By.ID, "register-first-name")
    REGISTER_LAST_NAME = (By.ID, "register-last-name")
    BUSINESS_EMAIL = (By.ID, "register-email")
    REGISTER_ORGANIZATION_NAME = (By.ID, "register-company-name")
    REGISTER_PASSWORD = (By.ID, "password-field")
    CREATE_ORG_BTN = (By.ID, "create_org_btn")
    # REGISTER_PROJECT_NAME = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/input")
    # REGISTER_CLIENT_NAME = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[2]/div[1]/div[2]/input")
    # REGISTER_FIRST_USER_NAME = (By.CSS_SELECTOR,
    #                             "html > body > div:nth-of-type(2) > div:nth-of-type(3) > div > div > div > div > div:nth-of-type(4) > div > div > input")
    # REGISTER_LAST_USER_NAME = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[4]/div[1]/div[2]/input")
    # REGISTER_USER_EMAIL = (By.XPATH, "/html/body/div[2]/div[3]/div/div[1]/div/div[1]/div[4]/div[1]/div[3]/input")
    REGISTER_NEXT_BTN = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/button")
    REGISTER_SKIP_BTN = (By.XPATH, "/html/body/div[2]/div[3]/div/div[2]/p")




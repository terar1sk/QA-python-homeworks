xpaths = [
    '//header//a[@routerlink="/" and contains(@class,"header_logo")]',
    '//header//button[contains(@class,"header_signin") and normalize-space()="Sign In"]',
    '//header//button[contains(@class,"-guest") and normalize-space()="Guest log in"]',
    '//button[@appscrollto="aboutSection" and normalize-space()="About"]',
    '//div[@id="contactsSection"]//h2[normalize-space()="Contacts"]'
]

css_locators = [
    'header a.header_logo[routerlink="/"]',
    'button.header_signin',
    'button.header-link.-guest',
    'button[appscrollto="aboutSection"]',
    '#contactsSection h2'
]
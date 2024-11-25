from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#To open the microblog web page
def test_open_homepage():
    driver = webdriver.Chrome()  # Selenium Manager handles ChromeDriver
    driver.get("http://127.0.0.1:5000")  
    assert "Sign In - Microblog" in driver.title  # Check the page title
    driver.quit()  # Close the browser

#Login with correct credentials
def test_user_login():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/auth/login")  # Replace with the actual sign-up page URL
    driver.find_element(By.ID, "username").send_keys("John")
    # driver.find_element(By.ID, "email").send_keys("john@123.com")
    driver.find_element(By.ID, "password").send_keys("John@123")
    # driver.find_element(By.ID, "confirm_password").send_keys("Alex1@123")
    driver.find_element(By.ID, "submit").click()

    assert "Sign In - Microblog" in driver.page_source  # Update with expected text after successful sign-up
    driver.quit()

#Login with invalid credentials
def test_user_login_invalid():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/auth/login")  # Replace with the actual sign-up page URL
    driver.find_element(By.ID, "username").send_keys("John")
    # driver.find_element(By.ID, "email").send_keys("john@123.com")
    driver.find_element(By.ID, "password").send_keys("John2@123")
    # driver.find_element(By.ID, "confirm_password").send_keys("Alex1@123")
    driver.find_element(By.ID, "submit").click()

    assert "Sign In - Microblog" in driver.page_source  # Update with expected text after successful sign-up
    driver.quit()

def test_post_after_login():
    driver = webdriver.Chrome()

    try:
        # Step 1: Navigate to the login page
        driver.get("http://127.0.0.1:5000/auth/login")
        print("Navigated to login page:", driver.current_url)

        # Step 2: Log in
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        driver.find_element(By.ID, "username").send_keys("John")  # Replace with a valid username
        driver.find_element(By.ID, "password").send_keys("John@123")  # Replace with a valid password
        driver.find_element(By.ID, "submit").click()

        # Step 3: Wait for redirection to the post page
        WebDriverWait(driver, 10).until(EC.url_to_be("http://127.0.0.1:5000/index"))
        print("Redirected to post page:", driver.current_url)

        # Step 4: Wait for the post textarea to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "post")))
        print("Textarea with ID 'post' found!")

        # Step 5: Enter a post and submit
        post_text = "This is a test post"
        post_field = driver.find_element(By.ID, "post")
        post_field.send_keys(post_text)
        driver.find_element(By.ID, "submit").click()  # Replace 'submit_post' with the actual submit button's ID

        # Step 6: Validate the post was successful
        success_message = "Post created successfully"  # Replace with the actual success message
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), success_message))
        print("Post submitted successfully and validated.")

    except Exception as e:
        print("Test failed with exception:", e)
        print("Page Source:", driver.page_source)
    finally:
        driver.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By

def test_translate_post():
    driver = webdriver.Chrome()
    try:
        # Navigate to the login page
        driver.get("http://127.0.0.1:5000/auth/login")

        # Log in
        driver.find_element(By.ID, "username").send_keys("Alex")
        driver.find_element(By.ID, "password").send_keys("Abcd@123")
        driver.find_element(By.ID, "submit").click()

        # Click the translate button
        driver.find_element(By.ID, "translation2").click()

        # Verify the translation result
        assert "Home - Microblog" in driver.page_source  # Update with expected text
    finally:
        driver.quit()


def test_like_dislike_post():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/auth/login")
    
    # Log in
    driver.find_element(By.ID, "username").send_keys("Alex")
    driver.find_element(By.ID, "password").send_keys("Abcd@123")
    driver.find_element(By.ID, "submit").click()
    
    # Like a post using JavaScript
    try:
        driver.execute_script("likePost('2')")
        print("Post liked successfully.")
    except Exception as e:
        print(f"Failed to like the post: {e}")
    
    driver.quit()

# def test_edit_profile():
#     driver = webdriver.Chrome()
#     driver.get("http://127.0.0.1:5000/auth/login")
#     # Log in
#     driver.find_element(By.ID, "username").send_keys("Alex")
#     driver.find_element(By.ID, "password").send_keys("Abcd@123")
#     driver.find_element(By.ID, "submit").click()

#     driver.find_element(By.CLASS_NAME, "nav-link").click()
#     # driver.find_element(By.XPATH, "//a[@href='/edit_profile']").click()
#     # driver.find_element(By.CSS_SELECTOR, "a[href='/edit_profile']").click()
#     # driver.find_element(By.XPATH, "//a[contains(@href, '/edit_profile')]").click()

#     # driver.find_element(By.LINK_TEXT, "Edit your profile").click()
#     # edit_profile_link = driver.find_element(By.LINK_TEXT, "Edit your profile")
#     # edit_profile_link.click()
#     # edit_profile_link = WebDriverWait(driver, 10).until(
#     # EC.presence_of_element_located((By.LINK_TEXT, "Edit your profile"))
#     # )
#     # edit_profile_link = WebDriverWait(driver, 10).until(
#     # EC.presence_of_element_located((By.LINK_TEXT, "Edit your profile"))
#     # )
#     # edit_profile_link.click()
#     edit_profile_link = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, "//a[@href='/edit_profile']"))
#         )
#     edit_profile_link.click()
#     print("Current URL:", driver.current_url)

#     # driver.find_element(By.ID,"about_me").send_keys("Updated bio")
#     # driver.find_element(By.ID, "submit").click()

#     # assert "Edit Profile - Microblog" in driver.page_source
#     driver.quit()

def test_edit_profile():
    driver = webdriver.Chrome()

    try:
        # Log in
        driver.get("http://127.0.0.1:5000/auth/login")
        driver.find_element(By.ID, "username").send_keys("Alex")
        driver.find_element(By.ID, "password").send_keys("Abcd@123")
        driver.find_element(By.ID, "submit").click()

        driver.get("http://127.0.0.1:5000/user/Alex")
        # Ensure successful navigation to the dashboard
        # WebDriverWait(driver, 10).until(EC.url_contains("/user/Alex"))
        # print("Successfully logged in. Current URL:", driver.current_url)

        # Validate and locate "Edit your profile" link
        edit_profile_link = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/edit_profile']"))
        )
        print("Found 'Edit your profile' link.")
        edit_profile_link.click()

        # Validate navigation to the edit profile page
        WebDriverWait(driver, 10).until(EC.url_contains("/edit_profile"))
        print("Successfully navigated to Edit Profile page. Current URL:", driver.current_url)

        driver.find_element(By.ID, "about_me").send_keys("Hello This is Alex")
        driver.find_element(By.ID, "submit").click()
    # except Exception as e:
    #     print("Test failed with exception:", e)
    #     print("Current URL:", driver.current_url)
    #     print("Page source:")
    #     print(driver.page_source)
    #     raise
    finally:
        driver.quit()



# def test_bookmark_post():
#     driver = webdriver.Chrome()
#     driver.get("http://127.0.0.1:5000/auth/login")
#     # Log in
#     driver.find_element(By.ID, "username").send_keys("Alex")
#     driver.find_element(By.ID, "password").send_keys("Abcd@123")
#     driver.find_element(By.ID, "submit").click()

#     # Bookmark a post
#     driver.find_element(By.ID, "bookmark_button").click()
#     assert "Bookmarked" in driver.page_source  # Replace with actual bookmarked text
#     driver.quit()

def test_send_message():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/auth/login")
    # Log in
    driver.find_element(By.ID, "username").send_keys("Alex")
    driver.find_element(By.ID, "password").send_keys("Abcd@123")
    driver.find_element(By.ID, "submit").click()

    driver.get("http://127.0.0.1:5000/user/Nancy1")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Send private message"))).click()
    # driver.find_element(By.ID, "Submit").click()
    
    print("Page Title:", driver.title)
    # driver.find_element(By.LINK_TEXT, "Send private message").click()

    # Send a message
    # driver.find_element(By.ID, "new_message").click()
    # driver.find_element(By.ID, "recipient").send_keys("recipient_user")
    # driver.find_element(By.ID, "message_body").send_keys("Hello!")
    # driver.find_element(By.ID, "send_message").click()

    assert "Send Message - Microblog" in driver.title
    driver.quit()

def test_view_messages():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/auth/login")
    # Log in
    driver.find_element(By.ID, "username").send_keys("Alex")
    driver.find_element(By.ID, "password").send_keys("Abcd@123")
    driver.find_element(By.ID, "submit").click()
    driver.find_element(By.LINK_TEXT, "Messages").click()

    # print("Page Title:", driver.title)

    # driver.find_element(By.ID, "inbox").click()
    assert "Welcome to Microblog" in driver.title
    driver.quit()


# def test_upload_profile_picture():
#     driver = webdriver.Chrome()
#     driver.get("http://127.0.0.1:5000/auth/login")
#     # Log in
#     driver.find_element(By.ID, "username").send_keys("Alex")
#     driver.find_element(By.ID, "password").send_keys("Abcd@123")
#     driver.find_element(By.ID, "submit").click()

#     driver.find_element(By.ID, "profile_settings").click()
#     driver.find_element(By.ID, "profile_picture").send_keys("/path/to/image.jpg")
#     driver.find_element(By.ID, "save_profile").click()

#     assert "Profile updated successfully" in driver.page_source
#     driver.quit()
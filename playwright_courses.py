from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Переходим на страницу
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill("username")

    # Заполняем поле пароль
    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill("password")

    # Нажимаем на кнопку registration
    reg = page.get_by_test_id('registration-page-registration-button')
    reg.click()

    context.storage_state(path="browser-state.json")

    context2 = browser.new_context(storage_state="browser-state.json")
    page2 = context2.new_page()
    page2.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses",
        wait_until='networkidle')

    title_courses = page2.get_by_test_id("courses-list-toolbar-title-text")
    expect(title_courses).to_be_visible()
    expect(title_courses).to_have_text("Courses")

    empty_icon = page2.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_icon).to_be_visible()

    empty_title = page2.get_by_test_id("courses-list-empty-view-title-text")
    expect(empty_title).to_be_visible()
    expect(empty_title).to_have_text("There is no results")

    empty_description = page2.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_description).to_be_visible()
    expect(empty_description).to_have_text("Results from the load test pipeline will be displayed here")

    page.wait_for_timeout(3000)


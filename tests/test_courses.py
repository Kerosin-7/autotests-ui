import pytest
from playwright.sync_api import Playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses",
               wait_until='networkidle')

    title_courses = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(title_courses).to_be_visible()
    expect(title_courses).to_have_text("Courses")

    empty_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_icon).to_be_visible()

    empty_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(empty_title).to_be_visible()
    expect(empty_title).to_have_text("There is no results")

    empty_description = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_description).to_be_visible()
    expect(empty_description).to_have_text("Results from the load test pipeline will be displayed here")

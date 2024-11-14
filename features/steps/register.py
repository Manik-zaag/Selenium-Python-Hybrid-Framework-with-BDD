from behave import *

from pages.HomePage import HomePage
from utilities import EmailGenerator
from utilities import full_page_screenshot


@given(u'I navigate to Register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.register_page = context.home_page.navigate_to_register_page()


# Create a helper function that performs the common actions.
# This function will take additional parameters if necessary to handle variations in behavior between the steps.
def enter_details(context, email_generate=True, yes_radio_button=False):
    for data in context.table:
        context.register_page.enter_first_name(data["first_name"])
        context.register_page.enter_last_name(data["last_name"])
        context.register_page.enter_telephone(data["telephone"])
        context.register_page.enter_password(data["password"])
        context.register_page.enter_con_password(data["password"])

        if email_generate:
            context.register_page.enter_email(EmailGenerator.generate_email_with_time_stamp())

        if yes_radio_button:
            context.register_page.select_yes_radio_button()


@when(u'I enter below details into mandatory fields')
def step_impl(context):
    enter_details(context, email_generate=True, yes_radio_button=False)


@when(u'I click on continue button')
def step_impl(context):
    context.account_success_page = context.register_page.click_on_continue_button()


@then(u'Account should get created')
def step_impl(context):
    expected_heading_text = "Your Account Has Been Created!"
    assert context.account_success_page.retrive_account_creation_message().__eq__(expected_heading_text)
    # full_page_screenshot.take_full_page_screen_shot(context)


@when(u'I enter below details into all fields')
def step_impl(context):
    enter_details(context, email_generate=True, yes_radio_button=True)


@when(u'I select Privacy Policy option')
def step_impl(context):
    context.register_page.check_mark_on_privacy_policy()


@when(u'I enter details into all fields except email field')
def step_impl(context):
    enter_details(context, email_generate=True, yes_radio_button=True)


@when(u'I enter existing accounts email say "{email}" into email field')
def step_impl(context, email):
    context.register_page.enter_email(email)


@then(u'Proper warning message information about duplicate account should be displayed')
def step_impl(context):
    expected_warning_text = "Warning: E-Mail Address is already registered!"
    assert context.register_page.retrieve_duplicate_email_warning().__eq__(expected_warning_text)


@when(u'I don\'t enter anything into the fields')
def step_impl(context):
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_con_password("")


@then(u'Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    assert context.register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!"
                                                     , "First Name must be between 1 and 32 characters!"
                                                     , "Last Name must be between 1 and 32 characters!"
                                                     , "E-Mail Address does not appear to be valid!"
                                                     , "Telephone must be between 3 and 32 characters!"
                                                     , "Password must be between 4 and 20 characters!")

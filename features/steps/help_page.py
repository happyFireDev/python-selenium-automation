from behave import given, when, then


@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()

@when('Select Help topic {option_value}')
def select_topic(context, option_value):
    context.app.help_page.select_topic(option_value)

# @then('Verify help Returns page opened')
# def verify_help_returns_opened(context):
#     context.app.help_page.verify_help_returns_opened()
#
# @then('Verify help Current promotions page opened')
# def verify_promotions_opened(context):
#     context.app.help_page.verify_promotions_opened()

@then('Verify help {header} page opened')
def verify_correct_help_page_opened(context, header):
    context.app.help_page.verify_correct_help_page_opened(header)
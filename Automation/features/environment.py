def after_scenario(context, scenario):
    if 'web' == scenario.tags:
        context.driver.close()
        context.driver.quit()

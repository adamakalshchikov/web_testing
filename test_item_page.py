from .pages.item_page import ItemPage


def test_add_to_chart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ItemPage(browser, link)
    page.open()
    page.add_to_chart()
    page.solve_quiz_and_get_code()
    page.verify_success_msg(page.get_item_name())
    page.verify_cart_cost(page.get_item_price())

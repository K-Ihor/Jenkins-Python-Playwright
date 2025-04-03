# src/pages/main_page.py
import allure
from playwright.async_api import Page

class MainPage:
    """
    Page Object для страницы 'Find past papers and mark schemes'
    на сайте AQA.
    """

    def __init__(self, page: Page):
        self.page = page
        # Локаторы вынесены в переменные согласно паттерну Page Object.
        # Примеры локаторов (выберите нужные элементы из исходного HTML)
        self.search_input = page.locator('input[placeholder="Search past papers"]')
        self.search_button = page.locator('div.group > div.absolute > svg')
        # Пример локатора для заголовка страницы (можно брать по тегу h1)
        self.header_title = page.locator("h1")

    @allure.step("Переход на страницу")
    async def goto(self):
        """
        Переход на целевую страницу.
        """
        url = "https://www.aqa.org.uk/find-past-papers-and-mark-schemes"
        await self.page.goto(url)

    @allure.step("Получение заголовка страницы")
    async def get_title(self) -> str:
        """
        Возвращает заголовок страницы.
        """
        return await self.page.title()

    @allure.step("Выполнение поиска по запросу: {query}")
    async def search_past_papers(self, query: str):
        """
        Выполняет поиск по ключевому слову.
        :param query: текст запроса для поиска
        """
        await self.search_input.fill(query)
        # Если нажатие кнопки поиска требуется:
        # await self.search_button.click()
        # Можно имитировать нажатие Enter:
        await self.page.keyboard.press("Enter")

    @allure.step("Получение текста основного заголовка (h1)")
    async def get_header_text(self) -> str:
        """
        Возвращает текст заголовка страницы (например, h1).
        """
        return await self.header_title.text_content()

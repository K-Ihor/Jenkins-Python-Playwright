# src/tests/test_main_page.py
import pytest
import allure
from src.pages.main_page import MainPage

@allure.feature("Main Page")
@allure.story("Проверка заголовка страницы")
@pytest.mark.asyncio
async def test_page_title(page):
    """
    Тест проверяет, что заголовок страницы содержит ключевую фразу.
    """
    main_page = MainPage(page)
    await main_page.goto()
    title = await main_page.get_title()
    assert "Past papers" in title, "Заголовок страницы не содержит 'Past papers'"

@allure.feature("Main Page")
@allure.story("Проверка основного заголовка")
@pytest.mark.asyncio
async def test_header_text(page):
    """
    Тест проверяет, что на странице отображается основной заголовок (h1).
    """
    main_page = MainPage(page)
    await main_page.goto()
    header_text = await main_page.get_header_text()
    assert header_text is not None and "Find past papers" in header_text, "Основной заголовок не найден"

@allure.feature("Main Page")
@allure.story("Проверка видимости поля поиска")
@pytest.mark.asyncio
async def test_search_input_visible(page):
    """
    Тест проверяет, что поле ввода поиска видно на странице.
    """
    main_page = MainPage(page)
    await main_page.goto()
    is_visible = await main_page.search_input.is_visible()
    assert is_visible, "Поле поиска не отображается"

@allure.feature("Main Page")
@allure.story("Проверка функционала поиска")
@pytest.mark.asyncio
async def test_search_functionality(page):
    """
    Тест выполняет ввод запроса в поле поиска и имитирует нажатие клавиши Enter.
    """
    main_page = MainPage(page)
    await main_page.goto()
    await main_page.search_past_papers("Mathematics")
    # Ждём, пока результаты загрузятся (пример ожидания элемента, можно настроить)
    await page.wait_for_timeout(2000)
    # Проверяем, что URL изменился или появились результаты
    assert "search" in page.url or "Mathematics" in await page.content(), "Поиск не отработал корректно"

@allure.feature("Main Page")
@allure.story("Проверка URL страницы")
@pytest.mark.asyncio
async def test_page_url(page):
    """
    Тест проверяет, что после перехода на страницу URL корректный.
    """
    main_page = MainPage(page)
    await main_page.goto()
    assert "find-past-papers-and-mark-schemes" in page.url, "URL не соответствует ожидаемому"

@allure.feature("Main Page")
@allure.story("Проверка пустого поля поиска")
@pytest.mark.asyncio
async def test_search_input_empty(page):
    """
    Тест проверяет, что после перехода поле поиска пустое.
    """
    main_page = MainPage(page)
    await main_page.goto()
    value = await main_page.search_input.input_value()
    assert value == "", "Поле поиска не пустое при загрузке страницы"

@allure.feature("Main Page")
@allure.story("Проверка времени загрузки страницы")
@pytest.mark.asyncio
async def test_page_load_time(page):
    """
    Тест проверяет, что страница загружается в разумное время.
    """
    main_page = MainPage(page)
    start = page.context.browser.time() if hasattr(page.context.browser, "time") else 0
    await main_page.goto()
    # Простой пример: убеждаемся, что загрузка проходит менее чем за 5 секунд.
    load_time = 5  # здесь можно измерить реальное время через дополнительный код
    assert load_time < 5, "Время загрузки страницы превышает 5 секунд"

@allure.feature("Main Page")
@allure.story("Проверка атрибута placeholder поля поиска")
@pytest.mark.asyncio
async def test_page_contains_search_placeholder(page):
    """
    Тест проверяет, что атрибут placeholder у поля поиска соответствует ожидаемому.
    """
    main_page = MainPage(page)
    await main_page.goto()
    placeholder = await main_page.search_input.get_attribute("placeholder")
    assert placeholder == "Search past papers", "Placeholder не соответствует ожидаемому"

@allure.feature("Main Page")
@allure.story("Проверка заголовка H1")
@pytest.mark.asyncio
async def test_header_contains_expected_text(page):
    """
    Тест проверяет, что заголовок h1 содержит ожидаемое сообщение.
    """
    main_page = MainPage(page)
    await main_page.goto()
    header_text = await main_page.get_header_text()
    assert "Find past papers" in header_text, "Заголовок h1 не содержит ожидаемого текста"

@allure.feature("Main Page")
@allure.story("Проверка наличия кнопки поиска")
@pytest.mark.asyncio
async def test_search_button_exists(page):
    """
    Тест проверяет, что кнопка поиска (если она есть) присутствует на странице.
    """
    main_page = MainPage(page)
    await main_page.goto()
    exists = await main_page.search_button.count() > 0
    assert exists, "Кнопка поиска не найдена"

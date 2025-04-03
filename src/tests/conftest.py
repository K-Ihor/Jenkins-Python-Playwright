# src/tests/conftest.py
import asyncio
import os
import pytest
import allure
from playwright.async_api import async_playwright, Browser, Page

# Фикстура event_loop с областью "function"
@pytest.fixture(scope="function")
def event_loop():
    """
    Создаёт новый event loop для каждого теста.
    Это гарантирует, что все асинхронные операции будут выполняться в одном цикле.
    """
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

# Фикстура браузера теперь с областью "function"
@pytest.fixture(scope="function")
async def browser() -> Browser:
    """
    Создаёт новый экземпляр браузера (Chromium) для каждого теста.
    Это предотвращает проблему использования объекта, созданного в одном event loop,
    в другом.
    """
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        yield browser
        await browser.close()

@pytest.fixture
async def page(browser: Browser) -> Page:
    """
    Создаёт новую страницу (контекст) для каждого теста.
    После теста контекст закрывается.
    """
    context = await browser.new_context()
    page = await context.new_page()
    yield page
    await context.close()

# Синхронный hook для захвата скриншота при ошибке теста.
# Он реализован как обычная (не async) функция, что требуется pluggy.
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     # Если тест завершился с ошибкой на этапе вызова
#     if rep.when == "call" and rep.failed:
#         page = item.funcargs.get("page", None)
#         if page:
#             try:
#                 # Запускаем асинхронный метод для скриншота в новом event loop
#                 screenshot = asyncio.run(page.screenshot())
#                 allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
#             except Exception as e:
#                 # Если не удалось сделать скриншот, можно залогировать ошибку
#                 print("Ошибка при создании скриншота:", e)

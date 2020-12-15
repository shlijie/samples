#!/usr/bin/env python3
# screenshot.py

import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://www.baidu.com')
    await page.screenshot({'path': 'www.baidu.png'})
    await browser.close()

asyncio.run(main())

import asyncio
import aiohttp

from lxml import html


async def get_site(session: aiohttp.ClientSession, link: str):
    response = await session.get(link)
    text = await response.text()
    print(f"--- Página web {link} ------------------------")
    print(f"{text[:100]}")
    print("----------------------------------------------")
    print()
    print()


async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get("https://hckrnews.com")
        text = await response.text()

        root = html.fromstring(text)
        links = root.xpath(
            "//li[@class='entry row']/a[contains(@class, 'story')]/@href"
        )

        # tasks = []
        # for link in links[:3]:
        #     tasks.append(get_site(session, link))
        tasks = [get_site(session, link) for link in links[:3]]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import re
import sys

import aiohttp
from lxml import html


async def get_site(session: aiohttp.ClientSession, link: str):
    response = await session.get(link)
    text = await response.text()

    print(f"--- Página web {link} ------------------------")
    print(f"{text[:300]}")
    print("----------------------------------------------")
    print()
    print()

    root = html.fromstring(text)

    c_nombres = root.xpath("//h1/text()")
    if c_nombres:
        c_nombres = c_nombres[0].strip()
    else:
        c_nombres = link

    producto_n = root.xpath("//div[@class='product']//h2/text()")
    producto_p = root.xpath("//div[@class='product']//p[@class='price']/text()")

    limpios_p = []

    for p in producto_p:
        match = re.search(r"(\d+(?:.\d+)?)", p)
        if match:
            limpios_p.append(float(match.group(1)))

    # Por si no hay productos
    if not limpios_p:
        print(f"Category {c_nombres}")
        print("  (No products found)")
        print()
        return text

    max_precio = max(limpios_p)
    min_precio = min(limpios_p)
    avg_precio = sum(limpios_p) / len(limpios_p)

    max_nombre = producto_n[limpios_p.index(max_precio)]
    min_nombre = producto_n[limpios_p.index(min_precio)]

    print(f"Category {c_nombres}")
    print(f"Max. Price: {max_precio}€ ({max_nombre})")
    print(f"Min. Price: {min_precio}€ ({min_nombre})")
    print(f"Avg. Price: {avg_precio:.1f}€")  # formato .1f
    print()

    return text


async def main():
    if len(sys.argv) != 2:
        print("Error: Se debe invocar el script pasando la URL del sitio web.")
        print(f"Ejemplo: python {sys.argv[0]} http://localhost:8080")
        sys.exit(1)

    url = sys.argv[1]  

    if url.endswith("/"):
        url = url[:-1]

    async with aiohttp.ClientSession() as session:
        
        try:
            response = await session.get(url)
            text = await response.text()
            root = html.fromstring(text)
        except Exception as e:
            print(f"Error fatal al conectar con la URL base: {url}")
            print(e)
            sys.exit(1)

        links = root.xpath("//div[@class='link-card']//a/@href")
        print(f"Enlaces: {links}")
        print()

        tasks = []
        for link in links:
            full_url = f"{url}/{link}"
            tasks.append(get_site(session, full_url))

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

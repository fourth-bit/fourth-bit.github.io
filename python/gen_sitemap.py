import sys
import os

SITE_MAP_TEMPLATE = "templates/sitemap-template.xml"

def gen_site_map():
    target = open(sys.argv[1], 'w')

    fp = open(SITE_MAP_TEMPLATE)
    sitemap = fp.read()
    fp.close()

    insert_point = sitemap.rfind('</url>') + len('</url>')

    for doc in os.listdir('charities'):
        sitemap = sitemap[:insert_point] + \
f"""
    <url>
        <loc>http://fourth-bit.github.io/charities/{doc}</loc>
        <priority>1</priority>
    </url>""" \
        + sitemap[insert_point:]
    
    for doc in os.listdir('items'):
        sitemap = sitemap[:insert_point] + \
f"""
    <url>
        <loc>http://fourth-bit.github.io/charities/{doc}</loc>
        <priority>1</priority>
    </url>""" \
        + sitemap[insert_point:]

    target.write(sitemap)
    target.close()

if __name__ == '__main__':
    gen_site_map()
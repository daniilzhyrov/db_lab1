from lxml import etree

xml = etree.parse('task3_results/results.xml')
xslt = etree.parse('transform.xsl')

transform = etree.XSLT(xslt)
html = transform(xml)

html.write('task4_results/results.html')
from lxml import etree

n = 20
acumulator = 0

for i in range(n):
    xml = etree.parse('task1_results/' + str(i+1) + '.xml')
    texts = xml.xpath('//fragment[@type="text"]')
    acumulator += len(texts)

print(acumulator // n)
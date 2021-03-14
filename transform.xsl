<xsl:stylesheet version = "1.0" standalone="true" xmlns:xsl = "http://www.w3.org/1999/XSL/Transform"> 

<xsl:template match = "/data">
	<html>
		<body>
			<h2>Items List</h2>
			
			<table border = "1">
				<tr bgcolor="lightgreen">
					<th>Description</th>
					<th>Image</th>
					<th>Price</th>
				</tr>
				
				<xsl:for-each select = "item">
				
					<tr>
						<td><xsl:value-of select = "description"/></td>
						<td><xsl:value-of select = "image"/></td>
						<td><xsl:value-of select = "price"/></td>
					</tr>
				
				</xsl:for-each>
				
			</table>
		</body>
	</html>
</xsl:template>
</xsl:stylesheet>
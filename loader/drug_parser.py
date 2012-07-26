from pyPdf import PdfFileReader
from pyPdf.pdf import ContentStream
from pyPdf.generic import TextStringObject

inp = PdfFileReader(file('drug.pdf', 'rb'))
products = []
current = -1
new_field = True
f = open('lala_drugs.json', 'w')

#read all 184 pages of the Food pdf
for page in range(1):

    first = inp.getPage(page)
    content = first['/Contents'].getObject()
    content = ContentStream(content, first.pdf)
    op = [(operands,operator) for operands, operator in content.operations]

    new_op = []
    for operands, operator in op:
        if operator == "TJ":
            new_op.append(operands[0])
        elif operator == "EMC":
            new_op.append(1)

    if page==0:
        i = 48
    else:
        i = 0
    inner = 0
    #for x in new_op:
        #print x
    print "LALALALAL", new_op[48]
    while i < len(new_op):
        one = ''
        if new_op[i] == 1:
            new_field = True
        elif new_op[i][0].isdigit():
            for j in new_op[i]:
                if isinstance(j, TextStringObject):
                    one += j
            products.append([one])
            current+=1
            new_field = False
            inner = 0
        else:
            for j in new_op[i]:
                if isinstance(j, TextStringObject):
                    one += j
            if new_field:
                products[current].append(one)
                inner+=1
                new_field = False
            else:
                products[current][inner]+=one
        i+=1

# remove products that have more than 3 fields
remove = []
for i in range(len(products)):
    print products[i]
    if len(products[i]) == 9:
        pass
    else:
        remove.append(products[i])
for item in remove:
    products.remove(item)
for item in products:
    print item
'''

# write our json file
f.write("[\n")
for i in range(len(products)-1):
    f.write("{\n")
    f.write('"model":"verify.product",\n')
    f.write('"pk": '+str(i+1)+',\n')
    f.write('"fields": {\n')
    f.write('"product_name": "'+products[i][1].encode('utf-8')+'",\n')
    f.write('"FDB_number": "'+products[i][0].encode('utf-8')+'",\n')
    f.write('"manu_location": "'+products[i][2].encode('utf-8')+'",\n')
    f.write('"strength":"",\n')
    f.write('"dosage_form":"",\n')
    f.write('"local_agent":"",\n')
    f.write('"expiry_date":""\n')
    f.write("}\n")
    f.write("},\n")
i = len(products)-1
f.write("{\n")
f.write('"model":"verify.product",\n')
f.write('"pk": '+str(i+1)+',\n')
f.write('"fields": {\n')
f.write('"product_name": "'+products[i][1].encode('utf-8')+'",\n')
f.write('"FDB_number": "'+products[i][0].encode('utf-8')+'",\n')
f.write('"manu_location": "'+products[i][2].encode('utf-8')+'",\n')
f.write('"strength":"",\n')
f.write('"dosage_form":"",\n')
f.write('"local_agent":"",\n')
f.write('"expiry_date":""\n')
f.write("}\n")
f.write("}\n")
f.write("]")


f.close()
    ## elif len(products[i]) ==5:
    ##     products[i] = [products[i][0], products[i][1] + products[i][2]+products[i][3], products[i][4]]
    ## elif len(products[i]) ==6:
    ##     products[i] = [products[i][0], products[i][1] + products[i][2]+products[i][3]+ products[i][4], products[i][5]]
    ## elif len(products[i]) ==7:
    ##     products[i] = [products[i][0], products[i][1] + products[i][2]+products[i][3] + products[i][4]+ products[i][5], products[i][6]]
    ## else:
    ##     print 'lala'

#for product in products:
 #   print product, '\n'
'''
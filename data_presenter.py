cupcake_invoices = open('CupcakeInvoices.csv')



for line in cupcake_invoices:
    print(line)

cupcake_invoices.seek(0,0)

for cupcakes in cupcake_invoices:
    values = cupcakes.split(',')
    print(values[2])

cupcake_invoices.seek(0,0)


for total in cupcake_invoices:
    values = total.split(',')
    quantity = values[-2]
    price = values[-1]
    float1 = float(price)
    float2 = float(quantity)
    print(float1 * float2)

cupcake_invoices.seek(0,0)

total = 0

for all_total in cupcake_invoices:
    values = all_total.split(',')
    quantity = values[-2]
    price = values[-1]
    
    float3 = float(values[-2])
    float4 = float(values[-1])

    total = total + float3 * float4

print(total)

# going further answer

# cupcake_invoices = open('CupcakeInvoices.csv')

# import matplotlib.pyplot as plt 
    
# x = ["Chocolate", "Strawberry", "Vanilla"] 

# totals = []

# choc_total = 0
# straw_total = 0
# van_total = 0

# for row in cupcake_invoices:
#     values = row.split(',')
#     if values[2] == 'Chocolate':
#         quantity = values[-2]
#         price = values[-1]
#         float1 = float(price)
#         float2 = float(quantity)
#         choc_total += float1 * float2
#     elif values[2] == 'Strawberry':
#         quantity = values[-2]
#         price = values[-1]
#         float1 = float(price)
#         float2 = float(quantity)
#         straw_total += float1 * float2
#     elif values[2] == 'Vanilla':
#         quantity = values[-2]
#         price = values[-1]
#         float1 = float(price)
#         float2 = float(quantity)
#         van_total += float1 * float2
# totals.append(choc_total)
# totals.append(straw_total)
# totals.append(van_total)

# y = totals

# plt.bar(x, y, color = 'g', width = 0.72)
    

# plt.xlabel('Flavors') 

# plt.ylabel('Revenue') 
    

# plt.title('My Cupcake Sales') 
    

# plt.show()
cupcake_invoices.close()
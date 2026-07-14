#Atividade aula 01

id_venda = str(input("ID de Venda: "))
data = input("Data: ")
vendedor = input("Nome do vendedor: ")
cliente = input("Nome do Cliente: ")
produto = input("Produto: ")
categoria = input("Categoria: ")
quantidade = int(input("Quantidade: "))
preco_unitario = float(input("Preço Unitário: R$ "))

valor_total = preco_unitario * quantidade
valor_debito = valor_total * 0.95
valor_credito = valor_total * 1.05

if quantidade > 100:
    print("Estoque insuficiente.")
else:
    print(f"Preço total: R$ {valor_total:.2f}")

pagamento = str(input(
    "Forma de pagamento. Digite:\n\n"
    "1 para Débito\n"
    "2 para Crédito\n\n"
    "Forma de pagamento:"
    )
)

while pagamento != "1" and pagamento != "2":
    print("\n\nERROR 404! \n\nPor favor, digite 1 para DÉBITO e 2 para CRÉDITO:")
    pagamento = str(input("Forma de pagamento: "))

if pagamento == "1":
    valor_final = valor_debito
    print("Forma de pagamento: Débito. Desconto de 5% concedido.")
else:
    valor_final = valor_credito
    print("Forma de pagamento: Crédito. 5% de juros da maquininha.")


print("\n===== EXTRATO =====")

print(f"ID da venda: {id_venda}")
print(f"Data: {data}")
print(f"Vendedor: {vendedor}")
print(f"Cliente: {cliente}")
print(f"Produto Comprado: {produto}")
print(f"Categoria: {categoria}")
print(f"Quantidade: {quantidade}")
print(f"Preço de uma unidade:        R$ {preco_unitario:.2f}")
print(f"Valor da compra:             R$ {valor_total:.2f}")

if pagamento == "1":
    print(f"Desconto de 5%:            - R$ {valor_total - valor_final:.2f}")
else:
    print(f"Juros de 5% na maquininha: + R$ {valor_final - valor_total:.2f}")
print(f"\n\nTotal a pagar:               R$ {valor_final:.2f}")
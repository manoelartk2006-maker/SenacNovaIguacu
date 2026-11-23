from banco_dados import banco_dados



# F16 — Gateway de Pagamento Digital (Função Completa)
# * **Arquivo:** `modulos/f16_gateway_pagamento.py`
# * **Assinatura:** `def finalizar_checkout_digital(banco_dados, id_pedido, opcao_pagamento):`
# * **Parâmetros:** `banco_dados` (`dict`), `id_pedido` (`int`), `opcao_pagamento` (`int`).
# * **Retorno Esperado:** `bool`.
# * **Passo a Passo da Lógica:**
#   1. Verifique se o pedido existe, se `status == "ABERTO"` e se o `carrinho` não está vazio. Se falhar, retorne `False`.
#   2. Utilize `match opcao_pagamento:` (ou `if/elif/else`) para definir `"metodo_pagamento"`:
#      * `1` -> `"PIX"`
#      * `2` -> `"CARTAO_VIRTUAL"`
#      * `3` -> `"CRIPTO_REAL"`
#      * Outro valor -> retorne `False`.
#   3. Altere o `"status"` do pedido para `"PAGO"`.
#   4. Some o `"valor_liquido"` do pedido em `banco_dados["faturamento_total"]` e retorne `True`.



def finalizar_checkout_digital(banco_dados, id_pedido, opcao_pagamento):
    pedidos = banco_dados["pedidos"]

    if id_pedido not in pedidos:
        return False
    
    pedidos = pedidos[id_pedido]

    if pedidos["status"] != "ABERTO":
        return False
    
    if len(pedidos["carrinho"]) == 0:
        return False
    
#definição do metoo de pagamento
    
    if opcao_pagamento == 1:
        metodo_de_pagamento = "PIX"
    elif opcao_pagamento == 2 :
        metodo_de_pagamento = "CARTAO_VIRTUAL"
    elif opcao_pagamento == 3:
        metodo_de_pagamento = "CRIPTO_REAL"
    else:
        return False





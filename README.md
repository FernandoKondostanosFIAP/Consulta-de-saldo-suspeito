# Case 2 — Consulta de saldo suspeito

**Arena Devin | Itaú × FIAP (case acadêmico fictício)**  
**Turma:** 1º ano | **Nível:** Médio | **Disciplina:** Building Relational Database | **Tempo estimado:** ~25 min

## Contexto
O extrato bancário apresenta saldos incorretos porque os débitos estão sendo somados como créditos.

## Sua missão
- Corrija a consulta em `consulta_saldo.sql` para obter créditos menos débitos.
- Entenda `CASE WHEN` e `GROUP BY`.
- Bônus: mostre somente contas com saldo positivo usando `HAVING`.

## Como trabalhar com Ask Devin
1. Abra o Ask Devin e selecione este repositório indexado.
2. Peça ao Devin para explicar o problema e localizar a causa.
3. Solicite uma proposta de correção, analise a resposta e aplique as alterações nos arquivos do projeto.
4. Execute os testes indicados abaixo e valide o resultado.
5. Faça commit da sua solução no repositório conforme orientação dos tutores.

**Importante:** o repositório começa propositalmente com falhas. Não altere os testes para fazê-los passar; ajuste a implementação. O Ask Devin é um chat de análise; ele não modifica automaticamente o repositório.

## Como validar
```bash
python -m unittest discover -s tests -v
```
O teste utiliza SQLite, disponível no Python padrão.

## Exemplo de pergunta ao Ask Devin
> Examine `consulta_saldo.sql` e `dados.sql`. Como calcular saldo com CASE WHEN sem somar os débitos?

> Todos os nomes, cadastros e valores são fictícios e usados apenas para fins educacionais. Este projeto não é software oficial do Itaú.

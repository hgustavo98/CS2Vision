# CS2Vision - Guia de Implementação

## Visão Geral
O projeto **CS2Vision** trata da criação de um sistema para análise automatizada e visualização de partidas de Counter-Strike 2 (CS2). Ele visa lidar com as seguintes tarefas fundamentais:

1. Renderizar visualmente as demos e eventos capturados.
2. Identificar padrões nas jogadas usando aprendizado de máquina.
3. Criar um frontend interativo para visualização e análise dos dados processados.

## Tecnologias
- **Backend:** Python com Flask ou FastAPI
- **Frontend:** React com TypeScript
- **Data Processing e ML:** PyTorch ou TensorFlow
- **Visualização:** D3.js / Three.js para gráficos e animações

## Estrutura do Projeto
```
CS2Vision/
|-- backend/
|   |-- app.py
|   |-- requirements.txt
|
|-- frontend/
|   |-- src/
|   |-- package.json
|
|-- demos/
|-- IMPLEMENTATION_GUIDE.md
|-- README.md
```

## Passos de Implementação

### 1. Backend
- [x] Configurar ambiente com `virtualenv` e instalar dependências básicas.
- [x] Criar endpoints para upload de demos e processamento de dados.
- [x] Integrar bibliotecas para extração de dados das demos.

### 2. Inteligência Artificial
- [x] Desenvolver modelo para identificar padrões (movimentação, estratégias, etc.).
- [x] Salvamento e carregamento de modelos treinados.

### 3. Frontend
- [x] Configurar ambiente React.
- [x] Criar interface inicial para upload de demos e visualização de progresso.
- [x] Implementar componentes visuais para análises (graficos, mapas).

### 4. Integração Backend + Frontend
- [x] Criar API RESTful no backend.
- [x] Consumir API no frontend para visualização.

### 5. Documentação e Testes
- [ ] Documentar as APIs e as funções implementadas.- [x] Testar o fluxo de ponta-a-ponta.

---

## Requisitos de Ambiente
1. **Python 3.10+** (com `pip` e `virtualenv` configurados)
2. **Node.js 16+**
3. **Ferramentas necessárias**: `git`, `gh` (GitHub CLI) e navegador web.

## Próximos Passos
Começando pela configuração inicial do backend:

1. Configurar `virtualenv` dentro de `backend` e instalar Flask/FastAPI.
2. Criar estrutura de pastas básica para o servidor.
3. Adicionar suporte a upload e parse de demos.

Depois disso, pulemos para o frontend e integração dos dois módulos.
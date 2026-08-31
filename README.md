# Hypotheses — Marketing branch

Ветка `Hypotheses` переводит evidence из `CustomerDevelopment` и opportunity analysis из `JobesToBeDone` в **начальный Product Backlog из 24 Markdown-гипотез**, а также фиксирует **HLA v0.1**, bounded contexts и основные data flows будущего SaaS.

## Назначение ветки

Эта ветка отвечает на вопрос: **«Что именно мы должны проверить следующим, какой эффект ожидаем и какой объём реализации допустим до получения evidence?»**

Backlog — не список обязательных features. Каждая запись должна быть falsifiable hypothesis с source lineage, expected behaviour, threshold и kill criterion.

## Структура ветки

```text
Hypotheses/
├── .agents/product-marketing.md
├── backlog/
│   ├── H001.md
│   ├── H002.md
│   ├── ...
│   └── H024.md
├── product-backlog.md
├── evidence-to-hypothesis-map.csv
├── experiment-register.md
├── learning-roadmap.md
├── docs/
│   ├── architecture/
│   │   ├── HLA-v0.1.md
│   │   ├── data-flows.md
│   │   └── research-to-product-flow.md
│   └── adr/
│       ├── 0001-event-driven-architecture.md
│       ├── 0002-data-lineage.md
│       ├── 0003-llm-provider-abstraction.md
│       └── 0004-context-model.md
├── tests/
│   └── test_hypothesis_rigor.py
├── validate_hypotheses.py
├── SKILLS-USED.md
└── README.md
```

## 24 Product Backlog hypotheses

В `backlog/` находится ровно **24 Markdown-файла** `H001.md`–`H024.md`.

Каждая гипотеза содержит:

- Hypothesis ID;
- related JTBD;
- source/evidence IDs;
- evidence state;
- problem/assumption;
- behavioural prediction;
- proposed experiment;
- **Expected Impact**;
- **Implementation Complexity**;
- Confidence;
- Priority Score;
- success metric / pre-registered threshold;
- kill criterion;
- negative evidence to capture;
- dependencies/status.

## Сортировка backlog

Основная формула:

```text
Priority = (Expected Impact × Confidence) / Implementation Complexity
```

Таким образом, backlog отсортирован по expected impact и implementation complexity с поправкой на confidence. На synthetic-only стадии Confidence намеренно ограничен: искусственные fixtures не дают права назначать высокий empirical confidence.

## Почему нужен kill criterion

Без kill criterion команда легко превращает backlog в confirmation-bias machine. Для каждой гипотезы заранее фиксируется, какой результат заставит:

- отказаться от гипотезы;
- сузить сегмент;
- изменить механизм;
- вернуться к research;
- не строить feature дальше.

## `evidence-to-hypothesis-map.csv`

Machine-readable lineage от source interview IDs/JTBD до backlog items. Цель — иметь возможность ответить на вопрос: **«Почему H007 вообще существует?»** без чтения всей истории проекта.

## `experiment-register.md`

Регистр experiments хранит sequence и результат проверки hypotheses. Он должен обновляться после реальных тестов, а не только после разработки.

## `learning-roadmap.md`

Сортирует работу по learning risk: сначала проверяются problem/segment/trigger assumptions, затем value, затем usability/retention, и только потом масштабируемость.

# HLA v0.1

`docs/architecture/HLA-v0.1.md` описывает High-Level Architecture будущего SaaS. Архитектура следует bounded-context подходу и не привязывает domain logic напрямую к конкретному LLM-провайдеру.

## Bounded contexts

### Context Management
Отвечает за восстановление контекста: source ingestion, timeline, summaries, open loops, evidence references.

### Decision Support
Отвечает за decision cases, criteria, alternatives, evidence, recommendation/rationale и decision history.

### Time / Behaviour Analytics
Отвечает за фактическое распределение времени/внимания, mapping к priorities и retrospective feedback.

### Data Lineage / Evidence
Отвечает за происхождение derived outputs: source → transformation → derived artifact → recommendation/decision.

### LLM Orchestration
Инфраструктурная граница для генерации/синтеза. Domain contexts зависят от `LLMProvider`, а не от GigaChat напрямую.

### Identity / Tenant / Billing — future SaaS context
Не реализован в skeleton v0.1, но должен быть отдельным bounded context до multi-user production release.

## Основные data flows

Подробности — в `docs/architecture/data-flows.md`.

### Context flow

```text
external/user source
  → ingestion
  → normalized evidence
  → lineage record
  → context reconstruction
  → source-linked summary
```

### Decision flow

```text
problem + alternatives + criteria
  → evidence retrieval
  → decision analysis
  → LLMProvider (optional reasoning/generation)
  → rationale + confidence + source links
  → decision event
```

### Time-feedback flow

```text
calendar/activity signals
  → normalized time evidence
  → declared priorities
  → allocation comparison
  → drift/fragmentation analysis
  → weekly feedback
```

### Event/data-lineage flow

```text
User Action → Domain Command → State Change → Domain Event
            → Lineage Record → Derived Context / Analytics / LLM
```

## Связь HLA с Backend и Frontend

`Backend` реализует API/application/infrastructure skeleton вокруг этих boundaries. `Frontend` организует UX вокруг трёх primary JTBD feature areas. HLA не означает, что все contexts уже production-ready: v0.1 фиксирует границы и data ownership до дальнейшей реализации.

## Architecture Decision Records

- `0001-event-driven-architecture.md` — почему domain events полезны для asynchronous processing и lineage.
- `0002-data-lineage.md` — почему source/provenance являются first-class data.
- `0003-llm-provider-abstraction.md` — почему GigaChat должен находиться за provider boundary.
- `0004-context-model.md` — правила представления рабочего context.

## Research → product promotion gate

`docs/architecture/research-to-product-flow.md` определяет, когда marketing hypothesis можно переводить в engineering task. Минимальный gate должен содержать segment, trigger, evidence, outcome, experiment result и explicit decision.

## Как проверить ветку

```bash
python validate_hypotheses.py
python -m pytest tests -q
```

Дополнительная ручная проверка:

```bash
find backlog -maxdepth 1 -name 'H*.md' | wc -l
# ожидается 24

test -f docs/architecture/HLA-v0.1.md
test -f docs/architecture/data-flows.md
```

## Definition of Ready для Engineering

Hypothesis может перейти в Backend/Frontend implementation только если:

1. связан с конкретным JTBD и segment;
2. имеет empirical evidence или явно обозначенный experiment-only статус;
3. имеет measurable expected outcome;
4. определён minimum implementation needed для теста;
5. записан success/fail threshold;
6. известен owner и срок эксперимента;
7. описано, что будет сделано при negative result;
8. architecture impact согласуется с HLA/ADR.

## Что не следует делать

- строить все 24 hypotheses параллельно;
- считать высокий Expected Impact доказанным эффектом;
- увеличивать Confidence на основании красивого прототипа;
- добавлять новую bounded context без data ownership/contract;
- давать LLM прямой доступ ко всем данным без policy/audit boundary.

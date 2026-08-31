# Marketing — one-step-forward-agent

Marketing-репозиторий хранит всю логику **Customer Development → JTBD → Product Hypotheses → Positioning → GTM** для будущего SaaS `one-step-forward-agent`.

> **Статус доказательств:** pre-PMF. Текущий набор из 30 интервью является **synthetic research fixture**, созданным для проверки исследовательского процесса и аналитического pipeline. Он не является подтверждением спроса, рынка, PMF или реальными цитатами клиентов.

## Назначение репозитория

`Marketing` отделён от `Backend` и `Frontend`, чтобы продуктовые решения не смешивались с реализацией. Здесь фиксируются проблема, evidence, Jobs To Be Done, маркетинговые гипотезы, позиционирование и план валидации. Код продукта должен опираться на подтверждённые гипотезы из этого репозитория, а не наоборот.

## Карта веток

| Ветка | Что находится | Для чего нужна | Основной результат |
|---|---|---|---|
| `main` | Product Marketing context, positioning, messaging, competitive alternatives, GTM, funnel metrics, content strategy | единая маркетинговая система и навигация | версия продуктового позиционирования и план проверки рынка |
| `CustomerDevelopment` | 30 CustDev Markdown-файлов, evidence matrix, research quality, interview guide | исследование проблемы и сбор первичного evidence | проверяемые сигналы по 3 JTBD |
| `JobesToBeDone` | Python-модули, CSV, методология, `Diagrams/` | количественная/описательная обработка JTBD и поиск candidate USP | 6 графиков + opportunity map + candidate USP |
| `Hypotheses` | 24 гипотезы, Product Backlog, experiment register, HLA v0.1, data flows, ADR | перевод research evidence в проверяемые продуктовые ставки | приоритизированный backlog и архитектурные ограничения |

> Имя `JobesToBeDone` сохранено намеренно, потому что именно такое имя задано в требованиях проекта.

## Сквозной Product Marketing процесс

```text
CustomerDevelopment
  30 интервью / evidence
        ↓
JobesToBeDone
  JTBD + importance + satisfaction + opportunity
        ↓
Hypotheses
  24 testable product hypotheses
        ↓
Backend / Frontend
  implementation only after evidence gate
        ↓
Real usage evidence
        ↺ обратно в CustomerDevelopment / JTBD
```

Ключевой принцип: **evidence precedes implementation**. Любая сильная формулировка в positioning должна иметь статус: `synthetic hypothesis`, `empirical observation`, `validated insight` или `decision`.

## Три исходных JTBD

1. **Потеря контекста** — восстановить состояние работы, причинно-следственную цепочку, прошлые решения и открытые вопросы после переключения/перерыва.
2. **Неспособность принять решение** — сделать критерии явными, сравнить варианты и evidence, принять решение и сохранить rationale.
3. **Отсутствие объективной обратной связи по использованию времени** — сопоставить фактическое распределение внимания с заявленными приоритетами и увидеть drift.

## Product Marketing foundation

Файл `.agents/product-marketing.md` — канонический контекст, который должен читаться перед любой downstream маркетинговой задачей. В нём зафиксированы:

- working category и product one-liner;
- beachhead ICP hypothesis и anti-persona;
- JTBD и trigger situations;
- status-quo alternatives;
- differentiation hypothesis;
- switching forces: Push / Pull / Habit / Anxiety;
- objections;
- message hypotheses;
- research-integrity policy;
- pre-PMF goals и learning metric.

## Структура `main`

```text
Marketing/
├── .agents/
│   └── product-marketing.md
├── strategy/
│   ├── positioning.md
│   ├── messaging.md
│   ├── competitive-landscape.md
│   ├── gtm-90-day.md
│   ├── funnel-metrics.md
│   └── marketing-audit.md
├── content/
│   └── content-strategy.md
├── experiments/
│   └── marketing-experiments.md
├── SKILLS-USED.md
└── README.md
```

### `strategy/positioning.md`
Positioning строится от конкурентной альтернативы к уникальному атрибуту, затем к ценности, сегменту и category hypothesis. До реальных интервью это **позиционирование-гипотеза**, не market truth.

### `strategy/messaging.md`
Хранит message hierarchy для трёх JTBD, proof mechanisms, headline candidates и CTA ladder. Synthetic phrases запрещено использовать как реальные VOC quotes.

### `strategy/competitive-landscape.md`
Сравнивает не feature lists, а альтернативные способы выполнения jobs: task/calendar tools, AI assistants, time trackers, memory tools, ручная weekly review. Главная цель — понять status quo и white space.

### `strategy/gtm-90-day.md`
Pre-PMF GTM делится на три фазы: заменить synthetic evidence реальными интервью, провести concierge validation, затем тестировать messaging/channels. Масштабирование paid acquisition до retention signal не рекомендуется.

### `strategy/funnel-metrics.md`
Метрики организованы от research quality до activation/retention/revenue. До PMF приоритет — learning density, а не vanity traffic.

### `content/content-strategy.md`
Контент разделён на searchable и shareable. Цель контента на текущей стадии — рекрутинг research participants, проверка языка проблемы и создание доверия к evidence-backed подходу.

### `experiments/marketing-experiments.md`
Каждый marketing experiment содержит hypothesis, test, primary metric и kill/revise criterion. Success criteria задаются **до** просмотра результатов.

### `strategy/icp-scorecard.md`
Фиксирует beachhead-segment hypotheses и evidence gates, чтобы не превращать «knowledge workers» в слишком широкий ICP.

### `strategy/channel-strategy.md`
Определяет каналы как механизм получения qualified evidence/activation, а не как гонку за vanity traffic.

### `strategy/pricing-hypotheses.md`
Разделяет price guesses, stated willingness, commitment, actual transaction и retained payment; pricing остаётся hypothesis до paid evidence.

### `strategy/launch-readiness.md`
Задаёт gates от research integrity до problem evidence, concierge value, activation, retention, paid pilot и broader launch.

### `content/editorial-backlog.md` и `experiments/experiment-template.md`
Дают executable backlog контента и единый preregistered шаблон экспериментов.

## Использованные специальные Marketing Skills

Подход построен на принципах специализированных Agent Skills:

- `customer-research` — JTBD, pains, trigger events, desired outcomes, alternatives, confidence and bias checks;
- `interview-to-jtbd` — traceability от source material к claims и разделение observation/inference/assumption;
- `marketing-plan` — AARRR и executable GTM planning, адаптированный под pre-PMF;
- `content-strategy` — searchable/shareable content и buyer-stage mapping;
- positioning/messaging frameworks — status quo → differentiation → value → segment → message.

Подробности и ограничение среды описаны в `SKILLS-USED.md`.

## Research integrity

Запрещено:

- называть synthetic fixtures «проведёнными реальными интервью»;
- публиковать synthetic фразы как customer quotes/testimonials;
- делать статистические выводы о рынке по искусственно сбалансированным 30 файлам;
- считать Opportunity Score доказательством demand;
- повышать Confidence только потому, что гипотеза выглядит логичной.

Разрешено использовать fixtures для:

- тестирования Markdown schema;
- тестирования extraction pipeline;
- проверки формул и диаграмм;
- репетиции исследовательского процесса;
- генерации вопросов для реальных интервью.

## Как работать с ветками

```bash
# посмотреть ветки
git branch --all

# CustDev
git switch CustomerDevelopment
python validate_interviews.py
python -m pytest tests -q

# JTBD
git switch JobesToBeDone
python -m src.extract_jtbd
python -m src.generate_all_diagrams
python -m pytest tests -q

# Hypotheses
git switch Hypotheses
python validate_hypotheses.py
python -m pytest tests -q
```

## Как проверить весь Marketing

Из корня release-пакета:

```bash
./verify_marketing.sh
python verify_updated_prompt.py
```

Проверяется наличие веток, 30 CustDev Markdown-файлов, 6 PNG-диаграмм, 24 hypothesis-файлов, HLA v0.1, data flows, подробных README и ключевых research-integrity правил.

## Что должно происходить дальше

1. Заменить synthetic corpus минимум 15–20 реальными problem interviews в 1–2 сегментах.
2. Не смешивать сегменты при подсчёте frequency/intensity.
3. Проверить switching trigger и реальные workarounds.
4. Запустить concierge tests отдельно для context, decision и time-feedback jobs.
5. Повысить confidence только после повторяющихся независимых empirical signals.
6. После выбора beachhead JTBD синхронизировать Product Backlog, Backend bounded contexts и Frontend journey.

## Definition of Done для маркетингового решения

Маркетинговое решение может считаться готовым к переносу в продукт только когда известно:

- **для кого** оно предназначено;
- **в какой ситуации/trigger** возникает job;
- **какой status quo** пользователь использует сейчас;
- **какое evidence** подтверждает проблему;
- **какой measurable outcome** ожидается;
- **какой риск/assumption** остаётся;
- **каким experiment** это можно опровергнуть;
- **какой product decision** следует при pass/fail.

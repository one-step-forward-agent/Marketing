# CustomerDevelopment — Marketing branch

Ветка `CustomerDevelopment` — источник исследовательских данных для проекта `one-step-forward-agent`. Здесь находятся **30 Markdown-файлов пилотных synthetic CustDev-интервью**, схема исследования, evidence matrix и правила перехода от искусственного corpus к реальным интервью.

> **Критически важно:** текущие 30 интервью являются synthetic fixtures. Они моделируют форму и возможные паттерны CustDev, но не должны представляться как реально проведённые интервью, реальные цитаты, статистика рынка или доказательство PMF.

## Назначение ветки

Цель ветки — сделать Customer Development **воспроизводимым и трассируемым**. Любой вывод должен быть связан с конкретным Interview ID, evidence type, наблюдаемым trigger/workaround и уровнем confidence.

Эта ветка отвечает на вопрос: **«Что мы действительно знаем о проблеме пользователя и откуда это знаем?»**

## Ключевой результат

Corpus включает ровно 30 `.md` файлов:

- 10 — JTBD **потеря контекста** (`context-restoration`);
- 10 — JTBD **неспособность принять решение** (`decision-support`);
- 10 — JTBD **объективная обратная связь по использованию времени** (`time-feedback`).

Равное распределение используется только для проверки pipeline и **не означает равную распространённость jobs в реальном рынке**.

## Структура ветки

```text
CustomerDevelopment/
├── .agents/
│   └── product-marketing.md
├── interviews/
│   ├── 001-interview.md
│   ├── 002-interview.md
│   ├── ...
│   └── 030-interview.md
├── templates/
│   └── custdev-interview-template.md
├── analysis/
│   ├── evidence-matrix.csv
│   ├── jtbd-summary.md
│   ├── segment-analysis.md
│   ├── research-quality.md
│   ├── research-gaps.md
│   ├── next-interview-guide.md
│   └── language-hypotheses.md
├── tests/
│   ├── test_validate_interviews.py
│   └── test_research_quality.py
├── validate_interviews.py
├── SKILLS-USED.md
└── README.md
```

## Схема каждого CustDev-файла

Каждый interview fixture содержит поля, позволяющие не превращать интервью в feature request list:

- Interview ID и segment/persona hypothesis;
- situation/context;
- trigger event;
- current behaviour и workaround;
- pain / friction;
- desired outcome;
- decision criteria;
- observed JTBD;
- functional job;
- emotional job;
- social job;
- switching forces: Push / Pull / Habit / Anxiety;
- Importance score;
- Satisfaction score;
- Evidence type;
- Confidence;
- interpretation risk / research notes;
- synthetic disclosure.

## Как читать evidence

### Observation
То, что реально присутствует в source material. Для текущего corpus это observation **внутри synthetic fixture**, а не market observation.

### Inference
Интерпретация observation: например, «пользователь теряет время на восстановление causal context».

### Assumption
То, что ещё не подтверждено: willingness to pay, frequency в сегменте, tolerance к data access, habit formation.

### Recommendation
Следующий test или product/marketing action. Recommendation не должна маскироваться под fact.

## `analysis/evidence-matrix.csv`

Нормализованная таблица для traceability. Она связывает Interview ID с JTBD, trigger, importance/satisfaction и evidence state. Именно этот слой должен использовать downstream-анализ вместо ручного выбора «удобных» цитат.

## `analysis/jtbd-summary.md`

Сводит три повторяющихся jobs и описывает их без product-solution bias. Фокус — progress, который пользователь пытается сделать, а не конкретная функция продукта.

## `analysis/segment-analysis.md`

Показывает покрытие synthetic corpus и объясняет, почему из него нельзя оценивать market prevalence. Для реальных данных анализ должен выполняться **по сегментам**, а не усреднять founders, PM, consultants и team leads.

## `analysis/research-quality.md`

Определяет evidence ladder и confidence rules. В реальном research высокий confidence требует нескольких независимых источников, повторяемости и предпочтительно unprompted language/behaviour.

## `analysis/research-gaps.md`

Список критических неизвестных, которые необходимо закрыть реальными интервью: частота проблемы, стоимость workaround, switching trigger, privacy anxiety, willingness to change/pay и фактический recurrence.

## `analysis/next-interview-guide.md`

Guide для следующего раунда **реальных** CustDev. Вопросы привязаны к конкретному недавнему эпизоду, а не к фантазиям «хотели бы вы такую функцию?». Приоритет — past behaviour, trigger, workaround и consequence.

## `analysis/language-hypotheses.md`

Хранит формулировки, которые можно тестировать как messaging hypothesis. Они не являются Voice of Customer до тех пор, пока не появятся в реальных независимых источниках.

## Три JTBD и что нужно доказать

### 1. Потеря контекста
Необходимо доказать, что context reconstruction происходит часто, имеет измеримую цену и что пользователи уже создают workaround.

### 2. Неспособность принять решение
Необходимо отделить обычную сложность решения от систематической проблемы с implicit criteria/evidence и проверить, возвращаются ли пользователи к сохранённому rationale.

### 3. Отсутствие объективной обратной связи по времени
Нужно доказать, что retrospective time feedback приводит к изменению поведения, а не просто к интересному dashboard.

## Как перейти от synthetic к real research

1. Рекрутировать респондента из явно выбранного сегмента.
2. Получить consent и обезличить PII.
3. Разбирать один конкретный недавний episode.
4. Фиксировать trigger → behaviour → workaround → consequence → desired outcome.
5. Не показывать решение до завершения problem interview.
6. Отдельно отмечать prompted и unprompted signals.
7. Сохранять source/provenance.
8. После каждого 5–10 интервью обновлять clusters и contradictions.
9. Не удалять negative evidence.
10. Передавать в `JobesToBeDone` только структурированные observations с provenance.

## Как проверить ветку

```bash
python validate_interviews.py
python -m pytest tests -q
```

Ожидаемый invariant:

- 30 Markdown интервью;
- уникальные Interview ID;
- обязательный synthetic disclosure;
- только три разрешённых JTBD key;
- корректные Importance/Satisfaction scores;
- research quality fields присутствуют;
- validator работает независимо от текущей рабочей директории.

## Связь с другими ветками

```text
CustomerDevelopment
    │ evidence / source IDs
    ▼
JobesToBeDone
    │ opportunity + outcome model
    ▼
Hypotheses
    │ testable backlog
    ▼
Backend / Frontend
```

`JobesToBeDone` не должен вручную «придумывать» JTBD scores: его extraction pipeline должен получать данные из этой ветки. `Hypotheses` обязана хранить source IDs/evidence lineage, чтобы feature hypothesis можно было проследить назад до research.

## Privacy и research ethics

Для будущих реальных интервью:

- хранить только необходимые данные;
- удалять/маскировать PII;
- не коммитить секреты и персональные идентификаторы;
- получать согласие на запись/хранение;
- не использовать реальную цитату вне согласованного контекста;
- отделять participant statement от researcher interpretation.

## Definition of Done для реального интервью

Интервью считается пригодным для synthesis, если есть: segment, episode, trigger, current alternative/workaround, consequence, desired outcome, JTBD mapping, provenance, confidence note и указание того, что осталось неизвестным.

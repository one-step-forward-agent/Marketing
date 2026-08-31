# JobesToBeDone — Marketing branch

Ветка `JobesToBeDone` реализует воспроизводимый аналитический pipeline **CustomerDevelopment → JTBD → opportunity analysis → candidate USP**.

> Написание `JobesToBeDone` сохранено строго по требованиям проекта. Текущие numerical scores основаны на synthetic fixtures и являются проверкой метода/кода, а не научным доказательством рыночного спроса.

## Назначение ветки

Ветка отвечает на вопрос: **«Какая работа выглядит наиболее недообслуженной и какой value proposition стоит проверять первым?»**

Под «научным методом» здесь понимается дисциплина: явная гипотеза → измеряемые переменные → воспроизводимый расчёт → falsifiable threshold → эксперимент → возможность опровергнуть вывод. Нельзя называть synthetic outcome статистически валидированным рыночным результатом.

## Откуда берутся данные

Python extraction получает записи из ветки `CustomerDevelopment`, а затем формирует:

```text
30 CustDev Markdown files
        ↓
extract_jtbd.py
        ↓
data/interview_features.csv
        ↓
aggregation
        ↓
data/jtbd_scores.csv
        ↓
analysis modules
        ↓
Diagrams/*.png + candidate-usp.md
```

Таким образом, JTBD должны быть **получены через созданные CustDev**, а не введены вручную как несвязанные числа.

## Структура ветки

```text
JobesToBeDone/
├── .agents/product-marketing.md
├── data/
│   ├── interview_features.csv
│   └── jtbd_scores.csv
├── src/
│   ├── extract_jtbd.py
│   ├── opportunity_score.py
│   ├── satisfaction_analysis.py
│   ├── underserved_analysis.py
│   ├── overserved_analysis.py
│   ├── solution_job_fit.py
│   └── generate_all_diagrams.py
├── tests/
│   ├── test_jtbd_analysis.py
│   ├── test_opportunity_score.py
│   └── test_research_rigor.py
├── Diagrams/
│   ├── jtbd-prioritization.png
│   ├── importance-vs-satisfaction.png
│   ├── overserved-jobs.png
│   ├── underserved-jobs.png
│   ├── opportunity-map.png
│   └── solution-job-fit.png
├── methodology.md
├── outcome-map.md
├── evidence-readiness.md
├── validation-protocol.md
├── candidate-usp.md
├── requirements.txt
├── SKILLS-USED.md
└── README.md
```

## Обязательные графики поиска УТП

Требование исходного промта закрывается шестью визуализациями:

1. **Приоритизация JTBD** — `Diagrams/jtbd-prioritization.png`.
2. **Удовлетворенность пользователей** и **Важность работы** — `Diagrams/importance-vs-satisfaction.png`.
3. **Переобслуженные работы** — `Diagrams/overserved-jobs.png`.
4. **Недообслуженные работы** — `Diagrams/underserved-jobs.png`.
5. **Opportunity / оптимальное соотношение решений / работ** — `Diagrams/opportunity-map.png`.
6. **Оптимальное соотношение решений / работ** как solution-job fit — `Diagrams/solution-job-fit.png`.

Все PNG имеют явную маркировку synthetic/descriptive, чтобы их нельзя было случайно использовать как эмпирическое market proof.

## Методика scoring

### Importance
Насколько критична работа для progress пользователя. В synthetic corpus шкала нужна только для проверки вычислений; в real research значение должно выводиться из структурированной survey/quant follow-up или заранее определённого coding protocol.

### Satisfaction
Насколько текущий workaround/решение удовлетворяет пользователя.

### Opportunity Score
Используется ODI-подобная формула:

```text
Opportunity = Importance + max(Importance - Satisfaction, 0)
```

Она повышает приоритет jobs, которые одновременно важны и неудовлетворительно решаются. Score — **приоритизационный сигнал**, а не доказательство willingness to pay.

### Overserved / underserved

- **underserved** — высокая importance при недостаточной satisfaction;
- **overserved** — satisfaction относительно высока по отношению к importance;
- **balanced** — gap не создаёт сильного opportunity signal.

Thresholds документированы и должны быть зафиксированы до анализа реального датасета.

## Python-модули

### `src/extract_jtbd.py`
Читает структуру CustDev, извлекает JTBD и количественные поля, нормализует данные и агрегирует `jtbd_scores.csv`.

### `src/opportunity_score.py`
Содержит чистую функцию расчёта opportunity и классификацию job state. Тестируется отдельно.

### `src/satisfaction_analysis.py`
Готовит данные для сравнения importance/satisfaction.

### `src/underserved_analysis.py`
Выделяет недообслуженные jobs.

### `src/overserved_analysis.py`
Выделяет переобслуженные jobs.

### `src/solution_job_fit.py`
Формирует показатель/представление связи candidate solution с job opportunity. Это не заменяет реальный experiment.

### `src/generate_all_diagrams.py`
Оркестрирует построение всех обязательных графиков и сохраняет результаты в `Diagrams/`.

## Как запустить

Из checkout ветки `JobesToBeDone`:

```bash
python -m pip install -r requirements.txt
python -m src.extract_jtbd
python -m src.generate_all_diagrams
python -m pytest tests -q
```

После запуска должны существовать 6 PNG-файлов в `Diagrams/`.

## Как проверить воспроизводимость

1. Изменить один synthetic score в конкретном CustDev source.
2. Повторно запустить extraction.
3. Проверить изменение `interview_features.csv`.
4. Повторно агрегировать `jtbd_scores.csv`.
5. Перегенерировать diagrams.
6. Убедиться, что изменение графика объяснимо исходным source ID.

Именно эта цепочка обеспечивает data lineage.

## `outcome-map.md`

Разделяет functional, emotional и social jobs и переводит их в measurable desired outcomes. Это важно: продукт не должен оптимизировать «feature adoption» вместо прогресса пользователя.

## `evidence-readiness.md`

Явно показывает, какие части анализа основаны только на synthetic fixtures и какие уровни evidence нужны для повышения confidence.

## `validation-protocol.md`

Содержит falsifiable tests. Для каждого JTBD должны быть определены segment, trigger, expected behaviour, threshold, negative evidence и правило принятия решения.

## `candidate-usp.md`

УТП здесь рассматривается как **candidate positioning hypothesis**. Допустимый вывод: «это направление стоит проверить первым». Недопустимый вывод: «рынок доказал, что это уникальное торговое предложение».

Candidate USP должен соединять:

```text
specific segment
+ trigger situation
+ underserved job
+ differentiated mechanism
+ observable outcome
+ reason to believe / evidence
```

## Как выбирать направление для реального эксперимента

Приоритет получает не просто максимальный score, а job, у которого одновременно:

- высокая importance;
- низкая satisfaction;
- повторяемый trigger;
- реальный workaround/cost;
- достаточное evidence coverage;
- segment concentration;
- понятный falsifiable prototype test.

Если quantitative score высокий, но evidence слабое — результат остаётся `research priority`, а не product decision.

## Связь с `Hypotheses`

Каждый высокий-priority outcome должен создавать **несколько альтернативных hypotheses**, а не одну «очевидную» feature. Затем `Hypotheses` сортирует их по expected impact и implementation complexity и задаёт experiments.

## Как проверить ветку

```bash
python -m pytest tests -q
python -m src.extract_jtbd
python -m src.generate_all_diagrams
find Diagrams -maxdepth 1 -name '*.png' | wc -l
```

Ожидается: tests GREEN и `6` PNG-файлов.

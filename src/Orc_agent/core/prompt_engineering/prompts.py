"""
Modular Prompt Repository
Role: Centralized management of LLM prompts.
"""


REPORT_PROMPT = """
당신은 숙련된 데이터 분석가이자 비즈니스 전략가입니다. 데이터를 기반으로 전문적이고 통찰력 있는 최종 보고서를 작성하는 것이 임무입니다.

<Context>
## 1. 데이터 개요
{data_summary}

## 2. 분석 실행 결과
{all_results}

## 3. 시각화 자료 (Visual Assets)
{figure_markdown}
</Context>

<Guidelines>
1. **언어**: 반드시 **한국어**로 작성하십시오.
2. **형식**: 가독성 높은 Markdown 형식을 사용하십시오.
3. **어조**: 전문적이고 객관적이며, 비즈니스 의사결정에 도움이 되는 구체적인 어조를 유지하십시오.
4. **시각화 활용 (중요)**:
   - 위 '<Context> 3. 시각화 자료' 섹션에 있는 이미지 목록을 활용하십시오.
   - **파일경로를 그대로 사용하여 이미지를 삽입하십시오.**
   - 형식: `![데이터 시각화](filepath)` (예: `![월별 매출 추이](app/img/session_id/figure_0_0.png)`)
   - **주의**: 경로를 임의로 변경하거나 가짜 링크를 생성하지 마십시오. 오직 제공된 파일경로만 사용하십시오.
</Guidelines>

<Output Structure>
다음 목차에 따라 보고서를 작성하십시오:

# [제목] 데이터 분석 최종 보고서

## 1. 경영진 요약 (Executive Summary)
   - 분석 배경 및 목적
   - 핵심 발견 사항 (3가지 이내 요약)
   - 최종 결론 및 제언

## 2. 데이터 품질 및 신뢰성 평가 (Data Audit)
   - 데이터 구조 및 품질 진단 (결측치, 이상치 등)
   - 분석의 한계점 및 가정

## 3. 상세 분석 결과 (Detailed Analysis)
   - 각 분석 항목별 해석 및 시각화 포함
   - **(여기에 시각화 자료를 적절히 배치하십시오)**
   - 통계적 수치와 패턴을 구체적으로 서술

## 4. 결론 및 액션 아이템 (Conclusion & Recommendations)
   - 데이터 기반의 구체적인 실행 계획 제안
   - 향후 추가 분석이 필요한 영역
</Output Structure>
"""


ANALYSIS_PROMPT = """
You are a Data Analyst.
Data Summary:
{df_summary}

Previous Feedback (if any):
{feedback}

Task: Write Python code to analyze this data.
- Calculate key statistics.
- Create visualizations (matplotlib/seaborn). 
- **CRITICAL**: If you generate a plot, save it as a PNG file (e.g., 'plot_1.png', 'plot_2.png').
- Print summary insights.

Constraints:
- Assume dataframe is in variable `df`.
- Do NOT read CSV again.
- Python Code Only.
"""

EVALUATION_PROMPT = """
You are a Data Analysis Auditor.

Analysis Result:
{last_result}

Evaluate the quality of this analysis.
- Does it contain Python code and execution results?
- Is there any error?
- Does it provide meaningful insights?
- Were visualizations generated and saved if requested?

If it is good, reply with only the word "APPROVE".
If it is bad or has errors, reply with "REJECT: <reason>".
"""
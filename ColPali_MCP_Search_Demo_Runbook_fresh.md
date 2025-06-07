
# 🚀 ColPali MCP Search Demo - Runbook (03 단계)

## 1️⃣ 발표 구성 개요

이번 데모는 Morphik-core MCP 구조를 기반으로 Elastic MCP Server를 사용한 ColPali 기반 검색 데모입니다.

- REST API abstraction layer (MCP)를 적용하여 LLM 기반 RAG 또는 external knowledge retrieval flow에 적합한 구조로 설계했습니다.
- Streamlit 기반 UI에서 사용자가 검색 옵션을 직접 조작하고 결과를 확인할 수 있도록 구성했습니다.

## 2️⃣ 데모 구성 요소

| 구성 요소        | 설명                                       |
|-----------------|------------------------------------------|
| Streamlit UI    | User Query 입력, 옵션 선택                   |
| MCP REST API    | `/retrieve/chunks` 호출                     |
| Elastic MCP Server | Elastic → search 처리                     |
| 결과 표시          | Score + Content 반환                      |

## 3️⃣ Demo Flow 단계별 시연

### Step 1️⃣ 기본 검색 (No Reranking, No ColPali)

- UI → Query 입력
- Reranking OFF, ColPali OFF
- 검색 실행

설명:
- 지금은 기본 vector search 만 사용해서 Elastic MCP Server에서 검색한 결과입니다.
- Morphik-core 기준으로 보면 Configuration 1번 flow 입니다.

### Step 2️⃣ Reranking 적용

- UI → Reranking ON, ColPali OFF
- 검색 실행

설명:
- 지금은 Reranker를 적용한 구조입니다.
- MCP REST API 호출 시 use_reranking=True 를 전달하고 있습니다.
- Elastic MCP Server 내부에서 Reranker module 적용 → 결과 재정렬이 이루어집니다.

### Step 3️⃣ ColPali 적용

- UI → Reranking OFF, ColPali ON
- 검색 실행

설명:
- 이번에는 ColPali 기반 Multi-Vector search 를 사용했습니다.
- MCP REST API 호출 시 use_colpali=True 를 전달합니다.
- Elastic MCP Server 내부에서 Multi-Vector embedding 기반으로 Elastic 검색을 수행합니다.

### Step 4️⃣ Reranking + ColPali 적용

- UI → Reranking ON, ColPali ON
- 검색 실행

설명:
- 이번에는 Reranker + ColPali 를 모두 적용했습니다.
- Morphik-core 기준에서는 Configuration 4번 구조입니다.
- Multi-Vector search 후 결과를 다시 Reranker 를 통해 정렬하여 최종 결과를 반환합니다.

## 4️⃣ 예상 질문 대응 포인트

| 예상 질문                              | 대응 포인트 |
|---------------------------------------|------------|
| Morphik-core 와 완전 동일한 구조인가?      | REST API param 구조 / Retriever abstraction은 동일하게 구현함. Elastic MCP Server 사용. |
| LLM integration은 되어 있는가?          | 현재 Streamlit 데모는 Retrieval 단계까지 구현. LLM integration은 이후 pipeline에서 쉽게 추가 가능. |
| Elastic MCP Server와 일반 Elastic search의 차이점은? | MCP abstraction layer를 통해 LLM-friendly API 제공. Standard search 와 분리된 REST API 구성 가능. |
| Multi-vector search에서 ColPali 적용은 어떻게 되었는가? | Morphik-core 분석 결과와 동일하게 use_colpali param → Multi-Vector embedding 사용 → Elastic vector search 수행. |

## 5️⃣ 발표 마무리 강조 문구

- 이번 데모는 기존 ColPali 기반 search flow 를 Morphik-core MCP 구조를 분석하여 정확하게 반영한 구조입니다.
- Elastic MCP Server를 활용하여 REST API 기반으로 RAG application 과 쉽게 통합 가능하도록 설계했습니다.
- Reranking / ColPali 옵션을 사용자 인터페이스에서 자유롭게 선택할 수 있도록 구성하여 다양한 검색 시나리오에 대응할 수 있습니다.


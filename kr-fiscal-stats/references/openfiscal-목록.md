# 열린재정 OPEN API 목록 — 198종

> 출처: 열린재정(www.openfiscaldata.go.kr) · 수집 2026-09-23 · 저작권은 그 기관에 있고 이용 조건은 그 기관 약관을 따릅니다(저장소의 NOTICE).

**서비스이름**을 `https://openapi.openfiscaldata.go.kr/{서비스이름}` 의 자리에 넣는다.

- **검색인자** = 그대로 주소에 붙이는 이름이다(`OJ_YY=2024` 처럼). `★필수` 가 붙은 것은 반드시 준다. 코드 값(`BDG_FND_DIV_CD` 등)은 `references/openfiscal.md` 4절 표.

- **출력칸** = 돌아오는 자료의 칸 이름이다.

- ★**금액 단위는 이 목록에 없다** — 서비스마다 조원·억원·천원·원이 다르다. `references/openfiscal.md` 함정 ⑥ 의 표를 보고, 표에 없으면 크기로 맞춰 보고 「추정」이라고 밝힌다.

- ★**예산인지 결산인지도 이름으로 가르지 않는다** — `DIV_NM`·`STL_BDG_DIV_NM` 같은 구분 칸을 본다(함정 ⑦).

- **2026-09-23 에 `openfiscal.py 대조 --고치기` 로 포털에서 받은 것**이다.


## (분류 없음 — 예산편성 OPEN API 묶음) (28종)

### (OPEN API) 세부사업 예산편성현황(추경포함-범정부EA포털 제공용)

- **서비스이름** `GEAportal`
- 기관: 기획예산처 예산실 · 갱신: 수시
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_CD`(소관코드), `FSCL_CD`(회계코드), `ACCT_CD`(계정코드), `FLD_CD`(분야코드), `SECT_CD`(부문코드), `PGM_CD`(프로그램코드), `ACTV_CD`(단위사업코드), `SACTV_CD`(세부사업코드), `BZ_CLS_CD`(사업분류코드), `SBUDG_DGR`(추경차수)
- 출력칸: `FSCL_YY` 회계연도, `SBUDG_DGR` 추경차수, `OFFC_CD` 소관, `OFFC_NM` 소관명, `FSCL_CD` 회계, `FSCL_NM` 회계명, `ACCT_CD` 계정, `ACCT_NM` 계정명, `FLD_CD` 분야, `FLD_NM` 분야명, `SECT_CD` 부문, `SECT_NM` 부문명, `PGM_CD` 프로그램, `PGM_NM` 프로그램명, `ACTV_CD` 단위사업, `ACTV_NM` 단위사업명, `SACTV_CD` 세부사업, `SACTV_NM` 세부사업명, `BZ_CLS_CD` 경비, `BZ_CLS_NM` 경비구분, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_DFN_FRC_AMT` 본예산외화금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_MEDI_FRC_AMT` 추경정부안외화금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액, `Y_YY_DFN_MEDI_FRC_AMT` 추경국회확정외화금액, `FIN_DE_EP_CD` 지출구분코드, `FIN_DE_EP_NM` 지출구분

### (OPEN API) 세입 예산편성현황(추경포함)

- **서비스이름** `BudgetRevenuesAdd2`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `IKWAN_NM`(수입관명), `IHANG_NM`(수입항명), `IMOK_NM`(수입목명), `SBUDG_DGR`(추경횟수)
- 출력칸: `FSCL_YY` 회계연도, `SBUDG_DGR` 추경횟수, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

### (OPEN API) 세입 예산편성현황(추경포함)

- **서비스이름** `BudgetRevenuesAdd`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `IKWAN_NM`(수입관명), `IHANG_NM`(수입항명), `IMOK_NM`(수입목명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

### (OPEN API) 세입/수입 예산편성현황(외화)

- **서비스이름** `ForeignRevenueIncomeBudget`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `IKWAN_NM`(수입관명), `IHANG_NM`(수입항명), `IMOK_NM`(수입목명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `Y_YY_MEDI_FRC_AMT` 정부안금액, `Y_YY_DFN_MEDI_FRC_AMT` 국회확정금액

### (OPEN API) 세입/수입 예산편성현황(총수입)

- **서비스이름** `TotalRevenue`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `IKWAN_NM`(수입관명), `IHANG_NM`(수입항명), `IMOK_NM`(수입목명), `REVN_INQ_STND_CD`(조회기준코드 ★필수), `BDG_FND_DIV_CD`(예산기금구분코드 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `Y_PREY_FIRST_KCUR_AMT` 전년도당초금액, `Y_PREY_FIRST_FRC_AMT` 전년도당초금액, `Y_PREY_FNL_KCUR_AMT` 전년도최종금액, `Y_PREY_FNL_FRC_AMT` 전년도최종금액, `Y_YY_REQ_KCUR_AMT` 금년도요구금액, `Y_YY_REQ_FRC_AMT` 금년도요구금액, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세입/수입 예산편성현황(총액)

- **서비스이름** `BudgetRevenuesInit`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `IKWAN_NM`(수입관명), `IHANG_NM`(수입항명), `IMOK_NM`(수입목명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세출 세목 예산편성현황(추경포함)

- **서비스이름** `ExpenditureBudgetAdd2`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(목명), `EITM_NM`(세목명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

### (OPEN API) 세출 세목 예산편성현황(추경포함)

- **서비스이름** `ExpenditureBudgetAdd4`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(목명), `EITM_NM`(세목명), `BZ_CLS_NM`(경비명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `BZ_CLS_NM` 경비구분, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

### (OPEN API) 세출 세목 예산편성현황(추경포함)

- **서비스이름** `ExpenditureBudgetAdd6`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(지출목명), `EITM_NM`(지출세목명), `BZ_CLS_NM`(사업분류명), `SBUDG_DGR`(추경차수)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `BZ_CLS_NM` 경비구분, `SBUDG_DGR` 추경횟수, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

### (OPEN API) 세출 세부사업 예산편성현황(추경포함)

- **서비스이름** `ExpenditureBudgetAdd5`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `SBUDG_DGR`(추경횟수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `BZ_CLS_NM`(경상경비명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `BZ_CLS_NM` 경비구분, `SBUDG_DGR` 추경횟수, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_DFN_FRC_AMT` 본예산외화금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

### (OPEN API) 세출 세부사업 예산편성현황(추경포함)

- **서비스이름** `ExpenditureBudgetAdd1`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_DFN_FRC_AMT` 본예산외화금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

### (OPEN API) 세출 세부사업 예산편성현황(추경포함)

- **서비스이름** `ExpenditureBudgetAdd3`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `BZ_CLS_NM`(경상경비명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `BZ_CLS_NM` 경비구분, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_DFN_FRC_AMT` 본예산외화금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

### (OPEN API) 세출 예산편성현황(추경포함)

- **서비스이름** `ExpenditureBudgetAdd`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `Y_YY_DFN_KCUR_AMT` 금년도예산, `Y_YY_MEDI_KCUR_AMT` 추경정부안, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정

### (OPEN API) 세출/지출 세목 예산편성현황(외화)

- **서비스이름** `ForeignExpenditureBudgget2`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(목명), `EITM_NM`(세목명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `Y_YY_MEDI_FRC_AMT` 정부안금액, `Y_YY_DFN_MEDI_FRC_AMT` 국회확정금액

### (OPEN API) 세출/지출 세목 예산편성현황(외화)

- **서비스이름** `ForeignExpenditureBudgget4`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(목명), `EITM_NM`(세목명), `BZ_CLS_NM`(경상경비명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `BZ_CLS_NM` 경비구분, `Y_YY_MEDI_FRC_AMT` 정부안금액, `Y_YY_DFN_MEDI_FRC_AMT` 국회확정금액

### (OPEN API) 세출/지출 세목 예산편성현황(총액)

- **서비스이름** `ExpenditureBudgetInit2`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(목명), `EITM_NM`(세목명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세출/지출 세목 예산편성현황(총액)

- **서비스이름** `ExpenditureBudgetInit4`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(지출목명), `EITM_NM`(지출세목명), `BZ_CLS_NM`(사업분류명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `BZ_CLS_NM` 경비구분, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세출/지출 세목 예산편성현황(총지출)

- **서비스이름** `TotalExpenditure4`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `SACTV_NM`(세부사업명), `ACTV_NM`(단위사업명), `CITM_NM`(목명), `EITM_NM`(세목명), `BZ_CLS_NM`(경비명), `ANEXP_INQ_STND_CD`(조회기준 ★필수), `BDG_FND_DIV_CD`(예산기금구분 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `BZ_CLS_NM` 경비구분, `Y_PREY_FIRST_KCUR_AMT` 전년도국회확정금액, `Y_PREY_FNL_KCUR_AMT` 전년도최종금액, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세출/지출 세목 예산편성현황(총지출)

- **서비스이름** `TotalExpenditure2`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(목명), `EITM_NM`(세목명), `ANEXP_INQ_STND_CD`(조회기준), `BDG_FND_DIV_CD`(예산기금구분)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `Y_PREY_FIRST_KCUR_AMT` 전년도국회확정금액, `Y_PREY_FNL_KCUR_AMT` 전년도최종금액, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세출/지출 세부사업 예산편성현황(외화)

- **서비스이름** `ForeignExpenditureBudgget1`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `Y_YY_MEDI_FRC_AMT` 정부안금액, `Y_YY_DFN_MEDI_FRC_AMT` 국회확정금액

### (OPEN API) 세출/지출 세부사업 예산편성현황(외화)

- **서비스이름** `ForeignExpenditureBudgget3`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `BZ_CLS_NM`(경상경비명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `BZ_CLS_NM` 경비구분, `Y_YY_MEDI_FRC_AMT` 정부안금액, `Y_YY_DFN_MEDI_FRC_AMT` 국회확정금액

### (OPEN API) 세출/지출 세부사업 예산편성현황(총액)

- **서비스이름** `ExpenditureBudgetInit1`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세출/지출 세부사업 예산편성현황(총액)

- **서비스이름** `ExpenditureBudgetInit3`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `BZ_CLS_NM`(경상경비명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `BZ_CLS_NM` 경비구분, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세출/지출 세부사업 예산편성현황(총지출)

- **서비스이름** `TotalExpenditure1`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `ANEXP_INQ_STND_CD`(조회구분코드), `BDG_FND_DIV_CD`(예산기금구분코드)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `Y_PREY_FIRST_KCUR_AMT` 전년도국회확정금액, `Y_PREY_FNL_KCUR_AMT` 전년도최종금액, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세출/지출 세부사업 예산편성현황(총지출)

- **서비스이름** `TotalExpenditure3`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `BZ_CLS_NM`(경비명), `FLD_NM`(분야명), `SECT_NM`(부문명), `ANEXP_INQ_STND_CD`(조회구분코드 ★필수), `BDG_FND_DIV_CD`(예산기금구분코드 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `BZ_CLS_NM` 경비구분, `Y_PREY_FIRST_KCUR_AMT` 전년도국회확정금액, `Y_PREY_FNL_KCUR_AMT` 전년도최종금액, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### (OPEN API) 세출/지출 예산편성현황(외화)

- **서비스이름** `ForeignExpenditureBudgget`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `Y_YY_MEDI_FRC_AMT` 금년도정부안, `Y_YY_DFN_MEDI_FRC_AMT` 금년도국회확정

### (OPEN API) 세출/지출 예산편성현황(총액)

- **서비스이름** `ExpenditureBudgetInit`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `Y_YY_MEDI_KCUR_AMT` 금년도정부안, `Y_YY_DFN_MEDI_KCUR_AMT` 금년도국회확정

### (OPEN API) 세출/지출 예산편성현황(총지출)

- **서비스이름** `TotalExpenditure`
- 기관: 기획예산처 예산실 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `ANEXP_INQ_STND_CD`(조회구분코드 ★필수), `BDG_FND_DIV_CD`(예산기금구분코드 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부분명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `Y_PREY_FIRST_KCUR_AMT` 전년도당초금액, `Y_PREY_FIRST_FRC_AMT` 전년도당초금액, `Y_PREY_FNL_KCUR_AMT` 전년도최종금액, `Y_PREY_FNL_FRC_AMT` 전년도최종금액, `Y_YY_REQ_KCUR_AMT` 금년도요구금액, `Y_YY_REQ_FRC_AMT` 금년도요구금액, `Y_YY_MEDI_KCUR_AMT` 금년도정부안, `Y_YY_DFN_MEDI_KCUR_AMT` 금년도국회확정

## 중앙정부>상세재정통계>결산>국유재산 (15종)

### 관리처분계획총괄표

- **서비스이름** `VW_OPFI374`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `MNG_DSPS_PLAN_DIV_CD` 관리처분계획구분코드, `MNG_DSPS_PLAN_DIV_CD_NM` 관리처분계획구분명, `A_PLAN_QTY` 토지계획수량, `A_PLAN_AMT` 토지계획금액, `B_PLAN_QTY` 건물계획수량, `B_PLAN_AMT` 건물계획금액, `X_PLAN_QTY` 기타계획수량, `X_PLAN_AMT` 기타계획금액, `TOT_PLAN_QTY` 합계계획수량, `TOT_PLAN_AMT` 합계계획금액

### 국유재산 증감 및 현재액 총괄

- **서비스이름** `National1`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(마감연도 ★필수)
- 출력칸: `FSCL_YY` 마감연도, `PROP_CLS_CD` 재산분류코드, `PROP_CLS` 재산분류명, `GUBN` 결산재산종류코드, `NAME` 결산재산종류명, `UNIT` 수량단위, `HALF1_BFW_QTY` 전기이월수량, `PRV_BFW_AMT` 전기이월금액(천원), `THISP_INCR_QTY` 본년도증가수량, `THISP_INCR_AMT` 본년도증가금액(천원), `THISP_DCR_QTY` 본년도감소수량, `THISP_DCR_AMT` 본년도감소금액(천원), `THISP_QTY` 비교증감수량, `THISP_AMT` 비교증감금액(천원), `THISP_PERIE_QTY` 본년도말수량, `THISP_PERIE_AMT` 본년도말금액(천원)

### 국유재산현황

- **서비스이름** `NationalProperty`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `NP_TOT_AMT` 국유재산 총액, `LAND_QTY` 토지 수량, `LAND_AMT` 토지 금액, `BLDG_AMT` 건물 금액, `VLP_AMT` 유가증권 금액, `ETC_AMT` 기타 금액

### 국유지현황

- **서비스이름** `StateOwnedLands`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `NSHIPLAND_AREA` 국유지 총면적, `PADM_PROP_AREA` 행정재산 면적, `PADM_PROP_RT` 행정재산 비율, `GEN_PROP_AREA` 일반재산 면적, `GEN_PROP_RT` 일반재산 비율

### 연도별국유재산취득처분현황

- **서비스이름** `VW_OPFI376`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `MNG_DSPS_PLAN_DIV_CD_NM` 관리처분계획구분명, `TY_NM` 유형명, `A_AMT` 토지금액, `B_AMT` 건물금액, `X_AMT` 기타금액, `TOT_AMT` 합계금액

### 용도별 국유건물 현황

- **서비스이름** `VW_OPFI048`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `STATS_YR`(통계연도)
- 출력칸: `STATS_YR` 통계연도, `STATS_ATC_NM` 구분, `LEDG_QTY` 건수, `ES_AREA` 연면적, `ES_AREA_RT` 비율, `AMT` 금액

### 종류별 국유재산 현황

- **서비스이름** `VW_OPFI044`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `STATS_YR`(통계연도)
- 출력칸: `STATS_YR` 통계연도, `STATS_ATC_NM` 구분, `AMT` 금액, `AMT_RT` 비율

### 종합계획유형별국유재산현황

- **서비스이름** `VW_OPFI372`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `MNG_DSPS_PLAN_DIV_CD_NM` 관리처분계획구분명, `CMPS_PLAN_TY_CD_NM` 종합계획유형명, `A_OUT_QTY` 토지실적수량, `A_OUT_AMT` 토지실적금액, `B_OUT_QTY` 건물실적수량, `B_OUT_AMT` 건물실적금액, `X_OUT_AMT` 기타실적금액, `TOT_OUT_QTY` 합계실적수량, `TOT_OUT_AMT` 합계실적금액

### 중앙관서별 국유건물현황

- **서비스이름** `VW_OPFI049`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `STATS_YR`(통계연도)
- 출력칸: `STATS_YR` 통계연도, `STATS_ATC_NM` 구분, `LEDG_QTY` 건수, `ES_AREA` 연면적, `ES_AREA_RT` 비율, `AMT` 금액

### 중앙관서별 국유지 현황

- **서비스이름** `VW_OPFI045`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `STATS_YR`(통계연도)
- 출력칸: `STATS_YR` 통계연도, `STATS_ATC_NM` 구분, `LEDG_QTY` 필지수, `ES_AREA` 면적, `ES_AREA_RT` 비율, `AMT` 금액

### 중앙관서별특례운용계획

- **서비스이름** `VW_OPFI375`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `SC_TY_CD_NM` 특례유형명, `OFFC_NM` 소관명, `A_SC_PLAN_CNT` 토지특례계획건수, `A_SC_PLAN_QTY` 토지특례계획수량, `A_SC_PLAN_AMT` 토지특례계획금액, `B_SC_PLAN_CNT` 건물특례계획건수, `B_SC_PLAN_QTY` 건물특례계획수량, `B_SC_PLAN_AMT` 건물특례계획금액, `X_SC_PLAN_CNT` 기타특례계획건수, `X_SC_PLAN_QTY` 기타특례계획수량, `X_SC_PLAN_AMT` 기타특례계획금액

### 지목별 국유지 현황

- **서비스이름** `VW_OPFI047`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `STATS_YR`(통계연도)
- 출력칸: `STATS_YR` 통계연도, `STATS_ATC_NM` 구분, `LEDG_QTY` 필지수, `LEDG_AST_RT` 비율, `ES_AREA` 면적, `ES_AREA_RT` 비율, `AMT` 금액, `AMT_RT` 비율

### 지역별 국유건물 현황

- **서비스이름** `VW_OPFI050`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `STATS_YR`(통계연도)
- 출력칸: `STATS_YR` 통계연도, `STATS_ATC_NM` 구분, `LEDG_QTY` 건수, `ES_AREA` 연면적, `ES_AREA_RT` 비율, `AMT` 금액

### 지역별 국유지 현황

- **서비스이름** `VW_OPFI046`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `STATS_YR`(통계연도)
- 출력칸: `STATS_YR` 통계연도, `STATS_ATC_NM` 구분, `LEDG_QTY` 필지수, `ES_AREA` 면적, `ES_AREA_RT` 비율, `AMT` 금액

### 특례운용집행실적

- **서비스이름** `VW_OPFI373`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `GRND_STTU_CD_NM` 근거법령명, `A_EXE_CNT` 토지집행건수, `A_AREA_QTY` 토지면적및수량, `A_EXE_AMT` 토지집행금액, `B_EXE_CNT` 건물집행건수, `B_AREA_QTY` 건물면적및수량, `B_EXE_AMT` 건물집행금액, `X_EXE_CNT` 기타집행건수, `X_AREA_QTY` 기타면적및수량, `X_EXE_AMT` 기타집행금액, `TOT_EXE_CNT` 합계집행건수, `TOT_AREA_QTY` 합계면적및수량, `TOT_EXE_AMT` 합계집행금액

## 중앙정부>상세재정통계>결산>부담금 (1종)

### 부담금운용현황

- **서비스이름** `LevyingAmount`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `OJ_YY`(대상연도)
- 출력칸: `OJ_YY` 기준년도, `SHAM_CNT` 부담금 개수, `SHAM_TOT_AMT` 부담금 총액, `RVS_SUJ_1_AMT` 귀속주체별-중앙, `RVS_SUJ_2_AMT` 귀속주체별-지자체, `RVS_SUJ_3_AMT` 귀속주체별-공공기관 등, `FLD_1_AMT` 분야별-산업·에너지, `FLD_2_AMT` 분야별-환경, `FLD_3_AMT` 분야별-금융, `FLD_4_AMT` 분야별-건설교통, `FLD_5_AMT` 분야별-보건의료, `FLD_6_AMT` 분야별-기타

## 중앙정부>상세재정통계>결산>세입/세출 (13종)

### 과목별결산세입수입현황

- **서비스이름** `VW_OPFI377`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `OFFC_NM` 소관명, `ACNT_NM` 회계코드명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `BDG_AMT` 예산금액, `FNT_UDA` 이체증감액, `BDG_CAMT` 예산현액, `RD_AMT` 징수결정금액, `RCVMT_AMT` 수납금액, `RV_NAMT` 수입순액, `NPL_AMT` 불납결손금액, `NRC_AMT` 미수납금액

### 기금별 수입/지출 결산 현황

- **서비스이름** `ClosingFundRevenuesExpenses`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `FSCL_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `FSCL_NM` 회계명, `RV_MOD_BDGAMT` (수입)수입계획액, `RV_RC_AMT` (수입)수납금액, `RV_RV_NAMT` (수입)순액, `RV_INCR_INT` (수입)증감액, `RV_INCR_INT_N` (수입)증감순액, `EP_EP_PL_CAMT` (지출)지출계획현액, `EP_EP_AMT` (지출)지출금액, `EP_EP_NAMT` (지출)순계, `EP_INCR_INT` (지출)순액, `EP_INCR_INT_N` (지출)증감순액, `EP_NEXT_YY_BFWAMT` (지출)다음년도이월액, `EP_DUSEAMT` (지출)불용액

### 사업별결산세출지출현황

- **서비스이름** `VW_OPFI379`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `OFFC_NM` 소관명, `ACNT_NM` 회계코드명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SAY_NM` 세부사업명, `ANE_BDG_AMT` 세출예산금액, `UDA` 증감액, `ANE_BDG_CAMT` 세출예산현액, `EP_AMT` 지출금액, `EP_NAMT` 지출순액, `NYR_BFW_AMT` 차년도이월금액, `DUSE_AMT` 불용금액

### 세계잉여금

- **서비스이름** `AnnualSurplusBudget`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `GEN_FSCL_REVN_AMT` 일반회계 세입, `GEN_FSCL_ANEXP_AMT` 일반회계 세출, `STL_SURPL_AMT` 결산상 잉여금, `BFT_AMT` 이월액, `RAESTL_SURPL_AMT` 세계 잉여금, `RAESTL_SURPL_1_AMT` 지방교부세 및 교부금 정산, `RAESTL_SURPL_2_AMT` 채무상환, `RAESTL_SURPL_3_AMT` 추경재원, `RAESTL_SURPL_4_AMT` 다음년도세입이입

### 세입/수입 결산 현황

- **서비스이름** `RevenuesSettled`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `ACCT_NM`(계정명), `FSCL_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_CD` 소관, `OFFC_NM` 소관명, `ACCT_CD` 계정, `ACCT_NM` 계정명, `FSCL_CD` 회계, `FSCL_NM` 회계명, `IKWAN_CD` 수입관, `IKWAN_NM` 수입관명, `IHANG_CD` 수입항, `IHANG_NM` 수입항명, `REVN_BDGAMT_F` 최종예산(추경포함)/당초수입계획액, `REVN_BDGAMT_M` 최종예산(추경포함)/수정수입계획액, `FNT_UDAMT` 이체등증감액, `REVN_BDG_CAMT` 세입예산현액/수입계획현액, `RD_AMT` 징수결정액, `RC_AMT` 수납액, `RV_NAMT` 수납순액, `NPL_AMT` 불납결손액, `NRC_AMT` 미수납액

### 세출/지출 결산 현황

- **서비스이름** `ExpendituresSettlement`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_CD` 소관, `OFFC_NM` 소관명, `FSCL_CD` 회계, `FSCL_NM` 회계명, `ACCT_CD` 계정, `ACCT_NM` 계정명, `FLD_CD` 분야, `FLD_NM` 분야명, `SECT_CD` 부문, `SECT_NM` 부문명, `PGM_CD` 프로그램, `PGM_NM` 프로그램명, `ACTV_CD` 단위사업, `ACTV_NM` 단위사업명, `CITM_CD` 지출목, `CITM_NM` 지출목명, `ANEXP_BDGAMT_F` 최종예산(추경포함)/당초지출계획액, `ANEXP_BDGAMT_M` 최종예산(추경포함)/수정지출계획액, `PREY_BFWAMT` 전년도이월액, `OVR_EP_AMT` 초과지출승인액, `RSVF_EP_DCS_IAMT` 예비비지출결정증액, `RSVF_EP_DCS_MAMT` 예비비지출결정감액, `BDTR_IAMT` 전용증액, `BDTR_MAMT` 전용감액, `AVDV_IAMT` 이용증액, `AVDV_MAMT` 이용감액, `FNT_IAMT` 이체증액, `FNT_MAMT` 이체감액, `ANEXP_BDG_CAMT` 세출예산현액/지출계획현액, `EP_AMT` 지출액, `EP_NAMT` 지출순액, `NEXT_YY_BFWAMT` 다음년도이월액, `DUSEAMT` 불용액

### 소관별 세입/세출 결산 현황

- **서비스이름** `DepartRevenExpenSettle`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `TREV_BDG_CAMT` (세입)예산현액, `RCVMT_AMT` (세입)수납액, `TREV_VARI_AMT` (세입)증감액, `ANE_BDG_CAMT` (세출)예산현액, `EP_AMT` (세출)지출액, `ANE_VARI_AMT` (세출)증감액, `NYR_BFW_AMT` 다음년도이월액, `DUSEAMT` 불용액

### 소관별결산세입현황(일반회계)

- **서비스이름** `VW_OPFI380`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ALY_YR`(회계연도)
- 출력칸: `ALY_YR` 회계연도, `OFFC_NM` 소관명, `BDG_AMT` 예산금액, `FNT_UDA` 이체증감액, `BDG_CAMT` 예산현액, `RD_AMT` 징수결정금액, `RCVMT_AMT` 수납금액, `RV_NAMT` 수입순액, `NPL_AMT` 불납결손금액, `NRC_AMT` 미수납금액

### 소관별결산세출현황(일반회계)

- **서비스이름** `VW_OPFI378`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `OFFC_NM` 소관명, `ANE_BDG_AMT` 세출예산금액, `ANE_BDG_CAMT` 세출예산현액, `EP_AMT` 지출금액, `NYR_BFW_AMT` 차년도이월금액, `DUSE_AMT` 불용금액

### 중앙정부결산

- **서비스이름** `VW_OPFI382`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `ALY_YR`(회계연도)
- 출력칸: `ALY_YR_NM` 회계연도명, `TREV_STL_BDG_AMT` 세입예산금액, `TREV_STL_RD_AMT` 세입징수결정금액, `TREV_STL_RCVMT_AMT` 세입수납금액, `TREV_STL_NPL_AMT` 세입불납결손금액, `TREV_STL_NRC_AMT` 세입미수납금액, `ANE_BDG_AMT` 세출예산금액, `BDG_AMT` 세출예산증감금액, `PREY_BFW_AMT` 전년도이월금액, `AVDV_AMT` 이용이체증감금액, `BDTR_AMT` 전용증감금액, `OVR_AMT` 초과지출승인증감금액, `RSVF_EP_AMT` 예비비지출결정증감금액, `ANE_BDG_CAMT` 세출예산현액, `EP_AMT` 지출금액, `NYR_BFW_AMT` 차년도이월금액, `DUSE_AMT` 불용금액

### 회계별 세입 결산 현황

- **서비스이름** `FiscalRevenSettle`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `REVN_BDGAMT` 세입예산액, `FNT_UDAMT` 이체등증감액, `REVN_BDG_CAMT` 세입예산현액, `RD_AMT` 징수결정금액, `RC_AMT` 수납금액, `NPL_AMT` 불납결손액, `NRC_AMT` 미수납액, `DIF_AMT` 세입예산현액과수납액의차

### 회계별 세입/세출 결산 현황

- **서비스이름** `FiacalRevenExpenSettle`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `GBN_NM`(회계구분명), `FSCL_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `GBN_NM` 회계구분명, `FSCL_NM` 회계명, `REVN_BDG_CAMT` (세입)예산현액, `RC_AMT` (세입)수납액, `REVN_RC_AMT` (세입)증감액, `ANEXP_BDG_CAMT` (세출)예산현액, `EP_AMT` (세출)지출액, `ANEXP_EP_AMT` (세출)증감액, `ELUC_BFWAMT` 다음년도이월액, `DUSEAMT` 불용액, `ACCT_NM` 계정명

### 회계별 세출 결산 현황

- **서비스이름** `FiscalExpenSettle`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `ANEXP_BDGAMT` 세출예산액, `PREY_BFWAMT` 전년도이월액, `RSVF_EP_DCS_IAMT` 예비비지출결정증액, `RSVF_EP_DCS_MAMT` 예비비지출결정감액, `BDTR_IAMT` 전용증액, `BDTR_MAMT` 전용감액, `AVDV_FNT_IAMT` 이용및이체증액, `AVDV_FNT_MAMT` 이용및이체감액, `RV_RPL_OVR_EP_PERM_AMT` 초과지출승인액, `ANEXP_BDG_CAMT` 세출예산현액, `EP_AMT` 지출금액, `NEXT_YY_BFWAMT` 다음년도이월액, `DUSEAMT` 불용액

## 중앙정부>상세재정통계>결산>연기금투자풀 (4종)

### 연기금투자풀 기간수익률

- **서비스이름** `ConsignInvestPoolPeriod`
- 기관: 재정경제부 · 갱신: 분기
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `MMF_ERT` MMF 수익율, `MMF_OVR_ERT` MMF 초과 수익율, `CT_TY_ERT` 채권형 수익율, `CT_TY_OVR_ERT` 채권형 초과 수익율, `MIX_TY_ERT` 혼합형 수익율, `MIX_TY_OVR_ERT` 혼합형 초과 수익율, `STK_TY_ERT` 주식형 수익율, `STK_TY_OVR_ERT` 주식형 초과 수익율

### 연기금투자풀 기간수익률(분기별)

- **서비스이름** `ConsignInvestPoolPeriodQuarter`
- 기관: 재정경제부 · 갱신: 분기
- **검색인자**: `OJ_YY`(대상년도)
- 출력칸: `OJ_YY` 대상년도, `QUARTER` 분기, `MMF_ERT` MMF 수익율, `MMF_OVR_ERT` MMF 초과 수익율, `CT_TY_ERT` 채권형 수익율, `CT_TY_OVR_ERT` 채권형 초과 수익율, `MIX_TY_ERT` 혼합형 수익율, `MIX_TY_OVR_ERT` 혼합형 초과 수익율, `STK_TY_ERT` 주식형(국내) 수익율, `STK_TY_OVR_ERT` 주식형 초과(국내) 수익율, `ELF_ERT` 주식형(해외) 수익율, `ELF_OVR_ERT` 주식형 초과(해외) 수익율

### 연기금투자풀 수탁규모

- **서비스이름** `ConsignInvestPoolSize`
- 기관: 재정경제부 · 갱신: 분기
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `TOT_TRU_AMT` 총수탁고, `MMF_AMT` MMF 금액, `MMF_RT` MMF 비중, `CT_TY_AMT` 채권형 금액, `CT_TY_RT` 채권형 비율, `MIX_TY_AMT` 혼합형 금액, `MIX_TY_RT` 혼합형 비율, `STK_TY_AMT` 주식형 금액, `STK_TY_RT` 주식형 비율, `ELF_AMT` ELF 금액, `ELF_RT` ELF 비율

### 연기금투자풀 수탁규모(분기별)

- **서비스이름** `ConsignInvestPoolSizeQuarter`
- 기관: 재정경제부 · 갱신: 분기
- **검색인자**: `OJ_YY`(대상연도)
- 출력칸: `OJ_YY` 대상년도, `QUARTER` 분기, `TOT_TRU_AMT` 총수탁고, `MMF_AMT` MMF 금액, `CT_TY_AMT` 채권형 금액, `MIX_TY_AMT` 혼합형 금액, `STK_TY_AMT` 주식형(국내) 금액, `ELF_AMT` 주식형(해외) 금액

## 중앙정부>상세재정통계>결산>일시차입 (2종)

### 재정증권 발행 및 상환내역

- **서비스이름** `FinanSecuriIssuanAndRedemp`
- 기관: 재정경제부 · 갱신: 수시
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `PBL_RQ_DT` 발행요청일자, `TOT_PBL_AMT` 총발행금액, `PBL_IRT` 발행이율, `RPM_DT` 상환일자, `RL_RPM_DT` 상환일자, `TOT_RPM_PRN_AMT` 총상환금액, `RAMT` 잔액

### 한은 일시차입 차입 및 상환내역

- **서비스이름** `VW_OPFI316`
- 기관: 재정경제부 · 갱신: 수시
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `OFFC_NM` 소관명, `ACNT_NM` 회계명, `FOG_NM` 계정명, `RPM_TN_S` 상환차수, `BOR_DMND_YMD` 차입요청일자, `BOR_AMT` 충차입금액, `BOR_IRT` 차입이율, `RPM_CLM_YMD` 상환일자, `PRN_RPM_AMT` 총상환금액, `DL_RAMT` 잔액, `OFFC_CD` , `ACNT_CD` , `ACCT_CD` , `FGO_CD` 

## 중앙정부>상세재정통계>결산>재무제표(2025이전) (9종)

### 소관별 순자산변동표

- **서비스이름** `VW_FOAC006`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `STL_TACCT_NM` 구분, `BAS_NAST_AMT` 기본순자산금액, `RSAM_SURPL_AMT` 적립금잉여금액, `NAST_MEDI_AMT` 순자산조정금액, `SUM_AMT` 합계금액

### 소관별 재정상태표

- **서비스이름** `VW_FOAC004`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `OFFC_NM`(소관명)
- 출력칸: `OFFC_NM` 소관명, `STL_TACCT_NM` 결산계정과목명, `THISP_1_AMT` 당기1금액, `THISP_2_AMT` 당기2금액, `THISP_3_AMT` 당기3금액, `PRV_1_AMT` 전기1금액, `PRV_2_AMT` 전기2금액, `PRV_3_AMT` 전기3금액, `ORG_CD` 직제코드

### 소관별 재정운영표

- **서비스이름** `VW_FOAC005`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `DIV` 구분, `CUR_TOT_COST` 당년도총원가, `CUR_PROFIT` 당년도수익, `CUR_COST` 당년도순원가, `LAST_TOT_COST` 전년도총원가, `LAST_PROFIT` 전년도수익, `LAST_COST` 전년도순원가

### 순자산변동표

- **서비스이름** `VW_FOAC009`
- 기관: 재정경제부 · 갱신: 연간
- 출력칸: `STL_TACCT_NM` 구분, `BAS_NAST_AMT` 기본순자산금액, `RSAM_SRP_AMT` 적립금및잉여금액, `NAST_MEDI_AMT` 순자산조정금액, `SUM_AMT` 합계금액, `FRST_REG_SYS_USE_ID` 최초등록시스템사용ID

### 재정상태표

- **서비스이름** `VW_FOAC007`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `STL_TACCT_NM` 결산계정과목명, `THISP_1_AMT` 당기1금액, `THISP_2_AMT` 당기2금액, `THISP_3_AMT` 당기3금액, `PRV_1_AMT` 전기1금액, `PRV_2_AMT` 전기2금액, `PRV_3_AMT` 전기3금액

### 재정운영표

- **서비스이름** `VW_FOAC008`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `DIV` 구분, `THISP_1_AMT` 당기1금액, `THISP_2_AMT` 당기2금액, `PRV_1_AMT` 전기1금액, `PRV_2_AMT` 전기2금액

### 회계·기금별 순자산변동표

- **서비스이름** `VW_FOAC003`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `FSCL2_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `FSCL2_NM` 회계명, `DIV` 구분, `BAS_NAST_AMT` 기본순자산금액, `RSAM_SURPL_AMT` 적립금잉여금액, `NAST_MEDI_AMT` 순자산조정금액, `SUM_AMT` 합계금액

### 회계·기금별 재정상태표

- **서비스이름** `VW_FOAC001`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `FSCL2_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `FSCL2_NM` 회계명, `STL_TACCT_NM` 결산계정과목명, `THISP_1_AMT` 당기1금액, `THISP_2_AMT` 당기2금액, `THISP_3_AMT` 당기3금액, `PRV_1_AMT` 전기1금액, `PRV_2_AMT` 전기2금액, `PRV_3_AMT` 전기3금액, `PFIN_STATS_DATA_SEQ` 재정통계자료일련번호

### 회계·기금별 재정운영표

- **서비스이름** `VW_FOAC002`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `FSCL2_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `FSCL2_NM` 회계명, `DIV` 구분, `CUR_TOT_COST` 당년도총원가, `CUR_PROFIT` 당년도수익, `CUR_COST` 당년도순원가, `LAST_TOT_COST` 전년도총원가, `LAST_PROFIT` 전년도수익, `LAST_COST` 전년도순원가

## 중앙정부>상세재정통계>결산>재무제표(2025이후) (15종)

### 성질별재정운영표

- **서비스이름** `VW_FOAC034`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `STL_TACCT_NM` 결산계정과목명, `THISP_3_AMT` 당기3금액, `PRV_3_AMT` 전기3금액

### 소관별 성질별재정운영표

- **서비스이름** `VW_FOAC029`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `STL_TACCT_NM` 결산계정과목명, `THISP_3_AMT` 당기3금액, `PRV_3_AMT` 전기3금액

### 소관별 순자산변동표

- **서비스이름** `VW_FOAC028`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `STL_TACCT_NM` 구분, `BAS_NAST_AMT` 기본순자산금액, `RSAM_SURPL_AMT` 적립금잉여금액, `NAST_MEDI_AMT` 순자산조정금액, `SUM_AMT` 합계금액

### 소관별 재정상태표

- **서비스이름** `VW_FOAC026`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `STL_TACCT_NM` 결산계정과목명, `THISP_1_AMT` 당기1금액, `THISP_2_AMT` 당기2금액, `THISP_3_AMT` 당기3금액, `PRV_1_AMT` 전기1금액, `PRV_2_AMT` 전기2금액, `PRV_3_AMT` 전기3금액

### 소관별 재정운영표

- **서비스이름** `VW_FOAC027`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `DIV` 구분, `CUR_TOT_COST` 당년도총원가, `CUR_PROFIT` 당년도수익, `CUR_COST` 당년도순원가, `LAST_TOT_COST` 전년도총원가, `LAST_PROFIT` 전년도수익, `LAST_COST` 전년도순원가

### 소관별 현금흐름표

- **서비스이름** `VW_FOAC030`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `STL_TACCT_NM` 결산계정과목명, `THISP_1_AMT` 당기1금액, `PRV_1_AMT` 전기1금액

### 순자산변동표

- **서비스이름** `VW_FOAC033`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `STL_TACCT_NM` 구분, `BAS_NAST_AMT` 기본순자산금액, `RSAM_SRP_AMT` 적립금및잉여금액, `NAST_MEDI_AMT` 순자산조정금액, `SUM_AMT` 합계금액

### 재정상태표

- **서비스이름** `VW_FOAC031`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `STL_TACCT_NM` 결산계정과목명, `THISP_1_AMT` 당기1금액, `THISP_2_AMT` 당기2금액, `THISP_3_AMT` 당기3금액, `PRV_1_AMT` 전기1금액, `PRV_2_AMT` 전기2금액, `PRV_3_AMT` 전기3금액

### 재정운영표

- **서비스이름** `VW_FOAC032`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `DIV` 구분, `THISP_1_AMT` 당기1금액, `THISP_2_AMT` 당기2금액, `THISP_3_AMT` 당기3금액, `PRV_1_AMT` 전기1금액, `PRV_2_AMT` 전기2금액, `PRV_3_AMT` 전기3금액

### 현금흐름표

- **서비스이름** `VW_FOAC035`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `STL_TACCT_NM` 결산계정과목명, `THISP_1_AMT` 당기1금액, `PRV_1_AMT` 전기1금액

### 회계·기금별 성질별재정운영표

- **서비스이름** `VW_FOAC024`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `FSCL2_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `FSCL2_NM` 회계명, `STL_TACCT_NM` 결산계정과목명, `THISP_3_AMT` 당기3금액, `PRV_3_AMT` 전기3금액

### 회계·기금별 순자산변동표

- **서비스이름** `VW_FOAC023`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `FSCL2_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `FSCL2_NM` 회계명, `DIV` 구분, `BAS_NAST_AMT` 기본순자산금액, `RSAM_SURPL_AMT` 적립금잉여금액, `NAST_MEDI_AMT` 순자산조정금액, `SUM_AMT` 합계금액, `TPD_FHY_DIV_CD` 당기전기구분코드, `OTPT_ORD` 출력순서

### 회계·기금별 재정상태표

- **서비스이름** `VW_FOAC021`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `FSCL2_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `FSCL2_NM` 회계명, `STL_TACCT_NM` 결산계정과목명, `THISP_1_AMT` 당기1금액, `THISP_2_AMT` 당기2금액, `THISP_3_AMT` 당기3금액, `PRV_1_AMT` 전기1금액, `PRV_2_AMT` 전기2금액, `PRV_3_AMT` 전기3금액

### 회계·기금별 재정운영표

- **서비스이름** `VW_FOAC022`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `FSCL2_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `FSCL2_NM` 회계명, `DIV` 구분, `CUR_TOT_COST` 당년도총원가, `CUR_PROFIT` 당년도수익, `CUR_COST` 당년도순원가, `LAST_TOT_COST` 전년도총원가, `LAST_PROFIT` 전년도수익, `LAST_COST` 전년도순원가

### 회계·기금별 현금흐름표

- **서비스이름** `VW_FOAC025`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `FSCL2_NM`(회계명)
- 출력칸: `FSCL_YY` 회계연도, `FSCL2_NM` 회계명, `STL_TACCT_NM` 결산계정과목명, `THISP_1_AMT` 당기1금액, `PRV_1_AMT` 전기1금액

## 중앙정부>상세재정통계>결산>채권 (4종)

### 국가채권추이

- **서비스이름** `TB_OPFI124`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `OJ_YY`(대상연도)
- 출력칸: `OJ_YY` 대상연도, `NAT_CT_0_AMT` 국가채권 합계, `NAT_CT_1_AMT` 연체채권 합계, `NAT_CT_2_AMT` 조세 국가 채권, `NAT_CT_3_AMT` 조세 연체 채권, `NAT_CT_4_AMT` 경상이전수입 국가채권, `NAT_CT_5_AMT` 경상이전수입 연체채권, `NAT_CT_6_AMT` 융자회수금 국가채권, `NAT_CT_7_AMT` 융자회수금 연체채권, `NAT_CT_8_AMT` 예금및예탁금 국가채권, `NAT_CT_9_AMT` 예금및예탁금 연체채권, `NAT_CT_10_AMT` 기타 국가채권, `NAT_CT_11_AMT` 기타 연체채권

### 국가채권현황

- **서비스이름** `ReceivedGovernment`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `NAT_CT_TOT_AMT` 국가채권총액, `NAT_CT_1_AMT` 융자회수금, `NAT_CT_2_AMT` 예금및예탁금, `NAT_CT_3_AMT` 조세채권, `NAT_CT_4_AMT` 경상이전수입, `NAT_CT_5_AMT` 사회보장기여금, `NAT_CT_6_AMT` 기타채권

### 채권현재액명세서

- **서비스이름** `VW_FOCT002`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `CT_KND_NM` 채권종류명, `PYE_PSNTAMT` 전년도말현재액, `BLY_OC_WTAMT_PFDL_ARRVAMT` 전년도이전발생금액중이행기한도래액, `BLY_OC_WTAMT_PFDL_NARVAMT` 전년도이전발생금액중이행기한미도래액, `BLY_OC_SUM_AMT` 전년도이전발생합계금액, `THY_OC_WTAMT_PFDL_ARRVAMT` 본년도발생금액중이행기한도래액, `THY_OC_WTAMT_PFDL_NARVAMT` 본년도발생금액중이행기한미도래액, `THY_OC_SUM_AMT` 본년도발생합계금액, `PFDL_ARRV_SUM_AMT` 이행기한도래합계금액, `PFDL_NARV_SUM_AMT` 이행기한미도래합계금액, `TOTT_AMT` 총계금액

### 회계·기금별 국가채권 현황

- **서비스이름** `NRAccountingFund`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `NAT_CT_SUM_AMT` 국가채권 총액, `GEN_FSCL_AMT` 일반회계, `SPC_FSCL_AMT` 특별회계, `FND_AMT` 기금

## 중앙정부>상세재정통계>결산>출자 (2종)

### 정부출자기관 정부배당 현황

- **서비스이름** `GovernmentDividend`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `TRGT_YR`(대상연도), `IV_INST_NM`(출자기관명)
- 출력칸: `TRGT_YR` 기준년도, `IV_INST_NM` 기관명, `TPD_NTPFT_AMT` 당기순이익, `DVD_PPS_RT` 배당성향, `DVD_TREV_AMT` 배당세입

### 정부출자현황

- **서비스이름** `GovernmentInvestment`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `OJ_YY`(대상연도), `OJ_M`(대상월), `INST_DIV_NM`(공기업, 준정부기관,기타공공기관,공공기관외), `CGP_MAO_NM`(주무부처), `INST_NM`(기관명)
- 출력칸: `OJ_YY` 대상연도, `OJ_M` 대상월, `INST_DIV_NM` 기관구분, `CGP_MAO_NM` 주무부처, `INST_NM` 기관명, `AUTH_CAPT_AMT` 수권자본금, `RAID_CAPT_AMT` 납입자본금, `GVRN_IV_AMT` 정부출자 금액, `GVRN_IV_ORT` 정부출자 지분율

## 중앙정부>상세재정통계>국가채무 (4종)

### 공공부문 부채(D3)

- **서비스이름** `PublicDebtAndNationalDebt`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `PUB_LAT_AMT` 공공부문부채, `PUB_LAT_RT` 공공부문부채 GDP대비, `GVRNM_LAT_AMT` 일반정부부채, `GVRNM_LAT_RT` 일반정부부채 GDP대비, `PUBERP_LAT_AMT` 비금융공기업부채, `PUBERP_LAT_RT` 비금융공기업부채 GDP대비, `GVRNM_PUBERP_AMT` 일반정부-공기업간내부거래

### 국가채무(D1)

- **서비스이름** `GovernmentDebtYear`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `GOD_SUM_AMT` 국가채무총계, `GOD_GDP_CMPRT` 국가채무 GDP대비, `CENTRAL_DEPT_AMT` 중앙정부채무, `NLOAN_SUM_AMT` 국채 합계, `NLOAN_1_AMT` 국고채권, `NLOAN_2_AMT` 국민주택채권, `NLOAN_3_AMT` 외평채권, `ETC_AMT` 기타금액, `BOR_AMT` 차입금, `ND_AMT` 국고채무부담행위, `LOCAL_DEPT_AMT` 지방정부순채무

### 보증채무 현황

- **서비스이름** `SuretyLiabilityYear`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `GURDB_TOT_AMT` 보증채무 총액, `GURDB_GDP_CMPRT` 보증채무 GDP대비, `GURDB_1_AMT` 예보채상환기금채권, `GURDB_2_AMT` 장학재단채권, `GURDB_3_AMT` 구조조정기금채권, `GURDB_4_AMT` 수리자금, `GURDB_5_AMT` 국내은행 외화표시 채무

### 일반정부 부채(D2)

- **서비스이름** `OPFI197`
- 기관: 재정경제부 · 갱신: 연간
- **검색인자**: `TRGT_YR`(기준연도 ★필수)
- 출력칸: `TRGT_YR` 기준연도, `GEN_GVRN_LAT_AMT` 일반정부부채(D2, ① + ② + ③ - ④), `CENT_GVRN_DB_AMT` ① 중앙정부, `LAF_LAT_AMT` ② 지방자치단체, `DST_EDU_PFIN_ITG_LAT_AMT` ③ 교육자치단체, `ISR_LAT_AMT` ④ 내부거래

## 중앙정부>상세재정통계>예산>세입/수입 (4종)

### 세입 예산편성현황(추경포함)

- **서비스이름** `BudgetRevenuesAdd3`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `SBUDG_DGR`(추경차수 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `IKWAN_NM`(수입관명), `IHANG_NM`(수입항명), `IMOK_NM`(수입목명)
- 출력칸: `FSCL_YY` 회계연도, `SBUDG_DGR` 추경차수, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

### 예산편성현황(외화)

- **서비스이름** `ForeignRevenueIncomeBudget2`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `IKWAN_NM`(수입관명), `IHANG_NM`(수입항명), `IMOK_NM`(수입목명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `RV_DE_DIV_NM` 수입구분, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `Y_YY_MEDI_FRC_AMT` 정부안금액, `Y_YY_DFN_MEDI_FRC_AMT` 국회확정금액

### 예산편성현황(총수입)

- **서비스이름** `TotalRevenue2`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `IKWAN_NM`(수입관명), `IHANG_NM`(수입항명), `IMOK_NM`(수입목명), `REVN_INQ_STND_CD`(예산편성집계구분코드 ★필수), `BDG_FND_DIV_CD`(전체예산기금구분코드 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `RV_DE_DIV_NM` 수입구분명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### 예산편성현황(총액)

- **서비스이름** `BudgetRevenuesInit2`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `IKWAN_NM`(수입관명), `IHANG_NM`(수입항명), `IMOK_NM`(수입목명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `RV_DE_DIV_CD` 수입구분코드, `RV_DE_DIV_NM` 수입구분명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `IMOK_NM` 수입목명, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

## 중앙정부>상세재정통계>예산>세출/지출 (8종)

### 세목 예산편성현황(외화)

- **서비스이름** `ForeignExpenditureBudgget6`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(지출목명), `EITM_NM`(지출세목명), `BZ_CLS_NM`(사업분류명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `BZ_CLS_NM` 경비구분, `FIN_DE_EP_NM` 지출구분, `Y_YY_MEDI_FRC_AMT` 정부안금액, `Y_YY_DFN_MEDI_FRC_AMT` 국회확정금액

### 세목 예산편성현황(총액)

- **서비스이름** `ExpenditureBudgetInit6`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(지출목명), `EITM_NM`(지출세목명), `BZ_CLS_NM`(사업분류명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `BZ_CLS_NM` 경비구분, `FIN_DE_EP_NM` 지출구분, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### 세목 예산편성현황(총지출)

- **서비스이름** `TotalExpenditure6`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `BDG_FND_DIV_CD`(전체예산기금구분코드(0:전체, 1:예산, 5:기금) ★필수), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(지출목명), `EITM_NM`(지출세목명), `BZ_CLS_NM`(사업분류명), `ANEXP_INQ_STND_CD`(세출조회기준코드(1:총지출, 2:세출순계) ★필수)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `BZ_CLS_NM` 경비구분, `FIN_DE_EP_NM` 지출구분, `Y_PREY_FIRST_KCUR_AMT` 전년도국회확정금액, `Y_PREY_FNL_KCUR_AMT` 전년도최종금액, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### 세부사업 예산편성현황(외화)

- **서비스이름** `ForeignExpenditureBudgget5`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `BZ_CLS_NM`(사업분류명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `BZ_CLS_NM` 경비구분, `FIN_DE_EP_NM` 지출구분, `Y_YY_MEDI_FRC_AMT` 정부안금액, `Y_YY_DFN_MEDI_FRC_AMT` 국회확정금액

### 세부사업 예산편성현황(총액)

- **서비스이름** `ExpenditureBudgetInit5`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `BZ_CLS_NM`(사업분류명)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `BZ_CLS_NM` 경비구분, `FIN_DE_EP_NM` 지출구분, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### 세부사업 예산편성현황(총지출)

- **서비스이름** `TotalExpenditure5`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `BDG_FND_DIV_CD`(전체예산기금구분코드(0:전체, 1:예산, 5:기금) ★필수), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `BZ_CLS_NM`(사업분류명), `ANEXP_INQ_STND_CD`(세출조회기준코드(1:총지출, 2:세출순계) ★필수)
- 출력칸: `FSCL_YY` 회계연도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `BZ_CLS_NM` 경비구분, `FIN_DE_EP_NM` 지출구분, `ANEXP_INQ_STND_CD` 조회기준, `Y_PREY_FIRST_KCUR_AMT` 전년도국회확정금액, `Y_PREY_FNL_FRC_AMT` 전년도최종금액, `Y_YY_MEDI_KCUR_AMT` 정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정금액

### 세출 세목 예산편성현황(추경포함)

- **서비스이름** `ExpenditureBudgetAdd8`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `CITM_NM`(지출목명), `EITM_NM`(지출세목명), `BZ_CLS_NM`(사업분류명), `SBUDG_DGR`(추경차수 ★필수)
- 출력칸: `FSCL_YY` 회계년도, `SBUDG_DGR` 추경차수, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `CITM_NM` 목명, `EITM_NM` 세목명, `BZ_CLS_NM` 경비구분, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액, `FIN_DE_EP_NM` 지출구분

### 세출 세부사업 예산편성현황(추경포함)

- **서비스이름** `ExpenditureBudgetAdd7`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `BZ_CLS_NM`(사업분류명), `SBUDG_DGR`(추경차수 ★필수)
- 출력칸: `FSCL_YY` 회계연도, `SBUDG_DGR` 추경차수, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `BZ_CLS_NM` 경비구분, `FIN_DE_EP_NM` 지출구분, `Y_YY_DFN_KCUR_AMT` 본예산금액, `Y_YY_DFN_FRC_AMT` 본예산외화금액, `Y_YY_MEDI_KCUR_AMT` 추경정부안금액, `Y_YY_DFN_MEDI_KCUR_AMT` 추경국회확정금액

## 중앙정부>상세재정통계>예산>정부구매예산 (1종)

### 정부구매예산

- **서비스이름** `GovOrdBz1`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `OFFC_NM`(소관명), `FSCL_NM`(회계명), `ACCT_NM`(계정명), `FLD_NM`(분야명), `SECT_NM`(부문명), `PGM_NM`(프로그램명), `ACTV_NM`(단위사업명), `SACTV_NM`(세부사업명), `EITM_NM`(비용성격)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `FSCL_NM` 회계명, `ACCT_NM` 계정명, `FLD_NM` 분야명, `SECT_NM` 부문명, `PGM_NM` 프로그램명, `ACTV_NM` 단위사업명, `SACTV_NM` 세부사업명, `EITM_NM` 비용성격, `Y_YY_DFN_MEDI_KCUR_AMT` 국회확정액

## 중앙정부>상세재정통계>집행>수입 (3종)

### 월별 수입운용상황

- **서비스이름** `VWFORM2`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `EXE_M`(회계월), `OFFC_CD`(소관코드), `FSCL_CD`(회계코드)
- 출력칸: `FSCL_YY` 회계년도, `EXE_M` 회계월, `OFFC_CD` 소관, `OFFC_NM` 소관명, `FSCL_CD` 회계, `FSCL_NM` 회계명, `IKWAN_CD` 수입관, `IKWAN_NM` 수입관명, `IHANG_CD` 수입항, `IHANG_NM` 수입항명, `BDG_AMT` 예산액, `BDG_CAMT` 예산현액, `RC_AMT` 당월수납금액, `RC_AGGR_AMT` 누계수납금액, `RC_AGGR_NAMT` 수납누계순액

### 월별 수입징수상황

- **서비스이름** `VWFORM`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `FSCL_YY`(회계연도), `EXE_M`(회계월), `OFFC_CD`(소관코드), `FSCL_CD`(회계코드)
- 출력칸: `FSCL_YY` 회계년도, `EXE_M` 회계월, `OFFC_CD` 소관, `OFFC_NM` 소관명, `FSCL_CD` 회계, `FSCL_NM` 회계명, `IKWAN_CD` 수입관코드, `IKWAN_NM` 수입관명, `IHANG_CD` 수입항코드, `IHANG_NM` 수입항명, `IMOK_CD` 수입목코드, `IMOK_NM` 수입목명, `BDG_CAMT` 예산, `RC_AMT` 수납본월금액, `RC_AGGR_AMT` 수납누계금액

### 일별 수입운용상황

- **서비스이름** `VWFORD`
- 기관: 재정경제부 · 갱신: 일간
- **검색인자**: `FSCL_YY`(회계연도), `OFFC_CD`(소관코드 ★필수), `FSCL_CD`(회계코드), `ACCT_CD`(계정코드)
- 출력칸: `FSCL_YY` 회계년도, `EXE_M` 회계월, `OFFC_CD` 소관, `OFFC_NM` 소관명, `FSCL_CD` 회계, `FSCL_NM` 회계명, `ACCT_CD` 계정, `ACCT_NM` 계정명, `IKWAN_CD` 수입관, `IKWAN_NM` 수입관명, `IHANG_CD` 수입항, `IHANG_NM` 수입항명, `BDG_AMT` 예산금액, `BDG_CAMT` 예산현액, `LM_RC_AGGR_AMT` 전월수납누계금액, `TD_RC_AMT` 당일수납금액, `TM_RC_AGGR_AMT` 당월수납누계금액, `RC_AGGR_AMT` 수납누계금액

## 중앙정부>상세재정통계>집행>지출 (3종)

### 월별 지출운용상황

- **서비스이름** `VWFOEM2`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `EXE_M`(집행연월 ★필수), `OFFC_CD`(소관코드 ★필수), `FSCL_CD`(회계코드)
- 출력칸: `FSCL_YY` 회계년도, `EXE_M` 집행월, `OFFC_CD` 소관, `OFFC_NM` 소관명, `FSCL_CD` 회계, `FSCL_NM` 회계명, `FLD_CD` 분야코드, `FLD_NM` 분야명, `SECT_CD` 부문코드, `SECT_NM` 부문명, `PGM_CD` 프로그램코드, `PGM_NM` 프로그램명, `ACTV_CD` 단위사업코드, `ACTV_NM` 단위사업명, `SACTV_CD` 세부사업코드, `SACTV_NM` 세부사업명, `ANEXP_BDG_AMT` 예산액, `ANEXP_BDG_CAMT` 예산현액, `EP_AMT` 당월지출금액, `THISM_AGGR_EP_AMT` 누계지출금액, `THISM_AGGR_EP_NAMT` 누계지출순계금액

### 월별 지출집행상황

- **서비스이름** `VWFOEM`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `FSCL_YY`(회계연도), `EXE_M`(집행월), `OFFC_CD`(소관코드 ★필수), `FSCL_CD`(회계코드)
- 출력칸: `FSCL_YY` 회계년도, `EXE_M` 집행월, `OFFC_CD` 소관, `OFFC_NM` 소관명, `FSCL_CD` 회계, `FSCL_NM` 회계명, `FLD_CD` 분야코드, `FLD_NM` 분야명, `SECT_CD` 부문코드, `SECT_NM` 부문명, `PGM_CD` 프로그램코드, `PGM_NM` 프로그램명, `ACTV_CD` 단위사업코드, `ACTV_NM` 단위사업명, `ANEXP_BDG_CAMT` 예산, `EP_AMT` 당월집행액, `THISM_AGGR_EP_AMT` 누계집행액

### 일별 지출운용상황

- **서비스이름** `VWFOED`
- 기관: 재정경제부 · 갱신: 일간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `EXE_M`(집행연월 ★필수), `EXE_DATE`(집행일자), `OFFC_CD`(소관코드), `FSCL_CD`(회계코드)
- 출력칸: `FSCL_YY` 회계년도, `EXE_M` 집행월, `EXE_DATE` 집행일, `OFFC_CD` 소관, `OFFC_NM` 소관명, `FSCL_CD` 회계, `FSCL_NM` 회계명, `FLD_CD` 분야, `FLD_NM` 분야명, `SECT_CD` 부문, `SECT_NM` 부문명, `PGM_CD` 프로그램, `PGM_NM` 프로그램명, `ACTV_CD` 단위사업, `ACTV_NM` 단위사업명, `SACTV_CD` 세부사업, `SACTV_NM` 세부사업명, `ANEXP_BDGAMT` 세출예산액, `ANEXP_BDG_CAMT` 세출예산현액, `EP_AMT` 지출금액, `THISM_AGGR_EP_AMT` 연간누계지출금액, `THISM_AGGR_EP_NAMT` 당월누계지출순계금액

## 중앙정부>상세재정통계>집행>집행실적 (1종)

### 공공기관별 주요관리대상사업 집행실적

- **서비스이름** `VW_FOBM303`
- 기관: 기획예산처 · 갱신: 월간
- **검색인자**: `FSCL_YY`(회계연도 ★필수), `ACTV_NM`(단위사업명), `OG_NM`(공공기관명)
- 출력칸: `FSCL_YY` 회계연도, `OG_NM` 기관명, `ACTV_NM` 단위사업명, `PL4_AMT` 연간계획, `EXE_AMT_01` 1월집행금액, `EXE_AMT_02` 2월집행금액, `EXE_AMT_03` 3월집행금액, `EXE_AMT_04` 4월집행금액, `EXE_AMT_05` 5월집행금액, `EXE_AMT_06` 6월집행금액, `EXE_AMT_07` 7월집행금액, `EXE_AMT_08` 8월집행금액, `EXE_AMT_09` 9월집행금액, `EXE_AMT_10` 10월집행금액, `EXE_AMT_11` 11월집행금액, `EXE_AMT_12` 12월집행금액

## 중앙정부>상세재정통계>집행>총사업비 (1종)

### 총사업비현황

- **서비스이름** `TotalProjectCost`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `FSCL_YY`(회계년도 ★필수), `TBCOST_NM`(총사업비명), `TBCOST_BZ_TY_NM`(사업유형), `OFFC_NM`(소관명)
- 출력칸: `FSCL_YY` 회계년도, `OFFC_NM` 소관명, `TBCOST_BZ_TY_LCLS_NM` 사업유형대분류, `TBCOST_BZ_TY_MCLS_NM` 사업유형중분류, `TBCOST_BZ_TY_NM` 사업유형, `BIZ_SCAL_EPL` 사업규모설명, `TBCOST` 총사업비, `TBCOST_TOT_CSTR_COST` 공사비, `TBCOST_RPAR_COST` 보상비, `TBCOST_DGN_COST` 설계비, `TBCOST_SPVS_COST` 감리비, `TBCOST_FACIL_ACCES_COST` 시설부대비, `TBCOST_ETC_MG_COST` 기타관리금액

## 중앙정부>월간재정동향>수입 (4종)

### 국세수입

- **서비스이름** `IncomeTax`
- 기관: 기획예산처 · 갱신: 월간
- **검색인자**: `OJ_YY`(대상연도), `OJ_M`(대상월)
- 출력칸: `OJ_YY` 대상연도, `OJ_M` 대상월, `ISMOK_NM` 세목명, `BDG_AMT` 예산액, `RV_AMT` 수입금액, `RV_AGGR_AMT` 수입누계금액, `OUT_RT` 진도율, `LY_CPRN_UAMT` 전년동기대비증감, `LY_CPRN_VARIRT` 전년동기대비진도율

### 기금수입

- **서비스이름** `FundIncome`
- 기관: 기획예산처 · 갱신: 월간
- **검색인자**: `OJ_YY`(대상연도), `OJ_M`(대상월)
- 출력칸: `OJ_YY` 대상연도, `OJ_M` 대상월, `ISMOK_NM` 세목명, `BDG_AMT` 예산액, `RV_AMT` 수입금액, `RV_AGGR_AMT` 수입누계금액, `OUT_RT` 진도율, `LY_CPRN_UAMT` 전년동기대비증감, `LY_CPRN_VARIRT` 전년동기대비진도율

### 세외수입

- **서비스이름** `NontaxIncome`
- 기관: 기획예산처 · 갱신: 월간
- **검색인자**: `OJ_YY`(대상연도), `OJ_M`(대상월)
- 출력칸: `OJ_YY` 대상연도, `OJ_M` 대상월, `ISMOK_NM` 세목명, `BDG_AMT` 예산액, `RV_AMT` 수입금액, `RV_AGGR_AMT` 수입누계금액, `OUT_RT` 진도율, `LY_CPRN_UAMT` 전년동기대비증감, `LY_CPRN_VARIRT` 전년동기대비진도율

### 총수입

- **서비스이름** `TotalIncome`
- 기관: 기획예산처 · 갱신: 월간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `OJ_M` 기준월, `TOT_RV_AMT` 총수입금액, `NTAX_RV_SUM_AMT` 국세수입 합계, `NTAX_RV_1_AMT` 국세수입 일반회계, `NTAX_RV_2_AMT` 국세수입 특별회계, `TAX_EXPT_SUM_AMT` 세외수입 합계, `TAX_EXPT_1_AMT` 세외수입 일반회계, `TAX_EXPT_2_AMT` 세외수입 특별회계, `FND_RV_SUM_AMT` 기금수입 합계, `RAEE_AMT` 세입세출 외

## 중앙정부>월간재정동향>수지 (1종)

### 재정수지

- **서비스이름** `BudgetBalance`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `OJ_M` 기준월, `TOT_RV_SUM_AMT` 총수입 합계, `TOT_RV_1_AMT` 사회보장성기금 수입, `TOT_EP_SUM_AMT` 총지출 합계, `TOT_EP_1_AMT` 사회보장성기금 지출, `ITG_PFIN_RAD_AMT` 통합재정수지, `SGU_CLAS_FND_RAD_AMT` 사회보장성기금 수지, `MG_PFIN_RAD_AMT` 관리재정수지

## 중앙정부>월간재정동향>지출 (1종)

### 총지출

- **서비스이름** `GrossExpend`
- 기관: 기획예산처 · 갱신: 월간
- **검색인자**: `OJ_YY`(기준년도)
- 출력칸: `OJ_YY` 기준년도, `OJ_M` 기준월, `TOT_EP_AMT` 총지출, `TOTEP_PGR` 총지출진도율, `BDG_EP_SUM_AMT` 예산 합계, `BDG_EP_1_AMT` 예산 일반회계, `BDG_EP_2_AMT` 예산 특별회계, `FND_EP_AMT` 기금, `RAEE_EP_AMT` 세입세출 외

## 중앙정부>월간재정동향>채무 (2종)

### 월별 국가채무(중앙정부)

- **서비스이름** `GovernmentDebtMonth`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `OJ_YY`(기준년도), `OJ_M`(기준월)
- 출력칸: `OJ_YY` 기준년도, `OJ_M` 기준월, `GOD_SUM_AMT` 국가채무총계, `NLOAN_SUM_AMT` 국채 합계, `NLOAN_1_AMT` 국고채권, `NLOAN_2_AMT` 국민주택채권, `NLOAN_3_AMT` 외평채권, `BOR_AMT` 차입금, `ND_AMT` 국고채무부담행위

### 월별 보증채무 현황

- **서비스이름** `SuretyLiabilityMonth`
- 기관: 재정경제부 · 갱신: 월간
- **검색인자**: `OJ_YY`(기준년도), `OJ_M`(기준월)
- 출력칸: `OJ_YY` 기준년도, `OJ_M` 기준월, `GURDB_TOT_AMT` 보증채무 총액, `GURDB_1_AMT` 예보채상환기금채권, `GURDB_2_AMT` 장학재단채권, `GURDB_3_AMT` 구조조정기금채권, `GURDB_4_AMT` 수리자금, `GURDB_5_AMT` 국내은행 외화표시 채무

## 중앙정부>재정보고서>국가재정운용계획 (5종)

### 분야별 재원배분 계획

- **서비스이름** `OPFB129`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `TMF_NM` 분야, `THY_PLAN_AMT` 당년 계획, `THY_PLAN_AMT_REIM` 비중, `THY_AF_Y1_PLAN_AMT` YYYY + 1 계획, `THY_REIM1` YYYY + 1 비중, `THY_AF_Y2_PLAN_AMT` YYYY + 2 계획, `THY_REIM2` YYYY + 2 비중, `THY_AF_Y3_PLAN_AMT` YYYY + 3 계획, `THY_REIM3` YYYY + 3 비중, `THY_AF_Y4_PLAN_AMT` YYYY + 4 계획, `THY_REIM4` YYYY + 4 비중, `YRAVG_VTR` 연평균증가율

### 조세부담률 및 국민부담률

- **서비스이름** `OPFB133`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `TBR_THY_AF_Y0` 당년도 조세부담률, `TBR_THY_AF_Y1` YYYY + 1 조세부담률, `TBR_THY_AF_Y2` YYYY + 2 조세부담률, `TBR_THY_AF_Y3` YYYY + 3 조세부담률, `TBR_THY_AF_Y4` YYYY + 4 조세부담률, `CTZ_BDRT_THY_AF_Y0` 당년도 국민부담률, `CTZ_BDRT_THY_AF_Y1` YYYY + 1 국민부담률, `CTZ_BDRT_THY_AF_Y2` YYYY + 2 국민부담률, `CTZ_BDRT_THY_AF_Y3` YYYY + 3 국민부담률, `CTZ_BDRT_THY_AF_Y4` YYYY + 4 국민부담률

### 중기 재정수입 전망

- **서비스이름** `OPFB130`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DIV_ATC_NM` 구분, `TSBDG_AMT` 본예산, `RVP_AMT` 추경, `THY_AF_Y1_PLAN` YYYY + 1 계획, `THY_AF_Y2_PLAN` YYYY + 2 계획, `THY_AF_Y3_PLAN` YYYY + 3 계획, `THY_AF_Y4_PLAN` YYYY + 4 계획, `YRAVG_VTR` 연평균증가율

### 중기 재정수지 전망

- **서비스이름** `OPFB141`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DIV_ATC_NM` 구분, `TSBDG_AMT` 본예산, `RVP_AMT` 추경, `THY_AF_Y1_PLAN` YYYY +  1 계획, `THY_AF_Y2_PLAN` YYYY +  2 계획, `THY_AF_Y3_PLAN` YYYY +  3 계획, `THY_AF_Y4_PLAN` YYYY +  4 계획

### 중기 재정지출 계획

- **서비스이름** `OPFB140`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DIV_ATC_NM` 구분, `TSBDG_AMT` 본예산, `RVP_AMT` 추경, `THY_AF_Y1_PLAN` YYYY + 1 계획, `THY_AF_Y2_PLAN` YYYY + 2 계획, `THY_AF_Y3_PLAN` YYYY + 3 계획, `THY_AF_Y4_PLAN` YYYY + 4 계획, `YRAVG_VTR` 연평균증가율

## 중앙정부>주요재정통계>기금별운용현황 (3종)

### 기금 자산운용 현황

- **서비스이름** `TB_OPFI192`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `OJ_YY`(대상년도)
- 출력칸: `OJ_YY` 대상년도, `FND_NM` 기금명, `ALL_AMT` 전체, `FND_ERT` 수익률

### 기금별 자산배분비중 현황

- **서비스이름** `TB_OPFI193`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `OJ_YY`(대상연도)
- 출력칸: `OJ_YY` 대상연도, `FND_NM` 기금명, `STM_AST_CASH_FT_RT` 현금성자금(단기), `STM_AST_LQD_FT_RT` 유동성자금(단기), `MLTM_AST_DFN_ITRT_RT` 확정금리형(중장기), `MLTM_AST_DMST_CT_RT` 국내채권형(중장기), `MLTM_AST_DMST_MIX_RT` 국내혼합형(중장기), `MLTM_AST_DMST_STK_RT` 국내주식형(중장기), `MLTM_AST_ETC_RT` 기타(중장기), `ALL_AST_STM_AST_RT` 단기자산(전체), `ALL_AST_MLTM_AST_RT` 중장기자산(전체)

### 기금별 투자풀 예치비중

- **서비스이름** `TB_OPFI194`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `OJ_YY`(대상년도)
- 출력칸: `OJ_YY` 대상년도, `FND_NM` 기금명, `ALL_ABLN_AMT` 전체평잔, `FNDP_ABLN_AMT` 투자풀평잔, `DPST_RT` 비중

## 중앙정부>주요재정통계>분야별 프로그램 (1종)

### 분야별 프로그램 예산

- **서비스이름** `OPFI172`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BDG_STL_DIV_NM` 예결산구분명, `FLD_CD` 분야코드, `FLD_NM` 분야명, `FLD_AMT` 지출순액, `SECT_CNT` 부문건수, `PGM_CNT` 프로그램건수, `ACTV_CNT` 단위사업건수, `SAY_CNT` 세부사업건수

## 중앙정부>주요재정통계>세계잉여금 (1종)

### 연도별총세입·총세출예산및결산

- **서비스이름** `OPFI140`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `ACNT_DIV_NM` 회계구분, `SUM_NASS_ANE_BDG_AMT` 본예산, `SUM_NASS_LAST_ANE_BDG_AMT` 최종세출예산 (A), `SUM_RCVMT_AMT` 징수액 (B), `SUM_TREV_OVR_AMT` 세입초과 (B-A), `SUM_EP_PLAN_CAMT` 예산현액 (C), `SUM_EP_AMT` 집행액 (D), `SUM_EXE_RT` 집행률 (D/C), `SUM_STL_SRP_AMT` 결산상잉여금 (B-D), `SUM_BFW_AMT` 이월액 (E), `SUM_RAES_SRP_AMT` 세계잉여금 (B-D-E), `SUM_DUSE_AMT` 불용액 (C-D-E)

## 중앙정부>주요재정통계>재정건전성>국가채무(D1) (1종)

### 성질별국가채무추이

- **서비스이름** `OPFI152`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `NAT_DB_AMT` 국가채무 (A+B), `LSS_DB_AMT` 적자성채무 (A), `GEN_ACNT_LSS_PSV_DB_AMT` 일반회계적자보전, `PFD_NBL_SW_DB_AMT` 공적자금국채전환등, `FNC_DB_AMT` 금융성채무(B), `FREX_MKT_SAFE_USWY_DB_AMT` 외환시장안전용, `HBT_SAFE_USWY_DB_AMT` 서민주거안전용등

## 중앙정부>주요재정통계>재정건전성>일반정부부채(D2),공공부문부채(D3) (3종)

### 부문별부채추이

- **서비스이름** `VW_OPFI153`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `CENT_GVRN_LAT_AMT` 중앙정부(A), `DST_GVRN_LAT_AMT` 지방정부(B), `GEN_GVRN_ISR_AMT` 중앙-지방 정부간 내부거래(C), `GEN_GVRN_LAT_AMT` 일반정부부채(D2=A+B-C), `CENT_GVRN_NFP_LAT_AMT` 중앙공기업(E), `DST_GVRN_NFP_LAT_AMT` 지방공기업(F), `NFP_ISR_AMT` 공기업간 내부거래(G), `NFP_LAT_AMT` 비금융 공기업 계(H=E+F-G), `GEN_GVRN_PBCO_ISR_AMT` 일반정부 비금융공기업간 내부거래(I), `PUB_SECT_LAT_AMT` 공공부문부채 계 (D3=D2+H-I), `GDP_AMT` GDP금액

### 비금융공기업부채추이

- **서비스이름** `VW_OPFI155`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `NFP_LAT_AMT` 비금융공기업부채 계, `NFP_CT_LAT_AMT` 비금융공기업부채 - 채권, `NFP_BOR_LAT_AMT` 비금융공기업부채 - 차입, `NFP_ETC_LAT_AMT` 비금융공기업부채 - 기타, `CENT_GVRN_NFP_LAT_AMT` 중앙공기업부채 계, `CENT_GVRN_NFP_CT_LAT_AMT` 중앙공기업부채 - 채권, `CENT_GVRN_NFP_BOR_LAT_AMT` 중앙공기업부채 - 차입, `CENT_GVRN_NFP_ETC_LAT_AMT` 중앙공기업부채 - 기타, `DST_GVRN_NFP_LAT_AMT` 지방공기업부채 계, `DST_GVRN_NFP_CT_LAT_AMT` 지방공기업부채 - 채권, `DST_GVRN_NFP_BOR_LAT_AMT` 지방공기업부채 - 차입, `DST_GVRN_NFP_ETC_LAT_AMT` 지방공기업부채 - 기타, `ISR_LAT_AMT` 내부거래 계, `ISR_CT_LAT_AMT` 내부거래 - 채권, `ISR_BOR_LAT_AMT` 내부거래 - 차입, `ISR_ETC_LAT_AMT` 내부거래 - 기타

### 지방정부부채추이

- **서비스이름** `VW_OPFI169`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DST_GVRN_LAT_AMT` 지방정부부채(계), `DST_GVRN_CT_LAT_AMT` 지방정부부채 - 채권, `DST_GVRN_BOR_LAT_AMT` 지방정부부채 - 차입, `DST_GVRN_ETC_LAT_AMT` 지방정부부채 - 기타, `LAF_LAT_AMT` 지방자치단체부채(계), `LAF_CT_LAT_AMT` 지방자치단체부채 - 채권, `LAF_BOR_LAT_AMT` 지방자치단체부채 - 차입, `LAF_ETC_LAT_AMT` 지방자치단체부채 - 기타, `EDU_PFIN_LAT_AMT` 교육재정부채(계), `EDU_PFIN_CT_LAT_AMT` 교육재정부채 - 채권, `EDU_PFIN_BOR_LAT_AMT` 교육재정부채 - 차입, `EDU_PFIN_ETC_LAT_AMT` 교육재정부채 - 기타, `NPF_PUB_INST_LAT_AMT` 비영리공공기관부채(계), `NPF_PUB_INST_CT_LAT_AMT` 비영리공공기관부채 - 채권, `NPF_PUB_INST_BOR_LAT_AMT` 비영리공공기관부채 - 차입, `NPF_PUB_INST_ETC_LAT_AMT` 비영리공공기관부채 - 기타, `ISR_LAT_AMT` 내부거래부채(계), `ISR_CT_LAT_AMT` 내부거래부채 - 채권, `ISR_BOR_LAT_AMT` 내부거래부채 - 차입, `ISR_ETC_LAT_AMT` 내부거래부채 - 기타

## 중앙정부>주요재정통계>재정건전성>재정수지 (2종)

### 작성기준별주요재정통계(중앙정부기준)

- **서비스이름** `OPFI150`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `ITG_PFIN_CRTR_RV_AMT` 통합재정기준수입금액, `ITG_PFIN_CRTR_EP_AMT` 통합재정기준지출금액, `TOTEP_CRTR_RV_AMT` 총지출기준수입금액, `TOTEP_CRTR_EP_AMT` 총지출기준지출금액, `SGU_FND_RAD_AMT` 사회보장기금수지금액, `PFD_RPM_AMT` 공적자금상환금액, `ITG_PFIN_RAD_AMT` 통합재정수지금액, `MNG_PFIN_RAD_AMT` 관리재정수지금액, `GDP_AMT` GDP금액

### 통합재정기준중앙정부규모

- **서비스이름** `VW_OPFI381`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ALY_YR`(회계연도)
- 출력칸: `ALY_YR` 회계연도, `ALY_YR_NM` 회계연도명, `GDP_CPRN_ITG_PFIN_EP_AMT_RT` GDP대비통합재정지출금액비율, `GDP_CPRN_ITG_PFIN_RAD_RT` GDP대비통합재정수지비율, `GDP_CPRN_MNG_PFIN_RAD_RT` GDP대비관리재정수지비율

## 중앙정부>주요재정통계>재정수입>국세수입 (2종)

### 국세수입추이

- **서비스이름** `OPFI157`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BC_DIV_NM` 예산결산구분명, `ACNT_DIV_NM` 회계구분명, `IKWAN_NM` 수입관명, `IHANG_NM` 수입항명, `SUM_RCVMT_AMT` 국세수입금액

### 조세부담률및국민부담률추이

- **서비스이름** `OPFI141`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BC_DIV_NM` 예산결산구분명, `CTZ_SHAM_CLS_NM` 국민부담분류명, `CTZ_SHAM_DIV_NM` 국민부담구분명, `SUM_CTZ_SHAM_AMT` 국민부담금

## 중앙정부>주요재정통계>재정수입>세외수입 (2종)

### 기금수입추이

- **서비스이름** `OPFI159`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `BC_DIV_NM` 예산결산구분명, `IKWAN_CD` 수입관코드, `IKWAN_NM` 수입관명, `SUM_RCVMT_AMT` 기금수입금액

### 일반·특별회계세외수입추이

- **서비스이름** `OPFI158`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BC_DIV_NM` 예산결산구분명, `ACNT_DIV_NM` 회계구분명, `IKWAN_CD` 수입관코드, `IKWAN_NM` 수입관명, `SUM_RCVMT_AMT` 세외수입금액

## 중앙정부>주요재정통계>재정수입>총수입 (1종)

### 재정수입구조(본예산총수입기준)

- **서비스이름** `OPFI156`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BDG_FND_DIV_NM` 예산기금구분명, `ACNT_DIV_NM` 회계구분명, `SMOK_DIV_NM` 세목분류명, `SUM_NASS_TREV_BDG_AMT` 총수입

## 중앙정부>주요재정통계>재정지출>분야별 (2종)

### 12대분야별(총지출기준)

- **서비스이름** `TB_OPFI155`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `TRGT_YR`(대상연도)
- 출력칸: `TRGT_YR` 대상연도, `DIV_NM` 구분명, `HLT_WEL_LBO_FLD_AMT` 1. 보건·복지·고용, `EDU_FLD_AMT` 2. 교육, `CTU_PHE_SSG_FLD_AMT` 3. 문화·체육·관광, `ENV_FLD_AMT` 4. 환경, `RND_FLD_AMT` 5. R&D, `IDS_SNC_EN_FLD_AMT` 6. 산업·중소·에너지, `SOC_FLD_AMT` 7. SOC, `GF_FLD_AMT` 8. 농림·수산·식품, `NDF_FLD_AMT` 9. 국방, `CPRT_FLD_AMT` 10. 외교·통일, `PUB_SAFE_FLD_AMT` 11. 공공질서·안전, `GEN_PUB_PADM_FLD_AMT` 12. 일반·지방행정, `SUM_AMT` 총지출

### 16대분야별재원배분(총지출기준)

- **서비스이름** `OPFI165`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DIV_NM` 구분명, `FLD_CD` 분야코드, `FLD_NM` 분야명, `SUM_AMT` 합계금액

## 중앙정부>주요재정통계>재정지출>성질별 (1종)

### 성질별지출추이

- **서비스이름** `OPFI123`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `EPMOK_QLT_CD` 지출목성질코드, `EPMOK_QLT_CD_NM` 지출성질목명, `EPMOK_CD` 지출목코드, `EPMOK_NM` 지출목명, `SUM_EP_AMT` 지출금액

## 중앙정부>주요재정통계>재정지출>소관별 (1종)

### 중앙관서별총지출추이

- **서비스이름** `OPFI166`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `OFFC_NM` 소관명, `SUM_EP_AMT` 지출금액

## 중앙정부>주요재정통계>재정지출>예산의집행(총지출기준) (10종)

### 분야별불용추이

- **서비스이름** `OPFI119`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `FLD_NM` 분야명, `SUM_DUSE_AMT` 불용금액

### 분야별이월추이

- **서비스이름** `OPFI118`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `FLD_NM` 분야명, `SUM_NYR_BFW_AMT` 이월금액

### 분야별집행추이

- **서비스이름** `OPFI117`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `FLD_NM` 분야명, `SUM_BDG_CAMT` 예산현액, `SUM_EXE_AMT` 집행금액

### 불용성질별추이

- **서비스이름** `OPFI122`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `EPMOK_QLT_CD` 지출목성질코드, `EPMOK_QLT_CD_NM` 지출성질목명, `EPMOK_CD` 지출목코드, `EPMOK_NM` 지출목명, `SUM_DUSE_AMT` 불용금액

### 성질별집행추이

- **서비스이름** `OPFI120`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `EPMOK_QLT_CD_NM` 지출성질목명, `EPMOK_NM` 지출목명, `SUM_EP_PLAN_CAMT` 예산합계현액, `SUM_EP_AMT` 집행합계금액

### 이월의성질별추이

- **서비스이름** `OPFI121`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `EPMOK_QLT_CD_NM` 지출성질목명, `EPMOK_NM` 지출목명, `SUM_NYR_BFW_AMT` 이월금액

### 총지출기준집행추이

- **서비스이름** `OPFI113`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `SUM_EP_PLAN_CAMT` 예산합계현액, `SUM_EP_AMT` 지출금액, `SUM_NYR_BFW_AMT` 이월금액, `SUM_DUSE_AMT` 불용금액

### 회계·기금별불용추이

- **서비스이름** `OPFI116`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `BDG_FND_DIV_NM` 예산기금구분명, `ACNT_DIV_NM` 회계구분명, `ACNT_FND_DIV_CD_NM` 회계기금분류명, `SUM_DUSE_AMT` 불용금액

### 회계·기금별이월추이

- **서비스이름** `OPFI115`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `BDG_FND_DIV_NM` 예산기금구분명, `ACNT_DIV_NM` 회계구분명, `ACNT_FND_DIV_CD_NM` 회계기금분류명, `SUM_NYR_BFW_AMT` 이월금액

### 회계·기금별집행추이

- **서비스이름** `OPFI114`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BDG_FND_DIV_NM` 예산기금구분명, `ACNT_FND_DIV_CD_NM` 회계기금분류명, `SUM_EP_PLAN_CAMT` 예산현액, `SUM_EP_AMT` 지출금액

## 중앙정부>주요재정통계>재정지출>유형별 (11종)

### 국고보조사업지출추이

- **서비스이름** `OPFI131`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `EPMOK_NM` 지출목명, `EP_SMOK_NM` 지출세목명, `SUM_EP_AMT` 지출금액

### 기본경비추이

- **서비스이름** `OPFI125`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `EPMOK_QLT_CD_NM` 지출성질목명, `SUM_EP_AMT` 지출금액

### 본예산기준인건비,경비,사업비추이

- **서비스이름** `OPFI126`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BDG_FND_DIV_NM` 예산기금구분명, `BIZ_CLS_NM` 사업분류명, `SUM_NASS_ANE_BDG_AMT` 국회세출예산금액

### 분야별국고보조사업지출추이

- **서비스이름** `OPFI132`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `FLD_NM` 분야명, `SUM_EP_AMT` 지출금액

### 분야별융자지출추이

- **서비스이름** `OPFI129`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `FLD_NM` 분야명, `SUM_EP_AMT` 지출금액

### 분야별이차보전지출추이

- **서비스이름** `OPFI130`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `FLD_NM` 분야명, `SUM_EP_AMT` 지출금액

### 분야별출연금지출추이

- **서비스이름** `OPFI134`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `FLD_NM` 분야명, `SUM_EP_AMT` 지출금액

### 분야별출자금추이

- **서비스이름** `OPFI128`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `FLD_NM` 분야명, `SUM_EP_AMT` 지출금액

### 인건비편성사업지출추이

- **서비스이름** `OPFI124`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `BDG_FND_DIV_NM` 예산기금구분명, `ACNT_DIV_NM` 회계구분명, `SUM_EP_AMT` 지출금액

### 자본지출현황

- **서비스이름** `OPFI127`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `EPMOK_QLT_CD_NM` 지출성질목명, `EPMOK_NM` 지출목명, `SUM_EP_AMT` 지출금액

### 출연금지출추이

- **서비스이름** `OPFI133`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `EPMOK_NM` 지출목명, `EP_SMOK_NM` 지출세목명, `SUM_EP_AMT` 지출금액

## 중앙정부>주요재정통계>재정지출>의무·재량별 (1종)

### 의무·재량지출규모추이

- **서비스이름** `TB_OPFI142`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BC_DIV_CD_NM` 예산결산구분, `BDG_EP_DIV_NM` 구분, `FLD_NM` 분야, `EP_AMT` 지출금액

## 중앙정부>주요재정통계>재정지출>총지출 (2종)

### 재정지출추이(본예산총지출기준)

- **서비스이름** `OPFI171`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BDG_STL_DIV_NM` 예결산구분명, `ACNT_DIV_NM` 회계구분명, `EP_AMT` 지출금액

### 재정지출추이(총계기준)

- **서비스이름** `OPFI160`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BC_DIV_NM` 예산결산구분명, `BDG_FND_DIV_NM` 예산기금구분명, `ACNT_DIV_NM` 회계구분명, `SUM_EP_NAMT_AMT` 지출순금액

## 중앙정부>주요재정통계>재정지출>회계·기금별 (4종)

### 기금성격별운용규모(총지출기준)

- **서비스이름** `OPFI162`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DIV_NM` 구분명, `FND_CLAS_CD_NM` 기금성격명, `SUM_AMT` 합계금액

### 기금운용구분별운용규모(총지출기준)

- **서비스이름** `OPFI164`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DIV_NM` 구분명, `FND_OP_DIV_CD` 기금운용구분코드, `FND_OP_DIV_CD_NM` 기금운용구분명, `AMT` 합계금액

### 사업성기금운용규모(총지출기준)

- **서비스이름** `OPFI163`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DIV_NM` 구분명, `ACNT_NM` 회계명, `AMT` 합계금액

### 특별회계별재정지출추이(총지출기준)

- **서비스이름** `OPFI161`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `BC_DIV_NM` 예산결산구분명, `ACNT_DIV_NM` 회계구분명, `ACNT_NM` 회계명, `SUM_NASS_ANE_BDG_AMT` 국회세출예산금액

## 중앙정부>주요재정통계>지방재정조정 (3종)

### 연도별교육재정교부금추이

- **서비스이름** `OPFI170`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DIV_NM` 구분명, `ACNT_FND_DIV_CD_NM` 회계기금분류명, `ACTV_NM` 단위사업명, `SAY_NM` 세부사업명, `SUM_AMT` 합계금액

### 연도별지방교부세추이

- **서비스이름** `OPFI168`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `DIV_NM` 구분명, `ACTV_NM` 단위사업명, `SAY_NM` 세부사업명, `SUM_AMT` 합계금액

### 자치단체국고보조사업추이

- **서비스이름** `OPFI167`
- 기관: 한국재정정보원 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `ACNT_YR` 회계연도, `STL_BDG_DIV_NM` 결산예산구분명, `SUM_EP_AMT` 지출금액, `SUM_GEN_EP_AMT` 일반회계지출금액, `GEN_ACNT_RT` 일반회계비중, `SUM_SPC_ACNT_AMT` 특별회계금액, `SPC_ACNT_SUM_RT` 특별회계합계비중, `SUM_NAT_EXCL_SPC_ACNT_AMT` 국가균형발전제외특별회계금액, `NAT_EXCL_SPC_ACNT_RT` 국가균형발전제외특별회계비중, `SUM_NAT_BLNC_DVLP_AMT` 국가균형발전특별회계금액, `NAT_BLNC_DVLP_RT` 국가균형발전특별회계비중, `SUM_FND_AMT` 기금금액, `FND_RT` 기금비중

## 중앙정부>통합재정통계>01 GFS (6종)

### 거래명세(01GFS)

- **서비스이름** `OPFI215`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `HNM` 구분, `AMT1` 중앙재정, `AMT2` 지방재정, `AMT3` 지방교육재정, `AMT4` 내부거래, `AMT5` 합계, `AMT6` 내부거래, `AMT7` 일반정부

### 거래외명세(01GFS)

- **서비스이름** `OPFI216`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `HNM` 구분, `AMT1` 중앙재정, `AMT2` 지방재정, `AMT3` 지방교육재정, `AMT4` 내부거래, `AMT5` 합계, `AMT6` 내부거래, `AMT7` 일반정부

### 비용명세(01GFS)

- **서비스이름** `OPFI214`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `HNM` 구분, `AMT1` 중앙재정, `AMT2` 지방재정, `AMT3` 지방교육재정, `AMT4` 내부거래, `AMT5` 합계, `AMT6` 내부거래, `AMT7` 일반정부

### 수익명세(01GFS)

- **서비스이름** `OPFI213`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `HNM` 구분, `AMT1` 중앙재정, `AMT2` 지방재정, `AMT3` 지방교육재정, `AMT4` 내부거래, `AMT5` 합계, `AMT6` 내부거래, `AMT7` 일반정부

### 재정상태표(01GFS)

- **서비스이름** `OPFI217`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `HNM` 구분, `AMT1` 중앙재정, `AMT2` 지방재정, `AMT3` 지방교육재정, `AMT4` 내부거래, `AMT5` 합계, `AMT6` 내부거래, `AMT7` 일반정부

### 정부운영표(01GFS)

- **서비스이름** `OPFI212`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `HNM` 구분, `AMT1` 중앙재정, `AMT2` 지방재정, `AMT3` 지방교육재정, `AMT4` 내부거래, `AMT5` 합계, `AMT6` 내부거래, `AMT7` 일반정부

## 중앙정부>통합재정통계>86 GFS (7종)

### 내부거래(86GFS결산)

- **서비스이름** `OPFI211`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `SA_RET_ATC_HG_NM` 구분, `GEN_ACNT_SUM_AMT` 일반회계, `ETC_SPC_ACNT_SUM_AMT` 기타특별회계, `TREV_ANEET_AMT` 세입세출외, `NFN_FND_SUM_AMT` 기금, `ERP_SPC_ACNT_SUM_AMT` 기업특별회계, `CENT_GVRN_NFN_ACV_SUM_AMT` 합계

### 보전재원(86GFS결산)

- **서비스이름** `OPFI210`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `SA_RET_ATC_HG_NM` 구분, `GEN_ACNT_SUM_AMT` 일반회계, `ETC_SPC_ACNT_SUM_AMT` 기타특별회계, `TREV_ANEET_AMT` 세입세출외, `NFN_FND_SUM_AMT` 기금, `ERP_SPC_ACNT_SUM_AMT` 기업특별회계, `CENT_GVRN_NFN_ACV_SUM_AMT` 합계

### 수입의경제적분류(86GFS결산)

- **서비스이름** `OPFI206`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `SA_RET_ATC_HG_NM` 구분, `GEN_ACNT_SUM_AMT` 일반회계, `ETC_SPC_ACNT_SUM_AMT` 기타특별회계, `TREV_ANEET_AMT` 세입세출외, `NFN_FND_SUM_AMT` 기금, `ERP_SPC_ACNT_SUM_AMT` 기업특별회계, `CENT_GVRN_NFN_ACV_SUM_AMT` 합계

### 순융자(86GFS결산)

- **서비스이름** `OPFI209`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `SA_RET_ATC_HG_NM` 구분, `GEN_ACNT_SUM_AMT` 일반회계, `ETC_SPC_ACNT_SUM_AMT` 기타특별회계, `TREV_ANEET_AMT` 세입세출외, `NFN_FND_SUM_AMT` 기금, `ERP_SPC_ACNT_SUM_AMT` 기업특별회계, `CENT_GVRN_NFN_ACV_SUM_AMT` 합계

### 지출및순융자의경제적분류(86GFS결산)

- **서비스이름** `OPFI207`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `SA_RET_ATC_HG_NM` 구분, `GEN_ACNT_SUM_AMT` 일반회계, `ETC_SPC_ACNT_SUM_AMT` 기타특별회계, `TREV_ANEET_AMT` 세입세출외, `NFN_FND_SUM_AMT` 기금, `ERP_SPC_ACNT_SUM_AMT` 기업특별회계, `CENT_GVRN_NFN_ACV_SUM_AMT` 합계

### 지출및순융자의기능적분류(86GFS결산)

- **서비스이름** `OPFI208`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `SA_RET_ATC_HG_NM` 구분, `GEN_ACNT_SUM_AMT` 일반회계, `ETC_SPC_ACNT_SUM_AMT` 기타특별회계, `TREV_ANEET_AMT` 세입세출외, `NFN_FND_SUM_AMT` 기금, `ERP_SPC_ACNT_SUM_AMT` 기업특별회계, `CENT_GVRN_NFN_ACV_SUM_AMT` 합계

### 통합재정수지(86GFS결산)

- **서비스이름** `OPFI205`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도 ★필수)
- 출력칸: `ACNT_YR` 회계연도, `SA_RET_ATC_HG_NM` 구분, `GEN_ACNT_SUM_AMT` 일반회계, `ETC_SPC_ACNT_SUM_AMT` 기타특별회계, `TREV_ANEET_AMT` 세입세출외, `NFN_FND_SUM_AMT` 기금, `ERP_SPC_ACNT_SUM_AMT` 기업특별회계, `CENT_GVRN_NFN_ACV_SUM_AMT` 합계

## 중앙정부>통합재정통계>중앙정부 (3종)

### 기업특별회계운용

- **서비스이름** `VW_OPFI383`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `SA_RET_ATC_HG_NM` 통합재정통계보고서항목코드명, `ACNT_YR` 회계연도, `ACNT_NM` 회계코드명, `SA_RET_ATC_AMT` 통합재정통계보고서항목금액

### 세입의경제적분류(94년이전)

- **서비스이름** `VW_OPFI384`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `SA_RET_ATC_HG_NM` 통합재정통계보고서항목코드명, `ACNT_YR` 회계연도, `SA_RET_ATC_AMT` 통합재정통계보고서항목금액

### 세출및순융자의기능적분류(94년이전)

- **서비스이름** `VW_OPFI385`
- 기관: 기획예산처 · 갱신: 연간
- **검색인자**: `ACNT_YR`(회계연도)
- 출력칸: `SA_RET_ATC_HG_NM` 통합재정통계보고서항목코드명, `ACNT_YR` 회계연도, `SA_RET_ATC_AMT` 통합재정통계보고서항목금액

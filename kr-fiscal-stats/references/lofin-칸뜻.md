# 지방재정365 — 응답 칸 이름과 뜻 (146개 자료 · 1396칸)

> 출처: 지방재정365(www.lofin365.go.kr) · 수집 2026-09-23 · 저작권은 그 기관에 있고 이용 조건은 그 기관 약관을 따릅니다(저장소의 NOTICE).

출처는 포털의 자료별 OpenAPI 상세 화면 「출력값」 표(2026-09-23 받음).

- ★**칸은 «이름»으로 맞춘다. 순서로 맞추지 않는다** — 포털 표와 실제 응답의 순서가 다른 자료가 있다.
- ★**금액 단위는 거의 안 적혀 있다.** 뜻 칸에 `(천원)`·`(원)`·`(%)` 로 적힌 것만 공식 표기다. 나머지는 크기로 맞춰 보고 «추정»이라고 밝힌다.
- ★**`AIDFA` 순계 두 칸은 포털 표가 거꾸로 적었다** — 값으로 재서 바로잡았다(`lofin.py` 의 `FIXES`). 총계 두 칸은 포털 표가 맞다.
- ★**`FNCST` 의 `wa_laf_cd`(지역코드)는 포털 표에 없지만 응답에는 온다** — 다른 자료와 같은 뜻으로 더했다(`lofin.py` 의 `ADDS`).

| 자료코드 | 칸 | 뜻 | 포털 설명 |
|---|---|---|---|
| `AAJCH` | `fyr` | 회계연도 |  |
| `AAJCH` | `wa_laf_cd` | 지역코드 |  |
| `AAJCH` | `wa_laf_hg_nm` | 지역명 |  |
| `AAJCH` | `laf_cd` | 자치단체코드 |  |
| `AAJCH` | `laf_hg_nm` | 자치단체명 |  |
| `AAJCH` | `self_ltax_efir` | 주민1인당 자체수입액(천원) |  |
| `AAJCH` | `ltax_efir` | 지방세(천원) |  |
| `AAJCH` | `nni_rv_efir` | 세외수입(천원) |  |
| `AAJCH` | `pptn_num` | 인구수(명) |  |
| `ABDBC` | `fyr` | 회계연도 |  |
| `ABDBC` | `wa_laf_cd` | 지역코드 |  |
| `ABDBC` | `wa_laf_hg_nm` | 지역명 |  |
| `ABDBC` | `laf_cd` | 자치단체코드 |  |
| `ABDBC` | `laf_hg_nm` | 자치단체명 |  |
| `ABDBC` | `pfa_amt1` | 체납 누계액 |  |
| `ABDBC` | `pfa_amt2` | 지방세체납액 |  |
| `ABDBC` | `pfa_amt3` | 세외수입체납액 |  |
| `ABIBA` | `fyr` | 회계연도 |  |
| `ABIBA` | `wa_laf_cd` | 지역코드 |  |
| `ABIBA` | `wa_laf_hg_nm` | 지역명 |  |
| `ABIBA` | `laf_cd` | 자치단체코드 |  |
| `ABIBA` | `laf_hg_nm` | 자치단체명 |  |
| `ABIBA` | `efir_trbd_tott_amt` | 예산액 |  |
| `ABIBA` | `sum_ltax_nni_rv_efir_tott_amt` | 자체수입 |  |
| `ABIBA` | `ltax_efir_tott_amt` | 지방세 |  |
| `ABIBA` | `bdg_lbst` | 인건비 |  |
| `ABIBA` | `rate1` | 총예산 대비 인건비 비율(%) |  |
| `ABIBA` | `rate2` | 자체수입 대비 인건비 비율(%) |  |
| `ABIBA` | `rate3` | 지방세수입 대비 인건비 비율(%) |  |
| `ABIFB` | `fyr` | 회계연도 |  |
| `ABIFB` | `wa_laf_cd` | 지역코드 |  |
| `ABIFB` | `wa_laf_hg_nm` | 지역명 |  |
| `ABIFB` | `laf_cd` | 자치단체코드 |  |
| `ABIFB` | `laf_hg_nm` | 자치단체명 |  |
| `ABIFB` | `fld_cd` | 분야코드 |  |
| `ABIFB` | `fld_nm` | 분야명 |  |
| `ABIFB` | `sect_cd` | 부문코드 |  |
| `ABIFB` | `sect_nm` | 부문명 |  |
| `ABIFB` | `ep_amt` | 세출결산액 |  |
| `ABIFB` | `rgstr_dt` | 생성일 |  |
| `ABIFB` | `rgstr_usr_id` | 생성아이디 |  |
| `ACCAM` | `fyr` | 회계연도 |  |
| `ACCAM` | `wa_laf_hg_nm` | 지역명 |  |
| `ACCAM` | `laf_cd` | 자치단체코드 |  |
| `ACCAM` | `laf_hg_nm` | 자치단체명 |  |
| `ACCAM` | `lgfd_ramt_amt1` | 일반회계 |  |
| `ACCAM` | `lgfd_ramt_amt2` | 기타특별회계 |  |
| `ACCAM` | `lgfd_ramt_amt3` | 공기업특별회계 |  |
| `ACCAM` | `lgfd_ramt_amt4` | 기금회계 |  |
| `ACCBI` | `laf_lat_rt` | 지자체 자산대비 부채비율(%) |  |
| `ACCBI` | `fyr` | 회계연도 |  |
| `ACCBI` | `wa_laf_cd` | 지역코드 |  |
| `ACCBI` | `wa_laf_hg_nm` | 지역명 |  |
| `ACCBI` | `laf_cd` | 자치단체코드 |  |
| `ACCBI` | `laf_hg_nm` | 자치단체명 |  |
| `ACCBI` | `lat_amt` | 부채 |  |
| `ACCBI` | `ast_amt` | 자산 |  |
| `ACEXBG` | `fyr` | 회계연도 | 회계연도 |
| `ACEXBG` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `ACEXBG` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `ACEXBG` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `ACEXBG` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `ACEXBG` | `ane_tott_amt` | 세출총계 | 세출총계 |
| `ACEXBG` | `gen_acnt_amt` | 일반회계 | 일반회계 |
| `ACEXBG` | `pbco_spc_acnt_amt` | 공기업특별회계 | 공기업특별회계 |
| `ACEXBG` | `etc_spc_acnt_amt` | 기타특별회계 | 기타특별회계 |
| `ACEXBG` | `fnd_amt` | 기금 | 기금 |
| `ACJDF` | `fyr` | 회계연도 |  |
| `ACJDF` | `wa_laf_cd` | 지역코드 |  |
| `ACJDF` | `wa_laf_hg_nm` | 지역명 |  |
| `ACJDF` | `laf_cd` | 자치단체코드 |  |
| `ACJDF` | `laf_hg_nm` | 자치단체명 |  |
| `ACJDF` | `pfa_amt1` | 물품수량 |  |
| `ACJDF` | `pfa_amt2` | 물품 현재액 |  |
| `AECFB` | `fyr` | 회계연도 |  |
| `AECFB` | `wa_laf_cd` | 지역코드 |  |
| `AECFB` | `wa_laf_hg_nm` | 지역명 |  |
| `AECFB` | `laf_cd` | 자치단체코드 |  |
| `AECFB` | `laf_hg_nm` | 자치단체명 |  |
| `AECFB` | `pfa_amt2` | 맞춤형복지비 |  |
| `AECFB` | `pfa_amt3` | 세출결산액 |  |
| `AECFB` | `rate` | 맞춤형복지비비율(%) |  |
| `AIDFA` | `fyr` | 회계연도 |  |
| `AIDFA` | `wa_laf_cd` | 지역코드 |  |
| `AIDFA` | `wa_laf_hg_nm` | 지역명 |  |
| `AIDFA` | `laf_cd` | 자치단체코드 |  |
| `AIDFA` | `laf_hg_nm` | 자치단체명 |  |
| `AIDFA` | `fld_cd` | 분야코드 |  |
| `AIDFA` | `fld_nm` | 분야명 |  |
| `AIDFA` | `sect_cd` | 부문코드 |  |
| `AIDFA` | `sect_nm` | 부문명 |  |
| `AIDFA` | `biz_bdg_tott_amt` | 정책사업예산총계 |  |
| `AIDFA` | `fin_acv_tott_amt` | 행정운영경비총계 |  |
| `AIDFA` | `padm_oper_exps_tott_amt` | 재무활동총계 |  |
| `AIDFA` | `biz_bdg_prsm_amt` | 정책사업예산순계 |  |
| `AIDFA` | `fin_acv_prsm_amt` | 행정운영경비순계 |  |
| `AIDFA` | `padm_oper_prsm_exps` | 재무활동순계 |  |
| `AIDFA` | `acnt_dv_nm` | 회계구분명 |  |
| `AJGCF` | `fyr` | 회계연도 |  |
| `AJGCF` | `wa_laf_cd` | 지역코드 |  |
| `AJGCF` | `wa_laf_hg_nm` | 지역명 |  |
| `AJGCF` | `laf_cd` | 자치단체코드 |  |
| `AJGCF` | `laf_hg_nm` | 자치단체명 |  |
| `AJGCF` | `tot_pfa_amt` | 세출결산 총계 |  |
| `AJGCF` | `pfa_amt1` | 일반회계 |  |
| `AJGCF` | `pfa_amt2` | 공기업특별회계 |  |
| `AJGCF` | `pfa_amt3` | 기타특별회계 |  |
| `AJGCF` | `pfa_amt4` | 기금 |  |
| `AOPUYF` | `fyr` | 회계연도 |  |
| `AOPUYF` | `laf_cd` | 자치단체코드 |  |
| `AOPUYF` | `wa_laf_hg_nm` | 지역명 |  |
| `AOPUYF` | `laf_hg_nm` | 자치단체명 |  |
| `AOPUYF` | `smy_cntt_amt` | 기준액 (A) |  |
| `AOPUYF` | `smy_cntt_amt2` | 편성액 (B) |  |
| `AOPUYF` | `smy_cntt_amt_rt` | 시책추진 업무추진비 비율 (B/A) * 100 |  |
| `ARBGT` | `fyr` | 회계연도 |  |
| `ARBGT` | `wa_laf_hg_nm` | 지역명 |  |
| `ARBGT` | `laf_cd` | 자치단체코드 |  |
| `ARBGT` | `laf_hg_nm` | 자치단체명 |  |
| `ARBGT` | `pfa_amt1` | 세입총계 |  |
| `ARBGT` | `pfa_amt2` | 일반회계 |  |
| `ARBGT` | `pfa_amt3` | 공기업특별회계 |  |
| `ARBGT` | `pfa_amt4` | 기타특별회계 |  |
| `ARBGT` | `pfa_amt5` | 기금 |  |
| `AUAES` | `fyr` | 회계연도 |  |
| `AUAES` | `wa_laf_hg_nm` | 지역명 |  |
| `AUAES` | `laf_cd` | 자치단체코드 |  |
| `AUAES` | `laf_hg_nm` | 자치단체명 |  |
| `AUAES` | `stl_amt0` | 계 |  |
| `AUAES` | `stl_amt1` | 자치단체 |  |
| `AUAES` | `stl_amt2` | 지방공공기관 |  |
| `AUAES` | `stl_amt3` | 교육재정 |  |
| `AUAES` | `stl_amt4` | 내(외)부거래 |  |
| `AUARS` | `fyr` | 회계연도 |  |
| `AUARS` | `wa_laf_hg_nm` | 지역명 |  |
| `AUARS` | `laf_cd` | 자치단체코드 |  |
| `AUARS` | `laf_hg_nm` | 자치단체명 |  |
| `AUARS` | `stl_amt0` | 계 |  |
| `AUARS` | `stl_amt1` | 자치단체 |  |
| `AUARS` | `stl_amt2` | 지방공공기관 |  |
| `AUARS` | `stl_amt3` | 교육재정 |  |
| `AUARS` | `stl_amt4` | 내(외)부거래 |  |
| `AUEAD` | `fyr` | 회계연도 |  |
| `AUEAD` | `wa_laf_hg_nm` | 지역명 |  |
| `AUEAD` | `laf_cd` | 자치단체코드 |  |
| `AUEAD` | `laf_hg_nm` | 자치단체명 |  |
| `AUEAD` | `stl_amt1` | 환금자산 |  |
| `AUEAD` | `stl_amt2` | 부채 |  |
| `AUEAD` | `rate` | 비율 |  |
| `AUEVR` | `fyr` | 회계연도 |  |
| `AUEVR` | `wa_laf_hg_nm` | 지역명 |  |
| `AUEVR` | `laf_cd` | 자치단체코드 |  |
| `AUEVR` | `laf_hg_nm` | 자치단체명 |  |
| `AUEVR` | `stl_amt1` | 세출결산액 |  |
| `AUEVR` | `stl_amt2` | 행사관련경비지출액 |  |
| `AUEVR` | `rate` | 비율 |  |
| `AUEXR` | `fyr` | 회계연도 |  |
| `AUEXR` | `wa_laf_hg_nm` | 지역명 |  |
| `AUEXR` | `laf_cd` | 자치단체코드 |  |
| `AUEXR` | `laf_hg_nm` | 자치단체명 |  |
| `AUEXR` | `stl_amt1` | 세출결산액 |  |
| `AUEXR` | `stl_amt2` | 업무추진비지출액 |  |
| `AUEXR` | `rate` | 비율 |  |
| `AUFDR` | `fyr` | 회계연도 |  |
| `AUFDR` | `wa_laf_hg_nm` | 지역명 |  |
| `AUFDR` | `laf_cd` | 자치단체코드 |  |
| `AUFDR` | `laf_hg_nm` | 자치단체명 |  |
| `AUFDR` | `showdepth` | showdepth |  |
| `AUFDR` | `stl_amt1` | 재정자금 |  |
| `AUFDR` | `stl_amt2` | 차입부채 |  |
| `AUFDR` | `rate1` | 비율 |  |
| `AULER` | `fyr` | 회계연도 |  |
| `AULER` | `wa_laf_hg_nm` | 지역명 |  |
| `AULER` | `laf_cd` | 자치단체코드 |  |
| `AULER` | `laf_hg_nm` | 자치단체명 |  |
| `AULER` | `stl_amt1` | 세입결산액 |  |
| `AULER` | `amt2` | 인건비지출액 |  |
| `AULER` | `rate1` | 비율 |  |
| `AUYDR` | `fyr` | 회계연도 |  |
| `AUYDR` | `wa_laf_hg_nm` | 지역명 |  |
| `AUYDR` | `laf_cd` | 자치단체코드 |  |
| `AUYDR` | `laf_hg_nm` | 자치단체명 |  |
| `AUYDR` | `stl_amt1` | 자산 |  |
| `AUYDR` | `stl_amt2` | 부채 |  |
| `AUYDR` | `rate` | 비율 |  |
| `AUYPL` | `fyr` | 회계연도 |  |
| `AUYPL` | `wa_laf_hg_nm` | 지역명 |  |
| `AUYPL` | `laf_cd` | 자치단체코드 |  |
| `AUYPL` | `laf_hg_nm` | 자치단체명 |  |
| `AUYPL` | `stl_amt1` | 세입 |  |
| `AUYPL` | `stl_amt2` | 세출 |  |
| `AUYPL` | `stl_amt3` | 결산상잉여금 |  |
| `BEDDH` | `fyr` | 회계연도 |  |
| `BEDDH` | `wa_laf_cd` | 지역코드 |  |
| `BEDDH` | `wa_laf_hg_nm` | 지역명 |  |
| `BEDDH` | `fld_cd` | 분야코드 |  |
| `BEDDH` | `fld_nm` | 분야명 |  |
| `BEDDH` | `bfae_totl_amt` | 세출예산총계액 |  |
| `BEDDH` | `bfae_prsm_amt` | 세출예산순계액 |  |
| `BGGCD` | `fyr` | 회계연도 |  |
| `BGGCD` | `wa_laf_cd` | 지역코드 |  |
| `BGGCD` | `wa_laf_hg_nm` | 지역명 |  |
| `BGGCD` | `laf_cd` | 자치단체코드 |  |
| `BGGCD` | `laf_hg_nm` | 자치단체명 |  |
| `BGGCD` | `bdg_amt1` | 수입 예산액 |  |
| `BGGCD` | `rcvmt_amt` | 수입 결산액 |  |
| `BGGCD` | `bdg_amt2` | 지출 예산액 |  |
| `BGGCD` | `ep_amt` | 지출 결산액 |  |
| `BJHJB` | `fyr` | 회계연도 |  |
| `BJHJB` | `wa_laf_cd` | 지역코드 |  |
| `BJHJB` | `wa_laf_hg_nm` | 지역명 |  |
| `BJHJB` | `laf_cd` | 자치단체코드 |  |
| `BJHJB` | `laf_hg_nm` | 자치단체명 |  |
| `BJHJB` | `one_llx_smam` | 주민1인당 지방세부담액(천원) |  |
| `BJHJB` | `ltax_efir_tott_amt` | 지방세액(천원) |  |
| `BJHJB` | `pptn_num` | 인구수(명) |  |
| `BQBRB` | `fyr` | 회계연도 |  |
| `BQBRB` | `laf_cd` | 자치단체코드 |  |
| `BQBRB` | `wa_laf_hg_nm` | 지역명 |  |
| `BQBRB` | `laf_hg_nm` | 자치단체명 |  |
| `BQBRB` | `smy_cntt_amt` | 성인지 예산액 (A) |  |
| `BQBRB` | `smy_cntt_amt2` | 세입예산액 (B) |  |
| `BQBRB` | `smy_cntt_amt_rt` | 성인지예산 비율(A/B)*100 |  |
| `BSHTZP` | `fyr` | 회계연도 |  |
| `BSHTZP` | `laf_cd` | 자치단체코드 |  |
| `BSHTZP` | `wa_laf_hg_nm` | 지역명 |  |
| `BSHTZP` | `laf_hg_nm` | 자치단체명 |  |
| `BSHTZP` | `smy_cntt_amt` | 세출 총액(A) |  |
| `BSHTZP` | `smy_cntt_amt2` | 편성액 (B) |  |
| `BSHTZP` | `smy_cntt_amt_rt` | 통장이장반장 활동보상금 비율 (B/A) * 100 |  |
| `BUDLK` | `fyr` | 기준년도 |  |
| `BUDLK` | `wa_laf_hg_nm` | 지역명 |  |
| `BUDLK` | `laf_cd` | 자치단체코드 |  |
| `BUDLK` | `laf_hg_nm` | 자치단체명 |  |
| `BUDLK` | `lnk_nm` | 링크명 |  |
| `BUDLK` | `lnk_url_nm` | URL |  |
| `BZKKC` | `fyr` | 회계연도 |  |
| `BZKKC` | `wa_laf_cd` | 지역코드 |  |
| `BZKKC` | `wa_laf_hg_nm` | 지역명 |  |
| `BZKKC` | `laf_cd` | 자치단체코드 |  |
| `BZKKC` | `laf_hg_nm` | 자치단체명 |  |
| `BZKKC` | `pfa_amt1` | 대상인원(A) |  |
| `BZKKC` | `pfa_amt2` | 지급총액(B) |  |
| `BZKKC` | `pfa_amt3` | 1인당맞춤형복지제도시행경비(C=B/A) |  |
| `BZKKC` | `pfa_amt4` | 1인당맞춤형복지제도 시행경비 기준액(D) |  |
| `BZKKC` | `rate` | 1인당 기준액 대비 시행경비 비율(C/D)(%) |  |
| `BZKKC` | `lup_ord` | 정렬순서 |  |
| `CCJBA` | `fyr` | 회계연도 |  |
| `CCJBA` | `wa_laf_cd` | 지역코드 |  |
| `CCJBA` | `wa_laf_hg_nm` | 지역명 |  |
| `CCJBA` | `laf_cd` | 자치단체코드 |  |
| `CCJBA` | `laf_hg_nm` | 자치단체명 |  |
| `CCJBA` | `pfa_amt1` | 전년도말 현재액 |  |
| `CCJBA` | `pfa_amt2` | 증감액 |  |
| `CCJBA` | `pfa_amt3` | 발생액 |  |
| `CCJBA` | `pfa_amt4` | 소멸액 |  |
| `CCJBA` | `pfa_amt5` | 당해년도 현재액 |  |
| `CDDFA` | `fyr` | 회계연도 |  |
| `CDDFA` | `wa_laf_cd` | 지역코드 |  |
| `CDDFA` | `wa_laf_hg_nm` | 지역명 |  |
| `CDDFA` | `laf_cd` | 자치단체코드 |  |
| `CDDFA` | `laf_hg_nm` | 자치단체명 |  |
| `CDDFA` | `gen_ane_stl_amt` | 일반회계 |  |
| `CDDFA` | `etc_ane_stl_amt` | 기타특별회계 |  |
| `CDDFA` | `pbco_ane_stl_amt` | 공기업특별회계 |  |
| `CEIGF` | `fyr` | 회계연도 |  |
| `CEIGF` | `wa_laf_cd` | 지역코드 |  |
| `CEIGF` | `wa_laf_hg_nm` | 지역명 |  |
| `CEIGF` | `laf_cd` | 자치단체코드 |  |
| `CEIGF` | `laf_hg_nm` | 자치단체명 |  |
| `CEIGF` | `bdg_tott_amt` | 정책사업예산액 |  |
| `CEIGF` | `self_biz_bdg_tott_amt` | 자체사업 |  |
| `CEIGF` | `aid_biz_bdg_tott_amt` | 보조사업 |  |
| `CEIGF` | `bfae_totl_amt` | 일반회계예산액 |  |
| `CEIGF` | `rate` | 정책사업비중(%) |  |
| `CHABG` | `fyr` | 회계연도 |  |
| `CHABG` | `wa_laf_cd` | 지역코드 |  |
| `CHABG` | `wa_laf_hg_nm` | 지역명 |  |
| `CHABG` | `laf_cd` | 자치단체코드 |  |
| `CHABG` | `laf_hg_nm` | 자치단체명 |  |
| `CHABG` | `pfa_amt1` | 비과세액 |  |
| `CHABG` | `pfa_amt2` | 감면액 |  |
| `CHABG` | `pfa_amt3` | 지방세 징수액 |  |
| `CHABG` | `rate` | 지방세 비과세 감면율(%) |  |
| `CHEDJ` | `fyr` | 회계연도 |  |
| `CHEDJ` | `wa_laf_cd` | 지역코드 |  |
| `CHEDJ` | `wa_laf_hg_nm` | 지역명 |  |
| `CHEDJ` | `laf_cd` | 자치단체코드 |  |
| `CHEDJ` | `laf_hg_nm` | 자치단체명 |  |
| `CHEDJ` | `pfa_amt1` | 보증채무현재액 |  |
| `CHEDJ` | `pfa_amt2` | 세출결산액 |  |
| `CHEDJ` | `rate` | 보증채무비율(%) |  |
| `CHFJJ` | `fyr` | 회계연도 |  |
| `CHFJJ` | `wa_laf_cd` | 지역코드 |  |
| `CHFJJ` | `wa_laf_hg_nm` | 지역명 |  |
| `CHFJJ` | `laf_cd` | 자치단체코드 |  |
| `CHFJJ` | `laf_hg_nm` | 자치단체명 |  |
| `CHFJJ` | `pfa_amt1` | 공유재산 수량 |  |
| `CHFJJ` | `pfa_amt2` | 공유재산 현재액 |  |
| `CONLK` | `fyr` | 기준년도 |  |
| `CONLK` | `wa_laf_hg_nm` | 지역명 |  |
| `CONLK` | `laf_cd` | 자치단체코드 |  |
| `CONLK` | `laf_hg_nm` | 자치단체명 |  |
| `CONLK` | `lnk_nm` | 링크명 |  |
| `CONLK` | `lnk_url_nm` | URL |  |
| `DADBC` | `fyr` | 회계연도 |  |
| `DADBC` | `wa_laf_cd` | 지역코드 |  |
| `DADBC` | `wa_laf_hg_nm` | 지역명 |  |
| `DADBC` | `laf_cd` | 자치단체코드 |  |
| `DADBC` | `laf_hg_nm` | 자치단체명 |  |
| `DADBC` | `lcl_asmb_exps` | 지방의회경비 |  |
| `DADBC` | `ane_stl_amt` | 세출결산액 |  |
| `DADBC` | `lcl_asmb_exps_rt` | 지방의회경비비율(%) |  |
| `DCFCE` | `fyr` | 회계연도 |  |
| `DCFCE` | `wa_laf_cd` | 지역코드 |  |
| `DCFCE` | `wa_laf_hg_nm` | 지역명 |  |
| `DCFCE` | `laf_cd` | 자치단체코드 |  |
| `DCFCE` | `laf_hg_nm` | 자치단체명 |  |
| `DCFCE` | `pfa_amt1` | 자체수입(개편전) |  |
| `DCFCE` | `pfa_amt2` | 자치단체 예산규모 |  |
| `DCFCE` | `rate1` | 재정자립도(개편전)(%) |  |
| `DCFCE` | `pfa_amt3` | 자체수입(개편후) |  |
| `DCFCE` | `rate2` | 재정자립도(개편후)(%) |  |
| `DDJAB` | `fyr` | 회계연도 |  |
| `DDJAB` | `wa_laf_cd` | 지역코드 |  |
| `DDJAB` | `wa_laf_hg_nm` | 지역명 |  |
| `DDJAB` | `laf_cd` | 자치단체코드 |  |
| `DDJAB` | `laf_hg_nm` | 자치단체명 |  |
| `DDJAB` | `boe` | 업무추진비 |  |
| `DDJAB` | `ane_stl_amt` | 세출결산액 |  |
| `DDJAB` | `boe_rt` | 업무추진비비율(%) |  |
| `DFGDGG` | `fyr` | 회계연도 |  |
| `DFGDGG` | `wa_laf_hg_nm` | 지역명 |  |
| `DFGDGG` | `laf_cd` | 자치단체코드 |  |
| `DFGDGG` | `laf_hg_nm` | 자치단체명 |  |
| `DFGDGG` | `pfin_stl_amt2` | 회계연도-3 |  |
| `DFGDGG` | `pfin_stl_amt3` | 회계연도-2 |  |
| `DFGDGG` | `pfin_stl_amt4` | 회계연도-1 |  |
| `DFGDGG` | `pfin_stl_amt5` | 회계연도 |  |
| `DFGDGG` | `rate` | 최근 3년간 평균 증가율 |  |
| `DFGDGG` | `lup_ord` | 정렬순서 |  |
| `DFPEEL` | `fyr` | 회계연도 |  |
| `DFPEEL` | `laf_cd` | 자치단체코드 |  |
| `DFPEEL` | `wa_laf_hg_nm` | 지역명 |  |
| `DFPEEL` | `laf_hg_nm` | 자치단체명 |  |
| `DFPEEL` | `smy_cntt_amt` | 총액한도(A) |  |
| `DFPEEL` | `smy_cntt_amt2` | 예산편성액(B) |  |
| `DFPEEL` | `smy_cntt_amt_rt` | 총액한도 대비 편성액 비율(B/A)*100 |  |
| `DIGNE` | `fyr` | 회계연도 |  |
| `DIGNE` | `laf_cd` | 자치단체코드 |  |
| `DIGNE` | `laf_hg_nm` | 자치단체명 |  |
| `DIGNE` | `smy_cntt_amt` | 세출 산출액(A) |  |
| `DIGNE` | `smy_cntt_amt2` | 일반예비비(B) |  |
| `DIGNE` | `smy_cntt_amt3` | 재해‧재난목적예비비(C) |  |
| `DIGNE` | `smy_cntt_amt_rt` | 일반예비비 비율(B/A) |  |
| `DIGNE` | `smy_cntt_amt_rt2` | 재해‧재난목적예비비 비율(C/A) |  |
| `DIGNE` | `wa_laf_hg_nm` | 지역명 |  |
| `DIJGH` | `fyr` | 회계연도 |  |
| `DIJGH` | `wa_laf_cd` | 지역코드 |  |
| `DIJGH` | `wa_laf_hg_nm` | 지역명 |  |
| `DIJGH` | `laf_cd` | 자치단체코드 |  |
| `DIJGH` | `laf_hg_nm` | 자치단체명 |  |
| `DIJGH` | `lsa_amt` | 교부액 |  |
| `DIJGH` | `ane_stl_amt` | 세출결산액 |  |
| `DIJGH` | `lsa_rt` | 교부액비율(%) |  |
| `DIZFMP` | `fyr` | 회계연도 |  |
| `DIZFMP` | `wa_laf_hg_nm` | 지역명 |  |
| `DIZFMP` | `laf_cd` | 자치단체코드 |  |
| `DIZFMP` | `laf_hg_nm` | 자치단체명 |  |
| `DIZFMP` | `pfin_stl_amt1` | 예산현액 |  |
| `DIZFMP` | `pfin_stl_amt2` | 집행액 |  |
| `DIZFMP` | `rate` | 집행률 |  |
| `DJAIH` | `fyr` | 회계연도 |  |
| `DJAIH` | `wa_laf_cd` | 지역코드 |  |
| `DJAIH` | `wa_laf_hg_nm` | 지역명 |  |
| `DJAIH` | `laf_cd` | 자치단체코드 |  |
| `DJAIH` | `laf_hg_nm` | 자치단체명 |  |
| `DJAIH` | `pfa_amt1` | 전년도 현재액 |  |
| `DJAIH` | `pfa_amt2` | 증감액 총계 |  |
| `DJAIH` | `pfa_amt3` | 조성액 |  |
| `DJAIH` | `pfa_amt4` | 사용액 |  |
| `DJAIH` | `pfa_amt5` | 당해년도 현재액 |  |
| `DJIELS` | `fyr` | 회계연도 |  |
| `DJIELS` | `laf_cd` | 자치단체코드 |  |
| `DJIELS` | `laf_hg_nm` | 자치단체명 |  |
| `DJIELS` | `smy_cntt_amt` | 세출결산액(A) |  |
| `DJIELS` | `smy_cntt_amt2` | 일반예비비 집행액(B) |  |
| `DJIELS` | `smy_cntt_amt3` | 재해‧재난목적예비비 집행액(C) |  |
| `DJIELS` | `smy_cntt_amt_rt` | 일반예비비 집행비율(B/A) |  |
| `DJIELS` | `smy_cntt_amt_rt2` | 재해‧재난목적예비비 집행비율(C/A) |  |
| `DJIELS` | `wa_laf_hg_nm` | 지역명 |  |
| `EAGGD` | `rate` | 사회복지비중(%) |  |
| `EAGGD` | `fyr` | 회계연도 |  |
| `EAGGD` | `wa_laf_cd` | 지역코드 |  |
| `EAGGD` | `wa_laf_hg_nm` | 지역명 |  |
| `EAGGD` | `laf_cd` | 자치단체코드 |  |
| `EAGGD` | `laf_hg_nm` | 자치단체명 |  |
| `EAGGD` | `sum_bfae_totl_amt` | 자치단체예산규모 |  |
| `EAGGD` | `sum_social_bfae_totl_amt` | 사회복지분야예산 |  |
| `EECCC` | `fyr` | 회계연도 | 회계연도 |
| `EECCC` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `EECCC` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `EECCC` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `EECCC` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `EECCC` | `fld_nm` | 분야명 | 분야명 |
| `EECCC` | `sum_amt` | 합계 | 합계 |
| `EECCC` | `capt_ep_amt` | 자본지출 | 합계_40000 |
| `EECCC` | `fl_iv_amt` | 융자및출자 | 합계_50000 |
| `EECCC` | `byqt_psv_frsc_amt` | 보전재원 | 합계_60000 |
| `EECCC` | `itrd_amt` | 내부거래 | 합계_70000 |
| `EEHIA` | `fyr` | 회계연도 |  |
| `EEHIA` | `wa_laf_cd` | 지역코드 |  |
| `EEHIA` | `wa_laf_hg_nm` | 지역명 |  |
| `EEHIA` | `laf_cd` | 자치단체코드 |  |
| `EEHIA` | `laf_hg_nm` | 자치단체명 |  |
| `EEHIA` | `pfa_amt1` | 세입 |  |
| `EEHIA` | `pfa_amt2` | 지출 |  |
| `EEHIA` | `pfa_amt3` | 순융자 |  |
| `EEHIA` | `pfa_amt4` | 통합재정규모 |  |
| `EEHIA` | `rate` | 통합재정수지비율(%) |  |
| `EJAEE` | `fyr` | 회계연도 |  |
| `EJAEE` | `wa_laf_cd` | 지역코드 |  |
| `EJAEE` | `wa_laf_hg_nm` | 지역명 |  |
| `EJAEE` | `laf_cd` | 자치단체코드 |  |
| `EJAEE` | `laf_hg_nm` | 자치단체명 |  |
| `EJAEE` | `pfa_amt1` | 자체수입(개편전) |  |
| `EJAEE` | `pfa_amt2` | 자주재원 |  |
| `EJAEE` | `pfa_amt3` | 자치단체 예산규모 |  |
| `EJAEE` | `rate1` | 재정자주도[최종](개편전)(%) |  |
| `EJAEE` | `pfa_amt4` | 자체수입(개편후) |  |
| `EJAEE` | `rate2` | 재정자주도[최종](개편후) |  |
| `EJIEH` | `fyr` | 회계연도 |  |
| `EJIEH` | `wa_laf_cd` | 지역코드 |  |
| `EJIEH` | `wa_laf_hg_nm` | 지역명 |  |
| `EJIEH` | `laf_cd` | 자치단체코드 |  |
| `EJIEH` | `laf_hg_nm` | 자치단체명 |  |
| `EJIEH` | `ynd_amt` | 연말지출 원인행위액 |  |
| `EJIEH` | `ane_stl_amt` | 세출결산액 |  |
| `EJIEH` | `ynd_ep_rt` | 연말지출비율(%) |  |
| `ELIHNG` | `smy_cntt_amt2` | 총 예산편성액(B) |  |
| `ELIHNG` | `smy_cntt_amt_rt` | 1인당 편성액(B/A) |  |
| `ELIHNG` | `fyr` | 회계연도 |  |
| `ELIHNG` | `laf_cd` | 자치단체코드 |  |
| `ELIHNG` | `wa_laf_hg_nm` | 지역명 |  |
| `ELIHNG` | `laf_hg_nm` | 자치단체명 |  |
| `ELIHNG` | `smy_cntt_amt` | 대상인원(A) |  |
| `ELYET` | `exe_amt` | 집행액 |  |
| `ELYET` | `rate1` | 대상액대비집행률 |  |
| `ELYET` | `rate2` | 목표액대비집행률 |  |
| `ELYET` | `fyr` | 회계연도 |  |
| `ELYET` | `wa_laf_hg_nm` | 지역명 |  |
| `ELYET` | `laf_cd` | 자치단체코드 |  |
| `ELYET` | `laf_hg_nm` | 자치단체명 |  |
| `ELYET` | `erex_trgt_amt` | 신속(조기)집행대상액 |  |
| `ELYET` | `erex_gls_amt` | 신속(조기)집행목표액 |  |
| `EUSPBG` | `fyr` | 회계연도 | 회계연도 |
| `EUSPBG` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `EUSPBG` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `EUSPBG` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `EUSPBG` | `ref_mttr_cn` | 구분 | 구분 |
| `EUSPBG` | `edu_bdg_dts_cd` | 상세코드 | 상세코드 |
| `EUSPBG` | `edu_bdg_dts_nm` | 상세코드명 | 상세코드명 |
| `EUSPBG` | `bdg_amt` | 예산액 | 예산액 |
| `EVFTCT` | `fyr` | 회계연도 | 회계연도 |
| `EVFTCT` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `EVFTCT` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `EVFTCT` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `EVFTCT` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `EVFTCT` | `pdct_acnt_info_cd` | 원가회계정보코드 | 원가회계정보코드 |
| `EVFTCT` | `event_fstv_nm` | 행사축제명 | 행사축제명 |
| `EVFTCT` | `biz_cn` | 사업내용 | 사업내용 |
| `EVFTCT` | `tott_amt` | 총비용 | 총비용 |
| `EVFTCT` | `biz_ern_amt` | 사업수익 | 사업수익 |
| `EVFTCT` | `nc_amt` | 순원가 | 순원가 |
| `EVFTCT` | `hdmt_bgng_ymd` | 개최시작일자 | 개최시작일자 |
| `EVFTCT` | `hdmt_end_ymd` | 개최종료일자 | 개최종료일자 |
| `FBHFE` | `fyr` | 회계연도 |  |
| `FBHFE` | `wa_laf_cd` | 지역코드 |  |
| `FBHFE` | `wa_laf_hg_nm` | 지역명 |  |
| `FBHFE` | `laf_cd` | 자치단체코드 |  |
| `FBHFE` | `laf_hg_nm` | 자치단체명 |  |
| `FBHFE` | `tot_pfa_amt` | 민자사업재정부담액 |  |
| `FBHFE` | `pfa_amt1` | BTL 임대료 및 운영비 |  |
| `FBHFE` | `pfa_amt2` | BTO 재정지원금 |  |
| `FBHIF` | `fyr` | 회계연도 |  |
| `FBHIF` | `wa_laf_cd` | 지역코드 |  |
| `FBHIF` | `wa_laf_hg_nm` | 지역명 |  |
| `FBHIF` | `laf_cd` | 자치단체코드 |  |
| `FBHIF` | `laf_hg_nm` | 자치단체명 |  |
| `FBHIF` | `self_biz_bdg_tott_amt` | 자체사업예산액 |  |
| `FBHIF` | `bfae_totl_amt` | 일반회계예산액 |  |
| `FBHIF` | `rate` | 자체사업비중(%) |  |
| `FDDDI` | `fyr` | 회계연도 |  |
| `FDDDI` | `wa_laf_cd` | 지역코드 |  |
| `FDDDI` | `wa_laf_hg_nm` | 지역명 |  |
| `FDDDI` | `laf_cd` | 자치단체코드 |  |
| `FDDDI` | `laf_hg_nm` | 자치단체명 |  |
| `FDDDI` | `acnt_dv_nm` | 회계구분명 |  |
| `FDDDI` | `fld_cd` | 분야코드 |  |
| `FDDDI` | `fld_nm` | 분야명 |  |
| `FDDDI` | `bfae_totl_amt` | 세출예산총계액 |  |
| `FDDDI` | `bfae_prsm_amt` | 세출예산순계액 |  |
| `FDHHH` | `fyr` | 회계연도 | 회계연도 |
| `FDHHH` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `FDHHH` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `FDHHH` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `FDHHH` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `FDHHH` | `lnnc_plan_dts_dv_cd` | 세입세출구분코드 | 세입세출구분코드 |
| `FDHHH` | `lnnc_plan_dts_dv_cd_nm` | 세입세출구분 | 세입세출구분 |
| `FDHHH` | `tpd_plan_amt` | 1차년도 | 1차년도 |
| `FDHHH` | `prm_yr_plan_amt` | 2차년도 | 2차년도 |
| `FDHHH` | `scnd_yr_plan_amt` | 3차년도 | 3차년도 |
| `FDHHH` | `trds_yr_plan_amt` | 4차년도 | 4차년도 |
| `FDHHH` | `ftsq_yr_plan_amt` | 5차년도 | 5차년도 |
| `FDHHH` | `rate` | 연평균증가율(%) | 연평균증가율 |
| `FDOST` | `fyr` | 회계연도 |  |
| `FDOST` | `wa_laf_hg_nm` | 지역명 |  |
| `FDOST` | `laf_cd` | 자치단체코드 |  |
| `FDOST` | `laf_hg_nm` | 자치단체명 |  |
| `FDOST` | `pfa_amt1` | 자체수입(개편전) |  |
| `FDOST` | `pfa_amt2` | 자주재원 |  |
| `FDOST` | `pfa_amt3` | 자치단체세입결산규모 |  |
| `FDOST` | `rate1` | 재정자주도[결산](개편전) |  |
| `FDOST` | `pfa_amt4` | 자체수입(개편후) |  |
| `FDOST` | `rate2` | 재정자주도[결산](개편후) |  |
| `FFHCB` | `fyr` | 회계연도 |  |
| `FFHCB` | `wa_laf_cd` | 지역코드 |  |
| `FFHCB` | `wa_laf_hg_nm` | 지역명 |  |
| `FFHCB` | `laf_cd` | 자치단체코드 |  |
| `FFHCB` | `laf_hg_nm` | 자치단체명 |  |
| `FFHCB` | `rate` | 행정운영경비비중(%) |  |
| `FFHCB` | `padm_oper_exps_tott_amt` | 행정운영경비 |  |
| `FFHCB` | `bfae_totl_amt` | 일반회계예산액 |  |
| `FIACRV` | `fyr` | 회계연도 | 회계연도 |
| `FIACRV` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `FIACRV` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `FIACRV` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `FIACRV` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `FIACRV` | `armk_cd` | 세목코드 | 세목코드 |
| `FIACRV` | `armk_nm` | 세목명 | 세목명 |
| `FIACRV` | `lvl_no` | 레벨번호 | 레벨번호 |
| `FIACRV` | `tott_sum_amt` | 총계합계 | 총계합계 |
| `FIACRV` | `gen_acnt_tott_amt` | 일반회계총계 | 일반회계총계 |
| `FIACRV` | `pbco_spc_acnt_tott_amt` | 공기업특별회계총계 | 공기업특별회계총계 |
| `FIACRV` | `etc_spc_acnt_tott_amt` | 기타특별회계총계 | 기타특별회계총계 |
| `FIACRV` | `prsm_amt` | 순계합계 | 순계합계 |
| `FIACRV` | `gen_acnt_prsm_amt` | 일반회계순계 | 일반회계순계 |
| `FIACRV` | `pbco_spc_acnt_prsm_amt` | 공기업특별회계순계 | 공기업특별회계순계 |
| `FIACRV` | `etc_spc_acnt_prsm_amt` | 기타특별회계순계 | 기타특별회계순계 |
| `FIFGB` | `fyr` | 회계연도 |  |
| `FIFGB` | `wa_laf_cd` | 지역코드 |  |
| `FIFGB` | `wa_laf_hg_nm` | 지역명 |  |
| `FIFGB` | `laf_cd` | 자치단체코드 |  |
| `FIFGB` | `laf_hg_nm` | 자치단체명 |  |
| `FIFGB` | `pfa_amt1` | 자체수입(개편전) |  |
| `FIFGB` | `pfa_amt2` | 자주재원 |  |
| `FIFGB` | `pfa_amt3` | 자치단체 예산규모 |  |
| `FIFGB` | `rate1` | 재정자주도(개편전)(%) |  |
| `FIFGB` | `pfa_amt4` | 자체수입(개편후) |  |
| `FIFGB` | `rate2` | 재정자주도(개편후) |  |
| `FINLK` | `fyr` | 기준년도 |  |
| `FINLK` | `wa_laf_hg_nm` | 지역명 |  |
| `FINLK` | `laf_cd` | 자치단체코드 |  |
| `FINLK` | `laf_hg_nm` | 자치단체명 |  |
| `FINLK` | `pba_dv_nm` | 구분 |  |
| `FINLK` | `lnk_nm` | 링크명 |  |
| `FINLK` | `lnk_url_nm` | URL |  |
| `FIPROF` | `fyr` | 회계연도 |  |
| `FIPROF` | `wa_laf_cd` | 지역코드 |  |
| `FIPROF` | `wa_laf_hg_nm` | 지역명 |  |
| `FIPROF` | `laf_cd` | 자치단체코드 |  |
| `FIPROF` | `laf_hg_nm` | 자치단체명 |  |
| `FIPROF` | `pfa_amt1` | 수익총계 |  |
| `FIRVBG` | `fyr` | 회계연도 | 회계연도 |
| `FIRVBG` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `FIRVBG` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `FIRVBG` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `FIRVBG` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `FIRVBG` | `armk_cd` | 세목코드 | 세목코드 |
| `FIRVBG` | `armk_nm` | 세목명 | 세목명 |
| `FIRVBG` | `pryr_last_bdg_prsm_amt` | 예산순계 | 예산순계 |
| `FIRVBG` | `last_bdg_tott_amt` | 예산총계 | 예산총계 |
| `FNCST` | `fyr` | 회계연도 |  |
| `FNCST` | `wa_laf_cd` | 지역코드 |  |
| `FNCST` | `wa_laf_hg_nm` | 지역명 |  |
| `FNCST` | `laf_cd` | 자치단체코드 |  |
| `FNCST` | `laf_hg_nm` | 자치단체명 |  |
| `FNCST` | `pfa_amt1` | 자체수입(개편전) |  |
| `FNCST` | `pfa_amt2` | 자치단체세입결산규모 |  |
| `FNCST` | `rate1` | 재정자립도[결산](개편전) |  |
| `FNCST` | `pfa_amt3` | 자체수입(개편후) |  |
| `FNCST` | `rate2` | 재정자립도[결산](개편후) |  |
| `FNSTT` | `fyr` | 회계연도 |  |
| `FNSTT` | `laf_cd` | 자치단체코드 |  |
| `FNSTT` | `toa_cd` | 원가대상과목코드 |  |
| `FNSTT` | `toa_no` | 항목행번 |  |
| `FNSTT` | `wa_laf_hg_nm` | 지역명 |  |
| `FNSTT` | `laf_hg_nm` | 자치단체명 |  |
| `FNSTT` | `toa_nm` | 항목명 |  |
| `FNSTT` | `tpd_amt` | 당기 |  |
| `FNSTT` | `fhy_amt` | 전기 |  |
| `FNSTT` | `ast_rtvr` | 증감율 |  |
| `FNSTT` | `rgstr_dt` | 등록일자 |  |
| `FUMPEX` | `fyr` | 회계연도 | 회계연도 |
| `FUMPEX` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `FUMPEX` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `FUMPEX` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `FUMPEX` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `FUMPEX` | `outl_cls_cd` | 분류코드 | 통합개요분류코드 |
| `FUMPEX` | `itg_outl_cls_nm` | 분류명 | 통합개요분류명 |
| `FUMPEX` | `exps_cntt_dts_atc_cd` | 세부항목코드 | 세부항목코드 |
| `FUMPEX` | `exps_cntt_dts_atc_nm` | 세부항목명 | 세부항목명 |
| `FUMPEX` | `sum_nop` | 인원합계 | 인원합계 |
| `FUMPEX` | `gen_acnt_nop` | 일반회계인원 | 일반회계인원 |
| `FUMPEX` | `etc_spc_acnt_nop` | 기타특별회계인원 | 기타특별회계인원 |
| `FUMPEX` | `pbco_spc_acnt_nop` | 공기업특별회계인원 | 공기업특별회계인원 |
| `FUMPEX` | `bdg_sum_amt` | 예산액합계 | 예산액합계 |
| `FUMPEX` | `gen_acnt_bdg_amt` | 일반회계예산액 | 일반회계예산액 |
| `FUMPEX` | `etc_spc_acnt_bdg_amt` | 기타특별회계예산액 | 기타특별회계예산액 |
| `FUMPEX` | `pbco_spc_acnt_bdg_amt` | 공기업특별회계예산액 | 공기업특별회계예산액 |
| `GAECF` | `laf_hg_nm` | 자치단체명 |  |
| `GAECF` | `total` | 행사축제경비 |  |
| `GAECF` | `fyr` | 회계연도 |  |
| `GAECF` | `wa_laf_cd` | 지역코드 |  |
| `GAECF` | `wa_laf_hg_nm` | 지역명 |  |
| `GAECF` | `laf_cd` | 자치단체코드 |  |
| `GAECF` | `pfa_amt1` | 세출결산액 |  |
| `GAECF` | `rate` | 행사축제경비비율(%) |  |
| `GAEJG` | `fyr` | 회계연도 |  |
| `GAEJG` | `wa_laf_cd` | 지역코드 |  |
| `GAEJG` | `wa_laf_hg_nm` | 지역명 |  |
| `GAEJG` | `laf_cd` | 자치단체코드 |  |
| `GAEJG` | `laf_hg_nm` | 자치단체명 |  |
| `GAEJG` | `pfa_amt1` | 수의계약실적금액 |  |
| `GAEJG` | `pfa_amt2` | 총계약실적금액 |  |
| `GAEJG` | `rate` | 수의계약비율(%) |  |
| `GGAED` | `fyr` | 회계연도 |  |
| `GGAED` | `wa_laf_cd` | 지역코드 |  |
| `GGAED` | `wa_laf_hg_nm` | 지역명 |  |
| `GGAED` | `laf_cd` | 자치단체코드 |  |
| `GGAED` | `laf_hg_nm` | 자치단체명 |  |
| `GGAED` | `rate` | 예비비확보율(%) |  |
| `GGAED` | `bfae_totl_amt1` | 예비비 |  |
| `GGAED` | `bfae_totl_amt2` | 자치단체예산규모 |  |
| `GGNSE` | `fyr` | 회계연도 |  |
| `GGNSE` | `wa_laf_cd` | 지역코드 |  |
| `GGNSE` | `wa_laf_hg_nm` | 지역명 |  |
| `GGNSE` | `laf_cd` | 자치단체코드 |  |
| `GGNSE` | `laf_hg_nm` | 자치단체명 |  |
| `GGNSE` | `fld_cd` | 분야코드 |  |
| `GGNSE` | `fld_nm` | 분야명 |  |
| `GGNSE` | `pol_bizct` | 정책사업 |  |
| `GGNSE` | `fin_acv_amt` | 재무활동 |  |
| `GGNSE` | `padm_oper_exps` | 행정운영경비 |  |
| `GGNSE` | `rgstr_dt` | 생성날짜 |  |
| `GGNSE` | `rgstr_usr_id` | 생성아이디 |  |
| `GHDIE` | `fyr` | 회계연도 |  |
| `GHDIE` | `wa_laf_cd` | 지역코드 |  |
| `GHDIE` | `wa_laf_hg_nm` | 지역명 |  |
| `GHDIE` | `laf_cd` | 자치단체코드 |  |
| `GHDIE` | `laf_hg_nm` | 자치단체명 |  |
| `GHDIE` | `rate` | 의회비비중(%) |  |
| `GHDIE` | `asmb_bdg_amt` | 의회비 |  |
| `GHDIE` | `asmb_sct_exps` | 의회사무처경비 |  |
| `GHDIE` | `bfae_totl_amt` | 일반회계예산액 |  |
| `GJFHC` | `fyr` | 회계연도 |  |
| `GJFHC` | `wa_laf_cd` | 지역코드 |  |
| `GJFHC` | `wa_laf_hg_nm` | 지역명 |  |
| `GJFHC` | `laf_cd` | 자치단체코드 |  |
| `GJFHC` | `laf_hg_nm` | 자치단체명 |  |
| `GJFHC` | `goem_lbst` | 공무원인건비 |  |
| `GJFHC` | `ane_stl_amt` | 세출결산액 |  |
| `GJFHC` | `goem_lbst_rt` | 공무원인건비비율(%) |  |
| `GJHCD` | `laf_hg_nm` | 자치단체명 |  |
| `GJHCD` | `pfa_amt1` | 사회복지분야 결산액 |  |
| `GJHCD` | `fyr` | 회계연도 |  |
| `GJHCD` | `wa_laf_cd` | 지역코드 |  |
| `GJHCD` | `wa_laf_hg_nm` | 지역명 |  |
| `GJHCD` | `laf_cd` | 자치단체코드 |  |
| `GJHCD` | `pfa_amt9` | 세출결산액 |  |
| `GJHCD` | `rate` | 사회복지비비율(%) |  |
| `GJSCS` | `laf_hg_nm` | 자치단체명 |  |
| `GJSCS` | `fld_cd` | 분야코드 |  |
| `GJSCS` | `fld_nm` | 분야명 |  |
| `GJSCS` | `gsa_amt` | 국고보조금 |  |
| `GJSCS` | `zon_dvlp_spc_acnt_sbat_amt` | 지특보조금 |  |
| `GJSCS` | `fnd_sbat_amt` | 기금보조금 |  |
| `GJSCS` | `spc_grsb_txam_amt` | 특별교부세 |  |
| `GJSCS` | `ftg_safe_grsb_txam_amt` | 소방안전교부세 |  |
| `GJSCS` | `capep` | 시도비 |  |
| `GJSCS` | `spc_grsb_amt` | 특별교부금 |  |
| `GJSCS` | `sggep` | 시군구비 |  |
| `GJSCS` | `lgfd_amt` | 지방채 |  |
| `GJSCS` | `pvcp_amt` | 민자 |  |
| `GJSCS` | `etc_amt` | 기타 |  |
| `GJSCS` | `rgstr_dt` | 생성날짜 |  |
| `GJSCS` | `rgstr_usr_id` | 생성아이디 |  |
| `GJSCS` | `fyr` | 회계연도 |  |
| `GJSCS` | `wa_laf_hg_nm` | 지역명 |  |
| `GJSCS` | `laf_cd` | 자치단체코드 |  |
| `GJSCS` | `lcl_dspr_cntrm_fnd_amt` | 지방대응소멸기금 |  |
| `GMWKB` | `fyr` | 회계연도 |  |
| `GMWKB` | `wa_laf_hg_nm` | 지역명 |  |
| `GMWKB` | `laf_cd` | 자치단체코드 |  |
| `GMWKB` | `laf_hg_nm` | 자치단체명 |  |
| `GMWKB` | `aemk_grp_cd` | 공무원관련경비코드 |  |
| `GMWKB` | `itst_indc_nm` | 공무원관련경비명 |  |
| `GMWKB` | `gen_acnt_amt` | 일반회계(천원) |  |
| `GMWKB` | `etc_spc_acnt_amt` | 기타특별회계(천원) |  |
| `GMWKB` | `pbco_spc_acnt_amt` | 공기업특별회계(천원) |  |
| `GMWKB` | `rgstr_dt` | 생성날짜 |  |
| `GMWKB` | `rgstr_usr_id` | 생성아이디 |  |
| `GNLAE` | `fyr` | 회계연도 |  |
| `GNLAE` | `wa_laf_hg_nm` | 지역명 |  |
| `GNLAE` | `laf_cd` | 자치단체코드 |  |
| `GNLAE` | `laf_hg_nm` | 자치단체명 |  |
| `GNLAE` | `ane_rflt_stl_amt` | 세출결산액 |  |
| `GNLAE` | `ane_rflt_amt` | 반영액 |  |
| `GNLAE` | `ane_rflt_rt` | 비율 |  |
| `GNLAR` | `fyr` | 회계연도 |  |
| `GNLAR` | `wa_laf_hg_nm` | 지역명 |  |
| `GNLAR` | `laf_cd` | 자치단체코드 |  |
| `GNLAR` | `laf_hg_nm` | 자치단체명 |  |
| `GNLAR` | `txrv_rflt_stl_amt` | 세입결산액 |  |
| `GNLAR` | `txrv_rflt_amt` | 반영액 |  |
| `GNLAR` | `txrv_rflt_rt` | 비율 |  |
| `GVBDAC` | `fyr` | 회계연도 | 회계연도 |
| `GVBDAC` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `GVBDAC` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `GVBDAC` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `GVBDAC` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `GVBDAC` | `dts_snum` | 순번 | 순번 |
| `GVBDAC` | `gbd_nct_biz_nm` | 청사신축사업명 | 청사신축사업명 |
| `GVBDAC` | `gbd_ty_nm` | 청사유형명 | 청사유형명 |
| `GVBDAC` | `nct_amt` | 신축비용 | 신축비용 |
| `GVBDAC` | `puar_amt` | 면적당비용 | 면적당비용 |
| `GVBDAC` | `rst_psby_amt` | 주민1인당비용 | 주민1인당비용 |
| `GVBDAC` | `goem_psby_amt` | 공무원1인당비용 | 공무원1인당비용 |
| `HCDIB` | `fyr` | 회계연도 |  |
| `HCDIB` | `wa_laf_cd` | 지역코드 |  |
| `HCDIB` | `wa_laf_hg_nm` | 지역명 |  |
| `HCDIB` | `laf_cd` | 자치단체코드 |  |
| `HCDIB` | `laf_hg_nm` | 자치단체명 |  |
| `HCDIB` | `rate` | 주민1인당 세출예산액(천원) |  |
| `HCDIB` | `bfae_totl_amt` | 일반회계 세출예산액(천원) |  |
| `HCDIB` | `pptn_num` | 인구수(명) |  |
| `HCFDA` | `bdg_camt_amt` | 예산현액 |  |
| `HCFDA` | `bdg_ntep` | 국비 |  |
| `HCFDA` | `city_amt` | 시도비 |  |
| `HCFDA` | `sggep` | 시군구비 |  |
| `HCFDA` | `ep_amt` | 지출액 |  |
| `HCFDA` | `cpl_amt` | 편성액 |  |
| `HCFDA` | `rgstr_dt` | 생성일시 |  |
| `HCFDA` | `acnt_dv_nm` | 회계구분명 |  |
| `HCFDA` | `fld_cd` | 분야코드 |  |
| `HCFDA` | `fld_nm` | 분야명 |  |
| `HCFDA` | `exe_ymd` | 집행일자 |  |
| `HCFDA` | `fyr` | 회계연도 |  |
| `HCFDA` | `wa_laf_cd` | 광역자치단체코드 |  |
| `HCFDA` | `wa_laf_hg_nm` | 지역명 |  |
| `HCFDA` | `laf_cd` | 자치단체코드 |  |
| `HCFDA` | `laf_hg_nm` | 자치단체명_한글 |  |
| `HCFDA` | `acnt_dv_cd` | 회계구분코드 |  |
| `HCFDA` | `rgstr_usr_id` | 생성자ID |  |
| `HEDFC` | `laf_cd` | 자치단체코드 |  |
| `HEDFC` | `laf_hg_nm` | 자치단체명 |  |
| `HEDFC` | `pfa_amt1` | 채무잔액 |  |
| `HEDFC` | `pfa_amt2` | 최종예산액 |  |
| `HEDFC` | `rate` | 예산대비채무비율(%) |  |
| `HEDFC` | `fyr` | 회계연도 |  |
| `HEDFC` | `wa_laf_cd` | 지역코드 |  |
| `HEDFC` | `wa_laf_hg_nm` | 지역명 |  |
| `HFBFE` | `fyr` | 회계연도 |  |
| `HFBFE` | `wa_laf_cd` | 지역코드 |  |
| `HFBFE` | `wa_laf_hg_nm` | 지역명 |  |
| `HFBFE` | `laf_cd` | 자치단체코드 |  |
| `HFBFE` | `laf_hg_nm` | 자치단체명 |  |
| `HFBFE` | `pfa_amt1` | 출자금 |  |
| `HFBFE` | `pfa_amt2` | 출연금 |  |
| `HFBFE` | `pfa_amt3` | 세출결산액 |  |
| `HFBFE` | `rate` | 출자출연금비율(%) |  |
| `HFJGE` | `fyr` | 회계연도 |  |
| `HFJGE` | `wa_laf_cd` | 지역코드 |  |
| `HFJGE` | `wa_laf_hg_nm` | 지역명 |  |
| `HFJGE` | `laf_cd` | 자치단체코드 |  |
| `HFJGE` | `laf_hg_nm` | 자치단체명 |  |
| `HFJGE` | `pfa_amt1` | 세입 |  |
| `HFJGE` | `pfa_amt2` | 지출 |  |
| `HFJGE` | `pfa_amt3` | 순융자 |  |
| `HFJGE` | `pfa_amt4` | 통합재정규모 |  |
| `HFJGE` | `rate` | 통합재정수지비율(%) |  |
| `HHBJG` | `laf_cd` | 자치단체코드 |  |
| `HHBJG` | `tot_stl_amt` | 계(A+B+C-D)(원) |  |
| `HHBJG` | `stl_amt1` | 자치단체(A)(원) |  |
| `HHBJG` | `stl_amt2` | 지방공공기관(B)(원) |  |
| `HHBJG` | `stl_amt3` | 교육재정(C)(원) |  |
| `HHBJG` | `stl_amt4` | 내(외)부거래(D)(원) |  |
| `HHBJG` | `fyr` | 회계연도 |  |
| `HHBJG` | `wa_laf_hg_nm` | 지역 |  |
| `HHBJG` | `laf_hg_nm` | 자치단체명 |  |
| `HHRNV` | `fyr` | 회계연도 |  |
| `HHRNV` | `wa_laf_hg_nm` | 지역명 |  |
| `HHRNV` | `laf_cd` | 자치단체코드 |  |
| `HHRNV` | `laf_hg_nm` | 자치단체명 |  |
| `HHRNV` | `fcl_ty_nm` | 시설유형 |  |
| `HHRNV` | `fcl_dv_nm` | 시설구분 |  |
| `HHRNV` | `fcl_epl_cn` | 시설명 |  |
| `HHRNV` | `accnut_se_code` | 건립일 |  |
| `HHRNV` | `acht_tott_area` | 건물면적 |  |
| `HHRNV` | `ldar` | 토지면적 |  |
| `HHRNV` | `oper_mth_nm` | 운영방식 |  |
| `HHRNV` | `cns_inst_nm` | 위탁기관명 |  |
| `HHRNV` | `prod_co` | 관리인력 |  |
| `HHRNV` | `oper_fom_knd_nm` | 운영형태종류명 |  |
| `HHRNV` | `est_yn` | 산정여부 |  |
| `HHRNV` | `ann_utzt_nop` | 연간이용인원 |  |
| `HHRNV` | `tott_amt` | 건립비용 |  |
| `HHRNV` | `dprc_amt` | 감가상각액 |  |
| `HHRNV` | `dprc_aggr_amt` | 감가상각누계액 |  |
| `HHRNV` | `rccst_amt` | 장부가액 |  |
| `HHRNV` | `svlf` | 내용연수 |  |
| `HHRNV` | `oper_epn_amt` | 비용 |  |
| `HHRNV` | `pufc_oper_lbst` | 인건비 |  |
| `HHRNV` | `mtn_mgct_amt` | 유지관리비 |  |
| `HHRNV` | `thy_etc_epn_amt` | 기타 |  |
| `HHRNV` | `ern_amt` | 수익 |  |
| `HHRNV` | `entc_ern_amt` | 입장료 |  |
| `HHRNV` | `gesu_ern_amt` | 대관료 |  |
| `HHRNV` | `ls_ern_amt` | 임대료 |  |
| `HHRNV` | `rvs_ern_amt` | 귀속된수익(민간위탁료 등) |  |
| `HHRNV` | `etc_ern_amt` | 기타수익 |  |
| `HHRNV` | `thy_nervn_amt` | 순수익 |  |
| `IAFHI` | `fyr` | 회계연도 |  |
| `IAFHI` | `wa_laf_cd` | 지역코드 |  |
| `IAFHI` | `wa_laf_hg_nm` | 지역명 |  |
| `IAFHI` | `laf_cd` | 자치단체코드 |  |
| `IAFHI` | `laf_hg_nm` | 자치단체명 |  |
| `IAFHI` | `aid_biz_bdg_tott_amt` | 보조사업예산액 |  |
| `IAFHI` | `bfae_totl_amt` | 일반회계예산액 |  |
| `IAFHI` | `rate` | 보조사업비중(%) |  |
| `IIBBH` | `pfa_amt4` | 기금 |  |
| `IIBBH` | `fyr` | 회계연도 |  |
| `IIBBH` | `wa_laf_cd` | 지역코드 |  |
| `IIBBH` | `wa_laf_hg_nm` | 지역명 |  |
| `IIBBH` | `laf_cd` | 자치단체코드 |  |
| `IIBBH` | `laf_hg_nm` | 자치단체명 |  |
| `IIBBH` | `total` | 세입결산 총계 |  |
| `IIBBH` | `pfa_amt1` | 일반회계 |  |
| `IIBBH` | `pfa_amt2` | 공기업 특별회계 |  |
| `IIBBH` | `pfa_amt3` | 기타 특별회계 |  |
| `JAIDB` | `fyr` | 회계연도 | 회계연도 |
| `JAIDB` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `JAIDB` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `JAIDB` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `JAIDB` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `JAIDB` | `gbn_cd` | 구분코드 | 구분코드 |
| `JAIDB` | `gbn_nm` | 구분명 | 구분명 |
| `JAIDB` | `armk_cd` | 세목코드 | 세목코드 |
| `JAIDB` | `armk_nm` | 세목명 | 세목명 |
| `JAIDB` | `ep_amt` | 금액 | 금액 |
| `JEDHI` | `wa_laf_hg_nm` | 지역명 |  |
| `JEDHI` | `laf_cd` | 자치단체코드 |  |
| `JEDHI` | `laf_hg_nm` | 자치단체명 |  |
| `JEDHI` | `pfa_amt1` | 지방공기업 부채 |  |
| `JEDHI` | `pfa_amt2` | 지방공기업 자산 |  |
| `JEDHI` | `rate` | 자본대비 부채비율(%) |  |
| `JEDHI` | `fyr` | 회계연도 |  |
| `JEDHI` | `wa_laf_cd` | 지역코드 |  |
| `JFCCJ` | `fyr` | 회계연도 |  |
| `JFCCJ` | `wa_laf_hg_nm` | 지역 |  |
| `JFCCJ` | `laf_hg_nm` | 자치단체명 |  |
| `JFCCJ` | `laf_cd` | 자치단체코드 |  |
| `JFCCJ` | `tot_stl_amt` | 계(A+B+C-D)(원) |  |
| `JFCCJ` | `stl_amt1` | 자치단체(A)(원) |  |
| `JFCCJ` | `stl_amt2` | 지방공공기관(B)(원) |  |
| `JFCCJ` | `stl_amt3` | 교육재정(C)(원) |  |
| `JFCCJ` | `stl_amt4` | 내(외)부거래(D)(원) |  |
| `JFIED` | `fyr` | 회계연도 |  |
| `JFIED` | `wa_laf_cd` | 지역코드 |  |
| `JFIED` | `wa_laf_hg_nm` | 지역명 |  |
| `JFIED` | `laf_cd` | 자치단체코드 |  |
| `JFIED` | `laf_hg_nm` | 자치단체명 |  |
| `JFIED` | `pfa_amt1` | 자체수입(개편전) |  |
| `JFIED` | `pfa_amt2` | 자치단체 예산규모 |  |
| `JFIED` | `rate1` | 재정자립도[최종](개편전)(%) |  |
| `JFIED` | `pfa_amt3` | 자체수입(개편후) |  |
| `JFIED` | `rate2` | 재정자립도[최종](개편후)(%) |  |
| `JGFCE` | `fyr` | 회계연도 |  |
| `JGFCE` | `wa_laf_cd` | 지역코드 |  |
| `JGFCE` | `wa_laf_hg_nm` | 지역명 |  |
| `JGFCE` | `laf_cd` | 자치단체코드 |  |
| `JGFCE` | `laf_hg_nm` | 자치단체명 |  |
| `JGFCE` | `pbco_acnt_nm` | 공기업명 |  |
| `JGFCE` | `com_dts_cd_nm` | 구분 |  |
| `JGFCE` | `lat_amt` | 부채 |  |
| `JGFCE` | `ast_amt` | 자산 |  |
| `JGFCE` | `rate` | 자본대비 부채비율(%) |  |
| `JGIBF` | `fyr` | 회계연도 |  |
| `JGIBF` | `wa_laf_cd` | 지역코드 |  |
| `JGIBF` | `wa_laf_hg_nm` | 지역명 |  |
| `JGIBF` | `laf_cd` | 자치단체코드 |  |
| `JGIBF` | `laf_hg_nm` | 자치단체명 |  |
| `JGIBF` | `pfa_amt1` | 세출결산액 |  |
| `JGIBF` | `pfa_amt2` | 기본경비 |  |
| `JGIBF` | `rate` | 기본경비비율(%) |  |
| `JHDAC` | `fyr` | 회계연도 |  |
| `JHDAC` | `wa_laf_cd` | 지역코드 |  |
| `JHDAC` | `wa_laf_hg_nm` | 지역명 |  |
| `JHDAC` | `laf_cd` | 자치단체코드 |  |
| `JHDAC` | `laf_hg_nm` | 자치단체명 |  |
| `JHDAC` | `nni_rv_efir_tot` | 주민1인당 세외수입액(천원) |  |
| `JHDAC` | `nni_rv_efir` | 일반회계 세외수입액(천원) |  |
| `JHDAC` | `pptn_num` | 인구수(명) |  |
| `JKAXRZ` | `fyr` | 회계연도 |  |
| `JKAXRZ` | `laf_hg_nm` | 자치단체명 |  |
| `JKAXRZ` | `laf_cd` | 자치단체코드 |  |
| `JKAXRZ` | `wa_laf_hg_nm` | 지역명 |  |
| `JKAXRZ` | `pfin_stl_amt1` | 지방의회 국외여비(A) |  |
| `JKAXRZ` | `pfin_stl_amt2` | 세출결산액(B) |  |
| `JKAXRZ` | `rate` | 지방의회 국외여비 비율 (A/B)*100 |  |
| `KAAAA` | `fyr` | 회계연도 |  |
| `KAAAA` | `rcvmt_aggr_amt` | 금액 |  |
| `KAAAA` | `rate1` | 전년대비 신장률 |  |
| `KAAAA` | `rate2` | 2010년 대비 신장률 |  |
| `KAAAB` | `fyr` | 회계연도 |  |
| `KAAAB` | `dtmk_cd` | 세목코드 |  |
| `KAAAB` | `dtmk_nm` | 세목명 |  |
| `KAAAB` | `rcvmt_aggr_amt` | 금액 |  |
| `KAAAB` | `rate` | 신장률 |  |
| `KAAAC` | `fyr` | 회계연도 |  |
| `KAAAC` | `wa_laf_cd` | 시도코드 |  |
| `KAAAC` | `wa_laf_hg_nm` | 시도명 |  |
| `KAAAC` | `rcvmt_aggr_amt` | 금액 |  |
| `KAAAC` | `rate` | 신장율 |  |
| `KAAAD` | `fyr` | 회계연도 |  |
| `KAAAD` | `wa_laf_cd` | 시도코드 |  |
| `KAAAD` | `wa_laf_hg_nm` | 시도명 |  |
| `KAAAD` | `rcvmt_aggr_amt` | 금액 |  |
| `KAAAD` | `rate` | 비중 |  |
| `KAAAE` | `fyr` | 회계연도 |  |
| `KAAAE` | `cap_dv_cd` | 시도군구분코드 |  |
| `KAAAE` | `cap_dv_nm` | 시도군구분명 |  |
| `KAAAE` | `dtmk_cd` | 세목코드 |  |
| `KAAAE` | `dtmk_nm` | 세목명 |  |
| `KAAAE` | `wa_laf_cd` | 시도코드 |  |
| `KAAAE` | `wa_laf_hg_nm` | 시도명 |  |
| `KAAAE` | `rcvmt_aggr_amt` | 금액 |  |
| `KAAAE` | `rate` | 비중 |  |
| `KAAAG` | `fyr` | 회계연도 |  |
| `KAAAG` | `dtmk_cd` | 세목코드 |  |
| `KAAAG` | `dtmk_nm` | 세목명 |  |
| `KAAAG` | `cltn_dcsn_aggr_amt` | 부과액 |  |
| `KAAAG` | `rcvmt_aggr_amt` | 징수액 |  |
| `KAAAG` | `rate` | 징수율 |  |
| `KAAAH` | `fyr` | 회계연도 |  |
| `KAAAH` | `wa_laf_cd` | 시도코드 |  |
| `KAAAH` | `wa_laf_hg_nm` | 시도명 |  |
| `KAAAH` | `cltn_dcsn_aggr_amt` | 부과액 |  |
| `KAAAH` | `rcvmt_aggr_amt` | 징수액 |  |
| `KAAAH` | `rate` | 징수율 |  |
| `KAABBD` | `fyr` | 회계연도 |  |
| `KAABBD` | `laf_cd` | 자치단체코드 |  |
| `KAABBD` | `wa_laf_hg_nm` | 지역명 |  |
| `KAABBD` | `laf_hg_nm` | 자치단체명 |  |
| `KAABBD` | `smy_cntt_amt` | 합계 (A=a+b+c+d) |  |
| `KAABBD` | `smy_cntt_amt2` | 자치단체 (a) |  |
| `KAABBD` | `smy_cntt_amt3` | 지방교육청 (b) |  |
| `KAABBD` | `smy_cntt_amt4` | 공사·공단 (c) |  |
| `KAABBD` | `smy_cntt_amt5` | 출자·출연기관 (d) |  |
| `KBAAA` | `fyr` | 회계연도 |  |
| `KBAAA` | `wa_laf_cd` | 시도코드 |  |
| `KBAAA` | `wa_laf_hg_nm` | 시도명 |  |
| `KBAAA` | `laf_cd` | 자치단체코드 |  |
| `KBAAA` | `laf_hg_nm` | 자치단체명 |  |
| `KBAAA` | `rate` | 지표값 (A/B)*100 |  |
| `KBAAA` | `flux_amt0` | 유동부채 소계 A=(a+b+c) |  |
| `KBAAA` | `flux_amt1` | 지자체(직영기업포함)(a) |  |
| `KBAAA` | `flux_amt2` | 지방공사공단(b) |  |
| `KBAAA` | `flux_amt3` | 출자출연기관(c) |  |
| `KBAAA` | `flux_amt4` | 유동자산 소계 B=(d+e+f) |  |
| `KBAAA` | `flux_amt5` | 지자체(직영기업포함)(d) |  |
| `KBAAA` | `flux_amt6` | 지방공사공단(e) |  |
| `KBAAA` | `flux_amt7` | 출자출연기관(f) |  |
| `KBAAB` | `fyr` | 회계연도 |  |
| `KBAAB` | `wa_laf_cd` | 시도코드 |  |
| `KBAAB` | `wa_laf_hg_nm` | 시도명 |  |
| `KBAAB` | `laf_cd` | 자치단체코드 |  |
| `KBAAB` | `laf_hg_nm` | 자치단체명 |  |
| `KBAAB` | `rate` | 지표값 (A/B)*100 |  |
| `KBAAB` | `lcl_asmb_exps0` | 지방의회경비결산액 소계 A=(a+b+c-d) |  |
| `KBAAB` | `lcl_asmb_exps1` | 국외여비(a) |  |
| `KBAAB` | `lcl_asmb_exps2` | 의정운영공통경비(b) |  |
| `KBAAB` | `lcl_asmb_exps3` | 의원운영업무추진비(c) |  |
| `KBAAB` | `lcl_asmb_exps4` | 예외사항으로 편성되어 집행된 국외여비 금액(d) |  |
| `KBAAB` | `lcl_asmb_exps5` | 지방의회경비기준액 소계 B=(e+f+g+h) |  |
| `KBAAB` | `lcl_asmb_exps6` | 국외여비(e) |  |
| `KBAAB` | `lcl_asmb_exps7` | 의정운영공통경비(f) |  |
| `KBAAB` | `lcl_asmb_exps8` | 의원운영업무추진비(g) |  |
| `KBAAB` | `lcl_asmb_exps9` | 변동분(h) |  |
| `KBAAC` | `fyr` | 회계연도 |  |
| `KBAAC` | `wa_laf_cd` | 시도코드 |  |
| `KBAAC` | `wa_laf_hg_nm` | 시도명 |  |
| `KBAAC` | `laf_cd` | 자치단체코드 |  |
| `KBAAC` | `laf_hg_nm` | 자치단체명 |  |
| `KBAAC` | `rate` | 지표값 (A/B)*100 |  |
| `KBAAC` | `boe_amt0` | 업무추진비결산액 소계 A=(a+b) |  |
| `KBAAC` | `boe_amt1` | 기관운영 업무추진비(a) |  |
| `KBAAC` | `boe_amt2` | 시책추진 업무추진비(b) |  |
| `KBAAC` | `boe_amt3` | 업무추진비기준액 소계 B=(c+d) |  |
| `KBAAC` | `boe_amt4` | 기관운영 업무추진비(c) |  |
| `KBAAC` | `boe_amt5` | 시책추진 업무추진비(d) |  |
| `KBAAD` | `fyr` | 회계연도 |  |
| `KBAAD` | `wa_laf_cd` | 시도코드 |  |
| `KBAAD` | `wa_laf_hg_nm` | 시도명 |  |
| `KBAAD` | `laf_cd` | 자치단체코드 |  |
| `KBAAD` | `laf_hg_nm` | 자치단체명 |  |
| `KBAAD` | `rate2` | 전년도 행사축제경비증감률 {(A-B)/B}x100 |  |
| `KBAAD` | `rate1` | 행사축제경비비율 A={(a-b)÷c}×100 |  |
| `KBAAD` | `event_fstv_amt5` | 행사축제경비 소계 a=(1)+(2)+(3)+(4) |  |
| `KBAAD` | `event_fstv_amt1` | 행사운영비(1) |  |
| `KBAAD` | `event_fstv_amt2` | 행사실비보상금(2) |  |
| `KBAAD` | `event_fstv_amt3` | 민간행사사업보조(3) |  |
| `KBAAD` | `event_fstv_amt4` | 행사관련시설비(4) |  |
| `KBAAD` | `event_fstv_amt10` | 제외대상행사축제경비 소계 소계 b=⑸+⑹+⑺+⑻ |  |
| `KBAAD` | `event_fstv_amt6` | 기재부 인정(5) |  |
| `KBAAD` | `event_fstv_amt7` | 문광부 인정(6) |  |
| `KBAAD` | `event_fstv_amt8` | 전국체전/소년체전/장애인체전(7) |  |
| `KBAAD` | `event_fstv_amt9` | 행자부인정(8) |  |
| `KBAAD` | `event_fstv_amt11` | 세출결산액 (c) |  |
| `KBAAE` | `fyr` | 회계연도 |  |
| `KBAAE` | `wa_laf_cd` | 시도코드 |  |
| `KBAAE` | `wa_laf_hg_nm` | 시도명 |  |
| `KBAAE` | `laf_cd` | 자치단체코드 |  |
| `KBAAE` | `laf_hg_nm` | 자치단체명 |  |
| `KBAAE` | `rate` | 지표값 (A/B)*100 |  |
| `KBAAE` | `dmf_amt1` | 회계연도 적립재난관리기금 전출액 A |  |
| `KBAAE` | `dmf_amt2` | 보통세 수입결산액 평균연액 소계 B=(a+b+c)/3 |  |
| `KBAAE` | `dmf_amt3` | (회계연도-2) 보통세 (a) |  |
| `KBAAE` | `dmf_amt4` | (회계연도-3) 보통세 (b) |  |
| `KBAAE` | `dmf_amt5` | (회계연도-4) 보통세 (c) |  |
| `LIMHJ` | `fyr` | 회계연도 |  |
| `LIMHJ` | `laf_cd` | 자치단체코드 |  |
| `LIMHJ` | `wa_laf_hg_nm` | 지역명 |  |
| `LIMHJ` | `laf_hg_nm` | 자치단체명 |  |
| `LIMHJ` | `smy_cntt_amt1` | 세출예산액(A) |  |
| `LIMHJ` | `smy_cntt_amt2` | 사회보장적 수혜금(B) |  |
| `LIMHJ` | `smy_cntt_amt_rt` | 비율(B/A) |  |
| `LLBSI` | `fyr` | 회계연도 |  |
| `LLBSI` | `wa_laf_hg_nm` | 지역명 |  |
| `LLBSI` | `laf_cd` | 자치단체코드 |  |
| `LLBSI` | `laf_hg_nm` | 자치단체명 |  |
| `LLBSI` | `pfa_amt1` | 인센티브계 |  |
| `LLBSI` | `pfa_amt2` | 지방재정혁신 | 2012년 : 원가회계제도 시범운영<br/>2013~2015년 : 예산집행율 제고<br/>2016년 이후 : 지방재정혁신 |
| `LLBSI` | `pfa_amt3` | 공기업혁신 | 2012년 : 예산효율화 우수 자치단체<br/>2013~2015년 : 예산 효율화<br/>2016년 이후 : 공기업혁신 |
| `LLBSI` | `pfa_amt4` | 재정분석 | 2013년 이후 : 재정분석 |
| `LLBSI` | `pfa_amt5` | 지방세체납액축소 | 2013~2015년 : 지방세 체납액 축소 |
| `LLBSI` | `pfa_amt6` | 신속집행이자보전 | 2015년 : 세외수입<br/>2018년 : 신속집행 이자보전<br/>2021년 : 지방세외수입혁신 |
| `LLBSI` | `pfa_amt7` | 재정공시 | 2015년 : 재정공시 |
| `LLBSI` | `pfa_amt8` | 지방재정대상 | 2026년 이후 : 지방재정분야 |
| `LLBSI` | `pfa_amt9` | 지방상하수도 |  |
| `LLBSI` | `pfa_amt10` | 지방세외수입 |  |
| `LLBSR` | `fyr` | 회계연도 |  |
| `LLBSR` | `wa_laf_hg_nm` | 지역명 |  |
| `LLBSR` | `laf_cd` | 자치단체코드 |  |
| `LLBSR` | `laf_hg_nm` | 자치단체명 |  |
| `LLBSR` | `mamt_amt1` | 감액총금액 |  |
| `LLBSR` | `mamt_amt2` | 감액금액 |  |
| `LLBSR` | `mamt_rson_cn` | 감액사유 |  |
| `LLBSR` | `viol_ep_cn` | 위반지출내역 |  |
| `MLNXOJ` | `fyr` | 회계연도 |  |
| `MLNXOJ` | `laf_cd` | 자치단체코드 |  |
| `MLNXOJ` | `wa_laf_hg_nm` | 지역명 |  |
| `MLNXOJ` | `laf_hg_nm` | 자치단체명 |  |
| `MLNXOJ` | `smy_cntt_amt_rt` | 재정자립도 |  |
| `MLNXOJ` | `smy_cntt_amt_rt2` | 재정자주도 |  |
| `MLNXOJ` | `smy_cntt_amt_rt3` | 사회복지분야 예산비율 |  |
| `MLNXOJ` | `smy_cntt_amt_rt4` | 자체사업 비율 |  |
| `MLNXOJ` | `smy_cntt_amt_rt5` | 보조사업 비율 |  |
| `MLNXOJ` | `smy_cntt_amt_rt6` | 지방세와 세외수입의 총액 중 인건비 비율 |  |
| `NBRILV` | `laf_cd` | 자치단체코드 |  |
| `NBRILV` | `wa_laf_hg_nm` | 지역명 |  |
| `NBRILV` | `laf_hg_nm` | 자치단체명 |  |
| `NBRILV` | `smy_cntt_amt` | 편성액(B=C+D+E) |  |
| `NBRILV` | `smy_cntt_amt2` | 단체장 예산편성액(C) |  |
| `NBRILV` | `smy_cntt_amt3` | 부단체장 예산편성액(D) |  |
| `NBRILV` | `smy_cntt_amt4` | 총액한도(A) |  |
| `NBRILV` | `smy_cntt_amt_rt` | 총액한도 대비 편성액 비율(B/A)*100 |  |
| `NBRILV` | `lup_ord` | 정렬순서 |  |
| `NBRILV` | `smy_cntt_amt5` | 실국장 및 읍면동장 등 기타(E) |  |
| `NBRILV` | `fyr` | 회계연도 |  |
| `NQGSSTZ` | `fyr` | 회계연도 |  |
| `NQGSSTZ` | `laf_cd` | 자치단체코드 |  |
| `NQGSSTZ` | `wa_laf_hg_nm` | 지역명 |  |
| `NQGSSTZ` | `laf_hg_nm` | 자치단체명 |  |
| `NQGSSTZ` | `smy_cntt_amt` | 세출 총액(A) |  |
| `NQGSSTZ` | `smy_cntt_amt2` | 편성액 (B) |  |
| `NQGSSTZ` | `smy_cntt_amt_rt` | 공무원 일·숙직비 비율 (B/A)*100 |  |
| `NSCNG` | `fyr` | 회계연도 |  |
| `NSCNG` | `laf_cd` | 자치단체코드 |  |
| `NSCNG` | `toa_cd` | 원가대상과목코드 |  |
| `NSCNG` | `toa_no` | 항목행번 |  |
| `NSCNG` | `wa_laf_hg_nm` | 지역명 |  |
| `NSCNG` | `laf_hg_nm` | 자치단체명 |  |
| `NSCNG` | `toa_nm` | 과목 |  |
| `NSCNG` | `tpd_amt` | 당기 |  |
| `NSCNG` | `fhy_amt` | 전기 |  |
| `NSCNG` | `ast_rtvr` | 증감율 |  |
| `NSCNG` | `rgstr_dt` | 등록일자 |  |
| `NTASEX` | `fyr` | 회계연도 | 회계연도 |
| `NTASEX` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `NTASEX` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `NTASEX` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `NTASEX` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `NTASEX` | `aemk_grp_cd` | 세목코드 | 세목코드 |
| `NTASEX` | `aemk_nm` | 세목명 | 세목명 |
| `NTASEX` | `atc_val_num` | 지방의회인원 | 지방의회인원 |
| `NTASEX` | `bdty_tott_amt` | 당해년도예산총계액(천원) | 당해년도예산총계액 |
| `NTASEX` | `psby_exps` | 1인당경비(천원) | 1인당경비 |
| `NTUVK` | `smy_cntt_amt2` | 의정운영 공통경비(A) |  |
| `NTUVK` | `smy_cntt_amt3` | 의회운영 업무추진비(B) |  |
| `NTUVK` | `smy_cntt_amt4` | 의원국외여비(C) |  |
| `NTUVK` | `smy_cntt_amt5` | 의원역량개발비(민간위탁)(D) |  |
| `NTUVK` | `fyr` | 회계연도 |  |
| `NTUVK` | `laf_cd` | 자치단체코드 |  |
| `NTUVK` | `wa_laf_hg_nm` | 지역명 |  |
| `NTUVK` | `laf_hg_nm` | 자치단체명 |  |
| `NTUVK` | `smy_cntt_amt` | 합계(=A+B+C+D) |  |
| `PBOPR` | `fyr` | 회계연도 |  |
| `PBOPR` | `wa_laf_hg_nm` | 지역명 |  |
| `PBOPR` | `laf_cd` | 자치단체코드 |  |
| `PBOPR` | `laf_hg_nm` | 자치단체명 |  |
| `PBOPR` | `fcl_ty_nm` | 시설유형 |  |
| `PBOPR` | `fcl_dv_nm` | 시설구분 |  |
| `PBOPR` | `fcl_epl_cn` | 시설명 |  |
| `PBOPR` | `accnut_se_code` | 건립일 |  |
| `PBOPR` | `oper_mth_nm` | 운영방식 |  |
| `PBOPR` | `acht_tott_area` | 건물면적 |  |
| `PBOPR` | `ldar` | 토지면적 |  |
| `PBOPR` | `prod_co` | 관리인력 |  |
| `PBOPR` | `ann_utzt_nop` | 연간이용인원 |  |
| `PBOPR` | `tott_amt` | 건립비용 |  |
| `PBOPR` | `ast_amt` | 취득가액 |  |
| `PBOPR` | `dprc_amt` | 감가상각액 |  |
| `PBOPR` | `dprc_aggr_amt` | 감가상각누계액 |  |
| `PBOPR` | `rccst_amt` | 장부가액 |  |
| `PBOPR` | `svlf` | 내용연수 |  |
| `PBOPR` | `oper_epn_amt` | 비용 |  |
| `PBOPR` | `ern_amt` | 수익 |  |
| `PBOPR` | `thy_nervn_amt` | 순수익 |  |
| `PBOPR` | `pufc_ty_cd` | 시설유형코드 |  |
| `PBOPR` | `pufc_dv_cd` | 시설구분코드 |  |
| `PRCOS` | `fyr` | 회계연도 |  |
| `PRCOS` | `wa_laf_cd` | 지역코드 |  |
| `PRCOS` | `wa_laf_hg_nm` | 지역명 |  |
| `PRCOS` | `laf_cd` | 자치단체코드 |  |
| `PRCOS` | `laf_hg_nm` | 자치단체명 |  |
| `PRCOS` | `pfa_amt1` | 비용총계 |  |
| `PRDET` | `fyr` | 회계연도 |  |
| `PRDET` | `wa_laf_cd` | 지역코드 |  |
| `PRDET` | `wa_laf_hg_nm` | 지역명 |  |
| `PRDET` | `laf_cd` | 자치단체코드 |  |
| `PRDET` | `laf_hg_nm` | 자치단체명 |  |
| `PRDET` | `pfa_amt1` | 부채총계 |  |
| `PRPRF` | `laf_hg_nm` | 자치단체명 |  |
| `PRPRF` | `pfa_amt1` | 자산총계 |  |
| `PRPRF` | `fyr` | 회계연도 |  |
| `PRPRF` | `wa_laf_cd` | 지역코드 |  |
| `PRPRF` | `wa_laf_hg_nm` | 지역명 |  |
| `PRPRF` | `laf_cd` | 자치단체코드 |  |
| `QCRCX` | `fyr` | 회계연도 |  |
| `QCRCX` | `laf_cd` | 자치단체코드 |  |
| `QCRCX` | `wa_laf_hg_nm` | 지역명 |  |
| `QCRCX` | `laf_hg_nm` | 자치단체명 |  |
| `QCRCX` | `smy_cntt_amt` | 대상인원(A) |  |
| `QCRCX` | `smy_cntt_amt2` | 총 예산편성액(B) |  |
| `QCRCX` | `smy_cntt_amt_rt` | 1인당 편성액(B/A) |  |
| `QWGJK` | `acnt_dv_nm` | 회계구분명 |  |
| `QWGJK` | `dept_cd` | 부서코드 |  |
| `QWGJK` | `dbiz_cd` | 세부사업코드 |  |
| `QWGJK` | `dbiz_nm` | 세부사업명 |  |
| `QWGJK` | `exe_ymd` | 집행일자 |  |
| `QWGJK` | `bdg_cash_amt` | 예산현액 |  |
| `QWGJK` | `bdg_ntep` | 국비 |  |
| `QWGJK` | `capep` | 시도비 |  |
| `QWGJK` | `sggep` | 시군구비 |  |
| `QWGJK` | `etc_amt` | 기타 |  |
| `QWGJK` | `ep_amt` | 지출액 |  |
| `QWGJK` | `cpl_amt` | 편성액 |  |
| `QWGJK` | `fld_cd` | 분야코드 | 분야코드 |
| `QWGJK` | `fld_nm` | 분야명 | 분야명 |
| `QWGJK` | `ane_part_cd` | 부문코드 | 부분코드 |
| `QWGJK` | `part_nm` | 부문명 | 부분명 |
| `QWGJK` | `acnt_dv_cd` | 회계구분코드 |  |
| `QWGJK` | `fyr` | 회계연도 |  |
| `QWGJK` | `wa_laf_cd` | 지역코드 |  |
| `QWGJK` | `wa_laf_hg_nm` | 지역명 |  |
| `QWGJK` | `laf_cd` | 자치단체코드 |  |
| `QWGJK` | `laf_hg_nm` | 자치단체명 |  |
| `QWGJK` | `padm_laf_cd` | 행정자치단체코드 | 행정자치단체코드 |
| `QWGJK` | `lup_ord` | 정렬순서 | 정렬순서 |
| `QWGJK` | `zon_cd` | 광역지역코드 | 지역코드의 앞 2자리 코드입니다 |
| `REVLK` | `fyr` | 기준년도 |  |
| `REVLK` | `wa_laf_hg_nm` | 지역명 |  |
| `REVLK` | `laf_cd` | 자치단체코드 |  |
| `REVLK` | `laf_hg_nm` | 자치단체명 |  |
| `REVLK` | `lnk_nm` | 링크명 |  |
| `REVLK` | `lnk_url_nm` | URL |  |
| `RHDTJF` | `fyr` | 회계연도 |  |
| `RHDTJF` | `wa_laf_hg_nm` | 지역명 |  |
| `RHDTJF` | `laf_cd` | 자치단체코드 |  |
| `RHDTJF` | `laf_hg_nm` | 자치단체명 |  |
| `RHDTJF` | `fcl_epl_cn` | 시설명 |  |
| `RHDTJF` | `accnut_se_code` | 건립일 |  |
| `RHDTJF` | `acht_tott_area` | 건물면적 |  |
| `RHDTJF` | `ldar` | 토지면적 |  |
| `RHDTJF` | `prod_co` | 관리인력 |  |
| `RHDTJF` | `ann_utzt_nop` | 연간이용인원 |  |
| `RHDTJF` | `tott_amt` | 건립비용 |  |
| `RHDTJF` | `dprc_amt` | 감가상각액 |  |
| `RHDTJF` | `dprc_aggr_amt` | 감가상각누계액 |  |
| `RHDTJF` | `rccst_amt` | 장부가액 |  |
| `RHDTJF` | `svlf` | 내용연수 |  |
| `RHDTJF` | `oper_epn_amt` | 비용 |  |
| `RHDTJF` | `ern_amt` | 수익 |  |
| `RHDTJF` | `thy_nervn_amt` | 순수익 |  |
| `RHDTJF` | `pufc_oper_lbst` | 인건비 |  |
| `RHDTJF` | `mtn_mgct_amt` | 유지관리비 |  |
| `RHDTJF` | `thy_etc_epn_amt` | 기타 |  |
| `RHDTJF` | `entc_ern_amt` | 입장료 |  |
| `RHDTJF` | `gesu_ern_amt` | 대관료 |  |
| `RHDTJF` | `ls_ern_amt` | 임대료 |  |
| `RHDTJF` | `rvs_ern_amt` | 귀속된수익(민간위탁료 등) |  |
| `RHDTJF` | `etc_ern_amt` | 기타수익 |  |
| `RHJDKD` | `fyr` | 회계연도 |  |
| `RHJDKD` | `laf_cd` | 자치단체코드 |  |
| `RHJDKD` | `laf_hg_nm` | 자치단체명 |  |
| `RHJDKD` | `rate` | 비율(B/A) |  |
| `RHJDKD` | `smy_cntt_amt1` | 세출결산액(A) |  |
| `RHJDKD` | `smy_cntt_amt2` | 사회보장적 수혜금(B) |  |
| `RHJDKD` | `wa_laf_hg_nm` | 지역명 |  |
| `SDSCF` | `fyr` | 회계연도 |  |
| `SDSCF` | `wa_laf_cd` | 지역코드 |  |
| `SDSCF` | `wa_laf_hg_nm` | 지역명 |  |
| `SDSCF` | `laf_cd` | 자치단체코드 |  |
| `SDSCF` | `laf_hg_nm` | 자치단체명 |  |
| `SDSCF` | `aemk_grp_cd` | 세목코드 |  |
| `SDSCF` | `aemk_nm` | 세목명 |  |
| `SDSCF` | `bdg_prsm_cash_amt` | 세출결산액 |  |
| `SDSCF` | `creat_dt` | 생성날짜 |  |
| `SDSCF` | `crtr_id` | 생성아이디 |  |
| `SDSIF` | `fyr` | 회계연도 | 회계연도 |
| `SDSIF` | `wa_laf_cd` | 지역코드 | 지역코드 |
| `SDSIF` | `wa_laf_hg_nm` | 지역명 | 지역명 |
| `SDSIF` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `SDSIF` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `SDSIF` | `armk_cd` | 세목코드 | 세목코드 |
| `SDSIF` | `armk_nm` | 세목명 | 세목명 |
| `SDSIF` | `txrv_amt` | 세입금액 | 세입금액 |
| `SETLK` | `fyr` | 기준년도 |  |
| `SETLK` | `wa_laf_hg_nm` | 지역명 |  |
| `SETLK` | `laf_cd` | 자치단체코드 |  |
| `SETLK` | `laf_hg_nm` | 자치단체명 |  |
| `SETLK` | `lnk_nm` | 링크명 |  |
| `SETLK` | `lnk_url_nm` | URL |  |
| `SIHHC` | `laf_cd` | 자치단체코드 |  |
| `SIHHC` | `laf_hg_nm` | 자치단체명 |  |
| `SIHHC` | `txrv_com_cls_cd_nm` | 회계구분명 |  |
| `SIHHC` | `txrv_ymd` | 세입일자 |  |
| `SIHHC` | `armk_cd` | 세입코드 |  |
| `SIHHC` | `armk_nm` | 세입코드명 |  |
| `SIHHC` | `ldy_aggr_amt` | 전일누계 |  |
| `SIHHC` | `tsd_rv_amt` | 당일수입액 |  |
| `SIHHC` | `tsd_erpd_gbk_amt` | 당일과오납반환액 |  |
| `SIHHC` | `tsd_sbj_rvsn_amt` | 당일과목경정액 |  |
| `SIHHC` | `data_crt_ymd` | 생성날짜 |  |
| `SIHHC` | `rgstr_usr_id` | 생성아이디 |  |
| `SIHHC` | `fyr` | 회계연도 |  |
| `SIHHC` | `wa_laf_cd` | 지역코드 |  |
| `SIHHC` | `wa_laf_hg_nm` | 지역명 |  |
| `SXIFNQ` | `fyr` | 회계연도 |  |
| `SXIFNQ` | `laf_cd` | 자치단체코드 |  |
| `SXIFNQ` | `wa_laf_hg_nm` | 지역명 |  |
| `SXIFNQ` | `laf_hg_nm` | 자치단체명 |  |
| `SXIFNQ` | `smy_cntt_amt` | 총액한도(A) |  |
| `SXIFNQ` | `smy_cntt_amt2` | 합계(B=C+D+E+F) |  |
| `SXIFNQ` | `smy_cntt_amt3` | 의정운영 공통경비(C) |  |
| `SXIFNQ` | `smy_cntt_amt4` | 의회운영 업무추진비(D) |  |
| `SXIFNQ` | `smy_cntt_amt5` | 의원국외여비(E) |  |
| `SXIFNQ` | `smy_cntt_amt6` | 의원역량개발비(민간위탁)(F) |  |
| `SXIFNQ` | `smy_cntt_amt_rt` | 총액한도 대비 편성액 비율(B/A)*100 |  |
| `UCHGA` | `fyr` | 회계연도 |  |
| `UCHGA` | `laf_cd` | 자치단체코드 |  |
| `UCHGA` | `wa_laf_hg_nm` | 지역명 |  |
| `UCHGA` | `laf_hg_nm` | 자치단체명 |  |
| `UCHGA` | `smy_cntt_amt` | 합계(=A+B) |  |
| `UCHGA` | `smy_cntt_amt2` | 단체장 예산편성액(A) |  |
| `UCHGA` | `smy_cntt_amt3` | 부단체장 예산편성액(B) |  |
| `UCMZQA` | `fyr` | 회계연도 |  |
| `UCMZQA` | `laf_cd` | 자치단체코드 |  |
| `UCMZQA` | `wa_laf_hg_nm` | 지역명 |  |
| `UCMZQA` | `laf_hg_nm` | 자치단체명 |  |
| `UCMZQA` | `smy_cntt_amt` | 총액한도(A) |  |
| `UCMZQA` | `smy_cntt_amt2` | 예산편성액 |  |
| `UCMZQA` | `smy_cntt_amt3` | 한도 내(B) |  |
| `UCMZQA` | `smy_cntt_amt4` | 한도 외 |  |
| `UCMZQA` | `smy_cntt_amt_rt` | 총액한도 대비 편성액 비율(B/A)*100 |  |
| `UCMZQK` | `fyr` | 회계연도 |  |
| `UCMZQK` | `laf_cd` | 자치단체코드 |  |
| `UCMZQK` | `wa_laf_hg_nm` | 지역명 |  |
| `UCMZQK` | `laf_hg_nm` | 자치단체명 |  |
| `UCMZQK` | `smy_cntt_amt` | 세출 총액(A) |  |
| `UCMZQK` | `smy_cntt_amt2` | 편성액 (B) |  |
| `UCMZQK` | `smy_cntt_amt_rt` | 지방보조금 비율 (B/A) * 100 |  |
| `UFOPR` | `fyr` | 회계연도 |  |
| `UFOPR` | `laf_cd` | 자치단체코드 |  |
| `UFOPR` | `toa_cd` | 원가대상과목코드 |  |
| `UFOPR` | `toa_no` | 항목행번 |  |
| `UFOPR` | `wa_laf_hg_nm` | 지역명 |  |
| `UFOPR` | `laf_hg_nm` | 자치단체명 |  |
| `UFOPR` | `toa_nm` | 과목 |  |
| `UFOPR` | `tpd_amt` | 당기 |  |
| `UFOPR` | `fhy_amt` | 전기 |  |
| `UFOPR` | `ast_rtvr` | 증감율 |  |
| `UFOPR` | `rgstr_dt` | 등록일자 |  |
| `UNIST` | `fyr` | 회계연도 |  |
| `UNIST` | `wa_laf_hg_nm` | 지역명 |  |
| `UNIST` | `laf_cd` | 자치단체코드 |  |
| `UNIST` | `laf_hg_nm` | 자치단체명 |  |
| `UNIST` | `pfa_amt1` | 세입 |  |
| `UNIST` | `pfa_amt2` | 지출 |  |
| `UNIST` | `pfa_amt3` | 순융자 |  |
| `UNIST` | `pfa_amt4` | 통합재정규모 |  |
| `UNIST` | `rate` | 통합재정수지비율[결산] |  |
| `VNBLIT` | `fyr` | 회계연도 |  |
| `VNBLIT` | `laf_cd` | 자치단체코드 |  |
| `VNBLIT` | `wa_laf_hg_nm` | 지역명 |  |
| `VNBLIT` | `laf_hg_nm` | 자치단체명 |  |
| `VNBLIT` | `smy_cntt_amt` | 세출 총액(A) |  |
| `VNBLIT` | `smy_cntt_amt2` | 편성액 (B) |  |
| `VNBLIT` | `smy_cntt_amt_rt` | 맞춤형복지제도 시행경비 비율 (B/A)*100 |  |
| `VZATVL` | `fyr` | 회계연도 |  |
| `VZATVL` | `laf_cd` | 자치단체코드 |  |
| `VZATVL` | `wa_laf_hg_nm` | 지역명 |  |
| `VZATVL` | `laf_hg_nm` | 자치단체명 |  |
| `VZATVL` | `mnof_gbd_crtr_area` | 기준면적(본청청사)(㎡) |  |
| `VZATVL` | `mnof_gbd_poss_area` | 보유면적(본청청사)(㎡) |  |
| `VZATVL` | `mnof_gbd_ovr_area` | 초과면적(본청청사)(㎡) |  |
| `VZATVL` | `asmb_gbd_crtr_area` | 기준면적(의회청사)(㎡) |  |
| `VZATVL` | `asmb_gbd_poss_area` | 보유면적(의회청사)(㎡) |  |
| `VZATVL` | `asmb_gbd_ovr_area` | 초과면적(의회청사)(㎡) |  |
| `VZATVL` | `hdlg_ofic_crtr_area` | 기준면적(단체장집무실)(㎡) |  |
| `VZATVL` | `hdlg_ofic_poss_area` | 보유면적(단체장집무실)(㎡) |  |
| `VZATVL` | `hdlg_ofic_ovr_area` | 초과면적(단체장집무실)(㎡) |  |
| `VZATVL` | `lup_ord` | 정렬순서 |  |
| `WCEGCF` | `laf_cd` | 자치단체코드 | 자치단체코드 |
| `WCEGCF` | `ctrt_ldgr_mng_no` | 계약대장관리번호 | 계약대장관리번호 |
| `WCEGCF` | `data_crt_ymd` | 자료생성일자 | 자료생성일자 |
| `WCEGCF` | `laf_hg_nm` | 자치단체명 | 자치단체명 |
| `WCEGCF` | `wa_laf_hg_nm` | 시도명 | 시도명 |
| `WCEGCF` | `ctrt_mth_nm` | 계약방법 | 계약방법 |
| `WCEGCF` | `ctrt_knd_nm` | 계약종류 | 계약종류 |
| `WCEGCF` | `ctrt_trgt_nm` | 계약명 | 계약명 |
| `WCEGCF` | `smz_ctrt_ymd` | 계약일자 | 계약일자 |
| `WCEGCF` | `ctrt_tot_tott_amt` | 계약집계금액 | 계약집계금액 |
| `WCEGCF` | `clt_nm` | 업체명 | 업체명 |
| `WCEGCF` | `sbc_yn` | 하도급유무 | 하도급유무 |
| `XFHHZC` | `fyr` | 회계연도 |  |
| `XFHHZC` | `laf_cd` | 자치단체코드 |  |
| `XFHHZC` | `wa_laf_hg_nm` | 지역명 |  |
| `XFHHZC` | `laf_hg_nm` | 자치단체명 |  |
| `XFHHZC` | `smy_cntt_amt` | 세출예산 총계(A) |  |
| `XFHHZC` | `smy_cntt_amt2` | 국외여비 총액 (B=C+D) |  |
| `XFHHZC` | `smy_cntt_amt3` | 국외업무여비 (C) |  |
| `XFHHZC` | `smy_cntt_amt4` | 국제화여비 (D) |  |
| `XFHHZC` | `smy_cntt_amt_rt` | 비율 (B/A) |  |
| `XTKTDC` | `fyr` | 회계연도 |  |
| `XTKTDC` | `laf_cd` | 자치단체코드 |  |
| `XTKTDC` | `wa_laf_hg_nm` | 지역명 |  |
| `XTKTDC` | `laf_hg_nm` | 자치단체명 |  |
| `XTKTDC` | `smy_cntt_amt` | 대상인원(A) |  |
| `XTKTDC` | `smy_cntt_amt2` | 총 예산편성액(B) |  |
| `XTKTDC` | `smy_cntt_amt_rt` | 1인당 편성액(B/A) |  |
| `YCEHF` | `fyr` | 회계연도 |  |
| `YCEHF` | `laf_cd` | 자치단체코드 |  |
| `YCEHF` | `wa_laf_hg_nm` | 지역명 |  |
| `YCEHF` | `laf_hg_nm` | 자치단체명 |  |
| `YCEHF` | `smy_cntt_amt` | 세출예산액(A) |  |
| `YCEHF` | `smy_cntt_amt2` | 행사･축제경비(B) |  |
| `YCEHF` | `smy_cntt_amt_rt` | 비율(B/A) |  |
| `YQMZYF` | `fyr` | 회계연도 |  |
| `YQMZYF` | `laf_cd` | 자치단체코드 |  |
| `YQMZYF` | `wa_laf_hg_nm` | 지역명 |  |
| `YQMZYF` | `laf_hg_nm` | 자치단체명 |  |
| `YQMZYF` | `smy_cntt_amt` | 시책업무추진비 기준액(A) |  |
| `YQMZYF` | `smy_cntt_amt2` | 시책업무추진비 예산편성액(B) |  |
| `YQMZYF` | `smy_cntt_amt_rt` | 기준액 대비 편성액 비율(B/A)*100 |  |

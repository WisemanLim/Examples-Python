/* 2020.04, 베트남[호치민,하노이], [20~34,35~49] */
SELECT /*seq, */sq1, sq2, sq3/*, qtxarea*/, sq4open, sq4/*, qtxage*/, sq5/*, qtxincome*/, sq6, sq7
	/*         직종, 성별, 거주지,             나이,    연령대,          평균소득,  기초화장품[1,2,3]필수, 구입시모습 */ /* [[8]] */
     , aq11, aq12, aq13, aq14, aq15, aq16, aq17, aq18, aq19/*, rc_a1*/ /* [[9]] */
     /* 피부상태[1,2,3]순위 : 9개 항목 중 3개 선택 */
	, aq2lp1_aq21, aq2lp1_aq22, aq2lp1_aq23, aq2lp1_aq24, aq2lp1_aq25, aq2lp1_aq26, aq2lp1_aq27, aq2lp1_aq28, aq2lp1_aq29, aq2lp1_aq210, aq2lp1_aq211, aq2lp1_aq212 /* 피부상태 1번 선택시 */
	, aq2lp2_aq21, aq2lp2_aq22, aq2lp2_aq23, aq2lp2_aq24, aq2lp2_aq25, aq2lp2_aq26, aq2lp2_aq27, aq2lp2_aq28, aq2lp2_aq29, aq2lp2_aq210, aq2lp2_aq211, aq2lp2_aq212 /* 피부상태 2번 선택시 */
	, aq2lp3_aq21, aq2lp3_aq22, aq2lp3_aq23, aq2lp3_aq24, aq2lp3_aq25, aq2lp3_aq26, aq2lp3_aq27, aq2lp3_aq28, aq2lp3_aq29, aq2lp3_aq210, aq2lp3_aq211, aq2lp3_aq212 /* 피부상태 3번 선택시 */
	, aq2lp4_aq21, aq2lp4_aq22, aq2lp4_aq23, aq2lp4_aq24, aq2lp4_aq25, aq2lp4_aq26, aq2lp4_aq27, aq2lp4_aq28, aq2lp4_aq29, aq2lp4_aq210, aq2lp4_aq211, aq2lp4_aq212 /* 피부상태 4번 선택시 */
	, aq2lp5_aq21, aq2lp5_aq22, aq2lp5_aq23, aq2lp5_aq24, aq2lp5_aq25, aq2lp5_aq26, aq2lp5_aq27, aq2lp5_aq28, aq2lp5_aq29, aq2lp5_aq210, aq2lp5_aq211, aq2lp5_aq212 /* 피부상태 5번 선택시 */
	, aq2lp6_aq21, aq2lp6_aq22, aq2lp6_aq23, aq2lp6_aq24, aq2lp6_aq25, aq2lp6_aq26, aq2lp6_aq27, aq2lp6_aq28, aq2lp6_aq29, aq2lp6_aq210, aq2lp6_aq211, aq2lp6_aq212 /* 피부상태 6번 선택시 */
	, aq2lp7_aq21, aq2lp7_aq22, aq2lp7_aq23, aq2lp7_aq24, aq2lp7_aq25, aq2lp7_aq26, aq2lp7_aq27, aq2lp7_aq28, aq2lp7_aq29, aq2lp7_aq210, aq2lp7_aq211, aq2lp7_aq212 /* 피부상태 7번 선택시 */
	, aq2lp8_aq21, aq2lp8_aq22, aq2lp8_aq23, aq2lp8_aq24, aq2lp8_aq25, aq2lp8_aq26, aq2lp8_aq27, aq2lp8_aq28, aq2lp8_aq29, aq2lp8_aq210, aq2lp8_aq211, aq2lp8_aq212 /* 피부상태 8번 선택시 */
	, aq2lp9_aq21, aq2lp9_aq22, aq2lp9_aq23, aq2lp9_aq24, aq2lp9_aq25, aq2lp9_aq26, aq2lp9_aq27, aq2lp9_aq28, aq2lp9_aq29, aq2lp9_aq210, aq2lp9_aq211, aq2lp9_aq212 /* 피부상태 9번 선택시 */ /* [[108]] */
	/* 기초 화장품 기능[1,2]순위 : 피부상태 1~3순위별 12개 항목 중 2개 선택 */
	, aq3 /* 관심 화장품 브랜드/트렌드[모두] : 9개 항목 중 */
	, aq41, aq42, aq43, aq44, aq45, aq46, aq47, aq48/*, aq499*/
	/* 선호 화장품 향[1,2]순위 : 8개 항목 중 2개 선택 */
	, aq51, aq52, aq53, aq54, aq55, aq56, aq57, aq58, aq59/*, aq599*/
	/* 화장품 성분[1,2]순위 : 9개 항목 중 2개 선택 */
	, aq61, aq62, aq63, aq64, aq65, aq66, aq67, aq68, aq69, aq610, aq611, aq612, aq613, aq614, aq615, aq616, aq617
	/* 화장품 사용 및 뷰티 성향[5점척도] : 1전혀동의하지않는다~5매우동의한다, 피부관리 및 화장품 사용 빈도(1~3), 뷰티(4~9), 구입(10~13), 기타(14~17) */ /* [[35]] */
	, bq1 /* 피부타입[건성,중성,복합,지성] */
	, bq1x1_1, bq1x1_2, bq1x1_3, bq1x1_4 /* 피부타입 : 1[oily/dry], 2[sensitive/resistant], 3[pigmented/non-pigmented], 4[wrinkle/tight] */
	, bq1x2 /* 피부톤[어두운,밝은,붉은,노란,중간] */
	, bq1x3 /* 세안 후 피부 수분[당김,약간 당김,적절] */
	, bq2 /* 피부 문제/고민[모두] : 10개 항목 중 */
	, bq31, bq32, bq33, bq34, bq35, bq36, bq37, bq38, bq39, bq310
	/* BQ2 심각정도[5점척도] : 1전혀 심각하지 않다~5매우 심각하다 */
	, cq1/*, cq1_98*/ /* 사용 클렌저[모두] : 7개 항목 중 */
	, cq2lp1_cq2, cq2lp2_cq2, cq2lp3_cq2, cq2lp4_cq2, cq2lp5_cq2, cq2lp6_cq2, cq2lp7_cq2
	/* CQ1 브랜드[모두] : 26개 항목 중, CQ1의 선택된 항목 중 */
	/*, cq2lp98_cq2, cq2lp1_cq2_98, cq2lp2_cq2_98, cq2lp3_cq2_98, cq2lp4_cq2_98, cq2lp5_cq2_98, cq2lp6_cq2_98, cq2lp7_cq2_98, cq2lp98_cq2_98*/
	, cq31, cq32, cq33, cq34, cq35, cq36, cq37, cq38, cq39, cq310, cq311, cq312, cq313, cq314, cq315
	/* 클렌저 사용 중요도[5점척도] : 향(1), 색(2), 제형(3), 원료(4), 세안시느낌(5,6), 세안후느낌(7,8), 기능/효과(9~12), 피부타입(13), 사용/편의(14,15) */
	, cq3x11, cq3x12, cq3x13, cq3x14, cq3x15, cq3x16, cq3x17, cq3x18, cq3x19, cq3x110, cq3x111, cq3x112, cq3x113, cq3x114, cq3x115
	/* 사용중인 클렌저 만족도[5점척도] : 향(1), 색(2), 제형(3), 원료(4), 세안시느낌(5,6), 세안후느낌(7,8), 기능/효과(9~12), 피부타입(13), 사용/편의(14,15) */
	, cq4 /* 선호 클렌저 제형 : 7개 항목 중 1개 선택 */
	, cq5 /* 클렌저 기능 추가(희망)[모두] : 12개 항목 중 */
	, cq6/*, cq6_98*/ /* 사용 보습제[모두] : 4개 항목 중 */
	, cq7lp1_cq7, cq7lp2_cq7, cq7lp3_cq7, cq7lp4_cq7, cq7lp5_cq7
	/* CQ6 브랜드[모두] : 26개 항목 중, CQ6의 선택된 항목 중 */
	/*, cq7lp98_cq7, cq7lp1_cq7_98, cq7lp2_cq7_98, cq7lp3_cq7_98, cq7lp4_cq7_98, cq7lp5_cq7_98, cq7lp98_cq7_98*/
	, cq81, cq82, cq83, cq84, cq85, cq86, cq87, cq88, cq89, cq810, cq811, cq812, cq813, cq814, cq815, cq816, cq817, cq818, cq819, cq820, cq821, cq822, cq823, cq824, cq825
	/* 보습제 사용 중요도[5점척도] : 향(1), 색(2), 제형(3), 원료(4), 바를때느낌(5~11), 흡수후느낌(12~16), 기능/효과(17~25) */
	, cq8x11, cq8x12, cq8x13, cq8x14, cq8x15, cq8x16, cq8x17, cq8x18, cq8x19, cq8x110, cq8x111, cq8x112
	, cq8x113, cq8x114, cq8x115, cq8x116, cq8x117, cq8x118, cq8x119, cq8x120, cq8x121, cq8x122, cq8x123, cq8x124, cq8x125
	/* 사용중인 보습제 만족도[5점척도] : 향(1), 색(2), 제형(3), 원료(4), 바를때느낌(5~11), 흡수후느낌(12~16), 기능/효과(17~25) */
	, cq9 /* 선호 보습제 제형 : 5개 항목 중 1개 선택 */
	, cq10 /* 보습제 기능 추가(희망)[모두] : 12개 항목 중 */
	, cq11/*, cq11_98*/ /* 사용 기초 화장품 기능성 제품[모두] : 3개 항목 중 */
	, cq12lp1_cq12, cq12lp2_cq12, cq12lp3_cq12 /* CQ11 제형[모두] : 5개 항목 중, CQ11의 선택된 항목 중 */
	/*, cq12lp98_cq12, cq12lp1_cq12_98, cq12lp2_cq12_98, cq12lp3_cq12_98, cq12lp98_cq12_98 */
	, cq12lp1_cq13lp1_cq13, cq12lp1_cq13lp2_cq13, cq12lp1_cq13lp3_cq13, cq12lp1_cq13lp4_cq13, cq12lp1_cq13lp5_cq13
	, cq12lp2_cq13lp1_cq13, cq12lp2_cq13lp2_cq13, cq12lp2_cq13lp3_cq13, cq12lp2_cq13lp4_cq13, cq12lp2_cq13lp5_cq13
	, cq12lp3_cq13lp1_cq13, cq12lp3_cq13lp2_cq13, cq12lp3_cq13lp3_cq13, cq12lp3_cq13lp4_cq13, cq12lp3_cq13lp5_cq13
	/* CQ11 브랜드[모두] : 26개 항목 중, CQ11의 선택된 항목 중 */
	/*, cq12lp98_cq13lp1_cq13, cq12lp98_cq13lp2_cq13, cq12lp98_cq13lp3_cq13, cq12lp98_cq13lp4_cq13, cq12lp98_cq13lp5_cq13
	, cq12lp1_cq13lp1_cq13_98, cq12lp1_cq13lp2_cq13_98, cq12lp1_cq13lp3_cq13_98, cq12lp1_cq13lp4_cq13_98, cq12lp1_cq13lp5_cq13_98
	, cq12lp2_cq13lp1_cq13_98, cq12lp2_cq13lp2_cq13_98, cq12lp2_cq13lp3_cq13_98, cq12lp2_cq13lp4_cq13_98, cq12lp2_cq13lp5_cq13_98
	, cq12lp3_cq13lp1_cq13_98, cq12lp3_cq13lp2_cq13_98, cq12lp3_cq13lp3_cq13_98, cq12lp3_cq13lp4_cq13_98, cq12lp3_cq13lp5_cq13_98
	, cq12lp98_cq13lp1_cq13_98, cq12lp98_cq13lp2_cq13_98, cq12lp98_cq13lp3_cq13_98, cq12lp98_cq13lp4_cq13_98, cq12lp98_cq13lp5_cq13_98 */
	, cq141, cq142, cq143, cq144, cq145, cq146, cq147, cq148, cq149, cq1410, cq1411, cq1412, cq1413, cq1414, cq1415, cq1416
	/* 기초 화장품 기능성 제품 사용 중요도[5점척도] : 향(1), 색(2), 제형(3), 원료(4), 바를때느낌(5~9), 흡수후느낌(10~13), 기능/효과(14~16) */
	, cq14x11, cq14x12, cq14x13, cq14x14, cq14x15, cq14x16, cq14x17, cq14x18, cq14x19, cq14x110, cq14x111, cq14x112, cq14x113, cq14x114, cq14x115, cq14x116
	/* 사용중인 기초 화장품 기능성 제품 만족도[5점척도] : 향(1), 색(2), 제형(3), 원료(4), 바를때느낌(5~9), 흡수후느낌(10~13), 기능/효과(14~16) */
	, cq15 /* 선호 기초 화장품 기능성 제품 제형 : 5개 항목 중 1개 선택 */
	, cq16 /* 기초 화장품 기능성 제품 기능 추가(희망)[모두] : 12개 항목 중 */
	, eq1 /* 기초 화장품 개수 변화(6개월 전) */
	, eq1x1 /* 기초 화장품 구입 평균 금액(월) */
	, eq2 /* 색조 화장품 개수 변화(6개월 전) */
	, eq2x1 /* 색조 화장품 구입 평균 금액(월) */
	, eq3/*, eq3_98*/ /* 화장품 정보 경로[모두] : 9개 항목 중 */
	, eq4 /* 한국 화장품 구입/사용 의향[5점척도] : 1전혀구입할의향이없다~5구입할의향이매우많다 */
	, eq4x1/*, eq4x1_98*/
	/* 긍정시[21개 항목 중 최대 2개 선택] : 제품기능 및 효과(1~5), 제품 성분(6~8), 패키지(9), 가격(10,11), 접근성/프로모션(12~15), 이미지(16~19), 기타(20,21) */
	, eq4x2/*, eq4x2_98*/
	/* 부정시[16개 항목 중 최대 2개 선택] : 제품기능 및 효과(1~5), 제품 성분(6,7), 가격(8,9), 접근성/프로모션(10~12), 정보 부족(13,14), 원산지(15,16) */
	, dq1, dq2, dq2x1, dq3, dq4
	/* 직업, 결혼, 자녀, 월평균소득, 학력 */
FROM sgip.form_vn2020f;

